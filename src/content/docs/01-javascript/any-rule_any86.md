
---
title: any-rule
---

# any-rule 项目

## 项目地址
[https://github.com/any86/any-rule](https://github.com/any86/any-rule)

## 主要特性
any-rule 是一个轻量级的 JavaScript 规则引擎库，专注于提供简单、高效的规则匹配和验证功能。主要特性包括：
- **规则链式调用**：支持 fluent API 风格的规则构建，便于链式组合多个规则。
- **内置常用规则**：预置了邮箱、手机号、URL、数字范围等常见验证规则。
- **自定义规则扩展**：允许用户轻松添加自定义验证逻辑。
- **异步支持**：部分规则支持异步验证，适用于复杂场景。
- **轻量无依赖**：纯 JS 实现，体积小巧，无需外部依赖。
- **跨环境兼容**：支持浏览器和 Node.js 环境。

## 主要功能
- **数据验证**：用于表单输入、API 参数等场景的规则校验。
- **条件匹配**：基于规则表达式进行条件判断和过滤。
- **错误处理**：提供详细的错误消息，支持国际化。
- **性能优化**：规则执行高效，适合大规模数据处理。

## 用法
### 安装
```bash
npm install any-rule
```

### 基本用法
```javascript
import { rule } from 'any-rule';

// 创建规则链
const validator = rule()
  .required('字段不能为空')
  .email('邮箱格式无效')
  .minLength(6, '长度至少6位');

// 验证数据
const result = validator.validate('user@example.com');
if (result.valid) {
  console.log('验证通过');
} else {
  console.log(result.errors); // 输出错误信息
}
```

### 自定义规则
```javascript
import { rule, Rule } from 'any-rule';

class CustomRule extends Rule {
  validate(value) {
    return value > 100 ? true : '值必须大于100';
  }
}

const customValidator = rule().add(new CustomRule());
```

更多用法请参考项目 README 和示例代码。