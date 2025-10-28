
---
title: OpenClash
---


# OpenClash - vernesong

> 项目地址: https://github.com/vernesong/OpenClash

## 1. 概述
OpenClash 是基于 OpenWrt 的高级代理软件，整合了 Clash、ShadowRocket 等多种代理协议，支持多种混合模式，可在路由器上实现流量分流、广告拦截、网络加速等功能。

## 2. 主要特性
- **多协议支持**：Clash、Surge、V2Ray、Trojan、Shadowsocks、WireGuard 等。
- **分流规则**：自定义规则、基于 GeoIP、域名等分流。
- **动态订阅**：支持订阅链接自动更新。
- **Web UI**：完整的管理界面，支持节点管理、规则编辑、日志查看。
- **插件系统**：可扩展自定义脚本和插件。
- **多节点切换**：支持节点快速切换、自动负载均衡。
- **系统集成**：与 OpenWrt 的防火墙、DHCP、QoS 等深度集成。

## 3. 功能说明
| 功能 | 说明 |
|------|------|
| **节点管理** | 导入、编辑、启用/禁用代理节点 |
| **规则管理** | 创建、编辑、导入自定义分流规则 |
| **流量监控** | 实时查看全局/节点/域名流量 |
| **日志分析** | 查看代理日志、错误日志 |
| **订阅更新** | 定时拉取订阅，自动更新节点 |
| **节点切换** | 手动或自动切换节点，支持排障 |
| **安全防护** | DNS 劫持防护、IP 黑名单等 |

## 4. 安装与使用
1. **准备 OpenWrt 系统**  
   - 需要 `root` 权限，且已安装 `curl`、`wget`、`unzip` 等工具。

2. **安装脚本**  
   ```bash
   # 安装 OpenClash
   curl -fsSL https://raw.githubusercontent.com/vernesong/OpenClash/master/utils/install.sh | sh
   ```
   - 该脚本会自动添加软件源、安装必要依赖以及 OpenClash 包。

3. **首次配置**  
   - 访问 `http://<router_ip>/openclash` 或在 OpenWrt LuCI → Services → OpenClash 进行配置。
   - 添加节点、规则、订阅，保存后启用服务。

4. **运行**  
   - 开启后，OpenClash 会在后台拦截并路由符合规则的流量。
   - 可通过 `clash -v` 查看版本与日志。

5. **更新**  
   ```bash
   # 在 OpenWrt 终端执行
   opkg update && opkg install openclash
   ```

## 5. 文档与支持
- 官方 Wiki: https://github.com/vernesong/OpenClash/wiki  
- 常见问题: https://github.com/vernesong/OpenClash/issues  
- 社区讨论: Discord / Telegram 组

## 6. 贡献
- Fork 本仓库，提交 Pull Request。
- 如发现 bug，请在 Issues 中提交详细描述。

