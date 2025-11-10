---
title: verifiers
---

# verifiers

https://github.com/PrimeIntellect-ai/verifiers

## 主要特性

- **类型安全**：基于 TypeScript 的强类型验证，支持对象、数组、字符串、数字、布尔等基本类型。  
- **可扩展自定义验证器**：提供 `addValidator` 接口，可注册任意自定义验证逻辑。  
- **异步验证支持**：支持返回 Promise 的验证函数，适用于数据库或网络校验。  
- **错误报告**：统一错误结构，包含 `path`、`message`、`value`，便于前端展示或日志记录。  
- **轻量级**：依赖仅 `tslib`，体积约 10 KB，适合前后端共享验证逻辑。

## 核心 API

| 函数 | 说明 | 示例 |
|------|------|------|
| `verifyObject(schema, data)` | 根据 schema 验证对象 | `verifyObject(userSchema, userData)` |
| `verifyArray(itemValidator, data)` | 验证数组每项 | `verifyArray(verifyString, ['a','b'])` |
| `addValidator(name, fn)` | 注册自定义验证器 | `addValidator('isEmail', val => /\S+@\S+\.\S+/.test(val))` |

## 安装

```bash
npm install verifiers
# 或
yarn add verifiers
```

## 使用示例

```ts
import { verifyObject, addValidator } from 'verifiers';

const userSchema = {
  id:  verifyNumber,
  name: verifyString,
  email: (v) => addValidator('isEmail', (val) => /\S+@\S+\.\S+/.test(val))(v),
};

const user = { id: 1, name: 'Alice', email: 'alice@example.com' };

try {
  verifyObject(userSchema, user);
  console.log('验证通过');
} catch (err) {
  console.error('验证失败', err);
}
```

## 贡献

- Fork → `git clone`  
- `npm install && npm run build`  
- 提交 PR

## 许可证

MIT © PrimeIntellect AI