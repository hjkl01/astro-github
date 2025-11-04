
---
title: Xget
---


# Xget

[GitHub Repository](https://github.com/xixu-me/Xget)

## 主要特性

- **仓库信息抓取**：一次性获取指定 GitHub 仓库的全部公开信息（项目描述、README、标签、分支、Golang 模块信息等）。  
- **Release 资源下载**：支持按仓库或 tag 直接下载 Release 的所有发行包，支持多线程并发、断点续传以及重试机制，极大提升大文件下载效率。  
- **Issue 与 PR 解析**：能够按标签、状态或作者筛选 Issues 与 PR，并导出为 Markdown/JSON/CSV 格式，方便后续分析。  
- **搜索与索引**：对仓库内文件、代码、注释等内容进行快速搜索，支持正则与模糊匹配。  
- **缓存与配置**：自动缓存请求结果，减少重复网络调用；支持自定义配置文件（`config.yaml`）以方便批量批处理或持续集成。  
- **Python API 与 CLI**：同时提供命令行工具与 Python API，既可在脚本中调用，又能快速集成到工作流程。

## 功能示例

### 1. 查看仓库基本信息

```bash
xget info --repo=xixu-me/Xget
```

输出包括项目名称、描述、创建日期、更新日期、主要语言、Stars/Watchers/Forks 等。

### 2. 下载指定 Release 的全部资产

```bash
xget download --repo=xixu-me/Xget --tag=v1.0.0
```

支持多线程并行下载，控制最大线程数：

```bash
xget download --repo=xixu-me/Xget --tag=v1.0.0 --threads=8
```

### 3. 批量下载某个账户下所有 Release

```bash
xget batch --user=xixu-me --folder=downloaded
```

所有 Release 依次下载到 `downloaded/` 目录下。

### 4. 导出 Issues 与 PR

```bash
xget export --repo=xixu-me/Xget --issues --pr --output=./data
```

会生成 `issues.json`, `prs.json`，可根据需求进一步处理。

### 5. 使用 Python 调用

```python
from xget import Xget

client = Xget()
repo_info = client.get_repo_info('xixu-me', 'Xget')
print(repo_info['description'])
```

## 安装

```bash
pip install xget
# 或使用 Go 安装
go install github.com/xixu-me/Xget@latest
```

> 详细安装与使用文档请参阅官方 README 或 `--help`。

---

> **路径**: `src/content/docs/00/Xget_xixu-me.md`
