---
title: social-auto-upload
---


# 社交自动上传（Social Auto Upload）

项目地址：<https://github.com/dreammis/social-auto-upload>

## 主要特性
- **目录监控**：实时**：内置 Twitter、Instagram、LinkedIn 等平台 SDK，支持图片、短视频等多媒体格式。
- **配置灵活**：通过 `config.yaml` 配置监控路径、平台凭证、发布内容模板；也可使用环境变量覆盖配置。
- **内容模板**：支持占位符（如 `{filename}`、`{created_at}`）的自定义发布正文。
- **日志与报告**：上传过程记录到 `upload.log`，支持生成 JSON/CSV 上传报告。

## 功能概览

| 功能 | 说明 |
|------|------|
| 目录监视 | 使用 `watchdog` 实时监听文件夹 |
| 平台 SDK | 通过官方 SDK 或 API 进行内容发布 |
| 配置管理 | `config.yaml` 主文件 + 环境变量可覆盖 |
| 日志记录 | 使用 `logging` 输出上传情况、错误信息 |
| 报告生成 | 支持导出上传报告（JSON/CSV） |

## 使用步骤

1. **克隆项目**
   ```bash
   git clone https://github.com/dreammis/social-auto-upload.git
   cd social-auto-upload
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **配置 `config.yaml`**  
   ```yaml
   watch_folder: /path/to/your/watched/folder
   platforms:
     twitter:
       api_key: YOUR_TWITTER_KEY
       api_secret: YOUR_TWITTER_SECRET
       access_token: YOUR_ACCESS_TOKEN
       access_secret: YOUR_ACCESS_SECRET
     instagram:
       client_id: YOUR_INSTAGRAM_CLIENT_ID
       client_secret: YOUR_INSTAGRAM_CLIENT_SECRET
       redirect_uri: YOUR_REDIRECT_URI
     linkedin:
       client_id: YOUR_LINKEDIN_CLIENT_ID
       client_secret: YOUR_LINKEDIN_CLIENT_SECRET
       access_token: YOUR_LINKEDIN_ACCESS_TOKEN
   publish_template: "New post: {filename} at {created_at}"
   ```

4. **运行主程序**
   ```bash
   python auto_upload.py
   ```
   或指定配置文件：
   ```bash
   python auto_upload.py --config config.yaml
   ```

5. **查看日志**  
   上传日志记录在 `upload.log`，包含成功与失败信息。

## 扩展说明

- **新增平台**：在 `platforms/` 目录添加对应 SDK，并实现 `_upload_<platform_name>` 方法；在 `config.yaml` 中添加凭证配置。
- **自定义模板**：修改 `templates/` 目录下的模板文件，支持更多占位符。
- **错误处理**：程序捕获常见 API 错误并自动重试，必要时可通过 `config.yaml` 调整重试策略。

```
