
---
title: tree-sitter
---

# Tree-sitter

**项目地址**: https://github.com/tree-sitter/tree-sitter  

## 主要特性

- **增量解析**：支持增量更新，修改代码后只重新解析受影响区域，性能高效。  
- **跨语言**：内置对多种编程语言的语法树生成支持，并可自定义新语言。  
- **低内存占用**：语法树采用结构化数据存储，内存占用低。  
- **可编程查询**：配合 Tree-sitter Query Language（TSQuery）可对语法树执行模式匹配。  

## 功能

- 语法树构建：把源代码解析为抽象语法树（AST）。  
- 语法高亮、代码补全、信息检索等编辑器插件底层。  
- 结构化代码分析工具（静态检查、格式化、重构等）。  
- 与编辑器、IDE 或其他工具的无缝集成。  

## 用法示例

```bash
# 安装（Node.js 版）
npm install tree-sitter
```

```js
const Parser = require('tree-sitter');
const JavaScript = require('tree-sitter-javascript');

const parser = new Parser();
parser.setLanguage(JavaScript);

const code = `function foo() { console.log('bar'); }`;
const tree = parser.parse(code);

console.log(tree.rootNode.toString()); // 输出语法树结构
```

```ts
import Parser from 'tree-sitter';
import Language from 'tree-sitter-javascript';

const parser = new Parser();
parser.setLanguage(Language);

const sourceCode = `const a = 1;`;
const tree = parser.parse(sourceCode);

const query = '(variable_declarator name: (identifier) @var)';
const matches = tree.rootNode.descendantsOfType('variable_declarator')
  .filter(node => node.firstNamedChild?.hasDescendantWithType('identifier'));

console.log(matches.map(node => node.text));
```

- **自定义语言**：编写 `grammar.js`，运行 `tree-sitter-cli generate` 生成解析器。  
- **增量解析**：使用 `parser.parse(newSource, oldTree)` 重用旧树。  
- **语法树查询**：使用 `tree-root.query(query)` 获取匹配节点。  

以上即为 Tree-sitter 的核心特性、功能与基本使用方式。