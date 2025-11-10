---
title: age
---

# age 项目概述

**GitHub 项目地址：** [https://github.com/FiloSottile/age](https://github.com/FiloSottile/age)

## 主要特性
age 是一个简单、安全、现代的文件加密工具，设计用于简单易用的加密场景。它基于现代密码学原语，提供以下核心特性：
- **简单性**：命令行界面简洁，易于集成到脚本和自动化流程中。
- **安全性**：使用 X25519（椭圆曲线 Diffie-Hellman）密钥交换、ChaCha20-Poly1305 加密和 BLAKE2b 哈希，确保高安全性。支持公钥加密和对称加密。
- **跨平台支持**：兼容 Unix-like 系统（Linux、macOS）和 Windows，支持多种架构。
- **无状态加密**：加密文件不依赖外部配置，易于分发。
- **开源与审计友好**：纯 Go 语言实现，便于代码审查，已通过社区审计。
- **轻量级**：无需复杂依赖，安装简单。

## 主要功能
- **公钥加密**：使用接收者的公钥加密文件，支持多个接收者。
- **对称加密**：使用密码短语加密文件。
- **解密**：自动检测加密类型，使用对应私钥或密码解密。
- **身份文件管理**：生成和管理密钥对，支持加密身份文件。
- **集成友好**：可与 age-keygen 生成密钥，并支持插件式扩展（如 age-plugin-yubikey 用于硬件密钥）。

## 用法示例
### 安装
通过 Go 安装：`go install filippo.io/age/cmd/...@latest`  
或从 GitHub Releases 下载预编译二进制文件。

### 生成密钥对
```bash
age-keygen -o key.txt
# 输出公钥：age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kgttnp4s0qlwegl
```
私钥保存在 `key.txt`，公钥用于加密。

### 加密文件（公钥）
```bash
age -e -o encrypted.age -r age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kgttnp4s0qlwegl plaintext.txt
```
支持多个接收者：`-r recipient1 -r recipient2`。

### 加密文件（对称，密码）
```bash
age -p -o encrypted.age plaintext.txt
# 输入密码短语
```

### 解密文件
```bash
age -d -i key.txt -o decrypted.txt encrypted.age
```
对于密码加密：`age -d -o decrypted.txt encrypted.age`（输入密码）。

### 更多用法
- 查看帮助：`age --help`
- 加密目录：结合 tar 使用，如 `tar -c dir/ | age -o encrypted.age -r pubkey`
- 支持 stdin/stdout：`cat file.txt | age -e -r pubkey > encrypted.age`

详细文档见项目 README。