---
title: diving
---

# diving

**注意：此仓库已归档，请改用 [diving-rs](https://github.com/vicanso/diving-rs) 代替。它更快、更简单，使用 Rust 开发。**

## 项目地址

[https://github.com/vicanso/diving](https://github.com/vicanso/diving)

## 项目简介

使用 diving 可以在网站上分析 Docker 镜像。它使用 [dive](https://github.com/wagoodman/dive) 来获取分析信息。

第一次可能很慢，因为它首先拉取镜像。

## 安装

```
docker run -d --restart=always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -p 7001:7001 \
  vicanso/diving
```
