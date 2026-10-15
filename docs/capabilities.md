# 能力地图

这张表列出仓库基础配置中的 Agent、工具与运行能力。文献、知识库、通知和领域数据都可使用自己的资源；天一、知汛及标有 🌐 的条目对应 [团队应用案例](team-use-cases.md)。

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
| 🌐 研发日报 | repo-scanner MCP 采集配置的仓库 → Hermes skill → 飞书推送；天一 bot 复用同源读能力（团队服务，部署见 [server-deploy](server-deploy.md)） | [git-contribution-stats](https://gitcode.com/dlut-water/git-contribution-stats) |
| 🌐 水文智能问答 | zhixun 知汛助手 — OpenClaw + zhixun-water-mcp → 飞书 bot（**团队公共 bot**；背后的 zhixun-agent 水文 MCP 即**团队服务**；独立栈，部署参考见 [server-deploy](server-deploy.md)） | [zhixun-agent](https://gitcode.com/dlut-water/zhixun-agent) |
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

## 如何选择

先用 [个人接入指南](personalize.md) 明确自己的任务，再按 [快速开始](setup.md) 配置入口与工具。组件如何与主仓配合见 [仓库关系](repositories.md)，运行拓扑与数据目录见 [架构](architecture.md)。

表格描述组件及其用途，具体实例需完成自己的凭据、来源、路径与运行验证。完整默认主栈的依赖检查仍按部署指南执行。
