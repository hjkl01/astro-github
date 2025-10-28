
---
title: Restore-JS
---

# Restore-JS 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/LoseNine/Restore-JS)

## 主要特性
Restore-JS 是一个用于恢复 JavaScript 代码的工具项目，主要针对混淆或压缩的 JS 代码进行反混淆和格式化处理。它支持多种 JS 代码恢复场景，帮助开发者或研究人员快速解析难以阅读的代码。核心特性包括：
- **自动反混淆**：识别并恢复常见的 JS 混淆模式，如变量名重命名、字符串编码等。
- **代码格式化**：将压缩的单行代码重新格式化为可读的多行结构，支持缩进和注释添加。
- **支持多种混淆器**：兼容 JavaScript Obfuscator 等流行混淆工具的输出。
- **轻量级设计**：纯 JS 实现，无需额外依赖，便于在浏览器或 Node.js 环境中运行。
- **开源免费**：基于 MIT 许可，允许自由修改和分发。

## 主要功能
- **代码恢复**：输入混淆 JS 代码，输出可读版本，包括变量解名和控制流恢复。
- **批量处理**：支持处理多个文件或代码片段，提高效率。
- **自定义规则**：用户可配置恢复规则，以适应特定混淆场景。
- **错误检测**：内置语法检查，确保恢复后的代码有效性。
- **集成友好**：可作为库集成到其他项目中，或通过 CLI 命令行使用。

## 用法
1. **克隆项目**：
   ```
   git clone https://github.com/LoseNine/Restore-JS.git
   cd Restore-JS
   ```

2. **安装依赖**（如果需要）：
   ```
   npm install
   ```

3. **基本用法（CLI）**：
   - 运行恢复命令：
     ```
     node restore.js input.js output.js
     ```
     - `input.js`：输入的混淆 JS 文件。
     - `output.js`：输出的恢复 JS 文件。

4. **浏览器中使用**：
   - 引入脚本：`<script src="restore.js"></script>`
   - 调用 API：
     ```javascript
     const restoredCode = RestoreJS.deobfuscate(obfuscatedCode, options);
     console.log(restoredCode);
     ```
     - `options`：可选配置对象，如 `{ format: true, renameVars: true }`。

5. **高级用法**：
   - 编辑 `config.json` 文件自定义规则。
   - 对于批量处理：使用 `node batch-restore.js --dir ./scripts` 处理目录下所有 JS 文件。

更多细节请参考项目 README.md 文件。