# 文档站：预览与发布

MySciAgent 使用 MkDocs Material 将本仓库的 Markdown 文档生成可搜索的静态站点，提供侧边导航、页面目录、代码复制和明暗主题。

计划的 GitHub Pages 地址为 **`https://zhuanglaihong.github.io/mysciagent/`**。该地址是发布目标；本地预览成功与线上发布完成分别确认。

## 1. 本地预览

在仓库根目录执行：

```bash
uv sync --group docs
uv run mkdocs serve --dev-addr 127.0.0.1:8766
```

打开 **http://127.0.0.1:8766/mysciagent/**，或使用命令输出的 Local URL。修改 `docs/` 或 `mkdocs.yml` 后，预览会自动重新构建。

## 2. 构建检查

```bash
uv run mkdocs build --strict
```

生成文件位于 `site/`，该目录不入 Git。文档页面必须登记到 `mkdocs.yml` 的导航，使用相对 Markdown 链接连接各页。

## 3. 准备 GitHub Pages

先审阅并确认需要发布的文档，再提交推送。随后在仓库的 **Settings → Pages → Build and deployment** 中选择 **GitHub Actions**，并启用文档工作流。

GitHub Pages 对公有仓库和私有仓库有不同的账号计划要求。当前仓库是私有仓库，正式启用前需核对账号是否支持私有仓库 Pages；详情见 [GitHub Pages 官方说明](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)。站点发布内容以最终选择的 Pages 访问方式为准。

## 4. 手动发布

工作流位于 `.github/workflows/docs.yml`。普通提交与 PR 只构建检查；部署通过 **Actions → docs → Run workflow → main** 手动触发。这样可以先审阅修改，再决定何时发布。

成功后检查部署任务返回的实际 Pages URL。计划地址、配置了 `site_url` 或本地构建成功，都不能单独说明网站已上线。

## 5. 后续维护

| 要修改的内容 | 文件 |
|---|---|
| 网站首页 | `docs/index.md` |
| 能力与仓库 | `docs/capabilities.md`、`docs/repositories.md` |
| 页面内容 | 对应的 `docs/*.md` |
| 名称、主题与导航 | `mkdocs.yml` |
| 首页样式与图标 | `docs/stylesheets/extra.css`、`docs/assets/logo.svg` |

站点只使用本仓库文档构建，不需要另外维护一套网页内容。上游同步方式见 [同步与查看更新](upstream-sync.md)。
