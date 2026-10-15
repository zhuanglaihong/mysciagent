# 可移植性

把自己的科研助手迁移到新电脑或 Linux 服务器时，需要核对模型、账号、资料路径、工具组件与持久化数据。先用 [个人接入指南](personalize.md) 明确自己的资源，再按 [快速开始](setup.md) 部署；团队特有的服务见 [应用案例](team-use-cases.md)。

## 依赖图

```
mysciagent (本仓库)
│
├── [必须] Docker Engine + Compose，或 Docker Desktop
│
├── [默认主栈源码依赖·启动前预检]
│   ├── ~/code/aisecretary/          ← build context for aisecretary 服务
│   ├── ~/code/git-contribution-stats/ ← build context for repo-scanner-mcp
│   ├── ~/code/yuque_mcp_server/     ← build context for 本机语雀 MCP 服务（无 tag，按 commit pin）
│   ├── ~/code/mylibrary/            ← 论文流水线代码（缺失时 build 从 GitHub clone）
│   └── ../zhixun-agent/             ← 团队案例独立栈的可选 build context
│
├── [可选·软依赖·运行时 graceful skip]
│   └── ~/code/dailyinfo/            ← 宿主机 launchd 调度（每日论文/资讯抓取推送）
│
├── [配置文件·需要手动创建]
│   ├── .env          (从 .env.example)
│   └── .cloud.conf   (从 .cloud.conf.example)
│
└── [数据·可从云盘恢复]
    ├── ~/.hermes/
    ├── ~/.claude/
    ├── ~/.openclaw/
    ├── ~/.cc-connect/
    └── ~/.myagentdata/
```

## 硬依赖：build 时需要的仓库

部分服务的构建上下文位于主仓库之外。默认启动脚本还会先读取 `repositories.json`，检查 `~/code` 下的默认主栈组件，即使已有镜像也必须通过该检查。下表列出主要的服务源码路径；完整清单还包含编码技能与论文下载组件，以清单和预检结果为准。

| 仓库 | 期望路径 | 用途 |
|------|----------|------|
| [aisecretary](https://github.com/iHeadWater/aisecretary) | `~/code/aisecretary` | aisecretary MCP 服务镜像构建 |
| [git-contribution-stats](https://gitcode.com/dlut-water/git-contribution-stats) | `~/code/git-contribution-stats` | repo-scanner-mcp 镜像构建 |
| [yuque_mcp_server](https://gitcode.com/dlut-water/yuque_mcp_server) | `~/code/yuque_mcp_server` | 本机语雀 MCP 服务（yuque-mcp）镜像构建。上游**无 tag**，镜像按 commit pin（守卫 `tests/test_yuque_mcp_local.py`）；升级 = 审查 diff 后改 pin + 重建 |
| [mylibrary](https://github.com/zhuanglaihong/mylibrary) | `~/code/mylibrary` | hermes / zotero-mcp 镜像里的论文流水线（hydrolitagent + skills）。`start.sh` 先 rsync 进 build context；Dockerfile 有 Git fallback，但默认启动前仍须满足源码预检与仓库访问条件 |
| [zhixun-agent](https://gitcode.com/dlut-water/zhixun-agent) | `../zhixun-agent` | zhixun 栈 `zhixun-water-mcp` 镜像的 `additional_contexts.zhixun_src`（可用 `ZHIXUN_AGENT_PATH` 覆盖）。只有启动 zhixun 栈时才需要 |

**已有镜像时也要预检：** `./scripts/start.sh` 不加 `--build` 仍会检查默认主栈源码。缓存镜像不会跳过缺失组件或版本检查。知汛独立栈的源码另按对应部署说明准备。

## 软依赖：运行时 graceful skip

这些仓库缺失不会导致启动失败，但对应功能不可用：

| 仓库 | 期望路径 | 缺失时的影响 |
|------|----------|-------------|
| [dailyinfo](https://github.com/iHeadWater/dailyinfo) | `~/code/dailyinfo` | AI 情报聚合不可用。launchd 定时任务找不到可执行文件 |

## 一键克隆

```bash
./scripts/clone-deps.sh
```

脚本读取 `repositories.json`，克隆其中可取得的个人组件副本；已有工作区保持原样。它默认把组件放在本仓库的同级目录，默认启动脚本则检查 `~/code`。建议把主仓库也放在 `~/code`；否则显式指定组件目录：

```bash
CODE_DIR="$HOME/code" ./scripts/clone-deps.sh
python3 scripts/repositories.py --check --directory "$HOME/code"
```

仓库权限、来源和版本必须匹配检查要求；`source_unavailable` 不会被自动变成可用组件。知汛的 [zhixun-agent](https://gitcode.com/dlut-water/zhixun-agent) 属于独立的团队领域案例，见 [团队应用](team-use-cases.md)。

## 配置文件的机器差异

以下文件每台机器不同，不能直接复制：

| 文件 | 原因 |
|------|------|
| `.env` | API Key 可能不同（虽然可以用同一组 key） |
| `.cloud.conf` | 云盘本机同步路径因用户名和云盘服务而异 |
| `~/.hermes/.env` | 邮箱密码、飞书凭证等 |
| `~/.hermes/SOUL.md` | 人格描述，迁移时通过备份恢复 |
| `~/.hermes/config.yaml` | Hermes 网关配置，迁移时通过备份恢复 |

可以通过云盘备份恢复的数据见 [备份系统](backup.md)。

另外，`~/.hermes/mcp-tokens/`（如千问办公 AI听记 MCP 的 OAuth token）**不在备份清单**：换机后需要重跑一次授权（见 [千问办公 AI听记](qwennote-mcp-hermes.md)）。

## macOS 特定

以下功能依赖 macOS launchd，在 Linux 上不可用：

| 功能 | 替代方案 (Linux) |
|------|-----------------|
| dailyinfo 定时调度 | systemd user timer |
| git-contribution-stats 采集 | systemd user timer |
| Healthchecks.io 心跳 | systemd timer 或 cron |
| collect-agentops 采集 | systemd timer 或 cron |

> **注意**：Hermes cron 任务（Daily Command Center、工作日晨间简报、daily-dev-report、yuque-daily-digest）运行在 Docker 容器内，不依赖 macOS launchd，Linux 上可直接使用。

所有 launchd 任务依赖 macOS launchd。Linux 上的替代方案见 [调度系统](scheduling.md) 的 Linux 等价物说明。

## Docker 路径

`/var/run/docker.sock` 在 macOS Docker Desktop 和 Linux 上路径相同，一般不需要修改。部分 Linux 发行版可能使用不同的 Docker socket 路径。

## 不在本仓库管理的内容

以下内容由各自的仓库独立管理，MySciAgent 负责按所用能力连接：

- dailyinfo 的 secret、数据源、业务逻辑 → dailyinfo 仓
- git-contribution-stats 的采集逻辑、SQLite schema → git-contribution-stats 仓
- aisecretary 的 MCP tools 实现 → aisecretary 仓
- yuque_mcp_server 的 MCP tools 实现、快照/变更报告逻辑 → yuque_mcp_server 仓（本仓库只做 compose 集成，按 commit pin）
