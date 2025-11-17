---
title: email-verification-protocol
---

# Email Verification Protocol

Email Verification Protocol 是一个用于验证电子邮件地址的协议，它允许网站获取经过验证的电子邮件地址，而无需发送验证电子邮件或要求用户离开当前页面。该协议通过浏览器中介，使用 SD-JWT+KB 令牌来实现隐私保护。

## 功能

- **无需发送电子邮件**：传统验证方法需要发送链接或验证码，用户需要切换到邮件应用并等待邮件到达，这会导致用户流失。Email Verification Protocol 通过浏览器直接与邮件域的授权发行者交互，避免了这一问题。
- **隐私保护**：协议使用 SD-JWT+KB 令牌，浏览器作为中介，确保发行者不知道用户正在验证电子邮件的具体网站。同时，邮件域不会知道用户正在使用哪些应用。
- **无缝用户体验**：用户只需在表单中选择或输入电子邮件地址，浏览器会自动处理验证过程，无需额外步骤。
- **DNS 委托**：邮件域通过 DNS TXT 记录委托验证权限给发行者，确保只有授权实体可以验证该域的电子邮件。

## 用法

### 网站集成

网站需要在 HTML 表单中使用特定的属性和事件监听器：

```html
<input
  id="email"
  type="email"
  autocomplete="email"
  nonce="12345677890..random"
/>
<script>
  const input = document.getElementById('email');

  input.addEventListener('emailverified', (e) => {
    // e.presentationToken 是 SD-JWT+KB
    console.log({
      presentationToken: e.presentationToken,
    });
  });
</script>
```

### 处理步骤

1. **电子邮件请求**：网站生成 nonce 并绑定到会话，返回包含 nonce 的页面。
2. **电子邮件选择**：用户聚焦输入字段，浏览器显示可用的电子邮件列表，用户选择一个。
3. **令牌请求**：浏览器解析邮件域，查找 DNS TXT 记录，获取发行者信息，然后向发行者请求令牌。
4. **令牌发行**：发行者验证用户身份和邮件控制权，生成 SD-JWT 返回给浏览器。
5. **令牌呈现**：浏览器验证 SD-JWT，创建 SD-JWT+KB，并通过事件提供给网站。
6. **令牌验证**：网站服务器验证 SD-JWT+KB，确保电子邮件已验证。

### DNS 配置

邮件域需要添加 TXT 记录来委托验证：

```
_email-verification.email-domain.example   TXT   iss=issuer.example
```

### 发行者配置

发行者需要在 `.well-known/email-verification` 提供元数据：

```json
{
  "issuance_endpoint": "https://accounts.issuer.example/email-verification/issuance",
  "jwks_uri": "https://accounts.issuer.example/email-verification/jwks",
  "signing_alg_values_supported": ["EdDSA", "RS256"]
}
```

该协议适用于需要验证电子邮件地址的任何网站，如注册、登录或账户恢复场景。
