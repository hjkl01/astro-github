---
title: EIPs
---

# EIPs_ethereum

## 项目介绍

EIPs (Ethereum Improvement Proposals) 是 Ethereum 改进提案的仓库，旨在标准化和提供高质量文档给 Ethereum 协议及其上的约定。该仓库跟踪过去和正在进行的 Ethereum 改进，以 EIP (Ethereum Improvement Proposal) 的形式记录。

## 功能

- **标准化文档**：提供高质量的 Ethereum 协议和约定文档。
- **分类提案**：
  - Core EIPs：Ethereum 共识协议的改进。
  - Networking EIPs：指定 Ethereum 的点对点网络层。
  - Interface EIPs：标准化用户和应用与区块链交互的接口。
  - Meta EIPs：需要某种共识的杂项改进。
  - Informational EIPs：不需要共识的非标准改进。
- **状态跟踪**：通过 https://eips.ethereum.org/ 网站跟踪 EIP 状态。
- **自动化验证**：PR 通过 eip-review-bot、eipw、HTMLProofer、CodeSpell 和 markdownlint 检查。

注意：ERCs (Ethereum Request for Comments) 现在位于单独的仓库 https://github.com/ethereum/ercs。

## 用法

1. **讨论想法**：在 [Ethereum Magicians](https://ethereum-magicians.org/) 或 [Ethereum Research](https://ethresear.ch/) 上彻底讨论提案。
2. **阅读 EIP-1**：了解 EIP 流程，详见 https://eips.ethereum.org/EIPS/eip-1。
3. **提交提案**：向此仓库提交 PR，提案必须遵循 EIP-1 规则。
4. **本地验证**：使用 `eipw` 工具验证 EIP：
   ```
   cargo install eipw
   eipw --config ./config/eipw.toml <文件或目录>
   ```
5. **构建状态页面**：
   - 安装 Ruby 3.1.4 和 Bundler。
   - 运行 `bundle install` 安装依赖。
   - 运行 `bundle exec jekyll serve` 启动本地服务器，预览于 http://localhost:4000。

## 注意事项

- 此仓库仅用于记录标准，不提供实现帮助。实现问题请咨询 [Ethereum Stack Exchange](https://ethereum.stackexchange.com)。
- 成为 EIP 编辑者请阅读 EIP-5069。
- 引用格式：规范 URL 为 https://eips.ethereum.org/，如 https://eips.ethereum.org/EIPS/eip-1。
