---
title: googlesans-code
---

# Google Sans Code

Google Sans Code 是一个固定宽度的字体家族，由 Google Fonts 开发，旨在为代码带来清晰度、可读性和 Google 品牌特色的元素。它源于 Google 的品牌类型设计美学，并为 Gemini 和 Android Studio 等产品开发，确保每个字符在小尺寸下保持清晰。此外，它针对编程语言语法的独特排版需求进行了精细调整。

## 功能特性

- **增强可读性**：专为代码编辑器和终端优化可读性。
- **支持脚本**：扩展拉丁语，支持多种语言。
- **可变字体**：提供从 300 到 800 的广泛权重轴范围。
- **OpenType 特性**：包括样式集、本地化形式等。
- **可变字体轴**：
  - `wght`：权重，范围 300 - 800；默认值=400。

## 安装和使用

要安装 Google Sans Code，请下载[最新的可变字体发布文件](https://github.com/googlefonts/googlesans-code/releases/latest)，并在您的操作系统上安装字体。下载的 ZIP 存档包括单独的罗马体和斜体可变字体。

### 构建说明

如果您想自己编译字体，请按照以下步骤操作：

1. 安装依赖项：使用 [`fontc` 字体编译器](https://github.com/googlefonts/fontc)。

2. 克隆仓库：

   ```
   git clone https://github.com/googlefonts/googlesans-code.git
   ```

3. 编译罗马体可变字体：

   ```
   fontc sources/GoogleSansCode.glyphspackage --flatten-components --decompose-transformed-components --output-file fonts/variable/GoogleSansCode[wght].ttf
   ```

4. 编译斜体可变字体：
   ```
   fontc sources/GoogleSansCode-Italic.glyphspackage --flatten-components --decompose-transformed-components --output-file fonts/variable/GoogleSansCode-Italic[wght].ttf
   ```

编译后的字体位于 `fonts/variable` 子目录中。

## 许可证

此字体软件根据 SIL Open Font License 版本 1.1 授权。该许可证可在 [https://openfontlicense.org](https://openfontlicense.org) 获取，并附带常见问题解答。
