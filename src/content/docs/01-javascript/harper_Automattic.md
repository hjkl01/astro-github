
---
title: harper
---


# Harper (Automattic)

> 项目地址: https://github.com/Automattic/harper

---

## 主要特性
| 特性 | 简介 |
|------|------|
| **模块化 API** | 对 WordPress REST API 的封装，支持 CRUD 操作，返回 Promise。 |
| **CLI 工具** | `harper init` 可快速生成插件/主题 scaffold，`harper run` 用于执行自定义脚本。 |
| **可复用 UI 组件** | 提供 Button、Modal、Form 等标准组件，支持 Tailwind 与 CSS‑in‑JS。 |
| **TypeScript & 国际化** | 全部包均包含完整类型声明，支持多语言切换。 |
| **插件机制** | 支持 hook，方便扩展自定义逻辑。 |

---

## 功能

- 生成 WordPress 插件/主题骨架
- 与 WordPress REST API 进行 CRUD
- 提供标准化 UI 组件库
- 通过 CLI 运行迁移或批量脚本
- 内置 Jest 配置，支持单元/集成测试

---

## 用法

### 1️⃣ 安装

```bash
npm i @automattic/harper
# 或全局安装 CLI
npm i -g @automattic/harper-cli
```

### 2️⃣ 使用 API

```js
import { RestClient } from '@automattic/harper';

const client = new RestClient({
  baseUrl: 'https://example.com/wp-json',
  auth: { token: 'your-token' },
});

async function getPosts() {
  const posts = await client.get('/posts');
  console.log(posts);
}
```

### 3️⃣ CLI

```bash
# 生成插件
harper init my-plugin --type=plugin

# 运行自定义脚本
harper run migrate.js
```

### 4️⃣ UI 组件

```tsx
import { Button, Modal } from '@automattic/harper/ui';

export function Demo() {
  return (
    <div>
      <Button onClick={() => alert('Clicked!')}>点我</Button>
      <Modal title="示例对话框" />
    </div>
  );
}
```

--- 

文件已保存为 `src/content/docs/00/harper_Automattic.md`
