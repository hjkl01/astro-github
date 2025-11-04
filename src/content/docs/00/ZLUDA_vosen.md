
---
title: ZLUDA
---


# ZLUDA (vosen) 项目

**项目地址**: <https://github.com/vosen/ZLUDA>

## 项目简介
ZLUDA 是一个开源的 CUDA 运行时与驱动实现，旨在使用户可以在不安装官方 NVIDIA 驱动的情况下运行 CUDA 程序。它提供了 CUDA API 的完整兼容实现，支持多 GPU、内存管理、流（stream）、事件（event）、IPC 等核心功能，并能与现有的 CUDA 编译器、工具链无缝配合。

## 主要特性

| # | 功能 | 说明 |
|---|------|------|
| 1 | **CUDA API 兼容** | 对 CUDA Runtime / Driver API 的完整实现，支持 `cudaMalloc`, `cudaMemcpy`, `cudaLaunchKernel` 等 |
| 2 | **多 GPU 支持** | 能够在多块 GPU 上分配资源、同步运行流，并支持设备间的 IPC 通信 |
| 3 | **硬件无关** | 通过宿主机的 OpenCL / Level‑Zero 接口实现，消除对 NVIDIA 驱动的依赖 |
| 4 | **调试与诊断** | 提供日志、性能计数器、设备信息查询接口，帮助定位性能瓶颈 |
| 5 | **插件化设计** | 运行时与驱动可单独编译，支持按需加载，便于集成到已有项目 |
| 6 | **MIT 许可证** | 开源许可证，方便商业使用与二次开发 |

## 快速入门

### 1. 环境准备
```bash
# 安装基本依赖（Ubuntu 示例）
sudo apt-get install build-essential cmake libopencl-dev

# 克隆仓库
git clone https://github.com/vosen/ZLUDA.git
cd ZLUDA
```

### 2. 编译

```bash
mkdir build && cd build
cmake ..
make -j$(nproc)
```

- 编译后可得到 `libzluDA.so`（运行时）与 `zluDriver.so`（驱动）等文件。

### 3. 运行时配置

```bash
# 将 ZLUDA 运行时加入搜索路径
export LD_LIBRARY_PATH=/path/to/ZLUDA/lib:$LD_LIBRARY_PATH

# 指定使用 ZLUDA 驱动
export ZLUDA_DRIVER=/path/to/ZLUDA/lib/zluDriver.so
```

### 4. 编译与运行 CUDA 示例

```bash
# 编译示例程序
nvcc -L/path/to/ZLUDA/lib -lzluDA -o example example.cu

# 运行
./example
```

> **提示**：如果你已经装有官方 CUDA Toolkit，只需在编译时使用 `-D ZLUDA_BACKEND=OpenCL` 或 `-D ZLUDA_BACKEND=LevelZero` 以切换后端。

## 示例代码

```cpp
#include <cuda_runtime.h>
#include <cstdio>

__global__ void kernel(int *d_out) {
    int tid = blockIdx.x * blockDim.x + threadIdx.x;
    d_out[tid] = tid;
}

int main() {
    const int N = 64;
    int *d_arr;
    cudaMalloc(&d_arr, N * sizeof(int));

    kernel<<<N/32, 32>>>(d_arr);
    cudaDeviceSynchronize();

    int h_arr[N];
    cudaMemcpy(h_arr, d_arr, N * sizeof(int), cudaMemcpyDeviceToHost);
    for (int i = 0; i < N; ++i) printf("%d ", h_arr[i]);

    cudaFree(d_arr);
    return 0;
}
```

> 以上程序可直接使用 ZLUDA 编译运行，无需 NVIDIA GPU 驱动即可得到正确结果。

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| 程序崩溃或报错 “CUDA error: unknown error” | 检查是否正确设置 `LD_LIBRARY_PATH` 与 `ZLUDA_DRIVER`，确保库路径无冲突 |
| 性能低于官方驱动 | 通过 `zluDaemon` 启动时指定 `-usecl=1` 或 `-lzi=1` 等参数，以开启 OpenCL 或 Level‑Zero 性能优化 |
| 支持的 CUDA 版本 | 当前支持 CUDA 10.x – 12.x，社区会不断扩展兼容范围 |

## 贡献与社区

- **拉取请求**：欢迎提交新特性、bug 修复或性能改进。
- **Issue**：报告问题或提出建议。
- **邮件列表 / Discord**：讨论与协作。

---

> 更多详细信息请参阅官方文档与 `README`，欢迎 Fork 与 Star  
> 
> 项目地址: <https://github.com/vosen/ZLUDA>
