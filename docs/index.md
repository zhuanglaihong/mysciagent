# MySciAgent

**开箱即用的 AI 科研助手与个人秘书。用自己的模型、工具和资料，搭建属于自己的科研助手。**

MySciAgent 面向不同专业的研究生和科研工作者，将文献、笔记、代码、计算环境与日常事务接入个人助手。你可以从一个具体任务开始，逐步加入文献整理、科研编程、事务追踪与定时简报，并用不同 Agent 分工处理。

## 从你的任务开始

| 你想做什么 | 阅读入口 |
|---|---|
| 第一次搭建，明确该接入哪些资源 | [个人接入指南](personalize.md) |
| 在自己的电脑或服务器部署 | [快速开始](setup.md) · [环境迁移](portability.md) |
| 了解 Agent、工具和数据如何配合 | [架构](architecture.md) · [Skill 机制](hermes-skills.md) |
| 查看真实科研中的应用方式 | [iHeadWater 应用案例](team-use-cases.md) |
| 参考团队共享服务的部署和接入 | [团队部署案例](server-deploy.md) · [成员接入自检](member-check.md) |

## 通用能力

| 能力 | 可使用的工具与资料 |
|---|---|
| 文献与知识管理 | [Zotero](zotero-cli-cc.md)、[论文清单](paper-queue.md)、[语雀](yuque-mcp-hermes.md)、[长期记忆](tdai-memory.md) |
| 科研编程与实验辅助 | [编码与服务架构](architecture.md)、自己的代码仓库、项目运行命令与结果文件 |
| 个人秘书 | [事务追踪](aisecretary.md)、[邮件](email.md)、[联系人](contacts.md)、[云盘](google-drive-rclone.md) |
| 信息与通知 | [dailyinfo](dailyinfo.md)、[Hermes 渠道](hermes-channels.md)、[OpenClaw 渠道](openclaw-channels.md)、[飞书 CLI](lark-cli.md) |
| 持续运行 | [调度](scheduling.md)、[备份](backup.md)、[监控](monitoring.md)、[AgentOps](agentops.md) |

这些能力通过具体工具接入。你的文献库、仓库、账号、数据路径与任务目标由你配置；新工具可通过 MCP、API、CLI 或文件接口扩展。

## 团队应用参考

**天一**（研发协作）与**知汛**（水文问答）是 iHeadWater 在实际科研环境中使用的助手案例。团队的知识库、仓库统计、服务器监控和水文 MCP 展示了专业服务如何接入 Agent。可复用的部分包括对话入口、工具连接、角色分工、简报与运行管理，具体专业工具按读者的研究方向选择。

详见 [团队应用案例](team-use-cases.md)。

## 维护与设计资料

| 主题 | 文档 |
|---|---|
| 日常维护 | [版本同步](upstream-sync.md) · [DNS](dns-setup.md) · [迁移状态](migration-status.md) |
| 科研流程设计 | [科研助手规划](research-platform-roadmap.md) · [研究引擎接入](research-engine-integration.md) |
| 技术调研 | [AI Scientist 调研](ai-scientist-landscape.md) |
| 部署设计参考 | [Linux 落地计划](linux-delivery-plan.md) · [Linux 环境参考](linux-server-setup.md) |

## 👤 作者 & 团队

**[庄赖宏 · zhuanglaihong](https://github.com/zhuanglaihong)** · iHeadWater

**大连理工大学 · 水资源与防洪研究所产学研联合团队**

MySciAgent 将团队科研实践中的工作流程提炼为个人可复用的助手体系。团队项目 [myopenclaw](https://github.com/OuyangWenyu/myopenclaw) 面向团队成员；MySciAgent 是作者在其基础上开发和维护的个人项目，保留原始作者署名、贡献历史及 BSD-3-Clause 许可证。
