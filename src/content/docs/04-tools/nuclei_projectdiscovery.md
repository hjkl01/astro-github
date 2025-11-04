
---
title: nuclei
---


# Nuclei – ProjectDiscovery 之快速、可扩展的安全扫描框架

**项目地址**  
<https://github.com/projectdiscovery/nuclei>

---

## 主要特性

| 特性 | 说明 |
|------|------|
| **模板驱动** | 通过 YAML 格式的模板描述检测逻辑，支持多种协议（HTTP/HTTPS、DNS、TLS、TCP、UDP 等）。 |
| **极致速度** | 用 Go 编写，采用高并发设计，能够在数千个目标上毫秒级完成扫描。 |
| **可扩展** | 用户可自定义模板，直接在本地或共享库中添加、更新、删除检测规则。 |
| **多协议支持** | 除常见的 HTTP/HTTPS 之外，还支持 DNS、TLS、TCP、UDP、SMTP、SIP 等协议。 |
| **多输出格式** | 支持 JSON、Simple、HTML、CSV、TSV、XML 等多种结果导出方式。 |
| **丰富的命令行参数** | 允许用户细粒度控制并发数、超时、速率限制、目标来源、模板过滤等。 |
| **集成与自动化** | 可与 CI/CD、Threat Intelligence、监控系统集成，支持定期自动扫描。 |
| **安全社区** | ProjectDiscovery 提供了活跃的模板仓库（`nuclei-templates`），持续更新最新漏洞检测规则。 |

---

## 核心功能

1. **快速漏洞扫描**  
   - 利用并发请求，快速识别已知漏洞、错误配置、无认证访问等安全问题。

2. **模板管理**  
   - 本地模板文件夹：`~/.config/nuclei-templates`  
   - 官方模板仓库：`https://github.com/projectdiscovery/nuclei-templates`  
   - 支持模板更新、同步与版本控制。

3. **多协议探测**  
   - HTTP/HTTPS：GET/POST/HEAD、Cookie、Header、Body、Redirect 等  
   - DNS：A、AAAA、MX、TXT、SRV 等记录查询  
   - TLS：证书信息、协议支持、密码套件等  
   - TCP/UDP：端口开启、服务协议探测  
   - 其它：SMTP、SIP、Shell、LDAP 等

4. **结果分析**  
   - 支持根据 CVE、severity、tags 进行过滤。  
   - 可将结果直接导入 SIEM、Jira、Slack 等系统。

---

## 用法示例

### 1. 安装

```bash
# 通过 Homebrew (macOS) 安装
brew install nuclei

# 或者使用官方发布的二进制包
curl -s https://api.projectdiscovery.io/download/nuclei/latest | sudo tar -xz -C /usr/local/bin
```

### 2. 更新官方模板

```bash
nuclei -update-templates
```

### 3. 扫描单个目标

```bash
nuclei -target https://example.com -t /path/to/templates
```

### 4. 扫描目标列表

```bash
nuclei -l targets.txt -t nuclei-templates/ -o results.json
```

### 5. 过滤特定标签

```bash
nuclei -l targets.txt -t nuclei-templates/ -tags http,sql-injection
```

### 6. 限制并发数与速率

```bash
nuclei -l targets.txt -t nuclei-templates/ -workers 200 -rate 500
```

### 7. 输出多种格式

```bash
nuclei -l targets.txt -t nuclei-templates/ -o results.json -oresults.txt -oresults.html
```

---

## 典型使用场景

- **漏洞评估**：快速识别 Web 应用、API、云服务等中的已知漏洞。  
- **渗透测试**：在渗透测试周期中快速定位攻击面。  
- **持续安全监控**：将 Nuclei 集成到 CI/CD 流水线，持续扫描新部署的服务。  
- **合规检查**：通过自定义模板检查安全合规要求（如 PCI‑DSS、GDPR 等）。  
- **威胁情报**：结合 Threat Intelligence 平台，实时扫描攻击者已知 IP/域。

---

## 进一步学习

- 官方文档：<https://nuclei.projectdiscovery.io/>  
- 模板仓库：<https://github.com/projectdiscovery/nuclei-templates>  
- 社区讨论：<https://github.com/projectdiscovery/nuclei/discussions>  

--- 

> **提示**：经常更新模板与执行本地自定义模板，可以显著提高检测覆盖率与准确率。