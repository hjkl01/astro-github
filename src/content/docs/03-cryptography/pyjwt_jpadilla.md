---
title: pyjwt
---

# PyJWT 项目

## 项目地址
[GitHub 项目地址](https://github.com/jpadilla/pyjwt)

## 主要特性
PyJWT 是一个纯 Python 实现的 JSON Web Token (JWT) 库，支持 JSON Web Signature (JWS)、JSON Web Encryption (JWE) 和 JSON Web Key (JWK)。它兼容 JWS JOSE 规范（RFC 7515、7516、7517、7518、7519），并提供安全的密钥管理功能。主要特性包括：
- 支持多种算法：HS256、HS384、HS512、RS256、RS384、RS512、ES256、ES384、ES512、EdDSA 等。
- 算法自动验证：防止签名算法混淆攻击（Signature Algorithm Confusion Attack）。
- 内置支持多种密钥类型：对称密钥、非对称密钥、JWK 等。
- 线程安全：适合多线程环境。
- 最小依赖：纯 Python 实现，无需外部依赖（可选集成 cryptography 库以支持更多算法）。
- 兼容性强：支持 Python 3.7+，并提供类型提示（typing 支持）。

## 主要功能
- **编码和解码 JWT**：生成和验证 JSON Web Token，支持自定义负载（payload）和头部（header）。
- **签名和验证**：使用各种算法对 token 进行签名和完整性验证。
- **加密和解密**：支持 JWE 加密 token 的内容。
- **密钥管理**：处理 JWK 和各种密钥格式。
- **错误处理**：提供详细的异常类，如 `InvalidTokenError`、`DecodeError` 等，用于处理无效 token。
- **自定义选项**：支持设置过期时间（exp）、签发者（iss）、受众（aud）等标准 JWT 声明。

## 用法
### 安装
```bash
pip install PyJWT
# 可选：安装 cryptography 以支持更多算法
pip install PyJWT[crypto]
```

### 基本用法示例
#### 编码（生成 JWT）
```python
import jwt

# 使用 HS256 算法编码
payload = {
    'sub': '1234567890',
    'name': 'John Doe',
    'iat': 1516239022  # 签发时间
}
secret_key = 'your-secret-key'
encoded_jwt = jwt.encode(payload, secret_key, algorithm='HS256')
print(encoded_jwt)  # 输出: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

#### 解码（验证 JWT）
```python
import jwt

# 解码并验证
try:
    decoded = jwt.decode(encoded_jwt, secret_key, algorithms=['HS256'])
    print(decoded)  # 输出: {'sub': '1234567890', 'name': 'John Doe', 'iat': 1516239022}
except jwt.InvalidTokenError as e:
    print(f"Token 无效: {e}")
```

#### 使用非对称密钥（RS256）
```python
import jwt

# 假设有私钥和公钥文件
with open('private.pem', 'rb') as f:
    private_key = f.read()
with open('public.pem', 'rb') as f:
    public_key = f.read()

# 编码
encoded = jwt.encode(payload, private_key, algorithm='RS256')

# 解码
decoded = jwt.decode(encoded, public_key, algorithms=['RS256'])
```

更多高级用法请参考官方文档：https://pyjwt.readthedocs.io/