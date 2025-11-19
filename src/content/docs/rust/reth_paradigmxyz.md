---
title: reth
---

## 功能介绍

reth（Rust Ethereum的缩写）是一个新的以太坊全节点实现，专注于用户友好、高度模块化、快速高效。它是以太坊执行层（EL），兼容所有支持Engine API的共识层（CL）实现。reth由Paradigm构建，使用Apache和MIT许可证。

### 主要目标

1. **模块化**：reth的每个组件都设计为可作为库使用，经过充分测试、文档化和基准测试。我们希望开发者可以导入节点的crates，混合搭配，并在之上创新。

2. **性能**：reth使用Rust和Erigon的阶段同步节点架构，以及我们经过战斗测试和优化的以太坊库（如Alloy和revm）。

3. **免费使用**：reth是免费的开源软件，使用Apache/MIT许可证，开发者可以自由使用而无需担心商业许可证或GPL-like许可证的限制。

4. **客户端多样性**：通过构建新的客户端，我们希望为以太坊的抗脆弱性做出贡献，确保网络不会因单一实现错误而最终确定坏块。

5. **支持多个EVM链**：reth不仅可以全同步以太坊，还希望支持其他链如Optimism、Polygon、BNB Smart Chain等。

6. **配置性**：reth旨在支持关心快速历史查询的节点运营商，也支持无法在大型硬件上操作的爱好者。我们希望提供可配置的"配置文件"来处理每个团队面临的权衡。

### 当前状态

reth已生产就绪，适合用于关键环境如质押或高正常运行时间服务。我们积极推荐专业节点运营商在需要高性能的用例（如RPC、MEV、索引、模拟和P2P活动）中切换到reth。

## 用法

### 安装和运行

请参考[reth文档](https://reth.rs/)获取安装和运行reth的详细说明。

### 作为库使用

您可以在项目中使用reth的各个crates。

crate文档可在[此处](https://reth.rs/docs/)找到。

项目布局概述请见[项目布局文档](https://github.com/paradigmxyz/reth/blob/main/docs/repo/layout.md)。

### 贡献

如果您想贡献或关注贡献者讨论，请使用我们的[主要Telegram](https://t.me/paradigm_reth)与我们讨论reth的开发！

- 贡献者指南可在[`CONTRIBUTING.md`](https://github.com/paradigmxyz/reth/blob/main/CONTRIBUTING.md)中找到。
- 更多项目信息请见[贡献者文档](https://github.com/paradigmxyz/reth/blob/main/docs)。好的起点是[项目布局](https://github.com/paradigmxyz/reth/blob/main/docs/repo/layout.md)。

### 构建和测试

此项目的支持的最低Rust版本（MSRV）为[1.88.0](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)。

详细的源码构建说明请见[文档](https://reth.rs/installation/source/)。

要完全测试reth，您需要安装[Geth](https://geth.ethereum.org/docs/getting-started/installing-geth)，但可以在没有Geth的情况下运行部分测试。

首先，克隆仓库：

```
git clone https://github.com/paradigmxyz/reth
cd reth
```

然后运行测试：

```
cargo nextest run --workspace
```

运行以太坊基金会测试：

```
make ef-tests
```

我们强烈推荐使用[`cargo nextest`](https://nexte.st/)来加速测试。使用`cargo test`运行测试可能可以工作，但这未经测试且不支持重试等高级功能。

> **注意**
>
> 一些测试使用随机数生成器生成测试数据。如果您想使用确定性种子，可以设置`SEED`环境变量。

### 获取帮助

如果您有任何问题，首先查看[文档](https://reth.rs/)是否能找到答案。

如果没有：

- 加入[Telegram](https://t.me/paradigm_reth)获取帮助，或
- 打开[讨论](https://github.com/paradigmxyz/reth/discussions/new)提出问题，或
- 打开[问题](https://github.com/paradigmxyz/reth/issues/new?assignees=&labels=C-bug%2CS-needs-triage&projects=&template=bug.yml)报告bug

### 安全

请见[`SECURITY.md`](https://github.com/paradigmxyz/reth/blob/main/SECURITY.md)。

### 致谢

reth是以太坊协议的新实现。在开发节点的过程中，我们调查了其他节点的设计决策，以了解哪些做得好，哪些不好，以及我们可以在哪里改进现状。

如果没有他们，这一切都不可能实现，所以向以下团队致敬：

- [Geth](https://github.com/ethereum/go-ethereum/)：我们衷心感谢go-ethereum团队多年来对以太坊的杰出贡献。
- [Erigon](https://github.com/ledgerwatch/erigon)（前Turbo-Geth）：Erigon开创了reth使用的["阶段同步"架构](https://erigon.substack.com/p/erigon-stage-sync-and-control-flows)，以及引入MDBX作为首选数据库。
- [Akula](https://github.com/akula-bft/akula/)：reth使用Akula的Apache版本的fork：[MDBX绑定](https://github.com/paradigmxyz/reth/pull/132)、[FastRLP](https://github.com/paradigmxyz/reth/pull/63)和[ECIES](https://github.com/paradigmxyz/reth/pull/80)。

### 警告

`NippyJar`和`Compact`编码格式及其实现设计用于内部存储和检索数据。它们没有硬化以安全地读取潜在恶意数据。
