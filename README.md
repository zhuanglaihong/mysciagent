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

## 我该从哪开始

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

---

<a id="author"></a>

## 👤 作者 & 团队

**[庄赖宏 · zhuanglaihong](https://github.com/zhuanglaihong)** · iHeadWater

**大连理工大学 · 水资源与防洪研究所产学研联合团队**

团队项目 **[myopenclaw](https://github.com/OuyangWenyu/myopenclaw)** 面向团队成员。**MySciAgent 是我在其基础上开发和维护的个人项目**，围绕自己的真实科研需求组织工具与流程，并向其他研究者提供可复用的个人助手体系。

保留上游代码的原始作者署名与贡献历史，遵循 [BSD-3-Clause 许可证](LICENSE)。[团队主页](https://github.com/iHeadWater) · [GitCode](https://gitcode.com/dlut-water)
