
---
title: PrettyErrors
---

# PrettyErrors 项目

**GitHub 项目地址:** [https://github.com/onelivesleft/PrettyErrors](https://github.com/onelivesleft/PrettyErrors)

## 主要特性
PrettyErrors 是一个 Python 库，主要用于美化 Python 错误消息的输出。它将原本枯燥的 traceback 信息转化为彩色、易读的格式，提高了调试效率。主要特性包括：
- **彩色输出**：使用 ANSI 颜色代码突出显示错误类型、文件名、行号和错误消息，使其在终端中更醒目。
- **简洁格式**：去除冗余信息，聚焦于关键错误细节，如变量值和调用栈。
- **自定义主题**：支持多种预设主题（如默认、黑暗模式），并允许用户自定义颜色和样式。
- **兼容性强**：适用于 Python 3.x 版本，支持各种 IDE 和终端环境。
- **轻量级**：无需额外依赖，仅通过简单导入即可激活。

## 主要功能
- **错误美化**：自动替换标准 Python 错误输出，提供更直观的 traceback 显示，包括语法错误、异常等。
- **变量高亮**：在错误上下文中突出显示局部变量的值，帮助快速定位问题。
- **多行支持**：处理长错误消息时，支持折行和分页显示，避免信息溢出。
- **主题切换**：通过配置文件或代码动态切换显示主题，适应不同开发环境。
- **扩展性**：可与其他调试工具集成，如 pdb 或 ipdb，进一步增强调试体验。

## 用法
1. **安装**：
   使用 pip 安装：
   ```
   pip install PrettyErrors
   ```

2. **基本使用**：
   在 Python 脚本开头导入并激活：
   ```python
   import pretty_errors
   ```
   一旦导入，库会自动捕获并美化所有后续错误输出，无需额外配置。

3. **自定义配置**：
   - 通过环境变量设置主题，例如：
     ```
     export PRETTY_ERRORS_THEME=Dark
     ```
   - 或在代码中配置：
     ```python
     import pretty_errors
     pretty_errors.configure(
         theme='Dark',
         display_vars=True  # 显示变量值
     )
     ```

4. **示例**：
   运行一个出错的脚本：
   ```python
   import pretty_errors

   def faulty_function(x):
       return 1 / x  # 除零错误

   faulty_function(0)
   ```
   输出将显示彩色的错误信息，包括文件名、行号和变量 `x=0` 的高亮。

更多细节请参考项目 README。