
---
title: vcrpy
---

# vcrpy 项目概述

## 项目地址
[https://github.com/kevin1024/vcrpy](https://github.com/kevin1024/vcrpy)

## 主要特性
vcrpy 是一个 Python 库，用于记录和重放 HTTP 交互，主要针对测试场景。它通过模拟 HTTP 请求和响应，避免了实际的网络调用，从而加速测试并确保测试的确定性和可重复性。主要特性包括：
- **记录与重放**：自动记录真实的 HTTP 请求和响应，并将其保存为 YAML 或 JSON 文件，在后续测试中重放这些记录，而无需真实网络交互。
- **支持多种 HTTP 库**：兼容 requests、urllib3、httplib 等流行 Python HTTP 客户端。
- **匹配机制**：基于 URI、方法、头部、查询参数和请求体等进行精确匹配，支持自定义匹配器。
- **过滤敏感数据**：允许过滤掉敏感信息（如 API 密钥、令牌），保护隐私。
- **Cassette 管理**：使用“磁带”（cassette）概念组织记录的文件，支持路径匹配和持久化。
- **集成测试框架**：易于与 pytest、unittest 等测试框架集成。
- **轻量级**：无外部依赖，纯 Python 实现。

## 主要功能
- **HTTP 交互模拟**：在测试环境中替换真实 API 调用，使用预录制的响应。
- **测试隔离**：确保测试不受外部服务（如网络延迟或 API 变更）影响。
- **调试支持**：提供详细的日志和记录查看，便于调试 HTTP 交互。
- **自定义扩展**：支持钩子（hooks）来修改请求/响应，或实现自定义序列化。

## 用法
### 安装
```bash
pip install vcrpy
```

### 基本用法
1. **装饰器方式**（推荐用于测试函数）：
   ```python
   import vcr
   import requests

   my_vcr = vcr.VCR(cassette_library_dir='fixtures/')  # 指定记录文件目录

   @my_vcr.use_cassette('example.yaml')  # 指定磁带文件
   def test_api_call():
       response = requests.get('http://httpbin.org/get')
       assert response.status_code == 200
   ```
   - 首次运行时，vcrpy 会记录请求并保存到 `fixtures/example.yaml`。
   - 后续运行会重放记录的响应。

2. **上下文管理器方式**：
   ```python
   import vcr
   import requests

   with vcr.use_cassette('example.yaml'):
       response = requests.get('http://httpbin.org/get')
       # 测试逻辑
   ```

3. **高级配置**：
   - **记录模式**：`record_mode='once'`（仅首次记录，后续重放）、`'new_episodes'`（记录新交互）、`'all'`（总是记录）或 `'none'`（仅重放）。
     ```python
     my_vcr = vcr.VCR(record_mode='once', cassette_library_dir='fixtures/')
     ```
   - **过滤**：隐藏敏感头部或 body。
     ```python
     my_vcr = vcr.VCR(filter_headers=[('authorization', 'DUMMY')])
     ```
   - **匹配器**：自定义 URI 匹配。
     ```python
     my_vcr = vcr.VCR(match_on=['method', 'scheme', 'host', 'port', 'path', 'query', 'headers', 'body'])
     ```

### 示例集成 pytest
在 `conftest.py` 中：
```python
import vcr
import pytest

@pytest.fixture
def vcr_cassette(request):
    with vcr.use_cassette('fixtures/{}.yaml'.format(request.node.name)):
        yield
```

更多细节请参考项目文档。