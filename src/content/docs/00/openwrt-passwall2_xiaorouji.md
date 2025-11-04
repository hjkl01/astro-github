
---
title: openwrt-passwall2
---


# OpenWrt Passwall2 (xiaorouji)

**项目地址**  
[https://github.com/xiaorouji/openwrt-passwall2](https://github.com/xiaorouji/openwrt-passwall2)

---

## 主要特性

- **多协议支持**  
  - Shadowsocks / ShadowsocksR  
  - V2Ray（VMess/VLess/VMess+TLS/TCP+TLS）  
  - Trojan / Trojan-Go  
  - WireGuard  
  - HTTP/HTTPS 代理  
  - Socks5  
- **自动路由与策略**  
  - 支持分流、全局、直连、绕过大陆等多种规则  
  - 可通过 IP、域名、应用等方式自定义路由  
- **高级 DNS 整合**  
  - DNS over TLS / DNS over HTTPS  
  - DNS 解析重写、缓存、分流  
- **安全与隐私**  
  - 支持 TLS/SSL 终端加密  
  - 支持 Socks5 认证、V2Ray 伪装  
- **易用的 Web UI**  
  - 基于 LuCI 的可视化配置界面  
  - 支持一键安装、自动更新、日志查看  
- **性能优化**  
  - 使用 iptables / nftables + Xtables-Target + ip6tables  
  - 支持多线程、内核加速（X86/ARM）  
- **插件化架构**  
  - 可扩展插件（如 dnsmasq、iptables、rewrite、cache 等）  
  - 支持自定义 Lua 脚本

---

## 功能概览

| 功能 | 说明 |
|------|------|
| **一键安装** | 通过 opkg 或 LuCI 一键安装所有依赖 |
| **多节点管理** | 支持多节点列表，节点切换、负载均衡 |
| **规则管理** | 内置常用规则集，支持自定义规则文件 |
| **日志与监控** | 实时日志、流量监控、连接状态 |
| **自动更新** | 支持 OTA 更新、插件自动升级 |
| **多平台兼容** | 支持 OpenWrt 18.06 以上版本，兼容大多数路由器 |

---

## 用法

### 1. 添加软件源

```sh
# 添加 Passwall2 软件源
echo 'src-git passwall2 https://github.com/xiaorouji/openwrt-passwall2.git' >> /etc/opkg/customfeeds.conf
opkg update
```

### 2. 安装

```sh
opkg install passwall2
```

> 也可以通过 LuCI → 系统 → 软件包 → 搜索 “passwall2” 进行安装。

### 3. 基础配置（示例）

#### 通过 LuCI

1. **进入 LuCI** → **网络** → **Passwall**  
2. **节点管理**：点击 “添加”，填写节点信息（地址、端口、加密方式等）  
3. **策略路由**：设置 “全局” 或 “分流”  
4. **DNS 设置**：选择 “DNS over TLS” 并填写解析服务器  
5. **保存并重启**  

#### 通过命令行

```sh
# 创建节点配置文件
cat <<EOF > /etc/passwall2/nodes.json
{
  "nodes": [
    {
      "name": "V2Ray1",
      "type": "vmess",
      "server": "example.com",
      "port": 443,
      "uuid": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "alterId": 64,
      "cipher": "auto",
      "tls": true
    }
  ]
}
EOF

# 启动 Passwall2
/etc/init.d/passwall2 start
```

> 你也可以编辑 `/etc/config/passwall2` 来手动配置策略与 DNS。

### 4. 流量监控与日志

- 日志查看：`logread | grep passwall2` 或 `cat /var/log/passwall2.log`
- 流量统计：`iptables -L -v -n`

---

## 常见命令

| 命令 | 用途 |
|------|------|
| `/etc/init.d/passwall2 start` | 启动 Passwall2 |
| `/etc/init.d/passwall2 stop` | 停止 Passwall2 |
| `/etc/init.d/passwall2 restart` | 重启 Passwall2 |
| `passwall2 -v` | 查看版本信息 |
| `passwall2 -c /etc/passwall2/nodes.json` | 手动加载节点配置 |

---

## 参考文档

- 官方 Wiki: https://github.com/xiaorouji/openwrt-passwall2/wiki
- LuCI 插件页面: `/usr/lib/lua/luci/controller/passwall.lua`

---

## 重要提示

- **安全**：请使用强密码或密钥，避免默认配置泄露。  
- **性能**：开启 `iptables` + `iptables-nft` 时，请确认内核支持 `nftables`。  
- **更新**：定期执行 `opkg update && opkg upgrade passwall2` 以获取最新特性。  

---

> 如需进一步帮助，请查看项目 Wiki 或提交 Issue。  
