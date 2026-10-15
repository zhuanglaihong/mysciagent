# 仓库迁移记录

记录日期：2026-10-14。目标账号：`zhuanglaihong`。主仓和新复制的组件仓库均设为私有；复用仓库的可见性未改变。

## 平台基线

`OuyangWenyu/myopenclaw` 的 `main` 提交 `2dccce2b9370c83eec8e5823ebdacf7e6cbcb00b` 已复制到 `zhuanglaihong/mysciagent`。原始提交和 LICENSE 保留，本次集成改动在其后独立提交。源码范围为 Git 跟踪的内容，不含原作者本机账号、环境、数据库、模型密钥和运行数据。

## 组件状态

| 目标个人仓库 | 来源 | 状态与版本 |
|---|---|---|
| [mysciagent](https://github.com/zhuanglaihong/mysciagent) | OuyangWenyu/myopenclaw | 已创建并保留历史；本次集成基线 |
| [dailyinfo](https://github.com/zhuanglaihong/dailyinfo) | 已有个人仓库 | 复用 `fba6001`；未改远端、未覆盖源码、未合并上游 |
| [mylibrary](https://github.com/zhuanglaihong/mylibrary) | iHeadWater/mylibrary（旧 OuyangWenyu 地址已重定向） | 已复制 `6566421`，全部分支和标签 refs 已核对 |
| [aisecretary](https://github.com/zhuanglaihong/aisecretary) | iHeadWater/aisecretary | 已复制 `c50997e`，全部分支和标签 refs 已核对 |
| [everything-claude-code](https://github.com/zhuanglaihong/everything-claude-code) | affaan-m/everything-claude-code（重定向 ECC） | 已复制 `b92f181`，91 个分支/标签 refs 已核对；继承 Dockerfile 直接依赖 |
| [yuque_mcp_server](https://github.com/zhuanglaihong/yuque_mcp_server) | 已有本地 GitCode checkout | 已复制提交 `b7fe24e`，保留原本地工作区；无法核对最新上游 |
| `git-contribution-stats` | GitCode dlut-water；旧 GitHub 地址 404 | 未创建：HTTPS/SSH 无法连接，未取得源码 |
| `zhixun-agent` | OuyangWenyu/zhixun-agent | 未创建：GitHub 404，需可访问来源；可选水文助手 |
| `server-monitoring` | GitCode dlut-water/server-monitoring | 未创建：无法连接；上游按外部服务消费，可选 |
| `paper-fetch` | Agents365-ai/paper-fetch | 未创建：GitHub 404；继承启动脚本会自动拉取此 skill |

未创建项的个人 URL 在清单中仅代表计划目标，不能当作存在的仓库或可用功能。没有创建空仓库来代替真实源码。

## 语雀兼容性缺口

本地快照 `b7fe24e` 不含继承 compose 所需的根目录 Dockerfile，也不含上游守卫要求的 `bfc55d7d4a019859eb2cd30a040c52126895192a` 提交。本次仅保存可取得的内容，不修改 pin、不改测试阈值来掩盖差异。需要取得匹配源码，再审查版本和运行协议。

原来的 `D:/project/Agent/yuque_mcp_server` 保留 GitCode origin；新个人副本可克隆到独立组件目录进行后续开发，避免修改用户已有工作区。

## 已修改的对接位置

依赖清单和克隆入口统一使用 `repositories.json` 与 `scripts/repositories.py`；私有组件使用个人 GitHub 地址。Hermes / Zotero MCP 的文献库 fallback、编码技能库构建来源、论文下载 skill 获取地址均指向个人命名空间；未取得的论文下载源仍为显式阻塞，未伪造可用性。

历史上游文档中的原始出处、许可证和运行时 `myopenclaw` 标识保留。新 README、文档首页、项目元数据和部署入口使用 MySciAgent 名称。底层 Hermes/OpenClaw/Claude Code 与普通软件包、基础镜像仍从各自上游分发，不把所有第三方库复制成个人项目。

## 当前验证边界

仓库复制已验证 Git 提交与分支/标签一致。新增仓库已关闭继承 Actions，避免尚未配置的上游发布/自动化直接运行。部署所需的真实凭据和服务未启用；Windows 环境未发现 Docker CLI，因此没有容器构建或端到端模型调用结论。

运行 `python scripts/repositories.py --check --json` 可复查实际本地源码就绪状态；该命令会诚实报告缺失依赖、远端不匹配及语雀版本差异。

本次检查结果：

| 检查 | 结果 |
|---|---|
| 个人仓库与 Git refs | 新建的 5 个仓库均可读取、私有；组件复制 refs/HEAD 已核对 |
| 脚本与清单 | start.sh / clone-deps.sh 的 Bash 语法、repositories.py 的 Python 语法、9 项组件清单及个人地址通过 |
| 文档构建 | `PYTHONUTF8=1 python -m mkdocs build --strict` 通过 |
| 语雀兼容守卫 | `PYTHONUTF8=1 uv run --with pytest --with pyyaml python -m pytest tests/test_yuque_mcp_local.py -q`：18 passed、2 skipped、1 failed；唯一失败是本地旧版本与所需 pin 不一致，未掩盖 |
| 部署与模型调用 | 未运行：依赖缺口尚在、当前环境无 Docker CLI |

Windows 下继承测试使用默认编码读取 UTF-8 文件时会遇到 GBK 解码错误；设置 `PYTHONUTF8=1` 后完成上述验证。GitHub Actions 未执行本地检查；本地结果与 CI 状态分别记录。

## 产品策略更新（2026-10-15）

用户确认可自行实现缺失能力。上表继续保留真实复制状态；缺失仓库不再作为科研产品建设必须等待的前置条件。具体功能映射、最小替代方案和优先级见 [规划中的依赖处理原则](research-platform-roadmap.md)。

本次仅修改规划。默认 Compose 和源码预检仍会报告实际缺口；后续将通过最小部署裁剪、替代工具及对应验证来解除，不直接修改清单把不可用项标为就绪。

## 后续处理顺序

1. 登记本人实际应用和科研资源，选择第一条真实工作流程。
2. 按该流程裁剪继承部署，替换缺失的必需工具；同步修改配置、清单和验证。
3. 根据本人实际应用、模型和服务器配置凭据；启动最小服务集并验证工具连接。
4. 按 [科研平台规划](research-platform-roadmap.md) 的阶段 1 跑通流程，再增加辅助能力；可取得的上游源码继续保留来源并按需复用。

## 上游更新与部署目标（2026-10-15）

已将上游新增的 9 个提交同步至 `1948e9826372c45941b6673e41b4763e32772bf6`，包含接入自检、端点参数化、兜底修复和个人/团队文档分界。保留 MySciAgent 的产品说明、个人仓库地址和研究规划；历史上游 README 不作为当前部署说明参与产品文档守卫。成员配置示例中的原作者内网端点改为空值，等待用户配置实际服务。

用户指定使用运行 hydromodel 的 Linux 服务器，已通过 SSH 只读检查确认。该机有 Podman 3.4.2、uv 与 Python 3.11/3.12，无 Docker/Compose 命令；现有 hydromodel 有未提交修改。下一步按 [Linux 落地计划](linux-delivery-plan.md) 采用独立环境和工作区，优先适配已有 hydrosystem，服务器安装和服务运行尚未执行。

同步时运行四组检查：最初 137 passed、7 skipped、5 failed。5 项失败均为未改动的备份脚本行为测试在 Windows 找不到 Bash，不能作为 Linux 运行结论；新接入、自检、文档和兜底的独立检查为 101 passed、6 skipped（无 live 配置），未触网调用模型。Shell 语法与 MkDocs 严格构建通过。
