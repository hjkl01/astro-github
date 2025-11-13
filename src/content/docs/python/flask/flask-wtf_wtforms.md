---
title: flask-wtf
---

# Flask-WTF 项目

## 项目地址
[GitHub 项目地址](https://github.com/wtforms/flask-wtf)

## 主要特性
Flask-WTF 是 Flask 框架的 WTForms 扩展库，主要用于简化表单处理。它集成了 WTForms（一个灵活的表单验证和渲染库），并与 Flask 无缝集成。核心特性包括：
- **CSRF 保护**：内置跨站请求伪造（CSRF）防护机制，自动生成和验证令牌，提高表单安全性。
- **表单验证**：支持多种内置验证规则，如必填、长度限制、正则表达式等，可自定义验证器。
- **表单渲染**：提供便捷的模板渲染方式，支持 HTML5 输入类型和 Bootstrap 等 CSS 框架集成。
- **文件上传处理**：简化文件上传表单的创建和处理。
- **国际化支持**：兼容 Flask 的 i18n 功能，便于多语言表单。
- **轻量级集成**：无需额外配置，即可与 Flask 应用结合使用。

## 主要功能
- **表单类定义**：使用 WTForms 的 `Form` 类创建表单，支持字段类型如 `StringField`、`PasswordField`、`BooleanField` 等。
- **CSRF 令牌管理**：自动在表单中添加隐藏字段，防止恶意提交。
- **数据验证与错误处理**：表单提交后自动验证数据，生成错误消息并渲染到模板。
- **AJAX 支持**：可与 JavaScript 结合，实现动态表单验证。
- **扩展性**：支持自定义字段和验证器，适用于复杂表单场景，如用户注册、登录或调查问卷。

## 用法
### 安装
使用 pip 安装：
```
pip install flask-wtf
```

### 基本用法示例
1. **初始化扩展**：
   在 Flask 应用中初始化：
   ```python
   from flask import Flask
   from flask_wtf import FlaskForm

   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'your-secret-key'  # 必需，用于 CSRF

   class MyForm(FlaskForm):
       name = StringField('姓名', validators=[DataRequired()])
       submit = SubmitField('提交')
   ```

2. **在视图中使用**：
   ```python
   from flask import render_template, request

   @app.route('/form', methods=['GET', 'POST'])
   def form():
       form = MyForm()
       if form.validate_on_submit():
           # 处理表单数据
           return '提交成功'
       return render_template('form.html', form=form)
   ```

3. **模板渲染（Jinja2）**：
   在 HTML 模板中：
   ```html
   <form method="POST">
       {{ form.hidden_tag() }}  <!-- 包含 CSRF 令牌 -->
       {{ form.name.label }} {{ form.name() }}
       {% for error in form.name.errors %}
           <span style="color: red;">{{ error }}</span>
       {% endfor %}
       {{ form.submit() }}
   </form>
   ```

更多高级用法详见官方文档，包括文件上传、自定义验证和集成第三方库。