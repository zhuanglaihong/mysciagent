# 团队应用案例：iHeadWater

本页记录 iHeadWater 在实际科研环境中使用的助手、服务与工具组合，供搭建个人科研助手时参考。团队的专业方向、机器人名称、知识库和内网服务属于具体应用配置；通用的工具连接、角色分工、记录、简报与通知方式可以复用到自己的工作中。

首次搭建自己的助手请从 [个人接入指南](personalize.md) 和 [快速开始](setup.md) 开始。

## 团队能力地图

🌐 表示团队服务案例；公共 bot 是使用这些服务的入口。

| 团队服务 | 在实际工作中的用途 | 可迁移到自己的能力 |
|---|---|---|
| 🌐 语雀知识库 | 阅读团队知识、跟踪文档变更，供个人助手和天一查询 | 接入自己的笔记或知识库，整理资料与行动项 |
| 🌐 研发日报 | repo-scanner 读取团队仓库信息，天一查询研发进展并协助处理 Issue | 换成自己的仓库、任务和汇报目标 |
| 🌐 服务器监控 | 天一接入 server-monitoring MCP，查询服务器、任务与服务状态 | 接入自己已有的计算环境监控与运行记录 |
| 🌐 水文智能问答 | 知汛通过 zhixun-agent 水文 MCP 查询专业数据与业务信息 | 换成自己专业领域的 MCP、API 或分析工具 |

团队服务包括语雀、仓库统计、服务监控与水文 MCP；公共 bot 包括 **天一、知汛**。成员直接连接的三项能力是语雀、仓库统计和服务监控，水文能力通过知汛使用，不在成员直连清单中。

## 这些工具怎样串起来

| 工作环节 | 团队中的组合 | 读者可以替换的内容 |
|---|---|---|
| 信息与文献 | dailyinfo、Zotero / mylibrary、论文清单、笔记 | 关注的信息源、课题论文、个人文献库与保存目录 |
| 编程与研究记录 | 编码 Agent、Git 仓库、测试和实验日志 | 自己的项目、环境、运行命令、指标与结果位置 |
| 项目跟进 | 天一、仓库统计、语雀、服务器监控 | 自己的机器人身份、仓库列表、知识库与监控端点 |
| 日常事务 | aisecretary、邮件、定时简报和推送 | 自己的待办、邮箱、提醒时间和推送渠道 |
| 领域数据查询 | 知汛与水文 MCP | 自己专业的服务、工具说明和数据权限 |

例如，“整理今天的课题进展”可以组织为：从文献和笔记读取新增内容，读取仓库与运行记录，汇总已完成事项和未解决问题，再保存为自己的工作记录。具体数据由已接入的工具提供；同样的组织方式可以用于其他课题。

## 组件关系

```text
mysciagent/              ← Agent 编排、工具连接、配置与运行管理
mylibrary/               ← Zotero 文献工具
dailyinfo/               ← 信息聚合（独立配置来源与推送）
aisecretary/             ← 事务记录 MCP
yuque_mcp_server/        ← 语雀知识库 MCP
git-contribution-stats/  ← 仓库统计 MCP
server-monitoring/       ← 团队服务：独立部署的服务器监控 MCP
zhixun-agent/            ← 团队服务：知汛背后的水文 MCP
```

主栈通过构建上下文、目录挂载和 MCP 使用组件；`server-monitoring` 由独立服务提供，天一作为客户端接入。团队服务的地址、认证方式与访问范围由其维护者提供。

## 部署与接入参考

| 场景 | 阅读入口 |
|---|---|
| 公共 bot 天一、知汛与团队服务的部署边界 | [团队部署案例](server-deploy.md) |
| 天一使用的研发日报与知识库 | [研发日报](daily-dev-report.md) · [语雀接入](yuque-mcp-hermes.md) |
| 知汛与水文 MCP | [知汛助手](zhixun-feishu-bot.md) · [zhixun-agent 源码](https://gitcode.com/dlut-water/zhixun-agent) |
| 服务器运行情况 | [服务器监控 MCP](server-monitoring-mcp.md) |
| 成员直连工具的连通与认证检查 | [member-check](member-check.md) |

团队案例的复制范围和组件源码状态见 [迁移记录](migration-status.md)。案例展示团队的实际用法，部署自己的实例时仍需配置自己的模型、账号、资料路径与服务。

## 团队应用的启动参考

### 天一：研发协作入口

按 [团队部署](server-deploy.md) 准备共享网络和服务。现有 `start-tianyi-bot.sh` 会检查主栈的 `repo-scanner-mcp` 是否运行，使用脚本前须满足该前置条件。

```bash
cp .env.tianyi-bot.example .env.tianyi-bot
# 填写自己的飞书应用凭据、模型 key，以及实际服务端点和账号配置
./scripts/start-tianyi-bot.sh --build
```

### 知汛：领域工具接入示例

先取得所需的 `zhixun-agent` 源码，按 [知汛助手](zhixun-feishu-bot.md) 核对构建路径与配置。知汛使用独立 Compose 栈、网络和数据目录。

```bash
cp .env.zhixun-bot.example .env.zhixun-bot
# 填写自己的飞书应用凭据与模型 key
./scripts/start-zhixun-bot.sh --build
```

复用到其他专业时，保留“对话入口调用专业工具”的组织方式，替换领域服务、工具说明与应用配置。
