---
title: x402
---


# x402

**项目地址**：<https://github.com/coinbase/x402>

## 概述
x402 是 Coinbase 开源的 Go 语言实现，用于执行 X.402 标准（基于 X.509 证书的密钥协商与加密）的库。该库提供安全的密钥派生、签名验证、对称加密等核心功能，适配服务之间的安全通信与数据保护。

## 主要特性
- **ECDH 密钥协商**：支持 P-256、P-384、P-521、secp256k1 等椭圆曲线。  
- **签名与验证**：使用 ECDSA/ED25519 等算法对数据进行签名与验证。  
- **对称加密**：基于共享密钥实现 AES‑GCM 加密/解密。  
- **X.509 证书处理**：读取、解析并验证证书链。  
- **简洁 API**：提供易用的函数接口，方便集成。  

## 安装
```bash
go get github.com/coinbase/x402
```

## 用法示例

### 生成密钥对
```go
package main

import (
    "github.com/coinbase/x402"
)

func main() {
    priv, err := x402.GeneratePrivateKey(x402.P256)
    if err != nil { panic(err) }
    pub := priv.Public()
    // ...
}
```

### ECDH 共享密钥
```go
sharedSecret, err := x402.DeriveSharedSecret(priv, otherPub)
```

### 签名与验证
```go
sig, err := x402.Sign(priv, data)
ok, err := x402.Verify(pub, data, sig)
```

### 对称加密
```go
cipherText, err := x402.Encrypt(sharedSecret, plaintext)
plainText, err := x402.Decrypt(sharedSecret, cipherText)
```
```
