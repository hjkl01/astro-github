---
title: LME
---

# LME 项目描述

## 项目地址
[GitHub 项目地址](https://github.com/cisagov/LME)

## 主要特性
LME（Log4j Mitigating Evidence）是由美国网络安全和基础设施安全局（CISA）开发的开源工具，主要针对 Log4Shell（CVE-2021-44228）漏洞进行检测和缓解。它具有以下主要特性：
- **漏洞扫描**：自动扫描 Java 应用程序和日志文件，识别潜在的 Log4j 漏洞利用痕迹。
- **证据收集**：生成缓解证据报告，帮助组织证明已采取措施防范 Log4Shell 攻击。
- **轻量级设计**：基于 Python 开发，易于部署和运行，支持多种操作系统。
- **开源与社区支持**：作为 CISA 的官方工具，提供免费访问和社区贡献，适用于企业级安全审计。

## 功能
LME 的核心功能聚焦于 Log4j 漏洞的检测与报告生成，包括：
- **日志分析**：解析应用程序日志，检测 JNDI 注入尝试或其他可疑模式，如 `${jndi:ldap://...}` 等字符串。
- **文件扫描**：检查 JAR 文件和类路径中 Log4j 库的版本，识别易受攻击的版本（例如 2.0 到 2.14.1）。
- **报告生成**：输出结构化报告，包括扫描结果、风险评估和推荐缓解步骤，支持 JSON 和 HTML 格式。
- **自定义配置**：允许用户指定扫描路径、日志模式和排除规则，以适应不同环境。
- **集成支持**：可与其他安全工具（如 SIEM 系统）结合使用，提供自动化证据收集。

## 用法
LME 的使用简单，通过命令行工具运行。以下是基本步骤：

1. **安装**：
   - 克隆仓库：`git clone https://github.com/cisagov/LME.git`
   - 进入目录：`cd LME`
   - 安装依赖：`pip install -r requirements.txt`（需要 Python 3.6+）

2. **运行扫描**：
   - 基本命令：`python lme.py --scan /path/to/logs --output report.json`
     - `--scan`：指定要扫描的目录或文件路径。
     - `--output`：指定输出报告文件。
   - 示例：扫描当前目录日志并生成 HTML 报告：`python lme.py --scan . --format html --output lme_report.html`

3. **高级选项**：
   - `--version-check`：仅检查 Log4j 版本。
   - `--exclude-patterns "pattern1,pattern2"`：排除特定日志模式。
   - `--verbose`：启用详细输出模式。

详细用法请参考项目 README.md 文件。建议在测试环境中先运行，以避免影响生产系统。