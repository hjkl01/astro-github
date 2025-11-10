---
title: pansou
---


# Pansou (fish2018/pansou)

**项目地址：** https://github.com/fish2018/pansou

## 主要特性

| 特色 | 描述 |
|------|------|
| 跨平台 | Windows / Linux / macOS |
| 命令行工具 | 纯命令行使用；支持参数化调用 |
| Baidu Pan 搜索 | 通过关键词在百度云盘中搜索文件或目录 |
| 文件管理 | 下载、上传、删除、移动、重命名等文件操作 |
| 结果导出 | 支持 JSON、CSV、TXT 等格式导出搜索结果 |
| 高并发下载 | 多线程/多进程下载加速 |
| API 代理 | 可配置 HTTP/HTTPS 代理，支持 SOCKS 方法 |
| 轻量易用 | 仅需 `pip install pansou`，无外部依赖 |

## 主要功能

- **搜索（`search`）**  
  在 Baidu Pan 上按关键词搜索文件/文件夹，支持正则、大小、时间过滤。

- **下载（`download`）**  
  下载单个或批量文件，支持断点续传。可指定本地保存路径。

- **上传（`upload`）**  
  上传本地文件至指定云盘路径，支持文件分块上传。

- **删除（`delete`）**  
  删除云盘文件/文件夹，支持递归删除。

- **移动/复制（`move` / `copy`）**  
  在云盘内部移动或复制文件/文件夹。

- **重命名（`rename`）**  
  修改云盘中文件/文件夹名称。

- **列表（`ls`）**  
  列出指定路径下的文件和文件夹信息。

- **统计（`stats`）**  
  输出云盘存储使用情况（已用空间、剩余空间、文件总数等）。

## 用法示例

```bash
# 1. 安装
pip install pansou

# 2. 搜索文件" --size-min 10M --size-max 100M

# 3. 下载搜索结果
pansou download -f results.txt -o ./downloads

# 4. 上传文件
pansou upload ./local/file.txt /remote/path/

# 5. 删除文件夹
pansou delete /remote/path/obsolete/ --recursive

# 6. 查看帮助
pansou --help
```

## 参数概览

| 参数 | 说明 |
|------|------|
| `pansou search [keyword]` | 按关键词搜索，并可使用 `--size-min`, `--size-max`, `--mtime` 等过滤器 |
| `pansou download -f file_list.txt -o /dest/` | 从列表文件中批量下载，`-o` 指定本地目录 |
| `pansou upload /src/file /dest/` | 上传单个文件，支持 `--block-size` 指定分块大小 |
| `pansou delete /path/ [--recursive]` | 删除单个路径，递归使用 `--recursive` |
| `pansou help` | 查看所有可用命令和参数 |

## 配置

- `~/.pansou/config.yaml`（可选）  
  ```yaml
  proxy:
    http: http://127.0.0.1:1080
    https: https://127.0.0.1:1080
  threads: 8
  chunk_size_mb: 4
  ```

> 若不提供配置文件，默认使用系统网络环境和 4 条下载线程。

## 需求与依赖

- Python 3.8+  
- `requests`、`rich`、`tqdm`

```bash
pip install "pansou[cli]"
```

## 开发与贡献

- 关注报 Issues 以提交功能请求或 bug。  
- Pull Request 歡迎，包含单元测试与文档更新。

---  

> 该文件旨在快速入门，更多详细使用请参考项目 README 与官方文档。  
