---
title: Tarantool
---

## 项目简介

Tarantool 是一个内存计算平台，由数据库和应用服务器组成。它采用 BSD 2-Clause 许可证发布。

## 主要功能

### 应用服务器特性

- 高度优化的 Lua 解释器，基于 LuaJIT 2.1，具有快速跟踪 JIT 编译器。
- 协作多任务和非阻塞 IO。
- 支持持久队列、Sharding 和集群管理框架。
- 可访问外部数据库，如 MySQL 和 PostgreSQL。
- 丰富的内置和独立模块。

### 数据库特性

- 使用 MessagePack 数据格式和基于 MessagePack 的客户端-服务器协议。
- 两种数据引擎：100% 内存中存储，支持完整的 WAL 持久化；以及 LSM-tree 实现，适用于大数据集。
- 支持多种索引类型：HASH、TREE、RTREE、BITSET。
- 文档导向的 JSON 路径索引。
- 异步主主复制和同步基于仲裁的复制。
- 基于 RAFT 的自动领导者选举，用于单领导者配置。
- 认证和访问控制。
- 支持 ANSI SQL，包括视图、连接、引用约束和检查约束。
- 为多种编程语言提供连接器。
- 数据库是应用服务器的 C 扩展，可以关闭。

## 支持平台

- Linux (x86_64, aarch64)
- Mac OS X (x86_64, M1)
- FreeBSD (x86_64)

## 适用场景

Tarantool 非常适合可扩展 Web 架构的数据丰富组件，如队列服务器、缓存和有状态 Web 应用程序。

## 安装和使用

- 要下载和安装 Tarantool 的二进制包或使用 Docker，请访问 [下载页面](https://www.tarantool.io/en/download/)。
- 要从源码构建 Tarantool，请参考 [构建指南](https://www.tarantool.io/en/doc/latest/dev_guide/building_from_source/)。
- 有关模块、连接器和工具，请查看 [Awesome Tarantool](https://github.com/tarantool/awesome-tarantool/) 列表。

## 贡献和反馈

- 请在 [问题跟踪器](https://github.com/tarantool/tarantool/issues) 上报告错误。
- 欢迎在 [讨论页面](https://github.com/tarantool/tarantool/discussions) 提供反馈，并在 [Stack Overflow](https://stackoverflow.com/questions/tagged/tarantool) 上提问。
- 接受通过拉取请求的贡献，请查看 [贡献指南](https://github.com/tarantool/tarantool/blob/master/CONTRIBUTING.md)。
