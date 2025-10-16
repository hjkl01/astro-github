
---
title: fx
---

# fx 项目

**GitHub 项目地址:** [https://github.com/antonmedv/fx](https://github.com/antonmedv/fx)

## 主要特性
- **人类友好的输出**: fx 使用类似 JavaScript 的语法来格式化和查询 JSON 数据，提供易读的输出，支持颜色高亮和美化显示。
- **轻量级工具**: 纯 Go 语言实现，体积小、速度快，无需依赖其他运行时环境。
- **管道支持**: 设计为命令行管道工具，可无缝集成到 shell 脚本中，处理 JSON 输入/输出。
- **内置函数**: 支持内置的查询函数，如 `.map()`、`.filter()`、`.reduce()` 等，类似于 JavaScript 操作。
- **跨平台**: 支持 macOS、Linux 和 Windows，易于安装和使用。
- **扩展性**: 可以自定义表达式来处理复杂数据结构，支持错误处理和调试。

## 主要功能
- **JSON 格式化和查询**: 从文件、stdin 或 API 读取 JSON 数据，并使用表达式提取、转换或过滤特定部分。
- **数据可视化**: 自动检测并美化输出，支持分页查看大型 JSON。
- **命令行集成**: 常用于开发调试、API 测试、日志解析等场景，帮助快速检查 JSON 响应。
- **表达式引擎**: 基于 f(x) 语法，支持变量、循环、条件判断等，类似于轻量级脚本语言。

## 用法
### 安装
使用 Homebrew (macOS/Linux):  
```
brew install fx
```

或从 GitHub Releases 下载二进制文件:  
访问 [Releases 页面](https://github.com/antonmedv/fx/releases) 下载对应平台的版本。

Go 安装:  
```
go install github.com/antonmedv/fx@latest
```

### 基本用法
fx 的基本语法: `fx [选项] <表达式> [文件或 stdin]`

1. **格式化 JSON**:  
   ```
   cat data.json | fx .
   ```  
   这会美化输出整个 JSON。

2. **提取特定字段**:  
   ```
   fx '.users[0].name' data.json
   ```  
   输出 users 数组中第一个用户的 name 字段。

3. **过滤数据**:  
   ```
   fx 'x => x.age > 18' data.json
   ```  
   过滤出年龄大于 18 的对象。

4. **管道示例**:  
   从 API 获取 JSON 并处理:  
   ```
   curl -s https://api.example.com/users | fx '.[] | select(.active == true) | .name'
   ```

5. **选项**:  
   - `-i`: 交互模式，支持实时编辑表达式。  
   - `--help`: 查看完整帮助。  
   示例: `fx -i data.json` 进入交互式 REPL。

更多示例和高级用法，请参考项目 README。