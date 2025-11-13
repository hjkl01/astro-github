---
title: docker-libreoffice
---

# LinuxServer.io Docker LibreOffice 项目

## 项目地址
[https://github.com/linuxserver/docker-libreoffice](https://github.com/linuxserver/docker-libreoffice)

## 主要特性
- **基于 Docker 的 LibreOffice 容器**：提供一个轻量级的 LibreOffice 办公套件容器镜像，支持在容器环境中运行 LibreOffice 的核心组件，包括 Writer（文字处理）、Calc（电子表格）和 Impress（演示文稿）等。
- **跨平台兼容性**：镜像基于 Alpine Linux，支持 x86-64 和 ARM 架构，适用于各种 Docker 环境，如 Docker Desktop、Kubernetes 或云服务器。
- **无头模式支持**：优化为 headless（无图形界面）运行，适合服务器端文档转换、自动化处理场景，而非交互式桌面使用。
- **易于扩展**：支持自定义配置和挂载卷，便于集成到更大的自动化工作流中。
- **社区维护**：由 LinuxServer.io 团队维护，提供定期更新、安全补丁和详细文档，确保稳定性和安全性。

## 主要功能
- **文档转换**：将各种格式的文档转换为 PDF、HTML、图像或其他办公格式，例如使用命令行工具将 DOCX 转换为 PDF。
- **自动化处理**：支持脚本化操作，如批量转换文件、生成报告或集成到 CI/CD 管道中。
- **API 和集成**：可与 UNO API（LibreOffice 的通用网络对象接口）结合，用于编程方式访问 LibreOffice 功能。
- **资源高效**：容器设计注重低资源消耗，适合资源受限的环境运行 LibreOffice 任务，而无需安装完整的桌面版。

## 用法
1. **拉取镜像**：
   ```
   docker pull lscr.io/linuxserver/libreoffice:latest
   ```

2. **运行容器**（基本示例，使用挂载卷处理文件）：
   ```
   docker run -d \
     --name=libreoffice \
     -e PUID=1000 \
     -e PGID=1000 \
     -e TZ=Etc/UTC \
     -p 3000:3000 \
     -v /path/to/input:/config/input \
     -v /path/to/output:/config/output \
     --restart unless-stopped \
     lscr.io/linuxserver/libreoffice:latest
   ```
   - `PUID` 和 `PGID`：设置用户和组 ID 以匹配主机权限。
   - `TZ`：设置时区。
   - 卷挂载：`/path/to/input` 为输入文件目录，`/path/to/output` 为输出目录。
   - 端口 3000：用于可选的 Web 界面或 API 访问（如果启用）。

3. **执行文档转换**（示例：将 input 中的文件转换为 PDF）：
   - 进入容器：`docker exec -it libreoffice sh`
   - 运行命令：`libreoffice --headless --convert-to pdf --outdir /config/output /config/input/*.docx`

4. **高级用法**：
   - **集成脚本**：编写 shell 脚本调用 LibreOffice 的 `--headless` 模式进行批量处理。
   - **Kubernetes 部署**：使用 Helm 或 YAML 文件部署，支持持久卷（PV）存储输入/输出文件。
   - **环境变量自定义**：通过 `-e` 参数调整 LibreOffice 设置，如字体路径或默认模板。
   - 详细文档：参考 GitHub 仓库的 README，包含更多示例和故障排除指南。

此容器适用于 DevOps、文档自动化和无服务器办公任务场景。