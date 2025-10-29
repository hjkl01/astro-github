
---
title: walker
---

# Walker

**项目地址**: https://github.com/abenz1267/walker

---

## 简介
Walker 是一个轻量级的 Node.js 文件系统遍历工具，提供同步与异步两种 API，并可直接通过命令行使用。它能够递归扫描目录，获取文件的详细信息，并支持多种过滤条件与自定义回调。

## 主要特性
- **递归遍历**：一次调用即可遍历整个目录树。
- **多种过滤**：按文件名、扩展名、大小、时间等进行筛选。
- **同步 & 异步**：满足不同使用场景的需求。
- **事件回调**：在遍历过程中可以自定义回调函数处理每个文件或目录。
- **命令行工具**：`walker` 命令可快速生成文件列表或做批处理。

## 功能
| 功能 | 描述 |
|------|------|
| `list` | 返回包含文件路径、大小、修改时间等信息的数组。 |
| `each` | 对每个文件/目录执行回调函数。 |
| `filter` | 配置过滤器（如 `ext`, `minSize`, `maxSize`, `mtimeAfter` 等）。 |
| `ignore` | 忽略指定的文件或目录。 |
| `depth` | 限制递归深度。 |
| `stats` | 获取文件系统的统计信息。 |

## 用法

### 1. 作为 Node.js 库

```bash
npm install walker
```

```js
const walker = require('walker');

// 同步遍历
const files = walker('/path/to/dir', { sync: true, ext: '.js' });
console.log(files);

// 异步遍历
walker('/path/to/dir', { ext: '.json' })
  .then(files => console.log(files))
  .catch(err => console.error(err));

// 使用回调处理每个文件
walker.each('/path/to/dir', file => {
  console.log(file.path, file.size);
});
```

### 2. 作为命令行工具

```bash
# 安装全局
npm install -g walker

# 查看帮助
walker --help

# 生成文件列表
walker /path/to/dir --ext .md --depth 3 > files.txt

# 过滤并执行命令
walker /path/to/dir --ext .txt | xargs -I{} sh -c 'echo {} > {}.txt'
```

## 贡献与支持
- **Issues**：在 GitHub 上提交 bug 或功能请求。
- **Pull Requests**：欢迎贡献代码，遵循项目的代码规范。

---

> 以上信息基于项目 README 与源码的公开内容，具体使用细节请参考官方文档与示例。