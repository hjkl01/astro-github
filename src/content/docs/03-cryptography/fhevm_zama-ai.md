---
title: fhevm
---


# FHEVM 项目概述

**GitHub 地址**  
[https://github.com/zama-ai/fhevm](https://github.com/zama-ai/fhevm)

## 一、项目简介  
FHEVM（Fully Homomorphic Encryption Virtual Machine）是一个基于 EVM（以太坊虚拟机）兼容方案的全同态加密（FHE）执行引擎。它允许在保密状态下对加密数据执行智能合约操作，保障数据隐私与安全。

## 二、主要特性  
| 特性 | 说明 |
|------|------|
| **全同态加密支持** | 兼容 Microsoft SEAL、IBM HELib、Microsoft 的 FHE-VM 等 FHE 项目，支持 Add、Multiply、Decrypt、Encrypt 等基本运算。 |
| **EVM 兼容** | 以太坊 Virtual Machine（EVM）的指令集保持几乎完整，方便现有 Solidity 合约迁移或直接编译。 |
| **脚本与编译器** | 提供 `fhevm-compiler`，可将 Solidity 合约编译为 FHEVM 可执行字节码。 |
| **安全性** | 所有状态与合约执行都在加密状态下进行，防止未授权读取。 |
| **可扩展插件** | 支持插件化，可添加自定义密钥管理、图形化调试等功能。 |
| **低延迟** | 通过优化密文运算与缓存，引入近实时交互体验。 |
| **跨链互操作** | 与 zkSygma 等链间桥接器集成，支持多链资产共享。 |

## 三、核心功能  
1. **加密与解密**  
   ```bash
   fhevm-cli encrypt <plainfile> -o <cipherfile>
   fhevm-cli decrypt <cipherfile> -o <plainout>
   ```
2. **合约编译**  
   ```bash
   fhevm-compiler --input MyContract.sol --output MyContract.fvm
   ```
3. **部署与执行**  
   ```bash
   fhevm-cli deploy MyContract.fvm --keypair private.key
   fhevm-cli call <contract_address> <function_name> <args> --keypair private.key
   ```
4. **调试**  
   - 通过 `fhevm-debugger` 可可视化执行堆栈、内存与寄存器状态。  
5. **密钥管理**  
   - 支持本地文件、硬件安全模块（HSM）以及 Zama Key Store 集成。

## 四、快速上手  

```bash
# 1. 安装依赖
npm install -g fhevm-cli fhevm-compiler

# 2. 编译 Solidity 合约
fhevm-compiler --input HelloWorld.sol --output HelloWorld.fvm

# 3. 生成密钥对
fhevm-cli keygen --output keypair.json

# 4. 合约部署
fhevm-cli deploy HelloWorld.fvm --keypair keypair.json --rpc https://fhevm.example.com

# 5. 调用合约
fhevm-cli call <contract_address> hello --args "world" --keypair keypair.json
```

## 五、文档与社区  
- 官方文档: [https://fhevm.zama.ai/docs](https://fhevm.zama.ai/docs)  
- 开发者指南: `docs/` 目录  
- 社区讨论: Discord / GitHub Discussions

---
> 通过 FHEVM，开发者可以在不泄露数据的前提下，构建可扩展且安全的智能合约生态。  
```
> 以上内容请保存为 `src/content/docs/00/fhevm_zama-ai.md`。