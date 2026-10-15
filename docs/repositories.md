# 仓库配合

MySciAgent 负责组织 Agent、配置、工具连接与运行管理。文献、信息、知识库和事务工具由各组件仓库提供，通过构建上下文、目录挂载或 MCP 配合。

## 组件与服务关系

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

## 仓库来源与接入方式

| 组件 | 用途与接入方式 | 来源 |
|---|---|---|
| mylibrary | 构建 Hermes / Zotero MCP 时使用文献工具与流水线源码 | [个人副本](https://github.com/zhuanglaihong/mylibrary) |
| dailyinfo | 信息源、抓取和摘要；配合 RSS、调度与推送 | [个人仓库](https://github.com/zhuanglaihong/dailyinfo) |
| aisecretary | 构建独立 MCP 服务，提供事务持久化 | [个人副本](https://github.com/zhuanglaihong/aisecretary) |
| yuque_mcp_server | 构建语雀 MCP，按运行要求检查源码版本 | [个人副本](https://github.com/zhuanglaihong/yuque_mcp_server) |
| git-contribution-stats | 仓库统计与 repo-scanner MCP | [团队源码](https://gitcode.com/dlut-water/git-contribution-stats) |
| zhixun-agent | 团队服务：知汛独立栈使用的水文 MCP | [团队源码](https://gitcode.com/dlut-water/zhixun-agent) |
| server-monitoring | 独立团队服务，天一通过已配置端点调用 MCP | [团队源码](https://gitcode.com/dlut-water/server-monitoring) |

编码技能和论文下载等依赖也登记在 [组件清单](https://github.com/zhuanglaihong/mysciagent/blob/main/repositories.json)。来源链接用于定位组件，是否能取得和版本是否兼容以 [依赖预检](setup.md#component-preflight) 为准。

## 路径与数据

建议将主仓和组件放在 `~/code/` 下；启动脚本按该位置检查默认组件。Agent 配置与数据分别保存在 `~/.hermes`、`~/.claude`、`~/.cc-connect`、`~/.openclaw` 和 `~/.myagentdata` 等目录，完整挂载关系见 [架构](architecture.md)。

账号、文献库、仓库列表、知识库、专业服务地址与推送目标使用自己的配置。团队案例的身份与内网环境属于案例本身，参见 [团队应用](team-use-cases.md)。

## 取得与检查源码

```bash
CODE_DIR="$HOME/code" ./scripts/clone-deps.sh
python3 scripts/repositories.py --check --directory "$HOME/code"
```

克隆工具保留已有工作区；完整主栈需满足默认清单的来源与版本要求。详细准备步骤见 [快速开始](setup.md)，换机差异见 [可移植性](portability.md)。
