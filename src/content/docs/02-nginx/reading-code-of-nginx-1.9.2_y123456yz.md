---
title: reading-code-of-nginx-1.9.2
---

# Nginx 1.9.2 源码阅读笔记项目

**项目地址：** [https://github.com/y123456yz/reading-code-of-nginx-1.9.2](https://github.com/y123456yz/reading-code-of-nginx-1.9.2)

## 主要特性

- Detailed analysis of Nginx 1.9.2 source code with extensive Chinese comments and function call flow annotations.
- Most comprehensive nginx source code reading analysis Chinese comments, updated.
- Covers high concurrency design, excellent ideas applied to other high concurrency proxy middleware.

## 主要功能

- Code reading notes with detailed function analysis, related function flow calls.
- Analysis of nginx startup, exit, connection pool, memory pool, event-driven, async I/O, HTTP framework, request processing, reverse proxy, load balancing, rate limiting, WAF, etc.
- Application of nginx multi-process high concurrency low latency high reliability mechanism to cache proxy middleware like twemproxy.
- Reading process: config compilation, user modules, processes, data structures, connection processing, request stages, compression, hash tables, logs, reverse proxy, load balancing, etc.

## 用法

1. Clone repo: `git clone https://github.com/y123456yz/reading-code-of-nginx-1.9.2.git`
2. Read notes: Browse markdown files, learn from basic to advanced modules.
3. With source: Download nginx 1.9.2 source, debug against notes.
4. Contribute: Fork, edit, PR.
5. Setup: Git, markdown viewer, Linux with nginx compile.
