
---
title: node_exporter
---

# node_exporter

**项目地址**：<https://github.com/prometheus/node_exporter>

## 简介
`node_exporter` 是一个轻量级的 Prometheus 监控插件，用于收集 Linux、Windows、macOS、FreeBSD 等主机系统的各种硬件与操作系统指标，并通过 HTTP 接口暴露给 Prometheus 服务器。只需一个可执行文件即可运行，适合在生产环境中快速部署。

---

## 主要特性

| 特色 | 说明 |
|------|------|
| **多平台支持** | 兼容 Linux、Windows、macOS、FreeBSD 等 |
| **指标覆盖** | CPU、内存、磁盘 I/O、文件系统、网络、进程、系统负载、交换空间、硬件温度、Power Supply 等 |
| **轻量级** | 仅需一个二进制文件，内存占用 < 20 MB |
| **可配置** | 通过命令行参数开启/关闭各个采集器 |
| **自定义指标** | `textfile` 采集器支持将自定义文件写入 `/metrics` |
| **安全** | 支持 TLS、Basic Auth、Bearer Token 认证 |
| **高可用** | 与 Prometheus 生态无缝集成，支持 Service Discovery、Static Targets 等 |

---

## 功能点

- **HTTP/HTTPS 端点**：默认 `/metrics`，可通过 `--web.listen-address` 指定监听地址与端口。
- **TLS/认证**：`--web.tls.server-cert`、`--web.tls.server-key`、`--web.auth.file`、`--web.auth.bearer-token-file` 等。
- **采集器**：如 `--collector.processes`、`--collector.diskstats`、`--collector.filesystem`、`--collector.netstat`、`--collector.meminfo` 等。
- **根文件系统**：`--path.rootfs` 指定根目录，支持跨容器、chroot 环境。
- **忽略挂载点**：`--collector.filesystem.ignored-mount-points` 过滤不需要的文件系统。

---

## 安装

### 1. 预编译二进制
```bash
# 下载对应系统的压缩包
wget https://github.com/prometheus/node_exporter/releases/download/v1.8.0/node_exporter-1.8.0.linux-amd64.tar.gz
tar -xzf node_exporter-1.8.0.linux-amd64.tar.gz
cd node_exporter-1.8.0.linux-amd64
```

### 2. Docker
```bash
docker run -d -p 9100:9100 --name node_exporter prom/node-exporter
```

### 3. 源码编译
```bash
go install github.com/prometheus/node_exporter@latest
```

---

## 使用方式

1. **启动**  
   ```bash
   ./node_exporter
   ```
   默认监听 `:9100`，可通过 `--web.listen-address=:9200` 改为其他端口。

2. **Prometheus 配置**  
   ```yaml
   scrape_configs:
     - job_name: 'node'
       static_configs:
         - targets: ['localhost:9100']
   ```

3. **自定义采集**（示例）  
   ```bash
   ./node_exporter \
     --collector.filesystem.ignored-mount-points='^/(sys|proc|dev|host|rootfs|run|tmp|var/lib/docker|var/lib/kubelet|var/lib/rancher|var/lib/rkt|var/lib/containers|var/lib/docker\.dev)($|/)' \
     --collector.diskstats \
     --collector.meminfo
   ```

---

## 文档与示例

- **官方 README**：<https://github.com/prometheus/node_exporter/blob/main/README.md>
- **示例配置**  
  ```yaml
  scrape_configs:
    - job_name: 'node'
      static_configs:
        - targets: ['192.168.1.100:9100']
      metrics_path: /metrics
      scheme: https
      tls_config:
        ca_file: /etc/ssl/certs/ca.pem
  ```

---

## 贡献

- Fork → Clone → `git checkout -b feat/your-feature` → 提交 Pull Request
- 代码遵循 `golang` 规范，使用 `golangci-lint` 进行静态检查。
- 详细贡献指南请查看项目根目录的 `CONTRIBUTING.md`。

---

### 备注
- 运行时请确保 `node_exporter` 有足够权限读取 `/proc`、`/sys` 等系统目录。
- 对于容器化部署，可使用 `--path.rootfs=/host` 指向宿主机根目录。

> **完成**  
> 以上即为 `node_exporter` 项目的主要特性、功能与使用方法。祝使用愉快！