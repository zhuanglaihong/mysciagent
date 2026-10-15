<h1 align="center">MySciAgent</h1>

<p align="center"><strong>开箱即用的 AI 科研助手与个人秘书</strong></p>

<p align="center">
  <a href="https://python.org/"><img alt="Python 3.12+" src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white"></a>
  <a href="docs/setup.md"><img alt="Linux Server" src="https://img.shields.io/badge/Linux-Server-FCC624?style=for-the-badge&amp;logo=linux&amp;logoColor=black"></a>
  <a href="docs/architecture.md"><img alt="Multi Agent" src="https://img.shields.io/badge/Agents-Hermes%20%2B%20OpenClaw%20%2B%20Claude%20Code-7C3AED?style=for-the-badge"></a>
  <a href="https://github.com/zhuanglaihong/mysciagent/blob/main/LICENSE"><img alt="License BSD 3-Clause" src="https://img.shields.io/badge/License-BSD--3--Clause-22C55E?style=for-the-badge"></a>
</p>

MySciAgent 面向研究生和科研工作者，将论文、笔记、代码、实验和日常待办连接到一个助手。你可以从熟悉的对话入口下达任务，让专业 Agent 协作处理资料整理、科研编程、实验跟进和日常事务。

当论文散落在文献库、研究结论留在笔记里、代码与实验运行在服务器上时，MySciAgent 围绕你已有的工具和工作环境串联科研流程，减少切换应用和重复整理，让研究过程与成果持续积累。

---

## 功能概览

个人操作系统——实用Agents管理。Docker Compose 一键部署，整合 Hermes、Claude Code、OpenClaw 三个 AI Agent 框架，配合长期记忆、飞书/Discord 桥接、晨间四签、论文管线、水文智能问答等能力。数据留在本机，配置用 Git 管理，定期快照备份到云盘。

## 我该从哪开始

| 你是 | 从这里开始 |
|---|---|
| **团队成员**（想用团队能力） | 飞书里直接问 **天一**（零配置；水文问答找 **知汛**）；想接进自己的 agent（WorkBuddy / 千问办公 / 豆包工作 / DeepSeek Harness / Claude Code / Codex）→ [部署到服务器时要看什么](docs/server-deploy.md) |
| **部署服务器**（团队侧） | [部署到服务器时要看什么](docs/server-deploy.md) —— 服务器只部署「**天一 / 知汛两个公共 bot + 团队服务**」，**与 hermes 个人栈无关** |
| **部署个人栈** | [快速开始](#快速开始)（下文） |
| **了解全貌** | [架构](docs/architecture.md) |

> 本仓库有**两条线**：**个人栈**（hermes 全家桶 + 个人服务，本 README 主体）与**服务器侧团队能力**（公共 bot 天一、知汛 + 团队服务：语雀 / 仓库统计 / 服务监控 / 水文 MCP）。成员接入机器自检：`./scripts/member-check.sh`（[说明](docs/member-check.md)）。

## 能力地图

<!-- 🌐 = 团队侧能力（服务器部署那条线）；其余为个人栈 -->

| 能力 | 实现方式 | 依赖仓库 |
|------|----------|----------|
| 多 Agent 协作 | Hermes ×4（爱玛士 / 爱码士 / 道元 / finance）+ Claude Code + OpenClaw ×3（虾酱 / 知汛 / 天一） | — |
| 跨 Agent 长期记忆 | TDAI Memory L0→L3 分层管线，3 agent + CC飞总 共享（道元独立） | — |
| Zotero 文献系统 | zotero-mcp 12 tools（mylibrary 提供）+ paper pipeline（爱码士写入，道元只读） | [mylibrary](https://github.com/zhuanglaihong/mylibrary) |
| 飞书直连 | cc-connect（CC飞总）+ lark-cli（Hermes CLI）+ 道元 bot + zhixun 知汛 bot + tianyi 天一 bot | — |
| Discord 桥接 | Hermes coder（爱码士）+ OpenClaw 虾酱 | — |
| 晨间四签 | Hermes cron skill → TDAI/AgentOps/语雀 MCP 等信号 → 飞书推送 | — |
| AI 情报聚合 | dailyinfo 多源抓取 + AI 摘要 → 飞书 / Discord 推送 | [dailyinfo](https://github.com/zhuanglaihong/dailyinfo) |
| 🌐 研发日报 | repo-scanner MCP 采集 35 仓库 → Hermes skill → 飞书推送；天一 bot 复用同源读能力（团队服务，服务器部署见 [server-deploy](docs/server-deploy.md)） | [git-contribution-stats](https://gitcode.com/dlut-water/git-contribution-stats) |
| 🌐 水文智能问答 | zhixun 知汛助手 — OpenClaw + zhixun-water-mcp → 飞书 bot（**团队公共 bot**；背后的 zhixun-agent 水文 MCP 即**团队服务**；独立栈，见 [server-deploy](docs/server-deploy.md)） | [zhixun-agent](https://gitcode.com/dlut-water/zhixun-agent) |
| 论文管线 | paper-fetch 下载 → Google Drive 上传 → Zotero 入库 | — |
| 事务追踪 | aisecretary MCP 服务 → SQLite 持久化 | [aisecretary](https://github.com/zhuanglaihong/aisecretary) |
| 邮件 | himalaya CLI 邮件客户端（IMAP/SMTP 多账户；Outlook 走 ortie OAuth；仅爱玛士可用，其余 agent 拒绝访问） | — |
| 联系人 | cardamum CLI 联系人管理（vdir 后端，vCard） | — |
| Google Drive | rclone 直连云端上传论文 PDF | — |
| 🌐 语雀知识库 | 本机 yuque-mcp 服务（个人栈侧实例；Hermes + 天一接入；**团队服务**，团队侧为服务器独立部署） | [yuque_mcp_server](https://gitcode.com/dlut-water/yuque_mcp_server) |
| 🌐 服务器监控 | 天一接入团队 server-monitoring MCP（HTTPS + Bearer + 内网 CA，12 个只读工具：9 运行 + 3 交付/CI） | [server-monitoring](https://gitcode.com/dlut-water/server-monitoring) |
| 千问办公 AI听记 | 爱玛士远程 MCP（OAuth，仅默认 profile）：听记列表 / AI 摘要 / 待办 / 转写查询与整理 | — |
| 云端备份 | 定时 rsync + sqlite3 热备 → 云盘（Google Drive / OneDrive） | — |
| 服务监控 | Uptime Kuma 面板 + Healthchecks.io 死士开关 + AgentOps 健康采集 | — |

## 仓库配合

```
dailyinfo/                 ← AI 情报聚合（RSS + AI 摘要）
aisecretary/               ← 事务数据库 MCP
git-contribution-stats/    ← 多仓库 Git 贡献统计（repo-scanner-mcp 源码）
yuque_mcp_server/          ← 语雀 MCP 服务端（yuque-mcp 构建依赖）
zhixun-agent/              ← 团队服务：统一水文 MCP（知汛背后的能力；本机作构建上下文）
mylibrary/                 ← Zotero 文献工具（zotero-mcp 源码）
server-monitoring/         ← 团队监控服务（⚠️ 非构建依赖：天一【运行时消费】其只读 MCP）
    │
    │  前六个通过 Docker volume、build context 或 MCP 接入；
    │  server-monitoring 在团队内网（10.48.x），只进 URL + CA + token 三样配置
    ▼
mysciagent/  (本仓库)     ← Docker 编排 + 执行层 + 兼容层
    │
    ├─ hermes        (4 个 profile: default / coder / daoyuan / finance)
    ├─ claude-code   (CC飞总，飞书直连)
    ├─ openclaw      (虾酱，Discord 网关)
    ├─ openclaw-zhixun (知汛助手，飞书水文 bot，独立栈)
    ├─ openclaw-tianyi (天一，飞书研发 bot，独立栈共享主栈网络；消费 server-monitoring MCP)
    ├─ zotero-mcp    (文献查询 MCP，mylibrary 源码)
    ├─ repo-scanner-mcp (研发日报 MCP)
    ├─ paper-queue-mcp (论文清单 MCP，独立容器)
    ├─ aisecretary   (事务数据库 MCP)
    ├─ yuque-mcp     (语雀知识库 MCP，本机 SSE)
    ├─ tdai-memory   (Agent 长期记忆)
    ├─ freshrss      (RSS 聚合，dailyinfo 数据源)
    ├─ backup-cron   (定时备份)
    └─ uptime-kuma   (服务监控)
```

- **两类配合关系**：① **构建/部署依赖**（前六个仓库：源码进 build context、volume mount 或本机 MCP 服务；其中 `zhixun-agent` 是**团队服务**——水文 MCP、知汛背后的能力，服务器侧随知汛栈一起部署）；② **运行时消费**（`server-monitoring`：团队维护的服务端，本仓只做客户端接入——天一通过 HTTPS + Bearer + 内网 CA 调其只读 MCP，12 个工具覆盖服务器/GFS/CI 状态，并每日 08:30 自动推服务器日报）。**服务端不在本仓管理**，详见 [服务器监控 MCP](docs/server-monitoring-mcp.md)
- **所有数据落 `~/.myagentdata/`** — 备份管线自动覆盖
- **每个仓库独立克隆** — 放在 `~/code/<repo>`，Docker 通过 volume mount 访问（`server-monitoring` 无需克隆，仅需维护者提供的 CA 与 token）

## 快速开始

```bash
# 1. 克隆本仓库
git clone https://github.com/zhuanglaihong/mysciagent.git
cd mysciagent

# 2. 配置环境变量
cp .env.example .env          # 编辑 .env，至少填入 DEEPSEEK_API_KEY
cp .cloud.conf.example .cloud.conf

# 3. （可选）克隆依赖仓库
./scripts/clone-deps.sh       # 克隆 dailyinfo、aisecretary、git-contribution-stats、yuque_mcp_server

# 4. 启动所有服务
./scripts/start.sh
```

首次启动自动完成：配置模板创建、API Key 物化、skill 安装。详见 [快速开始指南](docs/setup.md)。

镜像变更后需重新构建：

```bash
./scripts/start.sh --build
```

如需启动 zhixun 飞书机器人（知汛助手）：

```bash
git clone https://gitcode.com/dlut-water/zhixun-agent.git ../zhixun-agent
cp .env.zhixun-bot.example .env.zhixun-bot  # 编辑填入飞书 App ID/Secret + DeepSeek Key
./scripts/start-zhixun-bot.sh --build
```

如需启动 tianyi 飞书机器人（天一·研发助手，前提：主栈已启动，共享 repo-scanner-mcp）：

```bash
cp .env.tianyi-bot.example .env.tianyi-bot  # 编辑填入飞书 App ID/Secret + 模型 key + GitHub/GitCode token
./scripts/start-tianyi-bot.sh --build
```

## 服务一览

| 服务 | 端口 | Compose 文件 | 说明 |
|------|------|-------------|------|
| hermes | 8642 | 主栈 | Hermes gateway — 爱玛士（默认 profile，飞书 bot） |
| hermes-coder | 8643 | 主栈 | Hermes coder — 爱码士（Discord bot + Zotero 写入 + 论文管线） |
| hermes-finance | 8644 | 主栈 | Hermes finance — 金融 agent（飞书 bot） |
| hermes-daoyuan | 8645 | 主栈 | 道元 — 文献学者 agent（飞书 bot，Zotero 只读） |
| hermes-dashboard | 9119 | 主栈 | Hermes Web 面板（只读） |
| claude-code | 9090 | 主栈 | Claude Code + cc-connect（CC飞总，飞书直连） |
| openclaw-gateway | 18789 | 主栈 | OpenClaw 网关（虾酱 Discord bot） |
| zotero-mcp | 8002 | 主栈 | Zotero 文献 MCP（12 tools，mylibrary 提供） |
| tdai-memory | 8420 | 主栈 | Agent 长期记忆 Gateway（L0→L3） |
| aisecretary | 8000 | 主栈 | 事务数据库 MCP 服务 |
| repo-scanner-mcp | 8001 | 主栈 | 研发日报 MCP 数据服务 |
| yuque-mcp | —（仅容器网络） | 主栈 | 语雀知识库 MCP（本机 SSE，自持只读 token，不发布宿主端口；Hermes/天一接入；日报 skill 的 live 副本为 `~/.hermes/skills` 原生副本，见 [Hermes Skill 机制](docs/hermes-skills.md)） |
| paper-queue-mcp | 8003 | 主栈 | 论文清单 MCP（独立容器，队列目录只挂给它） |
| freshrss | 8081 | 主栈 | RSS 聚合（dailyinfo 数据源） |
| uptime-kuma | 3001 | 主栈 | 服务监控面板 |
| backup-cron | — | 主栈 | 定时快照备份 |
| zhixun-water-mcp | 18201 | zhixun 栈 | 水文 MCP（43 tools），兼容 zhixun-core v2 |
| openclaw-zhixun | 18791 | zhixun 栈 | 知汛助手 — OpenClaw 飞书 bot（独立网络 + 数据目录） |
| openclaw-tianyi | 18792 | tianyi 栈 | 天一研发助手 — OpenClaw 飞书 bot（共享主栈网络，复用 repo-scanner-mcp，gh/gc 写 GitHub/GitCode issue；可选接入 server-monitoring 监控 MCP） |

## 目录结构

```
mysciagent/
├── docker-compose.yml                # 主栈服务编排
├── docker-compose.zhixun-bot.yml     # zhixun 独立栈
├── docker-compose.tianyi-bot.yml     # tianyi 独立栈（共享主栈网络）
├── .env.example                      # 主栈环境变量模板
├── .env.zhixun-bot.example           # zhixun bot 环境变量模板
├── .env.tianyi-bot.example           # tianyi bot 环境变量模板
├── .env.member.example               # 成员接入自检配置模板（member-check 用）
├── .cloud.conf.example               # 云盘路径模板
├── docs/                             # 文档（→ GitHub Pages）
├── docker/                           # 自定义镜像
│   ├── hermes/                       #   Hermes（cardamum + himalaya + ortie + lark-cli + rclone + mylibrary）
│   ├── claude-code/                  #   Claude Code + cc-connect
│   ├── backup-cron/                  #   定时备份
│   ├── tdai-memory/                  #   Agent 长期记忆
│   ├── repo-scanner-mcp/             #   研发日报 MCP
│   ├── zotero-mcp/                   #   Zotero 文献 MCP（mylibrary 源码）
│   ├── zhixun-bot/                   #   zhixun 水文 MCP + 兼容层
│   ├── member-check/                 #   成员接入自检检查器（成员直连三项团队能力 MCP 握手）
│   └── tianyi-bot/                   #   tianyi bot entrypoint + 配置模板 + 渲染脚本 + 内网 CA（ca/）
├── openclaw-zhixun/workspace/        # zhixun bot agent 策略文件（AGENTS.md, SOUL.md）
├── openclaw-tianyi/workspace/        # tianyi bot agent 策略文件（AGENTS.md, SOUL.md, ACCESS.md=成员接入指南）
├── hermes/                           # Hermes 配置模板 + 备份脚本
├── claude/                           # Claude Code / cc-connect 配置模板 + 备份脚本
├── openclaw/                         # OpenClaw 配置模板 + 备份脚本
├── scripts/                          # 运维脚本（启动/停止/备份/恢复/调度/监控/zhixun bot/tianyi bot）
├── skills/                           # 执行层 skill 版本源（live 为 ~/.hermes/skills 原生副本，见 docs/hermes-skills.md）
└── tests/                            # 集成测试
```

## 文档

完整文档 → **[文档目录](docs/index.md)**

| 主题 | 阅读入口 |
|---|---|
| 安装与部署 | [快速开始](docs/setup.md) · [服务器部署](docs/server-deploy.md) · [成员接入自检](docs/member-check.md) · [迁移到新电脑](docs/portability.md) |
| 架构与 Agent | [架构](docs/architecture.md) · [Hermes 渠道](docs/hermes-channels.md) · [Skill 机制](docs/hermes-skills.md) |
| 工具与数据接入 | [AI 情报聚合](docs/dailyinfo.md) · [语雀知识库](docs/yuque-mcp-hermes.md) · [服务器监控 MCP](docs/server-monitoring-mcp.md) · [组件仓库清单](repositories.json) |
| 日常运维 | [任务调度](docs/scheduling.md) · [备份与恢复](docs/backup.md) · [版本同步](docs/upstream-sync.md) |
| 设计与规划 | [科研助手规划](docs/research-platform-roadmap.md) · [研究引擎接入](docs/research-engine-integration.md) · [AI Scientist 调研](docs/ai-scientist-landscape.md) |

本地预览文档：

```bash
uv sync --group docs
uv run mkdocs serve
```

---

<a id="author"></a>

## 👤 作者 & 团队

**[庄赖宏 · zhuanglaihong](https://github.com/zhuanglaihong)** · iHeadWater

**大连理工大学 · 水资源与防洪研究所产学研联合团队**

MySciAgent 围绕团队日常科研中实际涉及的流程与环境设计，将文献阅读、知识积累、科研编程、模型实验、结果整理和日常事务串联起来。论文库、笔记、代码仓库、服务器和沟通工具各有用途，本项目的出发点，就是让 AI 助手融入这些已有资源，在真实的科研任务中协作，减少重复操作，让研究经验与成果得到持续沉淀。

团队项目 **[myopenclaw](https://github.com/OuyangWenyu/myopenclaw)** 面向团队成员，提供 Agent 管理、公共助手和科研工具接入。**MySciAgent 是我在其基础上开发和维护的个人项目**，结合自己的科研需求与工作习惯，打造开箱即用的 AI 科研助手与个人秘书。

本项目保留上游代码的原始作者署名与贡献历史，遵循 [BSD-3-Clause 许可证](LICENSE)。

> 🔗 团队主页：[gitcode.com/dlut-water](https://gitcode.com/dlut-water) · [github.com/iHeadWater](https://github.com/iHeadWater)
