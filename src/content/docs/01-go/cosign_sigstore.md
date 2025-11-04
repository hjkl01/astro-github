
---
title: cosign
---


# sigstore/cosign

GitHub 地址: https://github.com/sigstore/cosign

## 主要特性

- **容器镜像签名与验证**：对 Docker 镜像进行数字签名，保证镜像完整性和真实性。  
- **文件签名**：支持签署任意二进制文件或压缩包，生成与镜像同名的签名文件（`.sig` / `.cosign`）。  
- **透明度日志**：签名信息被写入 Sigstore Transparency Log，提供不可篡改的审计追踪。  
- **无钥匙（Keyless）签名**：结合 Sigstore 的 Fulcio 与 Rekor，允许使用 X.509 证书直接签名，无需私钥。  
- **多平台与 CI/CD 集成**：适配 CI/CD 流水线、Kubernetes 等环境，支持自动签名与验证。  
- **多种密钥支持**：兼容 PGP、Keystore、KMS（AWS KMS、GCP KMS、Azure Key Vault）等。  
- **简化工作流**：单个命令即可完成签名、验证或生成签章文件。

## 常用功能

| 功能 | 示例命令 |
|------|-----------|
| 镜像签名 | `cosign sign --key $(pwd)/cosign.key docker.io/yourrepo/imagename:tag` |
| 镜像验证 | `cosign verify --key $(pwd)/cosign.pub docker.io/yourrepo/imagename:tag` |
| 文件签名 | `cosign sign-blob --key $(pwd)/cosign.key myfile.tar.gz` |
| 文件验证 | `cosign verify-blob --key $(pwd)/cosign.pub myfile.tar.gz.sig` |
| Keyless 签名 | `cosign sign --key env://CO_KEY env://COSIGN_PASSWORD docker.io/yourrepo/imagename:tag` |
| 查看签名信息 | `cosign describe docker.io/yourrepo/imagename:tag` |

## 使用步骤

1. **安装 cosign**  
   ```bash
   # Homebrew（macOS / Linux）
   brew install cosign
   # 官方脚本
   curl -fsSL https://raw.githubusercontent.com/sigstore/cosign/main/cosign-install.sh | sh
   ```

2. **创建/获取密钥（可选）**  
   ```bash
   cosign generate-key-pair
   # .pub 用于验证
   ```

. **签名镜像或文件**  
   ```bash
   cosign sign --key $(pwd)/cosign.key docker.io/yourrepo/imagename:latest
   # 或
   cosign sign-blob --key $(pwd)/cosign.key mybinary.bin
   ```

4. **验证签名**  
   ```bash
   cosign verify --key $(pwd)/cosign.pub docker.io/yourrepo/imagename:latest
   # 或
   cosign verify-blob --key $(pwd)/cosign.pub mybinary.bin.sig
   ```

5. **CI/CD 集成**  
   - 在 GitHub Actions 或其他流水线中使用 secrets 存储密钥，或启用 Keyless 签名。  
   - 在构建脚本中添加对应的签名/验证步骤。

## 参考

- 官方文档: https://docs.sigstore.dev/cosign/
- 代码仓库: https://github.com/sigstore/cosign
