---
title: flask-wtf
---

# Flask-WTF 项目描述

## 项目地址
[https://github.com/lepture/flask-wtf](https://github.com/lepture/flask-wtf)

## 主要特性
Flask-WTF 是 Flask 扩展，用于简化表单处理。它集成了 WTForms 库，提供安全、便捷的表单验证和渲染功能。主要特性包括：
- **CSRF 保护**：自动集成 Flask-WTF 的 CSRF 令牌，防止跨站请求伪造攻击。
- **表单验证**：支持 WTForms 的强大验证规则，如必填、长度、正则表达式等。
- **文件上传**：内置文件处理支持，包括多文件上传。
- **Recaptcha 集成**：可选集成 Google reCAPTCHA 防止垃圾提交。
- **国际化支持**：兼容 Flask-Babel 等工具，实现多语言表单。
- **简单集成**：无缝与 Flask 应用集成，无需复杂配置。

## 主要功能
- **表单类定义**：使用 WTForms 的 Field 和 Validator 创建自定义表单。
- **渲染和显示**：自动生成 HTML 表单，支持宏和模板渲染。
- **数据处理**：自动解析 POST 数据，进行验证和错误处理。
- **安全功能**：内置 CSRF 令牌生成和验证，确保表单提交安全。
- **扩展性**：支持自定义字段和验证器，适用于复杂表单场景。

## 用法示例
1. **安装**：
   ```
   pip install flask-wtf
   ```

2. **初始化**：
   在 Flask 应用中：
   ```python
   from flask import Flask
   from flask_wtf import FlaskForm
   from wtforms import StringField, SubmitField
   from wtforms.validators import DataRequired

   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'your-secret-key'

   class MyForm(FlaskForm):
       name = StringField('姓名', validators=[DataRequired()])
       submit = SubmitField('提交')
   ```

3. **在视图中使用**：
   ```python
   @app.route('/form', methods=['GET', 'POST'])
   def form():
       form = MyForm()
       if form.validate_on_submit():
           # 处理表单数据
           return '提交成功'
       return render_template('form.html', form=form)
   ```

4. **模板渲染**（form.html）：
   ```html
   <form method="POST">
       {{ form.hidden_tag() }}  <!-- 包含 CSRF 令牌 -->
       {{ form.name.label }} {{ form.name }}
       {{ form.submit }}
   </form>
   ```

更多细节请参考项目文档。