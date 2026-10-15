# 快速开始

按下面五步准备自己的模型、资料和工具，部署 MySciAgent 的完整容器主栈。希望复用现有 Agent 工具的读者，可先阅读 [个人接入指南](personalize.md)，再选择所需接入。

天一、知汛与水文服务的具体配置归入 [团队应用案例](team-use-cases.md)。个人部署使用自己的机器人身份、仓库、知识库和资料路径。

## 1. 准备运行环境

| 项目 | 要求 |
|---|---|
| 容器环境 | Linux 的 Docker Engine + Compose 插件，或已运行的 Docker Desktop；使用 Bash 执行脚本 |
| Python 与 Git | 项目环境使用 Python 3.12+；需要 `python3`、Git，以及所需组件仓库的读取权限 |
| 模型 | 默认配置使用 `DEEPSEEK_API_KEY`；使用其他服务时，同时调整对应 Agent 的模型端点与配置 |
| 交互入口 | 选择自己常用的终端、飞书或 Discord；消息渠道需要自己的应用或频道凭据 |
| 科研资源 | 准备自己的代码仓库、资料目录和希望启用的工具；云盘账号用于可选的附件同步或备份 |

项目不收取平台使用费；模型 API、计算资源及第三方服务按你的选择计费。Linux 上的系统调度与 macOS 的 launchd 配置分别见 [调度系统](scheduling.md)。

## 2. 获取项目并填写自己的配置

```bash
mkdir -p ~/code
cd ~/code
git clone https://github.com/zhuanglaihong/mysciagent.git
cd mysciagent
cp .env.example .env
```

`.env.example` 包含具体应用场景的示例值，复制后按自己的资源修改：

| 配置范围 | 需要填写或核对的内容 |
|---|---|
| 模型 | `DEEPSEEK_API_KEY`；其他供应商的 key、端点和模型名按所选 Agent 的配置处理 |
| 对话与通知 | 所用渠道的 App ID / Secret / Token、接收者和账号白名单；只填写自己要使用的渠道 |
| 文献与知识 | 自己的 Zotero 库、附件目录、语雀知识库；尤其替换 `YUQUE_CHANGE_REPOS_JSON` 中的团队示例 |
| 代码与环境 | 自己的 Git 凭据、仓库目录、数据路径和挂载；路径关系见 [架构](architecture.md) 与 [可移植性](portability.md) |
| 日常事务 | 自己的邮箱、待办和推送目标；未使用的接入无需填写业务凭据 |

各框架的配置模板分别在 `hermes/`、`claude/config/` 和 `openclaw/config/`。检查机器人名称、Agent 身份与任务说明是否适合自己的用途；已有运行配置不会全部被模板覆盖。

云盘备份按需配置：

```bash
cp .cloud.conf.example .cloud.conf
# 编辑为自己实际存在的云盘目录，然后配置备份路径
./scripts/setup-cloud.sh
```

不使用云盘时可跳过；启用备份时需核对实际写入位置，详见 [备份系统](backup.md)。

<a id="component-preflight"></a>

## 3. 准备组件并检查依赖

完整主栈通过 `repositories.json` 登记组件来源与版本。克隆工具读取清单，保留已有工作区，不会更新或重置其中的代码。

```bash
# 按清单取得可访问的组件，放在启动脚本使用的 ~/code 下
CODE_DIR="$HOME/code" ./scripts/clone-deps.sh

# 只读检查源码、远端和版本，不启动服务
python3 scripts/repositories.py --check --directory "$HOME/code"
```

完整启动需要清单中 `required_for_default_stack` 为 `true` 的组件通过检查。遇到 `missing`、`source_unavailable`、`version_mismatch` 或 `origin_mismatch` 时，按报告补齐源码、访问权限、版本或独立的个人副本后再启动；组件状态见 [迁移记录](migration-status.md)。检查通过仅表示源码准备完成，还要继续验证凭据、模型与工具。

**启动范围：** `scripts/start.sh` 会检查默认主栈依赖，并执行完整的 `docker compose up`。没有填写某个工具的业务凭据，并不会自动从主栈移除该容器；选择部分能力的部署裁剪设计见 [Linux 落地计划](linux-delivery-plan.md)。

## 4. 启动完整主栈

依赖检查通过、自己的配置准备完成后执行：

```bash
# 首次构建，或镜像定义变更后
./scripts/start.sh --build

# 后续启动
./scripts/start.sh
```

启动脚本会准备配置模板、工具目录、密钥传递和部分定时任务。它会读取已有运行配置，默认按多 Agent 与多工具的主栈启动。服务端口、持久化路径和网络见 [架构](architecture.md)。

## 5. 检查模型、工具和任务输出

```bash
docker compose ps
docker compose logs --tail=100 hermes
docker compose exec hermes /opt/hermes/.venv/bin/hermes mcp list
```

先从自己的入口完成一次真实任务：读取指定资料，调用已连接工具，把结果保存到自己的笔记或项目目录。核对来源、输出位置和运行记录；容器状态正常或工具列在配置中，不能单独证明任务可用。

文献连接见 [Zotero](zotero-cli-cc.md)，消息入口见 [Hermes 渠道](hermes-channels.md) 与 [OpenClaw 渠道](openclaw-channels.md)，跨会话记录见 [长期记忆](tdai-memory.md)。

## 后续扩展

| 需要加入的内容 | 操作入口 |
|---|---|
| 信息源、待办与邮件 | [dailyinfo](dailyinfo.md) · [aisecretary](aisecretary.md) · [邮件](email.md) |
| 定时通知与运行管理 | [调度](scheduling.md) · [监控](monitoring.md) · [备份](backup.md) |
| 自己的课题组共享服务 | [团队应用案例](team-use-cases.md) · [团队部署](server-deploy.md) |
| 领域工具参考 | [知汛助手](zhixun-feishu-bot.md)，对应 [zhixun-agent](https://gitcode.com/dlut-water/zhixun-agent) 水文 MCP；其他专业可以接入自己的服务 |
| 实验协调、Paper2Code 等设计 | [科研助手规划](research-platform-roadmap.md) · [研究引擎接入](research-engine-integration.md) |

## 日常命令

```bash
./scripts/stop.sh                         # 停止主栈
docker compose ps                        # 查看状态
docker compose logs -f claude-code       # 查看编码 Agent 日志
```

换机恢复自己的数据和配置时，按 [备份与恢复](backup.md) 操作。天一与知汛是独立的应用栈，相关启动命令见 [团队部署案例](server-deploy.md) 及 [知汛助手](zhixun-feishu-bot.md)。
