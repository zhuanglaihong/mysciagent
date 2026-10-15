<h1 align="center">MySciAgent</h1>

<p align="center"><strong>开箱即用的个人操作系统——实用 Agents 管理平台</strong></p>

<p align="center">
  <a href="https://python.org/"><img alt="Python 3.12+" src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white"></a>
  <a href="docs/setup.md"><img alt="Linux Server" src="https://img.shields.io/badge/Linux-Server-FCC624?style=for-the-badge&amp;logo=linux&amp;logoColor=black"></a>
  <a href="docs/architecture.md"><img alt="Multi Agent" src="https://img.shields.io/badge/Agents-Hermes%20%2B%20OpenClaw%20%2B%20Claude%20Code-7C3AED?style=for-the-badge"></a>
  <a href="https://github.com/zhuanglaihong/mysciagent/blob/main/LICENSE"><img alt="License BSD 3-Clause" src="https://img.shields.io/badge/License-BSD--3--Clause-22C55E?style=for-the-badge"></a>
</p>

MySciAgent 是面向研究生和科研工作者的 **个人 Agent 管理平台**。整合 Hermes、Claude Code、OpenClaw，连接你已有的文献库、笔记、代码仓库、计算环境和日常事务，让 AI 成为科研助手与个人秘书。

通过 Docker Compose 管理服务，使用飞书、Discord 或终端与助手交互，配合长期记忆、工具接入、定时任务与备份，把常用 Agent 和工具放进同一套工作环境。

## 核心能力

| 能力 | 包含什么 |
|---|---|
| Agent 管理 | Hermes 个人助手、Claude Code 编码、OpenClaw 消息网关，按角色配置模型与工具 |
| 记忆与工具接入 | TDAI 长期记忆，MCP / CLI 工具连接，复用已有应用与项目目录 |
| 文献与信息整理 | Zotero、论文清单、语雀知识库、dailyinfo 信息聚合 |
| 日常秘书 | 待办追踪、邮件、联系人、飞书 / Discord 通知与定时简报 |
| 持续运行 | 数据持久化、配置版本管理、服务监控与云盘快照备份 |

## 我的科研工作流

**MySciAgent 的重点是把这些基础能力组织成自己的科研与日常工作流**：围绕实际课题连接资料、代码、计算环境和事务安排，让阅读、实现、实验记录与结果整理能够衔接，并把接入方式沉淀为其他研究者可以复用的配置与方法。

团队开发的 **天一（研发协作）**、**知汛（水文问答）**，以及文献、知识库和服务器服务，是实际应用的参考。你可以替换为自己的账号、资料、仓库与专业工具，搭建属于自己的助手。详见 [团队应用案例](docs/team-use-cases.md)；科研流程与 Paper2Code 的设计放在 [规划文档](docs/research-platform-roadmap.md)。

### 能力地图

<details>
<summary>展开完整能力地图（19 项）</summary>

🌐 表示团队应用案例；角色名对应仓库中的实际配置，使用时可接入自己的账号、资料与服务。

| 能力 | 实现方式 | 依赖仓库 |
|------|----------|----------|
| 多 Agent 协作 | Hermes ×4（爱玛士 / 爱码士 / 道元 / finance）+ Claude Code + OpenClaw ×3（虾酱 / 知汛 / 天一） | — |
| 跨 Agent 长期记忆 | TDAI Memory L0→L3 分层管线，3 agent + CC飞总 共享（道元独立） | — |
| Zotero 文献系统 | zotero-mcp 12 tools（mylibrary 提供）+ paper pipeline（爱码士写入，道元只读） | [mylibrary](https://github.com/zhuanglaihong/mylibrary) |
| 飞书直连 | cc-connect（CC飞总）+ lark-cli（Hermes CLI）+ 道元 bot + zhixun 知汛 bot + tianyi 天一 bot | — |
| Discord 桥接 | Hermes coder（爱码士）+ OpenClaw 虾酱 | — |
| 晨间四签 | Hermes cron skill → TDAI/AgentOps/语雀 MCP 等信号 → 飞书推送 | — |
| AI 情报聚合 | dailyinfo 多源抓取 + AI 摘要 → 飞书 / Discord 推送 | [dailyinfo](https://github.com/zhuanglaihong/dailyinfo) |
| 🌐 研发日报 | repo-scanner MCP 采集配置的仓库 → Hermes skill → 飞书推送；天一 bot 复用同源读能力（团队服务，部署见 [server-deploy](docs/server-deploy.md)） | [git-contribution-stats](https://gitcode.com/dlut-water/git-contribution-stats) |
| 🌐 水文智能问答 | zhixun 知汛助手 — OpenClaw + zhixun-water-mcp → 飞书 bot（**团队公共 bot**；背后的 zhixun-agent 水文 MCP 即**团队服务**；独立栈，部署参考见 [server-deploy](docs/server-deploy.md)） | [zhixun-agent](https://gitcode.com/dlut-water/zhixun-agent) |
| 论文管线 | paper-fetch 下载 → Google Drive 上传 → Zotero 入库 | — |
| 事务追踪 | aisecretary MCP 服务 → SQLite 持久化 | [aisecretary](https://github.com/zhuanglaihong/aisecretary) |
| 邮件 | himalaya CLI 邮件客户端（IMAP/SMTP 多账户；Outlook 走 ortie OAuth；仅爱玛士可用，其余 agent 拒绝访问） | — |
| 联系人 | cardamum CLI 联系人管理（vdir 后端，vCard） | — |
| Google Drive | rclone 直连云端上传论文 PDF | — |
| 🌐 语雀知识库 | 本机 yuque-mcp 服务（个人栈侧实例；Hermes + 天一接入；**团队服务**，团队侧为服务器独立部署） | [yuque_mcp_server](https://github.com/zhuanglaihong/yuque_mcp_server) |
| 🌐 服务器监控 | 天一接入团队 server-monitoring MCP（HTTPS + Bearer + 内网 CA，12 个只读工具：9 运行 + 3 交付/CI） | [server-monitoring](https://gitcode.com/dlut-water/server-monitoring) |
| 千问办公 AI听记 | 爱玛士远程 MCP（OAuth，仅默认 profile）：听记列表 / AI 摘要 / 待办 / 转写查询与整理 | — |
| 云端备份 | 定时 rsync + sqlite3 热备 → 云盘（Google Drive / OneDrive） | — |
| 服务监控 | Uptime Kuma 面板 + Healthchecks.io 死士开关 + AgentOps 健康采集 | — |

</details>

[逐项阅读能力与接入说明](docs/capabilities.md)

### 仓库配合

<details>
<summary>展开组件仓库与服务关系</summary>

```text
dailyinfo/                 ← 信息聚合与摘要
mylibrary/                 ← Zotero 文献工具与论文流水线
aisecretary/               ← 事务数据库 MCP
yuque_mcp_server/          ← 语雀知识库 MCP
git-contribution-stats/    ← 仓库统计 MCP
zhixun-agent/              ← 团队服务：知汛背后的水文 MCP
server-monitoring/         ← 团队服务：独立部署的监控 MCP
    │
    │  源码构建 / 目录挂载 / MCP 接口
    ▼
mysciagent/                ← 编排、配置、工具连接与运行管理
    ├─ hermes              ← 个人助理 / 编码 / 文献 / 财经 profiles
    ├─ claude-code         ← 编码环境与飞书连接
    ├─ openclaw-gateway    ← 消息网关
    ├─ zotero-mcp          ← 文献查询
    ├─ paper-queue-mcp     ← 论文清单
    ├─ aisecretary         ← 事务记录
    ├─ yuque-mcp           ← 知识库接入
    ├─ repo-scanner-mcp    ← 研发日报数据
    ├─ tdai-memory         ← 长期记忆
    ├─ freshrss            ← RSS 数据源
    ├─ backup-cron         ← 定时备份
    ├─ uptime-kuma         ← 服务监控
    ├─ openclaw-tianyi     ← 团队案例：天一，独立应用栈
    └─ openclaw-zhixun     ← 团队案例：知汛，独立应用栈
```

组件分别通过构建、挂载或 MCP 连接；`server-monitoring` 作为独立服务消费。文献、账号与任务配置可替换为自己的资源。

</details>

[查看仓库来源、依赖与路径](docs/repositories.md)

## 快速开始

1. 准备 Docker Compose、Python 3.12+、Bash，以及自己的模型连接与常用消息入口。
2. 获取仓库和配置模板：

   ```bash
   mkdir -p ~/code
   cd ~/code
   git clone https://github.com/zhuanglaihong/mysciagent.git
   cd mysciagent
   cp .env.example .env
   ```

3. 编辑 `.env`，填写自己的模型、渠道和资源配置；按 [部署指南](docs/setup.md#component-preflight) 准备组件，检查通过后启动完整主栈：

   ```bash
   python3 scripts/repositories.py --check --directory "$HOME/code" && ./scripts/start.sh --build
   ```

想先梳理自己的接入方式，阅读 [个人接入指南](docs/personalize.md)；服务与数据路径见 [架构](docs/architecture.md)，其余说明见 [文档目录](docs/index.md)。项目不收平台使用费，模型与计算资源由你自行选择。

## 文档

**[MySciAgent 文档目录](docs/index.md)** · 计划发布地址：`https://zhuanglaihong.github.io/mysciagent/`

| 从这里阅读 | 内容 |
|---|---|
| [快速开始](docs/setup.md) · [个人接入](docs/personalize.md) | 环境、组件、配置与自己的第一条任务 |
| [能力地图](docs/capabilities.md) · [仓库配合](docs/repositories.md) · [架构](docs/architecture.md) | 框架、工具、依赖与数据路径 |
| [团队案例](docs/team-use-cases.md) · [调度](docs/scheduling.md) · [备份](docs/backup.md) | 实际应用与持续运行 |
| [预览与发布文档站](docs/docs-site.md) | 本地查看、构建与 GitHub Pages 发布方式 |

---

<a id="author"></a>

## 👤 作者 & 团队

**[庄赖宏 · zhuanglaihong](https://github.com/zhuanglaihong)** · iHeadWater

**大连理工大学 · 水资源与防洪研究所产学研联合团队**

团队项目 **[myopenclaw](https://github.com/OuyangWenyu/myopenclaw)** 面向团队成员。**MySciAgent 是我在其基础上开发和维护的个人项目**，围绕自己的真实科研需求组织工具与流程，并向其他研究者提供可复用的个人助手体系。

保留上游代码的原始作者署名与贡献历史，遵循 [BSD-3-Clause 许可证](LICENSE)。[团队主页](https://github.com/iHeadWater) · [GitCode](https://gitcode.com/dlut-water)
