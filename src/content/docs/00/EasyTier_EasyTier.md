---
title: EasyTier
---

# EasyTier

A simple, decentralized mesh VPN with WireGuard support.

## Features

- **Decentralized**: Nodes are equal and independent, no centralized services required.
- **Easy to Use**: Multiple operation methods via web, client, and command line.
- **Cross-Platform**: Supports Windows, macOS, Linux, FreeBSD, Android, and various architectures (x86, ARM, MIPS).
- **Secure**: AES-GCM or WireGuard encryption to prevent man-in-the-middle attacks.
- **NAT Traversal**: Supports UDP and IPv6 traversal, works with NAT4-NAT4 networks.
- **Subnet Proxy**: Nodes can share subnets for other nodes to access.
- **Intelligent Routing**: Latency priority and automatic route selection.
- **High Performance**: Zero-copy throughout the link, supports TCP/UDP/WSS/WG protocols.
- **UDP Loss Resistance**: KCP/QUIC proxy for high packet loss environments.
- **Web Management**: Easy configuration and monitoring via web interface.
- **Zero Config**: Simple deployment with statically linked executables.

## Installation

### Pre-built Binary (Recommended)

Download from [GitHub Releases](https://github.com/EasyTier/EasyTier/releases).

### Via Cargo

```bash
cargo install --git https://github.com/EasyTier/EasyTier.git easytier
```

### Docker

See [documentation](https://easytier.cn/en/guide/installation.html#installation-methods).

### Linux Quick Install

```bash
wget -O- https://raw.githubusercontent.com/EasyTier/EasyTier/main/script/install.sh | sudo bash -s install
```

### macOS via Homebrew

```bash
brew tap brewforge/chinese
brew install --cask easytier-gui
```

## Basic Usage

### Quick Networking with Shared Nodes

Use public shared nodes for quick setup:

```bash
# Node A
sudo easytier-core -d --network-name abc --network-secret abc -p tcp://public.easytier.cn:11010

# Node B
sudo easytier-core -d --network-name abc --network-secret abc -p tcp://public.easytier.cn:11010
```

Check status:

```bash
easytier-cli
```

Test connectivity:

```bash
ping 10.126.126.1
ping 10.126.126.2
```

### Decentralized Networking

Start nodes without central server:

```bash
# Node A
sudo easytier-core -i 10.144.144.1

# Node B
sudo easytier-core -i 10.144.144.2 -p udp://FIRST_NODE_PUBLIC_IP:11010
```

### Subnet Proxy

Share subnets with other nodes:

```bash
sudo easytier-core -i 10.144.144.2 -n 10.1.1.0/24
```

### WireGuard Integration

Enable WireGuard portal:

```bash
sudo easytier-core -i 10.144.144.1 --vpn-portal wg://0.0.0.0:11013/10.14.14.0/24
```

Get client config:

```bash
easytier-cli vpn-portal
```

For more details, visit the [full documentation](https://easytier.cn/en/).
