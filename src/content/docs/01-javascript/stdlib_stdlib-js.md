---
title: stdlib
---


# stdlib（stdlib-js/stdlib）

> 项目地址: <https://github.com/stdlib-js/stdlib>

stdlib 是一个专注于 JavaScript 与 Node.js 的标准库实现，提供了丰富的实用工具函数、数值计算库、数据结构、算法、数学函数等，旨在让开发者在编写高质量、可维护、可复用代码时不必重复造轮子。

## 主要特性

| 领域 | 说明 |
|------|------|
| **数学与数值计算** | 100+ 函数，支持线性代数、矩阵运算、随机数生成、统计分布、数值积分、ODE 求解等。 |
| **数据结构** | 基于数组、链表、栈、队列、哈希表、树、图等实现。 |
| **字符串与文本处理** | 正则、编码、分词、编辑距离、正则表达式工具。 |
| **文件与 I/O** | 文件读写、流处理、压缩、解压、路径解析等。 |
| **网络** | HTTP/HTTPS 客户端、WebSocket、TCP/UDP、DNS 等。 |
| **时间与日期** | 时区处理、时间戳、日期格式化、周期计算。 |
| **工具函数** | 组合函数、懒加载、节流/防抖、深拷贝、对象合并、随机数生成、类型检查等。 |
| **CLI 工具** | 命令行解析、进度条、颜色输出、提示框。 |
| **测试与调试** | 断言、Mock、覆盖率、调试工具。 |

## 核心功能

- **模块化**：每个功能都作为独立模块发布，支持 ES6/CommonJS。
- **性能优化**：使用 C/C++ 扩展、WebAssembly、并行化等技术提升性能。
- **跨平台**：兼容 Node.js、Babel、WebPack、Rollup、Deno 等多种环境。
- **类型安全**：提供 TypeScript 类型定义，支持严格类型检查。
- **文档完备**：详细 API 文档、示例代码、FAQ 与最佳实践。
- **社区维护**：活跃的维护团队与社区，持续发布新功能与 bug 修复。

## 用法

### 1. 安装

```bash
# npm
npm install @stdlib/stdlib

# yarn
yarn add @stdlib/stdlib

# pnpm
pnpm add @stdlib/stdlib
```

### 2. 基本导入

```js
// CommonJS
const stdlib = require('@stdlib/stdlib');

// ES6
import * as stdlib from '@stdlib/stdlib';
```

### 3. 常用示例

#### 数学运算

```js
const { add, sqrt } = stdlib.math;

// 计算平方根
const val = sqrt(16);   // 4

// 加法
const sum = add(5, 3);  // 8
```

#### 随机数生成

```js
const { randu } = stdlib.stats.rand;

// 生成 0~1 之间的随机数
const random = randu(); // 0.12345678...
```

#### 数据结构 - 队列

```js
const { Queue } = stdlib.ds;

// 创建队列
const q = new Queue();
q.enqueue(1);
q.enqueue(2);
q.dequeue(); // 1
```

#### 文件 I/O

```js
const { readFile, writeFile } = stdlib.io;

const content = await readFile('example.txt', 'utf8');
await writeFile('output.txt', content.toUpperCase());
```

#### CLI 工具

```js
const { ArgParser } = stdlib.cli;

const parser = new ArgParser({
  args: process.argv.slice(2),
  options: {
    help: { type: 'boolean', alias: 'h' }
  }
});

if (parser.getOption('help')) {
  console.log(parser.getHelp());
}
```

### 4. TypeScript 使用

```ts
import { add } from '@stdlib/stdlib/math';

const result: number = add(2, 3); // 5
```

### 5. 文档与资源

- 官方网站与文档: <https://stdlib.rocks/>
- API 参考: <https://stdlib.rocks/api>
- 示例代码仓库: <https://github.com/stdlib-js/docs>
- 社区讨论: <https://github.com/stdlib-js/stdlib/discussions>

---
> **提示**：所有模块均可单独安装，例如 `npm install @stdlib/math`，这在构建轻量化项目时非常有用。
