
---
title: openwrt-passwall
---

# openwrt-passwall_xiaorouji

**GitHub 地址**: https://github.com/xiaorouji/openwrt-passwall

## 主要特性

1. **多协议支持**  
   - ShadowSocks（ShadowsocksR、Shadowsocks-libev、Shadowsocks-libev+Xray）  
   - V2Ray / Xray（VMess、VLESS、Trojan、HTTPS、HTTP代理）  
   - WireGuard、OpenVPN、L2TP/IPSec

2. **智能路由**  
   - 根据目标域名或 IP 列表做自定义路由  
   - 自动为节点发现 “Node-Rule” 与 “GeoIP” 双重路由

3. **插件化设计**  
   - `passwall`、`passwall2` 分别覆盖不同协议与插件  
   - 通过 `luci-app-passwall` 集成 LuCI 控制面板  
   - 完整的 Web UI 操作，支持服务器、节点、规则、代理组管理

4. **高性能**  
   - 大量 OpenWrt 设备（ARM、x86、MIPS）支持  
   - 支持多线程、异步 IO 优化，减少 CPU 占用

5. **安全与隐私**  
   - 支持 TLS/QUIC 加密  
   - 允许自定义证书、加密方法与密码  
   - `koolshare`、`xiaopu` 等 OpenWrt 衍生产业支持

## 核心功能

| 功能 | 说明 |
|------|------|
| 节点管理 | 支持手动添加、批量导入、自动更新节点（SS/SSR/V2Ray/…） |
| 规则管理 | DNS 直连、Leak 防护、广告过滤、WAN 域名直连 |
| 代理组 | 支持多线路、流量量化、最少字段拾取 |
| Docker 版本 | 可在 Docker 环境部署，与 Docker‑compose 兼容 |
| 升级脚本 | 一键升级 `passwall` 及 LuCI 插件 |
| 统计与监控 | 日志视图、流量统计、流量图表 |

## 用法示例

1. **安装包**  
   ```bash
   # 先启用 Passwall
   opkg update
   opkg install luci-app-passwall
   opkg install passwall
   # 其它依赖按提示安装
   ```

2. **添加节点**  
   - 进入 LuCI → 系统 → Passwall  
   - 点击 “节点管理” → “添加”  
   - 填写协议、IP/域名、端口、加密方式、密码、倍率等字段  
   - 保存后启用节点

3. **配置路由**  
   - LuCI → 系统 → Passwall → 路由  
   - 设定自定义域名、IP、规则，选择对应的代理组  
   - 保存后自动更新 `dnsmasq` 与 `iproute2` 路由表

4. **使用局部透明代理**  
   - 在 “透明代理” 页面启用 `auto-bind sec`  
   - 配置需要透明代理的 IP/子网  
   - 系统将自动将流量从对应 IP/子网转发至 Passwall 代理组

5. **Docker 部署** (可选)  
   ```bash
   docker pull xiaorouji/openwrt-passwall
   docker run -d --restart=always -p 1080:1080 -e TZ=Asia/Shanghai xiaorouji/openwrt-passwall
   ```

6. **常用命令行工具**  
   ```bash
   # 统计流量
   uci show passwall
   # 重写配置
   uci commit pass
   # 运行日志查看
   logread | grep passwall
   ```

> **提示**：  
> - 在 V2Ray/Xray 节点配置中，`tls` 必须开启，且需对应证书。  
>需使用 `node-rule`，请在节点管理页面开启 “节点规则” 并提供规则文件。  
> - 频繁更新节点时建议使用 `passwall update` 脚本或自动代理列表（如 `ssr-shadowsocks` 子域）。

---

> 本文提供了项目概览及快速入门的核心操作步骤，帮助用户快速在 OpenWrt 环境中部署并使用 Passwall 进行网络代理与路由管理。

💝 Support this free API: https://www.paypal.com/donate/?hosted_button_id=XS3CAYT8LE2BL