# MySciAgent 与 myopenclaw 如何共同更新

## 两个地址，保留一条共同历史

| Git 远端 | 地址 | 用途 |
|---|---|---|
| origin | https://github.com/zhuanglaihong/mysciagent.git | 自己的产品、功能、配置和文档 |
| upstream | https://github.com/OuyangWenyu/myopenclaw.git | 上游公共改进与修复 |

MySciAgent 是个人独立仓库，GitHub 没有将其标记为 Fork；但复制时保留了原始提交历史，也已经合并过上游更新。因此可以继续使用 Git merge 同步，不依赖 GitHub 的 Sync fork 按钮。

## 怎么知道谁更新了

在 MySciAgent 根目录运行：

```bash
python scripts/upstream_status.py --fetch
```

Linux 若使用独立 Python，可用该环境的 python 或 `uv run --python 3.12 python scripts/upstream_status.py --fetch`。

| 输出 | 含义 |
|---|---|
| Upstream updates not integrated | myopenclaw 有多少提交尚未合入当前分支 |
| Personal-only commits | 当前分支有多少提交只属于自己这一侧；包含合并提交，不等于功能数量 |
| Local commits not pushed | 当前分支有多少提交尚未推到个人 origin/main |
| Personal remote updates not integrated | 自己的 GitHub main 比当前分支多出的提交，例如在其他电脑上推送的工作 |
| Working tree has changes | 本地是否有尚未提交的修改 |

`--fetch` 只更新本地的远端记录，不合并、不改工作区、不推送。没有 `--fetch` 时读取缓存，不能据此判断远端刚刚是否更新。脚本比较当前 HEAD 与两边 main；支持 `--json` 保存机器可读结果。

也可以查看原始 Git 信息：

```bash
git log --oneline HEAD..upstream/main
git log --oneline upstream/main..HEAD
git log --oneline origin/main..HEAD
```

## 怎么安全同步

先确认工作区干净，并把自己的修改正常提交；不要在不清楚当前状态时重置代码。下面是一轮人工审阅同步的步骤：

1. 运行查更新命令，确认上游提交内容以及自己是否有未推送工作。
2. 用 `git switch main` 切回自己的 main，再创建独立分支，例如 `git switch -c codex/sync-myopenclaw-20261015`。每次用一个未占用的新名字。
3. 执行 `git merge upstream/main`。能自动合并的部分由 Git 处理；有冲突时逐个审阅文件并解决。
4. 检查个人仓库地址、凭据模板、工具注册、启动配置和 README，运行相关测试与文档构建，提交合并结果。
5. 审阅后合入自己的 main 并推送 origin。团队协作时可在第 4 步提交 PR 进行评审。

同一段代码两边都改时可能产生冲突。Git 会指出文件和冲突位置，但不能保证自动判断哪一侧符合产品目标。MySciAgent 的定位、个人路径、仓库归属和新增科研功能需要保留；上游修复需要结合自己的设计吸收。少量不合适的改动可以延后或选择性引入，避免整文件覆盖。

## 后续自己的设计放在哪里

MySciAgent 的产品说明放 README 和自己的设计文档；新增科研协调、领域适配与实验管理放独立模块。继承的基础运行代码尽量做小范围修改，配置值使用个人覆盖层和环境变量，减少长期合并冲突。具体采用哪些模块，以实现后的运行验证为准。

每次同步应记录上游 commit、自己提交的变更、冲突处理和验证结果。平台仓的同步不会自动同步 mylibrary、dailyinfo 等组件，各组件保留各自 origin/upstream 和版本记录。新增功能、底层依赖或多仓库接口变化，都需要单独验证兼容性。

## 当前检查方式

本仓已提供手动查更新脚本，未安排定时运行或自动合并。上游更新不代表必须立即升级；先看差异，再决定是否纳入自己的版本。
