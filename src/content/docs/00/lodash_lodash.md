
---
title: lodash
---


# Lodash

**项目地址**: https://github.com/lodash/lodash

## 概述
Lodash 是一个现代的 JavaScript 工具库，提供大量实用函数，帮助在数据处理、函数式编程、性能优化等方面写出更简洁、更高效的代码。

## 主要特性
- **函数式工具**：深拷贝、节流/防抖、柯里化、偏函数、组合函数等。
- **数组与集合操作**：`chunk`, `compact`, `difference`, `flatten`, `uniq`, `zip`, `unzip` 等。
- **对象与映射**：`assign`, `clone`, `merge`, `pick`, `omit`, `values`, `keys` 等。
- **字符串处理**：`camelCase`, `kebabCase`, `snakeCase`, `capitalize`, `trim`, `pad` 等。
- **数学与随机**：`random`, `clamp`, `mean`, `sum`, `maxBy`, `minBy` 等。
- **性能优化**：`throttle`, `debounce`, `memoize`, `once`, `after` 等。
- **通用工具**：`identity`, `noop`, `constant`, `tap`, `isEqual`, `isEmpty` 等。

## 常用功能示例

```js
const _ = require('lodash');

// 节流
const throttled = _.throttle(() => console.log('tick'), 1000);

// 组合函数
const add = (a, b) => a + b;
const double = x => x * 2;
const addThenDouble = _.flow(add, double);
console.log(addThenDouble(1, 2)); // 6

// 深拷贝
const obj = { a: 1, b: { c: 2 } };
const copy = _.cloneDeep(obj);
copy.b.c = 3;
console.log(obj.b.c); // 2

// 数组去重
const arr = [1, 2, 2, 3];
console.log(_.uniq(arr)); // [1,2,3]

// 对象合并
const a = { foo: 'bar' };
const b = { baz: 'qux' };
console.log(_.merge(a, b)); // { foo: 'bar', baz: 'qux' }
```

## 安装

```bash
npm install lodash
# 或者
yarn add lodash
```

## 使用

- CommonJS: `const _ = require('lodash');`
- ES模块: `import _ from 'lodash';`
- 按需引入（推荐）:

```js
import map from 'lodash/map';
import filter from 'lodash/filter';
```

## 结语
Lodash 通过提供高质量、可组合的工具函数，让 JavaScript 开发更高效、更易维护。无论是前端还是后端项目，都能从中受益。

