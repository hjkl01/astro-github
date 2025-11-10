---
title: bottlerocket
---
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