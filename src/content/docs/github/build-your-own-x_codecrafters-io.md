
---
title: build-your-own-x
---

# Build Your Own X (Codecrafters)

**项目地址**：<https://github/codecrafters-io/build-your-own-x>

---

## 主要特性

- **多样化的实现挑战**  
  该仓库包含数十个“Build Your Own X”挑战，每个挑战都对应一个真实世界的软件组件（如 Linux 碎片、Shell、HTTP/1.1、网络编解码器、数据库、FTP、Redis 等）。  

- **通用框架与测试**  
  为每个挑战提供了统一的测试框架（Rust/Go/C++/Python 等多语言支持）。无论用哪种语言实现，只需遵循项目 README 中给出的接口，即可通过 CI 运行单元测试。  

- **自动化评测与持续集成**  
  `.github/workflows` 中配置的 GitHub Actions 会在 PR 或 push 时自动执行对应子项目的单元测试，并给出通过/未通过的报告。  

- **可扩展的项目结构**  
  每个子项目都拥有自己的目录结构（`specs`、`src`、`tests` 等），方便学习者快速定位题目描述、实现目录和测试代码。  

- **学习资源与社区支持**  
  README 提供了丰富的学习资源（提示、参考实现、FAQ）， 并且社区活跃，开发者可以通过 Issues 或 Discussions 寻求帮助或提议新挑战。  

---

## 功能

1. **实现从零开始**  
   用户可从零实现指定功能，必须遵守题目提供的 API 规范。  

2. **语言无关**  
   虽然项目中多数示例使用 Rust，但任何符合接口的语言均可完成，实现的代码放在 `src/`，测试代码放在 ``。  

3. **自动化评测**  
   CI 运行 `cargo test`（或对应语言的测试命令），验证实现的正确性与性能（如有指定）。  

4. **版本控制与提交**  
   提交时将实现代码与相关测试文件一起上传，方便老师或自动化系统评测。  

---

## 用法

1. **克隆仓库**  
   ```bash
   git clone https://github.com/codecrafters-io/build-your-own-x.git
   cd build-your-own-x
   ```

2. **选择挑战**  
   ```bash
   ls challenges
   ```
   例如：`linux`、`shell`、`http`、`redis` 等。  

3. **阅读挑战说明**  
   ```bash
   cd challenges/<challenge_name>
   cat README.md
   ```
   说明中会列出实现需求、接口定义、测试说明以及运行指令。  

4. **实现代码**  
   在 `src/` 目录编写代码（保持接口签名）。  

5. **本地测试**  
   进入对应挑战目录，运行对应语言的测试命令。  
   - Rust（默认）  
     ```bash
     cargo test
     ```
   - 其它语言（如 Go、Python 等）请根据 README 指引使用对应命令。  

6. **提交 PR**  
   ```bash
   git add .
   git commit -m "build: implement <challenge_name>"
   git push origin main
   ```
   GitHub Actions 将自动执行测试，结果会显示在 PR 页面。  

---

> **小贴士**  
> - 若使用 Rust，确保 `Cargo.toml` 已正确列出依赖。  
> - 对于需要网络 I/O 的挑战，测试会在 sandbox 环境中执行，确保你的实现不使用外部网络。  
> - 关注 `docs` 目录，里面提供更详细的学习笔记与实现思路。  

---