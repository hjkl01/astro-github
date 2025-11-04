
---
title: vault
---

# Vault (HashiCorp)

**项目地址**：<https://github.com/hashicorp/vault>

## 项目简介  
Vault 是一个开源的秘密管理与数据加密系统，提供安全存储、密钥管理、访问控制和审计等功能。它被广泛用于保护敏感信息、强制安全策略以及实现动态凭据生成。

## 主要特性  
| 特性 | 说明 |
|------|------|
| **加密即服务** | 支持多种加密算法（AES、RSA、ChaCha20 等），用户可通过 API 进行加密/解密操作。 |
| **动态凭据** | 对数据库、云服务、SSH 等后端生成一次性或短期凭证，提高安全性。 |
| **集中管理** | 统一管理多平台密钥、证书、令牌，降低配置复杂度。 |
| **多租户** | 通过命名空间或密钥路径实现多租户隔离。 |
| **安全审计** | 记录所有请求与响应，支持多种审计后端（file、syslog、kafka、opentelemetry 等）。 |
| **秘钥旋转** | 自动周期性旋转密钥与凭证，减少密钥泄露风险。 |

## 核心功能  
1. **Secret Engines**  
   - KV (Key-Value)  
   - PKI (私钥/公钥基础设施)  
   - Database, Cosmos, MySQL, MongoDB 等动态凭据生成  
   - Transit (加密/解密)  
   - Identity & Access Management  

2. **Auth Methods**  
   - Token  
   - AppRole  
   - LDAP / Active Directory  
   - Kubernetes  
   - AWS, GCP, Azure IAM  
   - GitHub, GitLab, JWT  

3. **Policy & ACL**  
   - 基于路径的权限控制  
   - 预定义策略 (`root`, `default`, `read`, `write`, `sudo` 等)  

4. **Raft 复制模式** (可选)  
   - 内置分布式共识协议  
   - 高可用与灾备  

5. **插件体系**  
   - 可通过自定义插件扩展功能  
   - 动态后端和认证插件  

## 用法示例（命令行 & API）  

### 1. 安装并初始化  
```bash
# 下载并安装
brew install vault

# 初始化 Vault
vault operator init
# 输出后需要保存每个unseal key与root token

# 解封
vault operator unseal <key-1>
vault operator unseal <key-2>
vault operator unseal <key-3>
```

### 2. 配置秘钥存储  
```bash
# 创建 KV secret
vault kv put secret/employee/JohnDoe name="John" department="Engineering"

# 读取 secret
vault kv get secret/employee/JohnDoe
```

### 3. 动态数据库凭据  
```bash
# 创建数据库后端
vault auth enable database
vault write database/config/mydb \
    plugin_name=mysql-database-plugin \
    allowed_roles="readonly" \
    connection_url="{{username}}:{{password}}@tcp(db-host:3306)/"

vault write database/roles/readonly \
    db_name="mydb" \
    creation_statements="CREATE USER '{{name}}'@'%' IDENTIFIED BY '{{password}}'; GRANT SELECT ON *.* TO '{{name}}'@'%';" \
    default_ttl="1h" \
    max_ttl="24h"

# 生成凭据
vault read database/creds/readonly
```

### 4. 加密/解密数据  
```bash
# 启用 Transit backend
vault secrets enable transit

# 创建密钥
vault write -f transit/keys/mykey

# 加密
vault write -f transit/encrypt/mykey plaintext="cGFzc3dvcmQ="
# 附注：plaintext 需要 Base64 编码

# 解密
vault write -f transit/decrypt/mykey ciphertext="AQABAIz..."
```

### 5. 访问控制示例  
```bash
# 创建策略
vault policy write dev-allow-read -<<EOT
path "secret/data/dev/*" {
  capabilities = ["read"]
}
EOT

# 创建 token 并绑定策略
vault token create -policy="dev-allow-read"

# 使用 token
export VAULT_TOKEN=<<generated-token>>
vault kv get secret/data/dev/project1
```

以上是 Vault 的核心概念与典型使用场景，帮助你快速开始在项目中安全管理机密信息。