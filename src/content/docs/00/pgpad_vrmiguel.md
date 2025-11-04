
---
title: pgpad
---


# pgpad

**项目地址**: https://github.com/vrmiguel/pgpad

---

## 主要特性

- **安全密码生成**：使用 cryptographically strong RNG 生成符合 PostgreSQL 要求的随机密码。  
- **一次性凭证**：支持生成一次性密码（一次性登录、临时访问）。  
- **CLI 与 API**：提供命令行工具 `pgpad` 与 `pgpad.py` 两种使用方式。  
- **多平台支持**：兼容 Linux、macOS 与 Windows（Python 3.8+）。  
- **易于集成**：支持通过环境变量或配置文件传递 PostgreSQL 连接信息。  
- **日志与错误处理**：针对密码生成与数据库操作提供详细日志，错误信息友好。  

---

## 功能说明

| 功能 | 说明 |
|------|------|
| `generate` | 生成一个安全的随机密码，支持自定义长度与字符集。 |
| `set-password` | 通过 PostgreSQL 连接信息为指定用户设置新密码。 |
| `reset-password` | 将指定用户的密码重置为生成的新密码，并返回新密码。 |
| `one-time` | 生成一次性密码，可用于临时访问或单次登录。 |
| `config` | 读取 `.pgpadrc` 配置文件或环境变量，自动注入连接参数。 |

---

## 用法

### 1. 安装

```bash
# 通过 pip 安装
pip install pgpad
```

> 也可直接克隆仓库后使用 `python -m pgpad` 运行。

### 2. 生成密码

```bash
pgpad generate --length 16
# 输出示例: 8N1vT3k9Jq2ZxLb4
```

### 3. 设置密码

```bash
pgpad set-password --user db_user --host localhost --port 5432 \
  --dbname mydb --password "old_pw" --new-password "$(pgpad generate --length 16)"
```

### 4. 重置密码并返回新密码

```bash
new_pw=$(pgpad reset-password --user db_user --host localhost --port 5432 \
  --dbname mydb --password "old_pw")
echo "新密码为: $new_pw"
```

### 5. 一次性密码

```bash
pgpad one-time --length 12
# 输出示例: aB3dE5hG7jK
```

---

## 配置示例

创建 `~/.pgpadrc`：

```ini
[postgres]
host = localhost
port = 5432
dbname = mydb
user = db_user
password = old_pw
```

然后可省略命令行中的连接参数。

---

## 许可证

MIT © 2024 vrmiguel
