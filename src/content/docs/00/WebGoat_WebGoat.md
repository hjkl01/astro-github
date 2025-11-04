
---
title: WebGoat
---

# WebGoat

> 项目地址: <https://github.com/WebGoat/WebGoat>

## 概述
WebGoat 是 OWASP 提供的一个基于 Web 的学习平台，旨在帮助安全研究人员、开发者和测试人员通过实际例子深入了解常见的 Web 安全漏洞。它提供了一系列交互式练习（Lessons），每个练习都模拟了真实世界中的攻击场景，让你可以在安全的环境下进行尝试和学习。

## 主要特性

- **交互式练习（Lessons）**  
  以实际代码和重现步骤组织，每个练习都有详细提示和评估机制。
  
- **漏洞类型覆盖**  
  覆盖 OWASP Top 10、SQL 注入、XSS、CSRF、文件上传、权限绕过、误用认证等常见漏洞。

- **易于部署**  
  基于 Java 的 Spring Boot 项目，可通过 Maven/Gradle 打包，亦可作为 Docker 镜像直接运行。

- **可视化评测**  
  每完成一次练习，系统会给出分数，帮助你跟踪学习进度，并能导出报告。

- **支持多语言**  
  只要你能使用浏览器，即可在任何操作系统上使用。

## 主要功能

| 功能 | 描述 |
|------|------|
| **练习页面** | 每个 Lesson 提供代码、描述、输入框和提示，帮助学习者完成攻击步骤。 |
| **扫描器** | 内置的增量扫描工具可以帮助你识别当前 WebGoat 实例中的已知漏洞。 |
| **插件系统** | 允许开发者扩展新的 Lesson 或自定义模块。 |
| **学习跟踪** | 记录练习完成情况、得分和学习路径。 |
| **示例代码** | 提供服务器端 Java 代码，帮助学习者理解后端实现与安全缺陷。 |

## 用法

1. **克隆仓库**  
   ```bash
   git clone https://github.com/WebGoat/WebGoat.git
   cd WebGoat
   ```

2. **构建并运行**  
   - 使用 Maven  
     ```bash
     mvn clean install -DskipTests
     java -jar target/webgoat-server.jar
     ```
   - 或使用 Docker (推荐)  
     ```bash
     docker run - 8080:8080 oasisbits/webgoat
     ```

3. **访问 WebGoat**  
   打开浏览器访问 `http://localhost:8080/webgoat/`。首次访问会提示你创建一个管理员账户。

4. **开始练习**  
   登录后，“Lessons” 页面展示可用练习；点击进入后按照页面提示完成步驟，即可获得分数并查看答案解析。

5. **使用扫描器**  
   在主页左侧的 “Scanner” 菜单中，输入目标 URL（默认是 `http://localhost:8080/webgoat/`），启动扫描，系统会列出检测到的漏洞信息。

6. **自定义练习**  
   - 在 `src/main/java/owasp/webgoat/` 下可编辑或新增 Java 代码。  
   - 在 `src/main/resources/scenarios` 下创建新 Lesson 的 YAML 配置，定义输入、期望输出等。  
   - 重新构建后即可在 UI 中看到新增练习。

7. **导出学习报告**  
   - 在 “Profile” 页面可下载 PDF 形式的学习报告。  

## 常见问题

- **端口冲突**  
  如果 8080 端口已被占用，可通过 `--server.port=9090` 参数修改端口。  
  ```bash
  java -jar target/webgoat-server.jar --server.port=9090
  ```

- **Java 版本要求**  
  WebGoat 需要 Java 17 或更高版本。

- **SSL/TLS 测试**  
  需要时可在 `application.yml` 中开启 https 配置导入自签名证书。

---

> **注意**：WebGoat 本身只是一个学习工具，不建议在生产环境中部署。始终在安全隔离的环境下练习。