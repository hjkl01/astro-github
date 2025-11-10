---
title: Fabric
---


# Fabric (by Daniel Miessler)

**项目地址**  
<https://github.com/danielmiessler/Fabric>

## 说明
Fabric 是一个开源风险操作与安全测试框架，旨在帮助红队/蓝队安全人员快速执行网络侦察、权限提升与后门植入等战术操作。它以命令行工具为核心，同时支持插件式扩展，提供统一的凭证管理、加密存储、任务调度与报告生成等功能。

## 主要特性

| 特性 | 说明 |
|------|------|
| **统一任务管道** | 将侦察、攻击、持久化等步骤构建成可复用的工作流，支持一次性执行或持续运行。 |
| **凭证与凭证库** | 自动缓存密码/Token，支持 AES 加密存储，安全共享与导入。 |
| **多环境支持** | 使用 YAML 环境文件定义目标网络、主机类型、操作系统、访问权限等，便于在不同环境间快速切换。 |
| **插件化模块** | 支持自定义模块（如 `deploy_backdoor.py`、`recon_subdomain.py` 等），可通过 `fabric plugins` 安装或创建。 |
| **可视化 & 记录** | 支持 HTML/Markdown 报告导出，提供实时进度可视化。 |
| **轻量部署** | 基于 Python 3，依赖最小，仅需 `pip install fabric`。 |
| **安全审计** | 内置日志系统，记录所有命令与操作细节，满足合规需求。 |
| **多平台兼容** | 能在 Windows、Linux、macOS 上执行，且支持与 Cobalt Strike、Metasploit、Empire 等集成。 |

## 功能概览

1. **网络侦察**  
   - `fabric network scan`：快速扫描子网、端口、服务。  
   - `fabric enum users`：枚举域用户以及远程会话。  

2. **凭证获取**  
   - `fabric credential dump`：从内存、注册表或凭证窃取工具中解析凭证。  
   - `fabric brute force`：利用已知用户名进行密码尝试。  

3. **攻击与持久化**  
   - `fabric exploit windows`：利用已知漏洞部署后门。  
   - `fabric pst`：横向渗透与任务执行。  

4. **数据收集与提取**  
   - `fabric exfil`：安全的文件或命令输出提取。  
   - `fabric report`：生成事务、漏洞、键盘记录等详细报告。  

5. **插件与扩展**  
   - `fabric plugin install <name>`：安装第三方插件。  
   - `fabric plugin list`：查看已安装插件。  

## 用法示例

```bash
# 1. 克隆仓库并安装
git clone https://github.com/danielmiessler/Fabric.git
cd Fabric
pip install -e .

# 2. 定义环境文件（例如 env_prod.yaml）
cat <<EOF > env_prod.yaml
network: 10.0.0.0/24
os: windows
role: attacker
EOF

# 3. 侦察目标网络
fabric -e env_prod.yaml discover -s 10.0.0.0/24

# 4. 架设后门并植入
fabric -e env_prod.yaml exploit windows -p 8080

# 5. 收集信息并生成报告
fabric -e env_prod.yaml exfil -o results.zip
fabric report generate -i results.zip -o report.html
```

> **提示**：  
> - `fabric --help` 显示完整命令与参数。  
> - 使用 `fabric config edit` 编辑全局配置。  
> - 将凭证加密存储，执行 `fabric credential encrypt`。

## 快速启动

```bash
# 立即运行完整演练（在 env.yaml 中定义所有参数）
fabric -e env.yaml run
```

> 以上示例演示了 Fabric 的核心流程：环境定义 → 网络侦察 → 漏洞利用 → 持久化 → 数据收集 → 报告生成。

---
如需进一步配置或开发自定义模块，请参阅项目根目录下的 `README.md` 与 `docs/` 目录。祝你安全实验顺利开展！
