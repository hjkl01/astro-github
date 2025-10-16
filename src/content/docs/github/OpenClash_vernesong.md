
---
title: OpenClash
---

# OpenClash 项目

## 项目地址
[GitHub 项目地址](https://github.com/vernesong/OpenClash)

## 主要特性
OpenClash 是一个基于 OpenWrt 的 Clash 客户端项目，主要用于在路由器上实现科学上网和流量分流。其核心特性包括：
- **支持多种代理协议**：兼容 Shadowsocks (SS)、ShadowsocksR (SSR)、V2Ray、Trojan 等主流代理协议。
- **规则引擎**：内置强大的规则匹配系统，支持 GeoIP、域名、IP 等多种规则类型，实现精细化的流量分流（如直连、中国优化、全球代理）。
- **TUN 模式支持**：通过 TUN 虚拟网卡实现透明代理，适用于所有设备流量劫持，无需手动配置。
- **可视化管理界面**：提供 Web 面板，支持实时监控连接状态、流量统计和日志查看。
- **订阅管理**：自动更新订阅链接，支持 YAML 配置文件导入和编辑。
- **DNS 优化**：集成 Fake-IP 和自定义 DNS 解析，防止 DNS 污染。
- **跨平台兼容**：专为 OpenWrt 设计，但可扩展到其他 Linux 系统。

## 主要功能
- **代理客户端**：将 Clash 核心移植到 OpenWrt，实现路由级代理，支持全设备透明上网。
- **流量控制**：通过策略组和规则集，实现基于地理位置、应用或域名的智能路由（如将国内流量直连，国外流量走代理）。
- **负载均衡**：支持多个节点轮询、延迟测试和自动选优。
- **安全增强**：集成混淆、加密和防探测功能，提升代理稳定性。
- **扩展插件**：可与 OpenWrt 的 luci 界面集成，提供一键安装和配置。
- **日志与调试**：详细的运行日志，支持故障排查和性能优化。

## 用法
1. **安装**：
   - 在 OpenWrt 路由器上，通过 SSH 登录，运行一键安装脚本：`sh -c "$(curl -sL https://github.com/vernesong/OpenClash/releases/latest/download/install.sh)"`。
   - 或在 LuCI 界面中搜索并安装 OpenClash 包（需先更新软件源）。

2. **配置**：
   - 访问路由器 Web 界面（通常为 `192.168.1.1/cgi-bin/luci/admin/services/openclash`）。
   - 上传或输入 Clash 配置文件（YAML 格式），或添加订阅 URL。
   - 下载并选择核心文件（Clash Premium 或 Meta 核心，根据需求）。

3. **启动与管理**：
   - 在面板中点击“启用 OpenClash”启动服务。
   - 配置规则模式（Rule/Global/Direct），设置 DNS 和 TUN 参数。
   - 测试连接：使用“延迟测试”功能验证节点可用性。
   - 监控：查看实时流量图、连接日志，调整规则以优化分流。

4. **高级用法**：
   - 编辑 `/etc/openclash/config.yaml` 文件自定义规则。
   - 支持脚本自动化，如定时更新订阅或重启服务。
   - 故障排除：检查日志文件 `/tmp/openclash.log`，确保内核模块（如 tun）已加载。

注意：使用前确保路由器有足够存储空间和 CPU 性能，建议备份配置。项目活跃维护，定期查看 GitHub 更新。