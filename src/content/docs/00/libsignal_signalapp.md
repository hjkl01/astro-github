
---
title: libsignal
---


# LibSignal (signalapp/libsignal)

**项目地址**:  
<https://github.com/signalapp/libsignal>

## 主要特性
- **端到端加密**：实现 Signal 协议中的完整加密链路，支持身份验证、消息加密/解密以及完整性验证。  
- **会话管理**：维护会话状态，支持会话建立、升级、丢失恢复。  
- **异步消息**：使用 RxJava/Rx Kotlin 进行异步操作与事件流处理。  
- **跨平台**：Java 语言实现，可在 Android、Desktop 或其他 JVM 环境下使用。  
- **模块化设计**：核心库分离 Credential、Group、Message 等子模块，便于单独引入。  

## 功能概览
| 功能 | 说明 |
|------|------|
| 加密/解密 | 对单播、群组、组渠道的消息进行加密与解密。 |
| 认证 | 对消息来源进行身份验证，防止伪造。 |
| 可靠交付 | 支持传输层的 ACK、重传逻辑（在上层实现）。 |
| 记录/搜索 | 在本地持久化加密消息，支持查询接口。 |
| 组管理 | 组成员增删、成员身份验证、分组密钥更新。 |
| 点对点与群组 | 支持 1:1、1:N 和多组协作。 |

## 用法示例

```java
// 添加依赖
implementation "com.github.signalapp.libsignal:libsignal-android:1.0.6" // 版本请以实际为准

// 初始化会话
SignalProtocolStore store = new InMemorySignalProtocolStore();
SessionBuilder builder = new SessionBuilder(store, recipientAddress);

// 发送消息
MessageCipher cipher = new SessionCipher(store, recipientAddress);
CiphertextMessage ciphertext = cipher.encrypt(messageBytes);
byte[] encrypted = ciphertext.getCiphertext();

// 接收消息
SessionCipher decoder = new SessionCipher(store, senderAddress);
PlaintextMessage plaintext = decoder.decrypt(ciphertext);
byte[] original = plaintext.getData();
```

> 以上仅为核心流程示例，完整实现需结合网络层、存储层和错误处理。

---  
此文件仅包含项目概要，详细 API 与使用细节请参阅官方文档与源代码。