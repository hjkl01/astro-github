
---
title: bruno
---

# Bruno 项目

**GitHub 项目地址:** [https://github.com/usebruno/bruno](https://github.com/usebruno/bruno)

## 主要特性
Bruno 是一个开源的 API 客户端工具，类似于 Postman，但以本地优先、文件为基础的设计为核心。它的主要特性包括：
- **本地存储**：所有 API 请求和集合以纯文本文件（JSON 格式）存储在本地，支持版本控制（如 Git），无需云端依赖。
- **跨平台支持**：基于 Electron 构建，支持 Windows、macOS 和 Linux 系统。
- **脚本支持**：内置 JavaScript 脚本引擎，支持在请求前/后执行自定义脚本，实现自动化测试和数据处理。
- **环境变量**：支持多环境配置（如开发、生产），便于切换不同 API 端点。
- **团队协作**：通过 Git 集成，实现版本管理和团队共享，无需额外订阅。
- **HTTP/GraphQL 支持**：全面支持 RESTful API、GraphQL 查询，以及 WebSocket 等协议。
- **插件扩展**：可通过社区插件扩展功能，如 OAuth 认证、数据生成器等。
- **离线可用**：完全本地运行，不依赖网络连接。

## 主要功能
- **API 请求构建**：支持 GET、POST、PUT、DELETE 等方法，轻松构建和发送 HTTP 请求。
- **集合管理**：组织多个相关请求成集合，支持文件夹结构和批量运行。
- **响应处理**：实时查看响应数据、状态码、响应时间，并支持格式化 JSON/XML 等。
- **测试与调试**：内置断言功能，用于自动化验证 API 响应；支持变量插值和动态数据生成。
- **导入/导出**：可从 Postman、Insomnia 等工具导入集合，或导出为文件/CLI 命令。
- **CLI 工具**：提供命令行接口（Bruno CLI），适合 CI/CD 集成和自动化脚本。
- **安全性**：支持多种认证方式，如 Basic Auth、Bearer Token、OAuth 2.0。

## 用法
1. **安装**：
   - 从 GitHub Releases 下载对应平台的安装包，或使用包管理器（如 Homebrew：`brew install --cask bruno`）。
   - 安装后启动应用。

2. **创建项目**：
   - 打开 Bruno，新建一个项目（Project），它会生成一个本地目录存储文件。
   - 使用 Git 初始化仓库：`git init` 以启用版本控制。

3. **构建请求**：
   - 在项目中右键新建请求（Request）。
   - 输入 URL、方法，选择 Headers、Body（支持 form-data、JSON 等）。
   - 添加环境变量：在项目设置中定义变量，如 `{{baseUrl}}`。

4. **运行和测试**：
   - 点击“Send” 发送请求，查看响应。
   - 添加脚本：在 Pre-request 或 Post-response 标签中编写 JS 代码，例如：
     ```javascript
     // Pre-request 示例：设置动态变量
     bruno.setVar('timestamp', Date.now());
     ```
   - 运行集合：右键集合选择“Run Collection” 执行批量测试。

5. **协作与导出**：
   - 提交文件到 Git 仓库，与团队共享。
   - 导出：选择请求/集合导出为 JSON 文件或 cURL 命令。

Bruno 适合开发者和测试人员，用于高效的 API 开发和调试，强调隐私和可移植性。更多细节请参考官方文档。