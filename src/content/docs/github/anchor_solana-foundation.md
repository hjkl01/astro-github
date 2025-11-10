---
title: anchor
---


# Anchor – Solana Foundation

> GitHub地址: <https://github.com/solana-foundation/anchor>

## 主要特性
- **高级DSL**：使用 Rust 宏提供简洁的程序/账户声明，自动生成 IDL（Interface Definition Language）。
- **类型安全**：在编译期验证账户结构、权限与序列化，减少运行时错误。
- **自动化测试**：内置 `solana-program-test` 与 `Anchor framework test`，支持集成测试与 Haskell 编写。
- **跨语言客户端**：生成 TypeScript / JavaScript 客户端 SDK，支持 IDL 导入、账户校验和交易签名。
- **离线签名 & 集群抽象**：提供可在本地离线签名且可切换 Devnet、Testnet、Mainnet 的功能。
- **错误码编译**：将 Rust 错误映射为可识别的程序错误码，便于前端处理。

## 核心功能
| 功能 | 简述 |
|------|------|
| **Accounts** | 定义账户结构、权限校验与序列化，使用 `#[account]` 宏 |
| **Instructions** | 用 `#[instruction(...)]` 定义入口参数，自动生成 `.idl.json` |
| **Idl** | 编译后自动生成 IDL，支持前端 SDK 自动更新 |
| **Client SDK** | 通过 `anchor-client` 生成 TS/JS SDK，包含 schema 校验 |
| **Macro** | `#[program]`、`#[error]`、`#[derive(Accounts)]` 等宏，生成程序入口、错误处理及账户校验 |
| **Testing** | `#[program_test]` 与 `#[processor_test]` 分别用于集成与单元测试 |
| **Accounts Loader** | `#[account]` 与 `borsh` 序列化，支持加载与创建账户 |
| **CPI 支持** | `invoke_signed` 与 `invoke` 的封装，支持签名调用 |

## 用法

### 1. 安装 Anchor
```bash
cargo install --git https://github.com/solana-foundation/anchor --tag v0.30.0 anchor-cli
```

### 2. 创建项目
```bash
anchor init my_anchor_project
```

### 3. 编写程序
```rust
#[program]
mod my_program {
    use super::*;
    pub fn initialize(ctx: Context<Initialize>, value: u64) -> Result<()> {
        let data_account = &mut ctx.accounts.data_account;
        data_account.value = value;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub data_account: Account<'info, DataAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[account]
pub struct DataAccount {
    pub value: u64,
}
```

### 4. 生成 IDL 与客户端
```bash
anchor idl --output-dir ./idl
anchor build
anchor test
```

### 5. 使用 TypeScript SDK
```bash
npm install @project-serum/anchor
```
```ts
import * as anchor from '@project-serum/anchor';
const idl = require('./idl/my_anchor_project.json');
const programId = new anchor.web3.PublicKey('PROGRAM_ID');
const provider = anchor.Provider.env();
const program = new anchor.Program(idl, programId, provider);

await program.rpc.initialize(42, {
  accounts: {
    dataAccount: await program.provider.connection.getAccountInfo(somePubkey),
    user: program.provider.wallet.publicKey,
    systemProgram: anchor.web3.SystemProgram.programId,
  }
});
```

### 6. 部署到 Devnet / Mainnet
```bash
anchor deploy --provider.cluster devnet
```

## 贡献指南
- Fork 仓库并提交 PR。
- 运行 `anchor test` 与 `cargo fmt` 与 `cargo clippy`。
- 跟随 Contributor 手册编写文档及案例。

---
> 以上为 Anchor 框架的核心特性与常用用法，帮助快速上手 Solana 程序开发。