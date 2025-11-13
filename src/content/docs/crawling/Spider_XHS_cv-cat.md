---
title: Spider
---

# Spider_XHS - 小红书爬虫

## 项目地址  
[https://github.com/cv-cat/Spider_XHS](https://github.com/cv-cat/Spider_XHS)

## 项目简介  
`Spider_XHS` 是基于 Python 的小红书（Xiaohongshu / 红人社区）数据爬取工具。它支持账号登录、自动管理 cookies、批量抓取笔记、图片、评论、点赞等信息，并将结果以 CSV 或 JSON 格式导出。项目采用模块化设计，方便扩展和二次开发。

## 主要功能  

| 功能 | 说明 |
|------|-----|
| **账号登录** | 支持手动扫码登录，自动保存并续期 cookies。 |
| **批量抓取笔记** | 按用户、标签、或关键词批量获取笔记列表及细节。 |
| **图片与视频下载** | 自动下载笔记中的所有图片与视频资源，支持多线程加速。 |
| **评论与点赞** | 可选抓取笔记下的所有评论及点赞数。 |
| **数据导出** | 支持 CSV/JSON/Excel 导出，字段可自定义。 |
| **调度与限速** | 内置请求限速，防止 IP 被封。 |
| **错误恢复** | 断点续爬，错误日志记录，自动重试。 |

## 使用方法  

1. **克隆仓库**  
   ```bash
   git clone https://github.com/cv-cat/Spider_XHS.git
   cd Spider_XHS
   ```

2. **安装依赖**  
   ```bash
   pip install -r requirements.txt
   ```

3. **配置文件**  
   编辑 `config.yaml`（示例见 `config.sample.yaml`）  
   - `cookies_path`：存放 cookies 的文件路径  
   - `download_dir`：图片/视频下载目录  
   - `log_level`：日志级别  
   - `max_threads`：并发下载线程数  
   - `request_interval`：请求间隔（秒）

4. **账号登录**（首次使用）  
   ```bash
   python spider_xhs.py login
   ```  
   扫码完成后，cookies 会保存到 `cookies_path`。

5. **开始抓取**  
   - 按用户抓取：  
     ```bash
     python spider_xhs.py crawl_user --user_id 123456
     ```
   - 按标签抓取：  
     ```bash
     python spider_xhs.py crawl_tag --tag '美食'
     ```
   - 按关键词搜索抓取：  
     ```bash
     python spider_xhs.py crawl_search --keyword '旅行'
     ```

6. **导出结果**  
   所有抓取的数据默认保存在 `output/` 目录下。  
   - CSV：`output/user_123456.csv`  
   - JSON：`output/user_123456.json`  

7. **查看帮助**  
   ```bash
   python spider_xhs.py -h
   ```

## 目录结构  

```
Spider_XHS/
├─ spider_xhs.py           # 主入口脚本
├─ config.yaml             # 配置文件
├─ requirements.txt        # 依赖列表
├─ utils/                  # 通用工具模块
├─ crawler/                # 爬虫业务逻辑
├─ downloader/             # 下载工具
└─ tests/                  # 单元测试
```

## 开发与自定义

- **添加新功能**：继承 `BaseCrawler` 或 `BaseDownloader`，实现对应接口。  
- **自定义字段**：在 `config.yaml` 中设置 `export_fields`，可控制 CSV/JSON 输出字段。  
- **插件化**：将自定义爬虫模块放入 `plugins/`，项目启动时自动加载。

## 常见问题  

| 问题 | 解决方案 |
|------|----------|
| 登录失败 | 检查 `config.yaml` 的 `cookies_path` 是否可写，或重新执行 `login` 步骤。 |
| 被限流 | 调整 `request_interval` 或使用代理池（待支持）。 |
| 下载失败 | 检查网络，或设置 `max_threads` 为 1，逐个重试。 |

---
> 以上内容已保存在 `src/content/docs/00/Spider_XHS_cv-cat.md`。