
---
title: syft
---

# syft – Anchore 的开源 SBOM 生成工具

**项目地址**  
[https://github.comanchore/syft](https://github.com/anchore/syft)

---

## 一、项目简介  
syft 是一款命令行工具，专门用于扫描软件包、容器镜像、文件系统以及其他多种资产，并生成**软件物料清单（SBOM）**。它支持多种格式（JSON、Syft、SPDX 2.2/1.3、CycloneDX 1.4 等）输出，并集成到 CI/CD 流程、容器安全扫描以及合规性审核等场景。

## 二、主要特性  

| 特性 | 说明 |
|------|------|
| 多源扫描 | 支持 Docker 镜像、OCI 镜像、文件系统、Git 仓库、URL 等多种输入源 |
| 多语言支持 | 自动识别并解析 Go、NPM、Yarn、RubyGems、Pip、RUBY、Composer、Cargo、Maven、Gradle、Python、Java、Dart、OCAML 等语言的依赖 |
| 丰富的输出格式 | JSON、YAML、SPDX 2.2/1.3、CycloneDX 1.4、Syft 特定格式、自定义模板 |
| 扫描并行化 | 内建并发扫描，提高大项目扫描效率 |
| 可通过 API 控制 | 提供 Go 库，可嵌入到自定义工具链中 |
| 轻量级 | 单一二进制，无运行时依赖 |
| 现成的 Helm Chart 与 Docker 镜像 | 直接使用发行版镜像或在 Kubernetes 集群中运行 |
| 详细元数据 | 记录包的许可、来源、构建信息、CVEs、签名信息等 |

## 三、安装方式  

```bash
# 1. Homebrew (macOS / Linux)
brew install anchore/syft/syft

# 2. apt (Debian/Ubuntu 通过官方仓库)
sudo apt update
sudo apt install -y syft

# 3. Scoop (Windows)
scoop bucket add anchore https://github.com/anchore/syft-scoop
scoop install syft

# 4. Go
go install github.com/anchore/syft/cmd/syft@latest

# 5. Docker 直接拉取官方镜像
docker pull anchore/syft:latest**：如果你已在 Docker 环境中，可以直接使用 `anchore/syft` 镜像：

```bash
docker run --rm -v /root/.cache:/root/.cache anchore/syft image:latest
```

## 四、基本用法  

| 命令 | 说明 | 示例 |
|------|------|------|
| `syft <source>` | 扫描一个源并打印默认 JSON SBOM | `syft docker://ubuntulatest` |
| `syft <source> -o spdx-json` | 将 SBOM 输出为 SPDX JSON 格式 | `syft docker://node:14 -o spdx-json -o /tmp/spdx.json` |
| `syft <source> -o cyclonedx-xml` | 以 CycloneDX XML 形式输出 | `syft docker://python:3.11 -o cyclonedx-xml -o /tmp/cdx.xml` |
| `syft <source> --output json,spdx-json` | 同时生成种格式 | `syft ./myapp -o json,spdx-json` |
| `syft <source> --exclude-config-key=<key>` | 排除指定配置项 | `syft docker://weird/image --exclude-config-key=binaries` |
| `syft <source> --no-cache` | 关闭本地缓存 | `syft image:latest --no-cache` |

### 常见源类型

| 源类型 | 示例 |
|--------|------|
| Docker 镜像 | `docker://centos7` |
| OCI 镜像 | `oci://registry.com/repo/image:tag` |
| 文件系统 | `/path/to/app` |
| Git 仓库 | `git://github.com/some/repo.git` |
| URL | `https://example.com/package.tgz` |

## 五、输出格式与自定义模板  

`syft` 支持多种标准化格式，使用 `-o <format>` 或 `--output` 指定。  
示例：

```bash
syft docker://nginx:latest -o json -o spdx-json
```

如果需要更细粒度的控制，可通过 *Go template* 编写自定义输出：

```bash
syft docker://nginx:latest -o template=MyTemplate.tmpl -o myoutput.txt
```

模板语法参考官方文档。

## 六、集成与使用

- **CI/CD**: 在构建阶段执行 `syft`，把生成的 SBOM 存到 Artifactory、S3、GitHub Package Registry 或导入到 Ansible, GitHub Actions。
- **安全扫描**: 配合 Anchore Engine、Trivy 或 Harbor 扫描插件使用。
- **合规性**: 通过odian` 或自定义脚本结合 `syft` 输出做许可证审计。

## 七、参考资料

- 官方文档: https://anchore.github.io/syft/
- GitHub 仓库: https://github.com/anchore/syft
 示例命令与 API: https://github.com/anchore/syft/blob/main/docs/pods.md

--- 

> 以上内容已整理为 Markdown 格式，可直接复制到 `src/content/docs/00/syft_anchore.md` 进行保存。