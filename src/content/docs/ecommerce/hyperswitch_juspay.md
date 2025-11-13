---
title: hyperswitch
---

# Hyperswitch

## 项目简介

Hyperswitch 是一个用 Rust 编写的开源支付开关，旨在使支付快速、可靠且经济。它提供模块化的支付基础设施，允许企业根据需要选择和集成特定模块，而无需不必要的复杂性或供应商锁定。

## 主要功能

Hyperswitch 提供以下核心模块：

- **成本可观测性 (Cost Observability)**：高级可观测性工具，用于审计、监控和优化支付成本。检测隐藏费用、降级和罚款，提供自助仪表板和可操作洞察。
- **收入恢复 (Revenue Recovery)**：通过智能重试策略对抗被动流失，根据卡 bin、地区、方法等进行调整。提供对重试算法、罚款预算和恢复透明度的精细控制。
- **保险库 (Vault)**：PCI 合规的保险库服务，用于存储卡、令牌、钱包和银行凭据。提供统一、安全且可重用的客户关联支付方法存储。
- **智能路由 (Intelligent Routing)**：将每个交易路由到具有最高预测授权率的 PSP。减少重试、避免停机并最小化延迟，同时最大化首次尝试成功率。
- **对账 (Reconciliation)**：自动化双向和三向对账，支持追溯、交错调度和可定制输出。减少手动操作工作量并提高审计信心。
- **替代支付方法 (Alternate Payment Methods)**：PayPal、Apple Pay、Google Pay、Samsung Pay、Pay by Bank 和 BNPL 提供商如 Klarna 的即插即用小部件。通过无缝一键结账最大化转化率。

## 用法

### 本地设置 (Docker)

1. 克隆仓库：

   ```bash
   git clone --depth 1 --branch latest https://github.com/juspay/hyperswitch
   cd hyperswitch
   ```

2. 运行设置脚本：

   ```bash
   scripts/setup.sh
   ```

   该脚本将检测 Docker/Podman，提供多个部署配置文件（标准、全功能、最小），并在完成后提供访问链接。

### 托管沙箱 (无需设置)

Hyperswitch 提供完全托管的沙箱环境，无需设置。您可以直接从 UI 探索控制中心、配置支付连接器并测试支付。

访问：[https://app.hyperswitch.io](https://app.hyperswitch.io)

### 云部署

您可以使用 Helm 或 CDK 脚本部署到 AWS、GCP 或 Azure。最快路径是点击 AWS 部署按钮。

详细说明请参考：[Cloud Install Guide](https://docs.hyperswitch.io/hyperswitch-open-source/deploy-on-kubernetes-using-helm)

## 架构概述

Hyperswitch 采用模块化架构，支持全局支付方法（卡、钱包、BNPL、UPI、按银行支付），公开智能路由和重试逻辑，并在控制中心提供可视化工作流构建器。

## 为什么选择 Hyperswitch？

- **模块化设计**：仅选择您需要的组件。
- **开源**：透明度驱动信任和更好的软件。
- **高性能**：用 Rust 构建，确保可靠性和性能。
- **社区驱动**：由真实世界用例和贡献者塑造路线图。
- **技术-agnostic**：不绑定特定技术栈或供应商。
- **GraphQL only**：高效的API设计，无碎片化。
- **Headless and API only**：API是交互、配置和扩展的唯一方式。
- **云原生**：在全球品牌上经过实战测试。

更多信息：[https://hyperswitch.io/](https://hyperswitch.io/)
