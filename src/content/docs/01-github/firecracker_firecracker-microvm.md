
---
title: firecracker
---

---

**文件路径**  
`src/content/docs/00/firecracker_firecracker-microvm.md`

**内容**  
```markdown
# Firecracker MicroVM

**项目地址**  
[https://github.com/firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker)

## 概述
Firecracker 是一个极简、内存占用低、启动快（< 1 s）的虚拟机监控器（VMM），专为 **微型虚拟机（microVM）** 设计常用于无服务器（Serverless）与容器运行时（如 AWS Lambda、Fargate、Cloud Functions 等）。

## 主要特性
- **轻量级**：单个 guest 微VM 只需数 MB 内存，几百 KB 虚拟磁盘。
- **快速启动**：启动时间可低至数百毫秒，减少冷启动延迟。
- **高安全隔离**：通过 KVM + Linux namespace + VirtIO 实现硬件级隔离；不暴露 host 系统。
- **资源限制**：可精确限制 CPU、内存、块/网络 IO 等。
- **兼容性**：仅需 Linux Guest 与 minimal initramfs；支持 X86‑64 与 ARMv7/8。
- **网络 & 存储**：VirtIO‐Net、VirtIO‑Block、virtio‑9p、virtio‑trans‑sockets 等虚拟设备。

## 主要功能
1. **创建 & 配置 microVM**  
   - 调用 **API Socket** 的 HTTP/JSON 接口（如 `/api/v1/boot-source`、`/api/v1/memory`、`/api/v1/hardware-config` 等）来设置 BIOS、kernel、initrd、CPU、内存、盘片、网络等。
2. **启动 / 停止 / 监控**  
   - `POST /api/v1/control/start` 启动 VM；  
   - `POST /api/v1/control/halt` 软停；  
   - `POST /api/v1/control/pause` 与 `resume`；  
   - `GET /api/v1/metrics` 查询资源使用情况。
3. **事件与日志**  
   - 通过 `firecracker --log-level` 设置日志，支持标准输出、syslog、以及自定义日志文件。
4. **VMI (VirtIO Machine IO) provider**  
   - 通过 `virtio‑9p` 为 guest 提供共享文件系统，或 `virtio‑net` 通过 tap/bridge。

## 用法示例

1. **编译与运行**
   ```bash
   # 克隆源码
   git clone https://github.com/firecracker-microvm/firecracker.git
   cd firecracker

   # 编译（需 Rust 1.57+）
   cargo build --release

   # 运行 Firecracker，监听套接字 /tmp/firecracker.socket
   sudo target/release/firecracker --api-sock /tmp/firecracker.socket
   ```

2. **使用 curl 配置并启动 VM**
   ```bash
   # 设置 boot-source
   curl -X PUT -d @- \
        -H "accept: application/json" \
        -H "Content-Type: application/json" \
        --unix-socket /tmp/firecracker.socket \
        http://localhost/api/v1/boot-source <<EOF
   {
     "kernel_image_path": "/path/to/vmlinuz",
     "boot_args": "console=ttyS0 reboot=k panic=1",
     "initrd_path": "/path/to/initrd.img"
   }
   EOF

   # 设置内存
   curl -X PUT -d @- \
        -H "accept: application/json" \
        -H "Content-Type: application/json" \
        --unix-socket /tmp/firecracker.socket \
        http://localhost/api/v1/memory <<EOF
   {
     "guest_memory_size_mib": 512
   }
   EOF

   # 启动 VM
   curl -X POST --unix-socket /tmp/firecracker.socket http://localhost/api/v1/control/start
   ```

3. **查看指标**
   ```bash
   curl --unix-socket /tmp/firecracker.socket http://localhost/api/v1/metrics
   ```

## 参考资料
- 官方文档: [https://firecracker-microvm.github.io/firecracker](https://firecracker-microvm.github.io/firecracker)
- GitHub 仓库: [https://github.com/firecracker-microvm/firecracker](https://github.com/firecracker-microvm/firecracker)
```

---