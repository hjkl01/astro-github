
---
title: nuclei-templates
---


# nuclei-templates（ProjectDiscovery）

> 项目地址: https://github.com/projectdiscovery/nuclei-templates

## 项目简介
`nuclei-templates` 是一个开源的安全测试模板库，专门为 Nuclei 漏洞扫描器设计。  
它收集了数千个针对常见漏洞、配置错误、敏感信息泄露等场景的可复用模板，帮助安全研究人员与企业快速、自动化地发现安全风险。

## 主要特性
| 特性 | 说明 |
|------|------|
| **丰富的模板库** | 超过 3,000+ 公开模板，涵盖 CVE、误配、敏感信息、后门、Web 漏洞、API 漏洞等多种类型 |
| **多维度分类** | 按 `category`（如 `vulnerability`、`misconfiguration`、`sensitive-data`）和 `tags` 进行细粒度标签，便于筛选 |
| **统一语法** | 采用 YAML 语法，支持 `request`、`matchers`、`extractors`、`log` 等字段，易于编写与维护 |
| **可扩展性** | 通过自定义 `templates` 目录，用户可快速添加、修改、删除模板，支持 `-t` 参数指定路径 |
| **社区驱动** | 任何人都可提交 PR，模板经过审核后合并，保持库的持续更新与质量 |
| **与 Nuclei 无缝集成** | 只需指定模板路径，Nuclei 自动解析并执行，支持多线程、速率控制、结果导出等高级功能 |

## 典型用法

1. **克隆模板库**

   ```bash
   git clone https://github.com/projectdiscovery/nuclei-templates.git
   cd nuclei-templates
   ```

2. **使用 Nuclei 扫描目标**

   ```bash
   nuclei -t ./ -u https://example.com
   ```

   - `-t`：指定模板目录（可直接指向克隆好的仓库）
   - `-u`：单个 URL
   - `-l`：使用 URL 列表文件
   - `-o`：输出结果文件

3. **更新模板**

   ```bash
   cd nuclei-templates
   git pull origin main
   ```

   或者使用 `nuclei` 自带的 `update-templates` 命令（需要 Nuclei 1.10+）：

   ```bash
   nuclei -update-templates
   ```

4. **自定义模板**

   - 在 `templates/` 目录下创建自己的 YAML 文件，遵循 Nuclei 语法
   - 通过 `-t` 指定自定义路径即可使用

5. **结果查看与导出**

   ```bash
   nuclei -t ./ -u https://example.com -o results.json
   ```

   支持 `json`、`html`、`txt` 等多种格式。

## 进一步阅读

- Nuclei 官方文档： https://nuclei.projectdiscovery.io
- 模板贡献指南： https://github.com/projectdiscovery/nuclei-templates/blob/main/CONTRIBUTING.md

---

> 本文件仅包含项目地址及核心说明，适用于快速了解 `nuclei-templates` 的功能与使用方法。