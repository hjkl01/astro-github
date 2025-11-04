
---
title: fscan
---


# fscan

**GitHub地址**: https://github.com/shadow1ng/fscan

---

## 主要特性

- **高速并发扫描**  
  采用多线程/协程实现端口扫描，支持上百个并发任务，极大提升扫描速度。

- **多协议支持**  
  - TCP/UDP端口扫描  
  - ICMPPing、ARP探测  
  - HTTP/HTTPS服务探测（返回页面标题、HTTP头等信息）

- **内置服务识别**  
  根据响应包特征识别常见服务（FTP, SSH, MySQL, Tomcat, Nginx 等），返回版本信息。

- **操作系统指纹识别**  
  通过TCP/IP选项解析、TTL值等方式识别目标主机操作系统。

- **插件化架构**  
  支持自定义脚本（Go、Python、Lua）进行漏洞检测或业务探测，插件目录可自定义。

- **多种输出格式**  
  - 普通文本 (`-o txt`)  
  - JSON (`-o json`)  
  - 详细报告 (`-v`)

- **交互式命令行**  
  提供丰富的命令行参数，支持 `-t`（目标）、`-p`（端口区间）、`-r`（IP列表文件）、`-o`（输出目录）等。

---

## 使用方法

### 1. 安装

```bash
# 直接从源码编译（需要Go 1.18+）
go install github.com/shadow1ng/fscan@latest

# 或下载二进制发行版
wget https://github.com/shadow1ng/fscan/releases/download/v1.2.3/fscan_linux_amd64.tar.gz
tar -xzf fscan_linux_amd64.tar.gz
sudo mv ./fscan /usr/local/bin/
```

### 2. 基本扫描

```bash
# 单目标完整扫描
fscan -t 192.168.1.1

# 区间扫描
fscan -t 192.168.1.0/24

# 指定端口
fscan -t 10.0.0.1 -p 80,443,22-1024

# UDP扫描
fscan -t 10.0.0.1 -u 53,67,69

# 指定输出格式
fscan -t 10.0.0.0/16 -o json -o /tmp/scan_result.json
```

### 3. 插件扫描

```bash
# 指定插件目录
fscan -t 192.168.1.0/24 -p 80 -P ./my_plugins

# 使用内置Python插件
fscan -t host -p 80 -P ./plugins/python
```

### 4. 高级功能

```bash
# 并行扫描数目调整（默认64）
fscan -t 10.0.0.0/24 -m 128

# 仅快速扫描（常用端口）
fscan -t 10.0.0.1 -a

# 设置代理
fscan -t 10.0.0.1 -x socks5://127.0.0.1:1080
```

---

## 结语

fscan 以其高性能、可扩展性与全面的扫描功能，成为日常网络安全评估、渗透测试以及运维巡检的利器。欢迎根据项目需求自行扩展插件或贡献代码。```
