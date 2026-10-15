---
title: 首页
hide:
  - toc
---

<div class="msa-hero" markdown="1">

<span class="msa-eyebrow">个人操作系统 · 实用 Agents 管理平台</span>

# MySciAgent

<div class="msa-lead" markdown="1">

把常用 Agent 和科研工具，放进自己的工作环境。

</div>

整合 Hermes、Claude Code、OpenClaw，连接已有的文献库、笔记、代码仓库、计算环境与日常事务，让 AI 成为科研助手与个人秘书。

[快速开始](setup.md){ .md-button .md-button--primary }
[能力地图](capabilities.md){ .md-button }
[仓库配合](repositories.md){ .md-button }

</div>

## 一套环境，连接日常工作

| 能力 | 具体内容 |
|---|---|
| Agent 管理 | 个人助手、编码与消息网关，按角色配置模型与工具 |
| 资料与记忆 | Zotero、论文清单、知识库、长期记忆与信息聚合 |
| 日常秘书 | 事务记录、邮件、联系人、定时简报与通知 |
| 持续运行 | 配置管理、监控、数据持久化和备份 |

[查看完整的 19 项能力与组件](capabilities.md) →

## 从你的目标开始

<div class="grid cards" markdown="1">

- **搭建自己的助手**

    选择一个真实任务，接入自己的模型、资料与工具。

    [个人接入指南](personalize.md) → [快速开始](setup.md)

- **了解 Agent 与工具**

    查看框架分工、组件仓库、数据路径与接入方式。

    [能力地图](capabilities.md) → [仓库配合](repositories.md) → [架构](architecture.md)

- **参考实际科研应用**

    团队的天一、知汛与文献、知识库、服务器服务如何配合。

    [团队应用案例](team-use-cases.md) → [共享服务部署](server-deploy.md)

- **让助手持续工作**

    配置调度、备份与监控，保留自己的工作记录。

    [调度](scheduling.md) · [备份](backup.md) · [监控](monitoring.md)

</div>

## 我的科研工作流

**MySciAgent 的重点是连接自己的科研与日常工作流**：以真实课题为中心，把资料、代码、计算环境和事务安排组织起来，衔接阅读、实现、实验记录与结果整理，并沉淀可以复用的配置与方法。

团队开发的 **天一（研发协作）** 与 **知汛（水文问答）** 是实际应用参考；使用者可以替换自己的账号、资料、仓库与领域工具。具体组合见 [团队应用案例](team-use-cases.md)，科研流程与 Paper2Code 的设计见 [科研助手规划](research-platform-roadmap.md)。

## 常用文档

| 主题 | 文档 |
|---|---|
| Agent 与入口 | [Hermes](hermes-channels.md) · [OpenClaw](openclaw-channels.md) · [飞书 CLI](lark-cli.md) |
| 工具与资料 | [Zotero](zotero-cli-cc.md) · [语雀](yuque-mcp-hermes.md) · [事务追踪](aisecretary.md) · [dailyinfo](dailyinfo.md) |
| 团队能力接入 | [共享服务部署](server-deploy.md) · [成员接入自检](member-check.md) |
| 维护与设计 | [版本同步](upstream-sync.md) · [科研引擎设计](research-engine-integration.md) · [AI Scientist 调研](ai-scientist-landscape.md) |
| 文档站 | [本地预览与发布](docs-site.md) |

## 👤 作者 & 团队

**[庄赖宏 · zhuanglaihong](https://github.com/zhuanglaihong)** · iHeadWater

**大连理工大学 · 水资源与防洪研究所产学研联合团队**

团队项目 [myopenclaw](https://github.com/OuyangWenyu/myopenclaw) 面向团队成员；MySciAgent 是作者在其基础上开发和维护的个人项目，保留原始作者署名、贡献历史及 BSD-3-Clause 许可证。
