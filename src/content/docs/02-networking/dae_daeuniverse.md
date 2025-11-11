---
title: dae
---

# dae

dae 是一个基于 eBPF 的 Linux 高性能透明代理解决方案。它通过在 Linux 内核中使用透明代理和流量分割套件来最大化增强流量分割性能，从而实现真正的直接流量绕过代理应用的转发，使直接流量真正直接通过。这使得直接流量的性能损失最小，额外资源消耗几乎为零。

作为 v2rayA 的继任者，dae 放弃了 v2ray-core，以更自由地满足用户需求。

## 功能特性

- **真正的直接流量分割**：需要启用 ipforward，实现高性能。
- **按进程名分割流量**：支持在本地主机中按进程名分割流量。
- **按 MAC 地址分割流量**：支持在 LAN 中按 MAC 地址分割流量。
- **反向匹配规则**：支持使用反向匹配规则分割流量。
- **自动节点切换**：根据策略自动切换节点，支持自动测试独立 TCP/UDP/IPv4/IPv6 延迟，然后根据用户定义的策略为相应流量使用最佳节点。
- **高级 DNS 解析**：支持高级 DNS 解析过程。
- **全锥 NAT 支持**：支持 shadowsocks、trojan(-go) 和 socks5 的全锥 NAT（socks5 未测试）。
- **多种代理协议**：支持各种流行的代理协议。

## 使用方法

请参考 [快速开始指南](https://github.com/daeuniverse/dae/blob/main/docs/en/README.md) 立即开始使用 dae！

### 注意事项

1. 如果在公共网络（如 VPS）上设置 dae 和 shadowsocks 服务器（或任何 UDP 服务器），请不要忘记为您的 UDP 服务器端口添加 `l4proto(udp) && sport(your server ports) -> must_direct` 规则。因为 UDP 状态难以维护，所有传出 UDP 数据包都可能被代理（取决于您的路由），包括到客户端的流量。这不是我们想要的行为。`must_direct` 使来自此端口的所有流量（包括 DNS 流量）直接通过。
2. 如果中国大陆用户发现首次访问某些国内网站时首屏时间很长，请检查是否在 DNS 路由中使用外国 DNS 处理某些国内域名。有时这很难发现。例如，`ocsp.digicert.cn` 意外包含在 `geosite:geolocation-!cn` 中，这会导致某些 TLS 握手时间很长。请小心在 DNS 路由中使用此类域名集。

## 工作原理

详见 [工作原理](https://github.com/daeuniverse/dae/blob/main/docs/en/how-it-works.md)。

## 许可证

AGPL-3.0 (C) daeuniverse
