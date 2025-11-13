---
title: freenom
---

# Freenom 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/luolongfei/freenom)

## 主要特性
- **自动化域名管理**：支持Freenom免费域名（.tk、.ml、.ga、.cf、.gq）的自动化注册、续期和更新操作，减少手动干预。
- **命令行工具**：基于Python开发的CLI工具，便于脚本化和批量处理域名任务。
- **API集成**：模拟Freenom API接口，实现域名信息的查询、登录和操作自动化。
- **开源免费**：使用MIT许可，代码开源，用户可自由修改和扩展。
- **跨平台支持**：兼容Windows、Linux和macOS环境，通过pip安装即可使用。

## 主要功能
- **域名注册**：自动注册新的免费域名，支持指定域名和后缀。
- **域名续期**：监控域名到期时间，并自动续期以保持活跃状态。
- **域名更新**：批量更新域名DNS记录、所有者信息等。
- **信息查询**：获取域名列表、状态和过期日期。
- **登录管理**：处理Freenom账户登录，支持多账户管理。
- **错误处理**：内置重试机制和日志记录，处理网络错误和API限制。

## 用法
1. **安装**：
   - 确保Python 3.x环境。
   - 通过pip安装：`pip install freenom`。
   - 或从GitHub克隆仓库：`git clone https://github.com/luolongfei/freenom.git`，然后`cd freenom`并`pip install -e .`。

2. **配置**：
   - 创建配置文件`freenom.ini`或使用环境变量设置Freenom账户凭证（用户名、密码）。
   - 示例配置：
     ```
     [freenom]
     username = your_username
     password = your_password
     ```

3. **基本命令**：
   - **登录**：`freenom login`（首次使用需登录）。
   - **列出域名**：`freenom list`（显示所有域名信息）。
   - **注册域名**：`freenom register example.tk`（注册指定域名）。
   - **续期域名**：`freenom renew --domain example.tk`（续期单个域名）。
   - **更新DNS**：`freenom update-dns --domain example.tk --nameserver ns1.example.com`。
   - **批量操作**：使用`--all`标志处理所有域名，例如`freenom renew --all`。

4. **高级用法**：
   - 支持JSON输出：添加`--format json`获取结构化数据。
   - 脚本集成：导入模块如`from freenom import Freenom`，然后调用API方法。
   - 查看帮助：`freenom --help` 或 `freenom <command> --help`。

注意：使用前确保Freenom账户有效，遵守Freenom服务条款。项目可能需根据API变化更新。