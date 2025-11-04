
---
title: bottlerocket
---

## Bottlerocket

**项目地址**  
[https://github.com/bottlerocket-os/bottlerocket](https://github.com/bottlerocket-os/bottlerocket)

---

### 项目简介
Bottlerocket 是一个专为容器化工作负载设计的、极简化、只读的 Linux 操作系统。它提供了更小的攻击面、更高的安全性和更简洁的管理体验，常用于 Kubernetes 集群中的节点系统。

---

### 主要特性

- **只读文件系统**：根文件系统默认只读，所有可写数据存放在 tmpfs 或 OverlayFS，减少磁盘写入次数。
- **安全性强**：采用基于映像的回滚、Tiny Core Linux + Alpine Linux 结合，默认开启 SELinux、AppArmor、seccomp 等安全强化。
- **微服务友好**：内置 Docker 和 containerd，支持多种容器镜像格式，简化部署。
- **自动升级**：通过 *bottlerocket-update* 自动处理镜像更新与安全补丁，无须人工干预。
- **资源占用低**：二进制包约 10 MiB，内核仅 12 MiB，适合低功耗设备。
- **云原生集成**：官方支持 Kubernetes、OpenShift 等主流云原生平台，配合 CSI、CRDs 等插件。

---

### 主要功能

| 功能 | 说明 |
|------|------|
| **基本系统管理** | 只读文件系统，管理通过 `bottlerocket` CLI 或 API 进行配置。 |
| **容器引擎** | 内置 Docker 与 containerd，支持 OCI 镜像，兼容 Docker Compose、Kubernetes Pod 规范。 |
| **镜像更新** | `bottlerocket-update` 自动拉取新镜像、校验签名并完成回滚或升级。 |
| **网络/存储插件** | 支持 CNI、CSI 等插件，可通过 `bottlerocket.conf` 配置网络与存储。 |
| **监控与日志** | 通过集成 rkt/Prometheus/Elasticsearch 等工具，可获取系统指标与日志。 |
| **安全补丁** | 自动签名校验，防止恶意镜像；内核与应用均采用官方安全镜像。 |

---

### 用法

1. **下载镜像**

   ```bash
   # 以镜像方式获取
   docker pull bottlerocket/bottlerocket:stable
   ```

2. **写入磁盘**

   ```bash
   # 使用最新 CLI 写入 USB
   bottlerocket /dev/sdX
   ```

3. **启动与配置**

   - 在 `/etc/bottlerocket`（也可通过 `bottlerocket` CLI）修改网络、日志级别等。  
   - 系统默认已启用 `docker` 与 `containerd`，可直接 `docker run`。

4. **更新系统**

   ```bash
   # 手动触发更新
   bottlerocket-update
   ```

5. **在 Kubernetes 中使用**

   - 将 Bottlerocket 镜像设为节点启动镜像。  
   - 通过 Kubelet `nodeSelector`、`runtimeClass` 等方式指定容器运行环境。

---

> 通过上述方式，Bottlerocket 可无缝嵌入云原生环境，提供安全、轻量、可维护的节点系统。  
> 更多细节请参考官方文档与 GitHub 仓库。