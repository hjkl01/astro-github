---
title: lighthouse
---

# Lighthouse（Google Chrome 性能审计工具）

GitHub项目地址: https://github.com/GoogleChrome/lighthouse

## 主要特性

- **性能评估**：测量页面加载速度、首屏渲染时间、交互延迟等关键指标。  
- **可访问性检测**：检查页面是否符合 WCAG、ARIA 等可访问性规范。  
- **最佳实践**：评估 HTTPS、HTTP/2、缓存策略等现代 Web 开发最佳做法。  
- **SEO 分析**：检测搜索引擎优化相关要素，如标题标签、元信息、结构化数据等。  
- **Progressive Web App（PWA）**：验证应用是否满足 PWA 要求（Service Worker、离线支持、HTTPS 等）。  
- **可定制报告**：支持多种输出格式（HTML、JSON、CSV、CLI）与自定义规则。  
- **CLI 与 API**：可通过命令行、Node API、Chrome DevTools Protocol 进行自动化测试。  
- **持续集成支持**：可与 CI/CD 流水线（GitHub Actions、GitLab CI、Jenkins 等）无缝集成。  

## 功能概览

| 功能 | 说明 |
|------|------|
| **生成 Lighthouse 报告** | 基于页面 URL 或本地文件生成完整审计报告。 |
| **离线模式** | 通过 `--offline-mode` 仅使用本地缓存进行测试，适用于网络受限环境。 |
| **模拟网络与设备** | `--throttling-method`、`--throttling.cpuSlowdownMultiplier` 等参数可模拟不同网络与 CPU 条件。 |
| **自定义审计** | 通过 `--config-path` 指定自定义 Lighthouse 配置，添加/删除审计项。 |
| **多标签页支持** | 使用 `--chrome-flags` 或 `--chrome-executable` 启动无头 Chrome。 |
| **报告导出** | `--output` 支持 `html`、`json`、`csv`、`json-summary` 等格式。 |

## 用法

### 1. 安装

```bash
# 通过 npm 安装
npm install -g lighthouse

# 或使用 npx 直接运行
npx lighthouse https://example.com
```

### 2. 基本命令

```bash
# 生成默认 HTML 报告
lighthouse https://example.com

# 仅输出 JSON
lighthouse https://example.com --output json --output-path ./report.json

# 在本地文件上运行（支持 Webpack，Parcel 等本地服务器）
lighthouse http://localhost:3000
```

### 3. 高级用法

```bash
# 模拟 3G 网络 + 2x CPU 降速
lighthouse https://example.com \
  --throttling-method provided \
  --throttling.cpuSlowdownMultiplier=2 \
  --throttling.requestLatency=400 \
  --throttling.downloadThroughput=750000 \
  --throttling.uploadThroughput=75000

# 使用自定义配置文件（JSON）
lighthouse https://example.com --config-path ./my-config.json

# 仅运行性能审计
lighthouse https://example.com --only-categories=performance

# 生成多格式报告
lighthouse https://example.com --output html,json --output-path ./report

# 通过 Node API 调用
const lighthouse = require('lighthouse');
const chromeLauncher = require('chrome-launcher');
const opts = { output: 'json' };

(async () => {
  const chrome = await chromeLauncher.launch({chromeFlags: ['--headless']});
  const result = await lighthouse('https://example.com', {...opts, port: chrome.port});
  console.log(result.lhr.categories.performance.score);
  await chrome.kill();
})();
```

### 4. 与 CI/CD 集成

**GitHub Actions 示例**

```yaml
name: Lighthouse CI
on:
  push:
    branches: [ main ]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install Chrome
        uses: chrome-actions/setup-chrome@v1
      - name: Run Lighthouse
        run: |
          npm i -g lighthouse
          lighthouse https://example.com --output json --output-path ./report.json
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: lighthouse-report
          path: report.json
```

## 贡献与维护

- 代码托管在 GitHub，采用 MIT 许可证。  
- 可通过 Pull Request 贡献功能改进或 bug 修复。  
- 文档与配置示例可在 `docs/` 与 `lighthouse-core/config` 目录中查阅。  

---
> **Tip**：使用 `lighthouse-ci`（https://github.com/GoogleChrome/lighthouse-ci）可实现持续性能监控与基准对比，建议结合实际项目使用。