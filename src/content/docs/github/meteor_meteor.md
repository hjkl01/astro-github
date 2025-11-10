---
title: meteor
---

# Meteor

**GitHub 项目地址**: https://github.com/meteor/meteor  

## 简介

Meteor 是一个全栈 JavaScript 框架，适用于快速开发 Web、移动和桌面应用。它把前后端无缝连接，依靠自动同步、实时更新以及一站式工具链，极大简化了开发流程。

## 主要特性

| 特性 | 说明 |
|------|------|
| **实时数据同步** | 内置 `live query`，数据变更立即推送到所有客户端。 |
| **同构代码** | 同一套代码可以在服务器端（Node.js）和客户端（浏览器）运行。 |
| **包系统** | `meteor add`/`meteor remove` 轻松集成第三方包，生态丰富。 |
| **自动刷新** | 代码修改后，浏览器即刷新，满足快速迭代需求。 |
| **全栈开发体验** | 从数据库（MongoDB）到路由、模板、构建工具，全部包含。 |
| **移动端支持** | 使用 Cordova 可一次构建并发布至 iOS/Android。 |
| **插件化** | 支持 community packages、Cordova 插件等扩展。 |
| **安全** | 默认使用 `published`/`restricted` 数据发布模式，减少意外泄露。 |

## 核心功能

| 功能 | 关键命令 / API |
|------|----------------|
| **创建项目** | `meteor create <project_name>` |
| **运行项目** | `meteor`（默认 `localhost:3000`） |
| **添加包** | `meteor add <package_name>` (如 `meteor add accounts-password` ) |
| **移除包** | `meteor remove <package_name>` |
| **打包发布** | `meteor build ../output_dir --architecture os.linux.x86_64` |
| **移动部署** | `meteor build ../output_dir --architecture os.linux.x86_64 --cordova` |
| **数据库操作** | `Meteor.Collection`、`Meteor.methods`、`getParams` 等 |

## 用法示例

```bash
# 1. 安装 Meteor
curl https://install.meteor.com/ | sh

# 2. 创建新项目
meteor create hello_meteor
cd hello_meteor

# 3. 运行项目
meteor

# 4. 添加实时聊天室包
meteor add meteorhacks:fast-render
meteor add meteorhacks:fast-form

# 5. 修改 main.js 添加简单集合
import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';

export const Messages = new Mongo.Collection('messages');

Meteor.startup(() => {
  // 代码仅在服务器启动时执行
});

Meteor.methods({
  'messages.insert'(text) {
    Messages.insert({ text, createdAt: new Date() });
  },
});
```

```html
<!-- client/main.html -->
<head>
  <title>Meteor Demo</title>
</head>

<template name="chatRoom">
  <ul>
    {{#each messages}}
      <li>{{text}} <small>{{createdAt}}</small></li>
    {{/each}}
  </ul>
  <input id="newMessage" type="text" placeholder="Type a message...">
  <button id="send">Send</button>
</template>
```

```js
// client/main.js
import { Template } from 'meteor/templating';
import { Messages } from './main';
import { Meteor } from 'meteor/meteor';
import './main.html';

Template.chatRoom.helpers({
  messages() {
    return Messages.find({}, { sort: { createdAt: -1 } });
  }
});

Template.chatRoom.events({
  'click #send'(event) {
    const text = document.getElementById('newMessage').value;
    Meteor.call('messages.insert', text);
    event.target.value = '';
  }
});
```

> 运行 `meteor`，浏览器即呈现实时聊天页面，所有用户都能看到新消息。

## 文档 & 资源

- 官方文档: https://docs.meteor.com/
- GitHub 仓库: https://github.com/meteor/meteor  
- 社区教程: https://guide.meteor.com/, https://guide.meteor.com/react.html  

> Meteor 集成了现代前端框架 (React, Vue, Angular 等)，可以依照所选框架继续实现高级 UI。