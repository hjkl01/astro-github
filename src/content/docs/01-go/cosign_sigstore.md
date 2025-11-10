---
title: cosign
---

# sigstore/cosign

GitHub 地址: https://github.com/sigstore/cosign

## 信息

`Cosign` 是 [`sigstore`](https://sigstore.dev) 项目的一部分。我们也使用一个 [slack 频道](https://sigstore.slack.com)! 点击 [这里](https://join.slack.com/t/sigstore/shared_invite/zt-mhs55zh0-XmY3bcfWn4XEyMqUUutbUQ) 获取邀请链接。

## 主要特性

- **容器签名、验证和存储**：在 OCI 注册表中。
- **无钥匙签名**：使用 Sigstore 公共良好 Fulcio 证书颁发机构和 Rekor 透明日志（默认）。
- **硬件和 KMS 签名**。
- **使用 cosign 生成的加密私钥/公钥对签名**。
- **支持其他工件**：二进制文件、脚本、配置文件等。
- **带来您自己的 PKI**。

## 常用功能

| 功能         | 示例命令                                                                                |
| ------------ | --------------------------------------------------------------------------------------- |
| 镜像签名     | `cosign sign --key $(pwd)/cosign.key docker.io/yourrepo/imagename:tag`                  |
| 镜像验证     | `cosign verify --key $(pwd)/cosign.pub docker.io/yourrepo/imagename:tag`                |
| 文件签名     | `cosign sign-blob --key $(pwd)/cosign.key myfile.tar.gz`                                |
| 文件验证     | `cosign verify-blob --key $(pwd)/cosign.pub myfile.tar.gz.sig`                          |
| Keyless 签名 | `cosign sign --key env://CO_KEY env://COSIGN_PASSWORD docker.io/yourrepo/imagename:tag` |
| 查看签名信息 | `cosign describe docker.io/yourrepo/imagename:tag`                                      |

## 使用步骤

1. **安装 cosign**
   - 请参见上面的安装部分。

2. **创建/获取密钥（可选）**

   ```bash
   cosign generate-key-pair
   # .pub 用于验证
   ```

3. **签名镜像或文件**

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
