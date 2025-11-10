---
title: openwrt-passwall2
---

# openwrt-passwall2

## 功能

openwrt-passwall2 是 OpenWRT 系统的一个 LuCI 应用插件，用于科学上网和代理服务。它支持多种代理协议，包括 V2Ray、Xray、Sing-Box 等，提供灵活的节点管理和规则配置。

主要功能：

- 支持多种代理协议：V2Ray, Xray, Sing-Box, Shadowsocks 等
- 节点管理：添加、编辑、删除代理节点
- 规则配置：域名规则、IP规则、应用规则等
- DNS 配置：支持自定义 DNS 和 DNS 劫持
- 负载均衡：多节点负载均衡
- 透明代理：支持全局代理、绕过中国大陆等模式
- 兼容性：支持多种 OpenWRT 版本

## 用法

1. 安装插件：通过 OpenWRT 的软件包管理器安装 luci-app-passwall2。
2. 配置节点：在 LuCI 界面中添加代理节点，输入服务器地址、端口、密码等信息。
3. 设置规则：配置哪些域名或IP使用代理，哪些绕过。
4. 启动服务：启用 passwall2 服务，开始代理。
5. 高级配置：根据需要配置 DNS、负载均衡等。

注意：使用前确保遵守当地法律法规。
