# MySciAgent

**个人科研多智能体协作平台：连接已有应用与资源，贯通论文阅读、研究设计、Paper2Code、实验执行和成果整理。**

基于 [OuyangWenyu/myopenclaw](https://github.com/OuyangWenyu/myopenclaw) 的源码和完整主分支历史继续开发。原始提交、作者和 BSD-3-Clause 许可证保留；上游 README 保存在 [docs/upstream/README.myopenclaw.md](docs/upstream/README.myopenclaw.md)。

## 我该从哪开始

| 目标 | 入口 |
|---|---|
| 在自己的 Linux 服务器落地科研助手 | [Linux 落地计划](docs/linux-delivery-plan.md) |
| 了解多模型、实验和 Paper2Code 的实现次序 | [研究引擎接入](docs/research-engine-integration.md) |
| 可选团队服务与天一 / 知汛公共 bot | [继承的团队部署说明](docs/server-deploy.md)、[接入自检](docs/member-check.md)；需要配置自己的或获授权的服务 |

## 能力地图

下表的 🌐 表示继承的团队侧能力，首版个人科研流程按需启用，未配置不代表已运行。

| 能力 | 在 MySciAgent 中的定位 |
|---|---|
| 科研任务、论文复现、实验管理 | 规划中的科研流程；实际运行验收见 Linux 落地计划 |
| 🌐 研发日报 | 可选仓库统计工具，未取得源码时可用 Git 接口替代 |
| 🌐 水文智能问答 | 可选团队服务，源项目 [zhixun-agent](https://gitcode.com/dlut-water/zhixun-agent)；个人副本待取得源码 |
| 🌐 语雀知识库 | 使用个人组件或获授权端点，部署与写回能力需验证 |
| 🌐 服务器监控 | 可选团队服务；实验状态由实际执行器记录 |

## 当前阶段

当前是**源码迁移与规划基线**。已经复制基础编排及可取得的组件源码、切换组件获取地址，并建立依赖清单。统一科研任务调度、分级模型协作、Paper2Code 和实验管理是后续目标，尚未实现。Docker/账号/模型未部署验证。

**完整启动目前有阻塞：** `git-contribution-stats`、`paper-fetch` 未取得；语雀副本是本地旧快照，缺少继承运行配置所需的 Dockerfile 与版本。`zhixun-agent`、`server-monitoring` 也是待补齐的可选组件。详见 [迁移状态](docs/migration-status.md)。

## 项目文档

| 文档 | 用途 |
|---|---|
| [科研平台建设规划](docs/research-platform-roadmap.md) | 目的、科研环节、对接平台、Agent 分工、模型路由、Paper2Code、实验仓库及五阶段验收 |
| [AI Scientist 调研](docs/ai-scientist-landscape.md) | 25 项相关工作、实现机制、适用边界与取舍 |
| [研究引擎接入设计](docs/research-engine-integration.md) | 研究任务、运行证据、模型交接、引擎接口与开发顺序 |
| [仓库迁移状态](docs/migration-status.md) | 哪些已经复制、哪些复用、哪些无法取得，以及验证范围 |
| [repositories.json](repositories.json) | 机器可读的个人仓库地址、上游来源、版本和依赖状态 |
| [上游运行架构](docs/architecture.md) | 继承的 Hermes / Claude Code / OpenClaw 与工具服务布局；不代表本机部署状态 |
| [部署说明](docs/setup.md) | 继承部署流程；先解决依赖阻塞再按此接入自己的配置 |

## 仓库组织

平台仓库是 `zhuanglaihong/mysciagent`。组件通过同级个人仓库独立维护，现有 `zhuanglaihong/dailyinfo` 直接复用，不覆盖其个人扩展。各科研课题及实验使用独立研究仓库，平台负责关联和调度。

```text
code/
  mysciagent/              # 协调、应用接入、部署、文档
  dailyinfo/               # 已有个人仓库
  mylibrary/               # 已复制：文献工具与 Zotero MCP
  aisecretary/             # 已复制：事务管理
  yuque_mcp_server/        # 已复制旧快照，运行版本待补齐
  everything-claude-code/  # 已复制：继承编码技能
  zhixun-agent/            # 可选团队服务（水文 MCP），源码待补齐
  # 其他依赖的来源与缺口见 repositories.json
```

主仓及本次新建的组件仓库均为私有仓库。原有运行时的 `myopenclaw/*` 镜像名、容器名和网络名暂时保留，以避免在源码迁移中改变部署协议；GitHub 源码归属已经独立。GitHub Pages 尚未配置，继承的 Actions 暂时关闭，后续配置好构建/发布目标后再开启。

## 获取与检查组件

```bash
git clone https://github.com/zhuanglaihong/mysciagent.git
cd mysciagent
# Git 需要能读取个人私有仓库，可在本机先运行 gh auth setup-git
python scripts/repositories.py
python scripts/repositories.py --check --json
```

Linux/WSL 可使用 `./scripts/clone-deps.sh`。Windows 也可直接运行上述 Python 命令。脚本默认将组件克隆到主仓的同级目录，支持 `--directory <父目录>`；已有工作区不会 pull、reset 或改远端。当前若存在必需依赖缺口，退出码为 1，并明确列出阻塞。检查只判断源码，不会启动容器或访问模型。

完整运行沿用 Linux/WSL + Docker 的上游方式，推荐目录 `~/code/mysciagent`。目前尚无原生 Windows 一键部署验证；上游若干运行路径仍使用 `~/code`。

## 实现方向

高能力模型负责研究思考、方案和关键审查；DeepSeek 等低成本模型负责按规格实现、执行测试和整理结果；工具提供真实运行证据。跨 Agent 使用结构化任务交接、共享课题记录和可追踪实验，而不是各自独立聊天。

首条目标流程：**已有论文收藏 → 带来源的方法笔记 → 研究方案 → 独立代码工作区 → 小规模实验 → 结果分析 → 写回原笔记应用**。

## 来源与许可证

平台原始代码遵循根目录 [LICENSE](LICENSE)；组件各自保留上游许可证，不能统一视为平台的 BSD 许可。`mylibrary` 为 AGPL-3.0，`aisecretary` 的 LICENSE 为 CC-BY-NC-4.0，编码技能库为 MIT；语雀旧快照未找到 LICENSE，已在迁移记录标注。相关运行配置中的原作者身份、知识库、密文和远程服务不代表用户已取得对应账号访问能力。
