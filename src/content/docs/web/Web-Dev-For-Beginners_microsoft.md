---
title: Web-Dev-For-Beginners
---


# Microsoft Web-Dev-For-Beginners

## 项目地址
- https://github.com/microsoft/Web-Dev-For-Beginners

## 主要特性
- **系统化学习路径**：按主题（HTML、CSS、JavaScript、后端、云端等）组织的课程，从基础到进阶。
- **交互式练习**：每节课配有代码片段、练习题和即时代码运行环境。
- **多平台支持**：可在 VS Code、GitHub Codespaces、GitHub Classroom 以及本地环境中使用。
- **持续集成**：使用 GitHub Actions 自动构建并验证学习内容的完整性。
- **云端示例**：整合 Azure App Service、Azure Functions、Azure Static Web Apps 等示例，展示云原生部署流程。

## 功能
- 课程目录浏览：通过 `README.md` 与 `docs/` 目录快速定位学习目标。
- 代码检查与部署：在 `scripts/` 中提供脚本用于本地测试、Lint、预览与 Azure 部署。
- 评测与反馈：`quizzes/` 包含多项选择题，帮助巩固知识点。

## 用法
1. **克隆仓库**  
   ```bash
   git clone https://github.com/microsoft/Web-Dev-For-Beginners.git
   cd Web-Dev-For-Beginners
   ```

2. **打开 VS Code**  
   ```bash
   code .
   ```

3. **开始学习**  
   - 依次打开 `docs/` 下的 Markdown 文件，跟随说明完成代码练习。
   - 运行 `npm install`（若有）或 `pip install -r requirements.txt`，按指引执行脚本。

4. **本地预览**  
   ```bash
   npm run start   # 或对应的启动命令
   ```

5. **部署到 Azure**  
   ```bash
   az webapp up --name <app-name> --resource-group <rg>
   ```

6. **CI 验证**  
   - 提交后 GitHub Actions 会自动执行构建与测试，确保学习路径无误。

> 以上步骤适用于 Windows、macOS 和 Linux。详情请参阅各章节的 `README.md`。
