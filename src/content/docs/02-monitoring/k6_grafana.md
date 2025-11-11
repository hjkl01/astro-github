---
title: k6
---

# k6

k6 是一个现代化的负载测试工具，由 Grafana 开发，使用 Go 和 JavaScript 构建。它旨在为开发者和测试者在 DevOps 时代提供强大的负载测试体验。

## 功能特性

- **可配置的负载生成**：即使在低端机器上也能模拟大量流量。
- **测试即代码**：支持脚本重用、逻辑模块化、版本控制，并与 CI/CD 集成。
- **全功能 API**：提供丰富的脚本 API，帮助模拟真实应用流量。
- **嵌入式 JavaScript 引擎**：结合 Go 的性能和 JavaScript 的脚本熟悉度。
- **多协议支持**：支持 HTTP、WebSockets、gRPC、Browser 等协议。
- **扩展生态系统**：可扩展以支持自定义需求，社区已分享大量扩展。
- **灵活的指标存储和可视化**：提供汇总统计或粒度指标，可导出到各种服务。
- **与 Grafana Cloud 集成**：原生支持 SaaS 解决方案，用于测试执行、指标关联和数据分析。

## 安装

从 [GitHub Releases](https://github.com/grafana/k6/releases) 下载最新版本的 k6 二进制文件。根据您的操作系统选择合适的版本。

例如，在 Linux 上：

```bash
wget https://github.com/grafana/k6/releases/download/v1.3.0/k6-v1.3.0-linux-amd64.tar.gz
tar -xzf k6-v1.3.0-linux-amd64.tar.gz
sudo mv k6-v1.3.0-linux-amd64/k6 /usr/local/bin/
```

## 用法

k6 使用 JavaScript 编写测试脚本。以下是一个简单的示例脚本，用于测试 HTTP 请求：

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

// 测试配置
export const options = {
  thresholds: {
    // 断言 99% 的请求在 3000ms 内完成
    http_req_duration: ['p(99) < 3000'],
  },
  // 逐步增加和减少虚拟用户数量
  stages: [
    { duration: '30s', target: 15 },
    { duration: '1m', target: 15 },
    { duration: '20s', target: 0 },
  ],
};

// 模拟用户行为
export default function () {
  let res = http.get('https://quickpizza.grafana.com');
  // 验证响应状态
  check(res, { 'status was 200': (r) => r.status == 200 });
  sleep(1);
}
```

运行脚本：

```bash
k6 run script.js
```

更多用法和配置，请参考 [官方文档](https://grafana.com/docs/k6/latest/)。

## 注意事项

- k6 支持多种场景，如开放模型、封闭模型、恒定 RPS 等。
- 可以设置阈值来定义测试目标和 SLO。
- 支持多种输出格式，包括 JSON、CSV 等。
- 对于不需要编写代码的用户，可以使用 [k6 Studio](https://github.com/grafana/k6-studio) 桌面应用生成脚本。
