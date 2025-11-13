---
title: sigma
---

# Sigma

## 项目简介

Sigma 是一个通用的开源签名格式，用于描述 SIEM（Security Information and Event Management）系统中的相关日志事件。它允许研究人员和分析师以结构化的方式描述检测方法，并与他人分享。Sigma 的目标是提供一种标准化的格式，使检测规则易于编写、共享和应用到任何类型的日志文件。

Sigma 可以比作日志文件的 Snort（网络流量）或 YARA（文件）。

## 主要功能

- **规则类型**：
  - **通用检测规则**：威胁无关的规则，用于检测行为、技术或过程的实现。
  - **威胁狩猎规则**：范围更广，用于狩猎潜在的可疑或恶意活动。
  - **新兴威胁规则**：针对特定威胁，如 APT 活动、零日漏洞利用等。
  - **合规规则**：基于 CIS Controls、NIST、ISO 27001 等框架识别合规违规。
  - **占位符规则**：在转换或使用时获得最终含义的规则。

- **社区驱动**：由专业检测工程师组成的社区同行评审，提供超过 3000 个检测规则。
- **供应商无关**：规则不依赖于特定 SIEM 供应商。
- **易于分享**：规则以 YAML 格式编写，便于跨社区和报告分享。

## 用法

1. **探索规则**：访问 [sigmahq.io](https://sigmahq.io) 开始探索 Sigma 生态系统。

2. **编写规则**：
   - 参考 [Rule Creation Guide](https://github.com/SigmaHQ/sigma/wiki/Rule-Creation-Guide)。
   - 查看 [How to Write Sigma Rules](https://www.nextron-systems.com/2018/02/10/write-sigma-rules/)。

3. **转换和使用规则**：
   - 使用 [Sigma CLI](https://github.com/SigmaHQ/sigma-cli) 或 [sigconverter.io](https://sigconverter.io) 将 Sigma 规则转换为特定 SIEM 查询语言。
   - 集成到工具链中使用 [pySigma](https://github.com/SigmaHQ/pySigma)。

4. **下载规则包**：从 [GitHub Releases](https://github.com/SigmaHQ/sigma/releases/latest) 下载最新规则包。

5. **贡献**：参考 [CONTRIBUTING.md](https://github.com/SigmaHQ/sigma/blob/master/CONTRIBUTING.md) 提交新规则或报告问题。

## 资源

- 官方网站：[sigmahq.io](https://sigmahq.io)
- GitHub 仓库：[SigmaHQ/sigma](https://github.com/SigmaHQ/sigma)
- 相关项目：Sigma 已集成到多个 SIEM 和安全工具中，如 IBM QRadar、Security Onion 等。

## 许可证

内容基于 [Detection Rule License (DRL) 1.1](https://github.com/SigmaHQ/Detection-Rule-License)。
