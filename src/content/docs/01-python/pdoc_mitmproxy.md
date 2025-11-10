---
title: pdoc
---

# mitmproxy/pdoc 项目

## 项目地址
[https://github.com/mitmproxy/pdoc](https://github.com/mitmproxy/pdoc)

## 主要特性
pdoc 是一个轻量级的 Python 模块文档生成器，主要特性包括：
- **自动生成文档**：从 Python 源代码的类型提示（type hints）和 docstrings 中提取信息，生成干净、现代的 HTML 文档。
- **无需额外依赖**：纯 Python 实现，不需要 Sphinx 等复杂工具，适合快速生成 API 文档。
- **支持 Markdown 和 reStructuredText**：自动解析 docstrings，支持多种格式的文档字符串。
- **自定义主题**：提供简洁的默认主题，并支持自定义 CSS 和模板。
- **模块化设计**：可以为单个模块、包或整个项目生成文档，支持过滤和排除特定模块。
- **Web 服务器模式**：内置简单 HTTP 服务器，可实时查看生成的文档。

## 主要功能
- **文档提取**：解析 Python 代码，提取类、函数、变量及其签名、类型和描述。
- **HTML 输出**：生成静态 HTML 文件，支持导航、搜索和交叉引用。
- **CLI 接口**：通过命令行工具快速生成和查看文档。
- **集成友好**：易于集成到 CI/CD 管道中，用于自动化文档构建。
- **类型支持**：充分利用 Python 3 的类型注解，提供更精确的文档描述。

## 用法
### 安装
使用 pip 安装：
```
pip install pdoc
```

### 基本用法
1. **生成单个模块的文档**：
   ```
   pdoc your_module
   ```
   这会在当前目录生成 `your_module.html` 文件。

2. **生成包的文档**：
   ```
   pdoc --html your_package
   ```
   生成整个包的 HTML 文档，包括子模块。

3. **启动 Web 服务器查看文档**（推荐，用于开发时实时预览）：
   ```
   pdoc --http :8080 your_module
   ```
   访问 `http://localhost:8080` 查看文档。支持 `--http host:port` 指定地址。

4. **高级选项**：
   - `--output-dir dir`：指定输出目录。
   - `--exclude "pattern"`：排除匹配的模块。
   - `--force`：强制覆盖现有文件。
   - `--template-dir dir`：自定义模板目录。
   示例：为项目生成完整文档并输出到 `docs/` 目录：
   ```
   pdoc --html --output-dir docs/ your_project
   ```

更多详情请参考项目 README 或运行 `pdoc --help`。