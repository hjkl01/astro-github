---
title: lingo.dev
---

# lingo.dev

## 功能

Lingo.dev 是一个开源的 AI 驱动的 i18n 工具包，用于使用大型语言模型 (LLM) 进行即时本地化。它提供了多种工具来帮助开发者轻松实现多语言支持：

- **Compiler**: 构建时 React 本地化，无需修改现有 React 组件。
- **CLI**: 从终端翻译代码和内容，支持指纹识别和缓存，仅重新翻译变更部分。
- **CI/CD**: 自动提交翻译，支持 GitHub Actions 集成。
- **SDK**: 实时翻译动态内容，如用户生成的内容。

支持多种格式：JSON、YAML、Markdown 等。可以使用自己的 LLM 或 Lingo.dev 本地化引擎。

## 用法

### Compiler

安装：

```bash
npm install lingo.dev
```

在 Next.js 配置中启用：

```javascript
import lingoCompiler from 'lingo.dev/compiler';

const existingNextConfig = {};

export default lingoCompiler.next({
  sourceLocale: 'en',
  targetLocales: ['es', 'fr'],
})(existingNextConfig);
```

运行构建：

```bash
next build
```

### CLI

运行翻译：

```bash
npx lingo.dev@latest run
```

### CI/CD

在 `.github/workflows/i18n.yml` 中配置：

```yaml
name: Lingo.dev i18n
on: [push]

jobs:
  i18n:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: lingodotdev/lingo.dev@main
        with:
          api-key: ${{ secrets.LINGODOTDEV_API_KEY }}
```

### SDK

```javascript
import { LingoDotDevEngine } from 'lingo.dev/sdk';

const lingoDotDev = new LingoDotDevEngine({
  apiKey: 'your-api-key-here',
});

const content = {
  greeting: 'Hello',
  farewell: 'Goodbye',
  message: 'Welcome to our platform',
};

const translated = await lingoDotDev.localizeObject(content, {
  sourceLocale: 'en',
  targetLocale: 'es',
});
// 返回: { greeting: "Hola", farewell: "Adiós", message: "Bienvenido a nuestra plataforma" }
```

更多详情请参考 [官方文档](https://lingo.dev)。
