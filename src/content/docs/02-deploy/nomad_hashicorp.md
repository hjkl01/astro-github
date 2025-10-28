
---
title: nomad
---

# HashiCorp Nomad 项目

## 项目地址
[https://github.com/hashicorp/nomad](https://github.com/hashicorp/nomad)

## 主要特性
Nomad 是 HashiCorp 公司开发的开源工作负载调度器和编排工具，主要用于管理容器化、非容器化应用以及其他工作负载。它具有以下核心特性：
- **多数据中心支持**：Nomad 可以跨多个数据中心运行，支持联邦部署，实现高可用性和全球分布式调度。
- **多运行时兼容**：支持多种运行时环境，包括 Docker、Java、Python 等容器和非容器应用，以及批处理作业和系统服务。
- **简单的架构**：采用单二进制文件设计，易于部署和扩展。Nomad 集群由服务器节点（负责调度）和客户端节点（执行任务）组成。
- **高性能调度**：内置高效的调度算法，支持 bin-packing 和 spread 策略，能处理大规模作业（数千节点）。
- **服务发现与监控集成**：无缝集成 Consul（服务发现）和 Vault（秘密管理），并支持 Prometheus 等监控工具。
- **灵活的任务类型**：支持服务（长期运行）、批处理（短期任务）和系统作业（守护进程）。
- **插件系统**：通过插件扩展功能，如设备插件（GPU、FPGA）和网络插件（CNI）。

## 主要功能
Nomad 的功能聚焦于工作负载的生命周期管理，包括：
- **作业调度**：根据资源需求自动分配任务到合适的节点，支持约束（如亲和性、反亲和性）和优先级。
- **资源管理**：动态分配 CPU、内存、磁盘和网络资源，支持隔离和配额控制。
- **健康检查与自动恢复**：内置健康检查机制，任务失败时自动重启或迁移。
- **CLI 和 API 接口**：提供强大的命令行工具（nomad CLI）和 RESTful API，便于自动化和集成。
- **安全性**：支持 ACL（访问控制列表）、TLS 加密和集成 Vault 进行动态凭证管理。
- **模板和 HCL 配置**：使用 HashiCorp 配置语言 (HCL) 定义作业规格，支持变量插值和模板化配置。

## 用法
Nomad 的用法主要通过 CLI 命令和 HCL 作业文件进行操作。以下是基本步骤：

1. **安装和启动集群**：
   - 下载 Nomad 二进制文件并配置服务器节点（`nomad agent -server -bootstrap-expect=1`）和客户端节点（`nomad agent -client`）。
   - 编辑配置文件 `nomad.hcl` 指定数据目录、绑定地址等。

2. **定义作业**：
   - 创建 HCL 文件（如 `example.nomad`）描述任务，例如一个简单的 Web 服务：
     ```
     job "example" {
       datacenters = ["dc1"]
       type = "service"

       group "web" {
         count = 1

         task "server" {
           driver = "docker"
           config {
             image = "nginx:1.14"
             ports = ["http"]
           }

           resources {
             cpu    = 500
             memory = 256
           }

           service {
             name = "web"
             port = "http"
             tags = ["nginx"]
           }
         }
       }
     }
     ```

3. **运行和监控作业**：
   - 提交作业：`nomad job run example.nomad`。
   - 查看状态：`nomad job status example` 或 `nomad ui`（Web 界面）。
   - 停止作业：`nomad job stop example`。
   - 扩展：`nomad job plan example`（预览变化）后 `nomad job run -check-index <index> example`。

4. **高级用法**：
   - 集成 Consul：使用 `consul` 驱动自动注册服务。
   - 批处理：定义 `type = "batch"` 的作业用于一次性任务。
   - API 调用：通过 HTTP API（如 `POST /v1/job/run`）提交作业，支持 CI/CD 管道集成。

更多细节请参考官方文档：https://developer.hashicorp.com/nomad/docs