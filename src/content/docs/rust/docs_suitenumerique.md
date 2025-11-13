---
title: docs
---

# La Suite Docs

**GitHub 项目地址：** [https://github.com/suitenumerique/docs](https://github.com/suitenumerique/docs)

## 主要特性

- **协作文本编辑**：Docs 是一个协作文本编辑器，旨在解决知识构建和分享中的常见挑战。
- **实时协作**：享受实时编辑，见证团队实时协作。
- **安全访问控制**：通过细粒度访问控制保持信息安全，仅与合适的人分享。
- **多格式导出**：以多种格式导出内容（.odt, .docx, .pdf），支持自定义模板。
- **自托管**：易于在自己的服务器上安装，支持 Kubernetes 和 Docker Compose。

## 主要功能

- **写作**：简单、可访问的在线编辑；美观格式；Markdown 语法；块类型和快捷键；离线写作；AI 动作如重述、总结、翻译。
- **协作**：实时编辑；安全控制；导出；子页面组织知识。
- **自托管**：支持 Docker Compose、Kubernetes 等安装方式。

## 用法

### 测试

访问 [demo document](https://impress-preprod.beta.numerique.gouv.fr/docs/6ee5aac4-4fb9-457d-95bf-bb56c2467713/) 在浏览器中测试。

### 本地运行

使用 Docker 和 Docker Compose：

1. 安装 Docker 和 Docker Compose。
2. 运行 `make bootstrap FLUSH_ARGS='--no-input'` 启动服务。
3. 访问 http://localhost:3000，默认凭据：username: impress, password: impress。

### 自托管

支持 Kubernetes、Docker Compose 等。详见 [安装文档](/docs/installation/README.md)。

### 贡献

在 [Crowdin](https://crowdin.com/project/lasuite-docs) 帮助翻译，或提交 PR。见 [CONTRIBUTING](https://github.com/suitenumerique/docs/blob/main/CONTRIBUTING.md)。
