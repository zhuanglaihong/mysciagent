<h1 align="center">MySciAgent</h1>

<p align="center"><strong>开箱即用的 AI 科研助手与个人秘书</strong></p>

<p align="center">
  <a href="https://python.org/"><img alt="Python 3.12+" src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white"></a>
  <a href="docs/setup.md"><img alt="Linux Server" src="https://img.shields.io/badge/Linux-Server-FCC624?style=for-the-badge&amp;logo=linux&amp;logoColor=black"></a>
  <a href="docs/architecture.md"><img alt="Multi Agent" src="https://img.shields.io/badge/Agents-Hermes%20%2B%20OpenClaw%20%2B%20Claude%20Code-7C3AED?style=for-the-badge"></a>
  <a href="https://github.com/zhuanglaihong/mysciagent/blob/main/LICENSE"><img alt="License BSD 3-Clause" src="https://img.shields.io/badge/License-BSD--3--Clause-22C55E?style=for-the-badge"></a>
</p>

MySciAgent 是面向研究生和科研工作者的 **AI 科研助手与个人秘书**。把你已有的文献库、笔记、代码仓库、计算环境和日常事务接入助手，从熟悉的对话入口安排工作，让不同 Agent 协作处理资料、代码与待办。

你可以用它整理一组论文、跟进一个代码项目，或汇总每天的信息与任务。研究方向、使用的工具和数据由你决定；已有的工作方式可以继续沿用，科研过程中产生的记录与成果也能持续积累。

**用自己的模型、自己的工具、自己的资料，搭建属于自己的科研助手。** 先连接一个真实任务，再按需扩展；本文后半部分的团队应用展示了这套体系在实际科研中的用法。

## 能力地图

| 通用能力 | 在你的工作中怎么用 |
|---|---|
| 资料与知识管理 | 结合文献检索、阅读队列、知识库与长期记忆，整理资料、查找来源、积累研究笔记 |
| 科研编程与实验辅助 | 让编码 Agent 进入指定仓库，协助实现方案、运行项目已有的测试或实验命令、整理日志与结果 |
| 日常事务与信息整理 | 接入待办、邮件、联系人和信息源，整理行动项、阅读清单与工作简报 |
| 多 Agent 分工 | 使用 Hermes、Claude Code、OpenClaw 等执行工具，为个人助理、编码、文献阅读设置不同角色与工具权限 |
| 持续运行与数据管理 | 使用定时任务、监控、持久化与备份，跟进任务并保留过程记录 |

文献、编程和秘书能力按你的实际工具组合使用。自动研究循环、Paper2Code 等进一步设计见 [科研助手规划](docs/research-platform-roadmap.md)。

## 我该从哪开始

| 你的目标 | 从这里开始 |
|---|---|
| **第一次接触，想搭建自己的助手** | [个人接入指南](docs/personalize.md)：选择一个任务、一个入口和自己的资源 |
| **在自己的电脑或服务器部署** | [快速开始](docs/setup.md)：环境、凭据、组件与启动方式 |
| **了解工具和 Agent 如何配合** | [架构](docs/architecture.md)：通用分层、服务与数据流 |
| **参考团队里的实际用法** | [iHeadWater 应用案例](docs/team-use-cases.md)：真实科研任务中的工具组合与使用方式 |

## 连接你已有的工具

通过 MCP、API、CLI 和文件目录接入已有资源。下面列出仓库中的接入方式；其他工具可沿用同样的接口思路扩展，具体配置见各项文档。

| 你的资源 | 仓库中的接入方式 |
|---|---|
| 论文与研究资料 | [Zotero / mylibrary](docs/zotero-cli-cc.md)、[论文清单](docs/paper-queue.md)、本地资料目录 |
| 笔记与知识库 | 本地 Markdown 文件、[语雀 MCP](docs/yuque-mcp-hermes.md)、[长期记忆](docs/tdai-memory.md) |
| 代码与计算环境 | 编码 Agent、Git / GitHub / GitCode CLI、项目自己的运行命令；[服务与路径](docs/architecture.md) |
| 对话与通知 | [Hermes 渠道](docs/hermes-channels.md)、[OpenClaw 渠道](docs/openclaw-channels.md)、[飞书 CLI](docs/lark-cli.md) |
| 日常事务与信息 | [aisecretary](docs/aisecretary.md)、[邮件](docs/email.md)、[联系人](docs/contacts.md)、[dailyinfo](docs/dailyinfo.md)、[云盘](docs/google-drive-rclone.md) |

## 快速开始

先准备自己的模型连接、一个常用入口，以及一个希望助手处理的资料目录或代码仓库。

```bash
# 获取项目与配置模板
mkdir -p ~/code
cd ~/code
git clone https://github.com/zhuanglaihong/mysciagent.git
cd mysciagent
cp .env.example .env
```

编辑 `.env`，填写自己的模型和所用渠道的凭据；资料路径、知识库、机器人身份与推送目标也使用自己的配置。

完整容器部署的组件准备、依赖检查和启动命令见 **[快速开始指南](docs/setup.md)**。希望沿用已有 Agent 工具的读者，可先参考 **[个人接入指南](docs/personalize.md)**，选择需要复用的工具与工作流程。

项目不收取平台使用费；模型调用、服务器和第三方服务的费用取决于你选择的资源。

## 实际应用：iHeadWater 科研工作流

以下是作者所在团队在日常科研中使用的具体组合，展示通用能力如何与真实工作结合。天一、知汛是团队助手的名字，水文业务是其中一个领域应用；搭建自己的助手时，可以使用自己的身份、知识库、仓库和专业服务。

| 团队应用 | 实际用途 | 你可以怎样复用 |
|---|---|---|
| 天一 · 研发协作 | 汇总仓库进展，查询团队知识，跟进服务状态 | 连接自己的代码仓库、知识库和计算环境，生成项目简报 |
| 文献与科研记录 | 结合文献库、论文清单、笔记与个人助手整理研究资料 | 替换为自己的课题资料、文献库和记录习惯 |
| 日常信息与事务 | 聚合资讯、整理待办、生成简报并推送到常用入口 | 选择自己关注的信息源、任务类型与推送渠道 |
| 知汛 · 水文问答 | 通过团队水文 MCP 查询专业数据与业务信息 | 按研究方向接入自己的领域 API、MCP 或分析脚本 |

案例的组件关系、部署入口与可替换项见 [团队应用案例](docs/team-use-cases.md)。

## 文档

| 主题 | 阅读入口 |
|---|---|
| 搭建自己的助手 | [个人接入指南](docs/personalize.md) · [快速开始](docs/setup.md) · [迁移到新环境](docs/portability.md) |
| Agent 与工具 | [架构](docs/architecture.md) · [Skill 机制](docs/hermes-skills.md) · [完整文档目录](docs/index.md) |
| 实际应用参考 | [iHeadWater 案例](docs/team-use-cases.md) · [团队服务部署](docs/server-deploy.md) · [团队接入自检](docs/member-check.md) |
| 运维与维护 | [任务调度](docs/scheduling.md) · [备份](docs/backup.md) · [监控](docs/monitoring.md) · [版本同步](docs/upstream-sync.md) |
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

团队项目 **[myopenclaw](https://github.com/OuyangWenyu/myopenclaw)** 面向团队成员，提供 Agent 管理、公共助手和科研工具接入。**MySciAgent 是我在其基础上开发和维护的个人项目**，结合自己的科研需求与工作习惯，提炼可复用的通用能力，让不同专业的研究者都能搭建属于自己的科研助手。

本项目保留上游代码的原始作者署名与贡献历史，遵循 [BSD-3-Clause 许可证](LICENSE)。

> 🔗 团队主页：[gitcode.com/dlut-water](https://gitcode.com/dlut-water) · [github.com/iHeadWater](https://github.com/iHeadWater)
