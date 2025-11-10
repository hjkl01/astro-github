---
title: ngxtop
---

# ngxtop 项目概述

**项目地址：** [https://github.com/lebinh/ngxtop](https://github.com/lebinh/ngxtop)

## 主要特性
ngxtop 是一个基于 Python 的实时 Nginx 日志监控工具，它将 Nginx 的访问日志解析为结构化的数据，并提供类似 `top` 命令的交互式界面。主要特性包括：
- **实时监控**：实时读取和解析 Nginx 日志文件，支持高吞吐量日志处理。
- **交互式界面**：提供类似 `htop` 的终端界面，支持排序、过滤和聚合视图。
- **数据聚合**：自动聚合日志数据，按响应时间、状态码、请求路径、客户端 IP 等维度统计。
- **低资源占用**：高效的日志解析引擎，使用 Python 的正则表达式和多线程实现，适合生产环境。
- **自定义配置**：支持自定义日志格式、过滤规则和输出选项。
- **无外部依赖**：仅依赖 Python 标准库和少量第三方包（如 curses），易于安装和部署。

## 主要功能
- **日志解析**：支持标准 Nginx 日志格式（如 combined、common），自动提取字段如时间戳、请求方法、URL、状态码、响应大小、用户代理等。
- **视图显示**：默认视图包括总体统计、Top 请求路径、Top 状态码、Top 用户代理、Top 客户端 IP 等，支持热键切换。
- **过滤与排序**：使用热键（如 's' 排序、'f' 过滤）快速分析数据，支持正则表达式过滤。
- **聚合统计**：计算请求速率（RPS）、平均响应时间、错误率等指标。
- **退出与持久化**：支持保存当前视图到文件或重定向输出到其他工具。

## 用法
### 安装
ngxtop 通过 pip 安装：
```
pip install ngxtop
```

### 基本用法
运行命令时指定 Nginx 日志文件路径：
```
ngxtop -l /var/log/nginx/access.log
```
- `-l, --log`：指定日志文件路径（必需）。
- 默认启动交互式界面，按 'q' 退出。

### 常用选项
- `-f, --format`：指定日志格式，例如 `-f '$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent"'`。
- `-t, --top`：指定 Top N 条目，例如 `-t 10` 显示 Top 10。
- `-d, --duration`：聚合时间窗口（秒），默认 1 秒。
- `--no-report`：禁用汇总报告。
- `--fields`：自定义显示字段，例如 `--fields status,request`。
- 示例：监控并过滤 5xx 错误
  ```
  ngxtop -l /var/log/nginx/access.log --filter 'status >= 500'
  ```

### 交互界面热键
- `↑/↓`：导航条目。
- `s`：切换排序字段。
- `f`：应用过滤器。
- `r`：刷新视图。
- `q/Esc`：退出。

更多细节请参考项目 README。