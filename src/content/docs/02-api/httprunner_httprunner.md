
---
title: httprunner
---

# HttpRunner 项目

**项目地址**: [https://github.com/httprunner/httprunner](https://github.com/httprunner/httprunner)

## 主要特性
HttpRunner 是一个开源的 API 测试框架，支持 HTTP(S)、HTTP2 和 WebSocket 协议。它具有以下核心特性：
- **跨语言支持**：核心引擎基于 Python 实现，但提供多种客户端工具，包括 Python、JavaScript、Java、Go 和 cURL 等，支持多语言测试脚本编写。
- **数据驱动测试**：支持参数化测试，通过变量、函数和数据文件（如 CSV、JSON）实现高效的测试用例复用。
- **强大的验证机制**：内置丰富的断言函数，支持 JSON Schema 验证、正则表达式匹配等，确保测试结果的准确性。
- **自动化与 CI/CD 集成**：无缝集成 Jenkins、GitLab CI 等工具，支持并行测试执行，提高测试效率。
- **可视化报告**：生成 HTML 测试报告，支持 HAR 文件格式，便于调试和分析。
- **模块化设计**：测试用例采用 YAML/JSON 格式，便于维护和版本控制；支持自定义插件扩展功能。
- **调试友好**：提供命令行调试模式、日志记录和断点支持，简化问题排查。

## 主要功能
HttpRunner 的功能覆盖 API 测试的全生命周期，包括：
- **测试用例管理**：通过 YAML/JSON 文件定义测试场景，支持步骤化脚本编写（如请求、提取变量、验证响应）。
- **请求发送与模拟**：支持 GET、POST、PUT、DELETE 等 HTTP 方法，以及文件上传、多部分表单等高级功能；内置 Mock 服务器模拟后端响应。
- **性能测试**：集成 Locust 引擎，支持负载测试和压力测试，监控 TPS、响应时间等指标。
- **Web UI 测试**：结合 Selenium，支持浏览器自动化测试，实现端到端（E2E）测试。
- **测试套件执行**：命令行工具 hrun 可运行单个用例或整个测试套件，支持过滤和标签管理。
- **结果分析**：自动生成详细报告，包括通过/失败统计、响应详情和性能图表；支持与 Allure 等报告工具集成。
- **扩展性**：允许自定义函数、钩子（hooks）和第三方库集成，适用于微服务、移动 API 等复杂场景。

## 用法
### 安装
1. 使用 pip 安装核心包：
   ```
   pip install httprunner
   ```
2. 对于特定语言客户端（如 JavaScript），通过 npm 安装：
   ```
   npm install httprunner -g
   ```
3. 验证安装：
   ```
   hrun --version
   ```

### 基本用法
1. **创建测试用例**：在 YAML 文件中定义测试，例如 `test.yml`：
   ```yaml
   config:
     name: sample_api_test
     base_url: https://httpbin.org/

   test:
     - name: GET request
       request:
         method: GET
         url: /get
       validate:
         - eq: {status_code: 200}
   ```

2. **运行测试**：
   ```
   hrun test.yml
   ```
   - 支持参数：`hrun test.yml -v`（详细输出）、`hrun test.yml --html=report.html`（生成报告）。

3. **数据驱动**：使用 `variables` 提取响应数据，或通过 `${func()}` 调用函数动态生成参数。

4. **调试**：运行 `hrun test.yml -d` 进入调试模式，逐步执行步骤。

5. **高级用法**：
   - 性能测试：`hrun locustfile.py --host=https://example.com`。
   - 集成 CI：将 `hrun` 命令添加到脚本中，实现自动化执行。

更多细节请参考项目文档：https://httprunner.com/