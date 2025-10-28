
---
title: argos-translate
---

# Argos Translate 项目

**GitHub 项目地址：** [https://github.com/argosopentech/argos-translate](https://github.com/argosopentech/argos-translate)

## 主要特性
Argos Translate 是一个开源的离线翻译库和工具，支持多种语言的翻译。它基于先进的机器学习模型，提供高质量的翻译结果。主要特性包括：
- **离线翻译**：无需互联网连接，即可在本地进行翻译，确保隐私和速度。
- **多语言支持**：支持数十种语言，包括英语、中文、法语、西班牙语等，语言包可扩展。
- **开源免费**：采用 MIT 许可证，完全开源，用户可自由修改和贡献。
- **轻量级**：核心库小巧，便于集成到各种应用中。
- **自定义模型**：允许用户训练或导入自定义翻译模型。
- **GUI 和 CLI 支持**：提供图形界面应用和命令行工具，适用于不同场景。

## 主要功能
- **文本翻译**：将输入文本从源语言翻译到目标语言，支持批量处理。
- **语言检测**：自动检测输入文本的语言。
- **语言包管理**：下载、安装和管理不同语言对的翻译模型。
- **API 接口**：提供 Python API，便于开发者集成到自己的项目中。
- **桌面应用**：通过 Argos Translate GUI，提供用户友好的翻译界面，支持复制粘贴或文件翻译。
- **格式支持**：处理纯文本、HTML 等格式的翻译。

## 用法
### 安装
1. **Python 库安装**（推荐使用 pip）：
   ```
   pip install argostranslate
   ```

2. **GUI 应用安装**：
   - 从 GitHub Releases 下载预编译的二进制文件（支持 Windows、macOS、Linux）。
   - 或通过包管理器安装，例如在 Ubuntu 上：`sudo apt install argos-translate-gui`（需添加 PPA）。

### 基本用法
#### 通过 Python API
```python
import argostranslate.package
import argostranslate.translate

# 更新可用语言包
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()

# 安装特定语言包（例如英语到中文）
package_to_install = next(
    filter(
        lambda x: x.from_code == "en" and x.to_code == "zh",
        available_packages,
    )
)
argostranslate.package.install_from_path(package_to_install.download())

# 翻译文本
translated_text = argostranslate.translate.translate("Hello, world!", "en", "zh")
print(translated_text)  # 输出：你好，世界！
```

#### 通过 GUI 应用
1. 启动 Argos Translate GUI。
2. 在界面中选择源语言和目标语言。
3. 输入或粘贴文本，点击翻译按钮获取结果。
4. 可下载额外语言包以扩展支持。

#### 通过命令行 (CLI)
安装 CLI 工具后，使用命令如：
```
argos-translate --from en --to zh "Hello, world!"
```

更多详情请参考项目文档：https://github.com/argosopentech/argos-translate/blob/master/README.md