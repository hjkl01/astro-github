---
title: grpcurl
---



---
title: grpcurl
---

项目地址: [https://github.com/fullstorydev/grpcurl](https://github.com/fullstorydev/grpcurl)

该项目是 `grpcurl`，一个用于与 gRPC 服务器交互的命令行工具。它的主要特性和功能包括：

1. **简单的 gRPC 调用**：可以方便地通过命令行调用 gRPC 方法，而无需写代码。
2. **支持反射**：可以自动获取服务定义和方法信息，支持通过 gRPC 反射与服务器交互。
3. **JSON 输入输出**：支持将请求和响应以 JSON 格式进行编码和解码，便于调试和测试。
4. **支持多种认证方式**：可以通过 TLS、JWT 等多种身份验证机制与 gRPC 服务进行安全通信。

用法示例：
- 通过命令行调用 gRPC 方法，示例：
  ```
  grpcurl -plaintext localhost:50051 ServiceName.MethodName
  ```

该工具非常适合开发人员在调试和测试 gRPC 服务时使用。