
---
title: django-autocomplete-light
---

# django-autocomplete-light 项目

## 项目地址
[GitHub 项目地址](https://github.com/yourlabs/django-autocomplete-light)

## 主要特性
django-autocomplete-light 是一个 Django 应用程序，旨在简化自动完成功能的实现。它基于 jQuery UI 的 Autocomplete 插件，提供高效的搜索和建议功能。主要特性包括：
- **轻量级集成**：无需复杂的 JavaScript 配置，支持 Django 的模型和表单。
- **服务器端搜索**：通过 AJAX 请求从服务器获取实时搜索结果，支持自定义查询过滤。
- **多字段支持**：可以基于模型的多个字段（如名称、描述）进行搜索。
- **选择器和验证**：自动处理选择的验证和错误处理，支持多选模式。
- **主题兼容**：易于与 Bootstrap 或其他前端框架集成。
- **性能优化**：支持缓存和分页，适用于大型数据集。

## 主要功能
- **自动完成表单字段**：在 Django 表单中快速添加自动完成输入框。
- **模型搜索**：针对 Django 模型实例进行模糊搜索，例如用户姓名或产品标签。
- **自定义视图**：允许开发者定义自定义的搜索视图和过滤逻辑。
- **多语言支持**：兼容 Django 的国际化（i18n）功能。
- **测试友好**：提供单元测试和文档化的 API，便于扩展和维护。

## 用法
### 安装
1. 通过 pip 安装：
   ```
   pip install django-autocomplete-light
   ```
2. 在 `settings.py` 中添加应用：
   ```python
   INSTALLED_APPS = [
       # ... 其他应用
       'dal',
       'dal_select2',  # 可选：用于 Select2 集成
       'autocomplete_light',
   ]
   ```
3. 运行迁移：
   ```
   python manage.py migrate
   ```

### 基本用法
1. **定义自动完成类**：在 `autocompletes.py` 文件中创建类，继承 `AutocompleteModelBase`：
   ```python
   from dal import autocomplete
   from .models import YourModel

   class YourModelAutocomplete(autocomplete.Select2QuerySetView):
       def get_queryset(self):
           qs = YourModel.objects.all()
           if self.q:
               qs = qs.filter(name__istartswith=self.q)
           return qs
   ```

2. **注册 URL**：在 `urls.py` 中添加：
   ```python
   from dal import autocomplete_urls
   from .autocompletes import YourModelAutocomplete

   urlpatterns = [
       # ... 其他 URL
       path('yourmodel-autocomplete/', YourModelAutocomplete.as_view(), name='yourmodel_autocomplete'),
   ]
   ```

3. **在表单中使用**：在模型表单中添加自动完成字段：
   ```python
   from autocomplete_light import shortcuts as al

   class YourForm(forms.ModelForm):
       your_field = al.ModelSelect2('YourModelAutocomplete', 'name')

       class Meta:
           model = YourModel
           fields = '__all__'
   ```

4. **模板集成**：在 HTML 模板中加载静态文件并渲染表单：
   ```html
   {% load static %}
   <script src="{% static 'autocomplete_light/jquery.init.js' %}"></script>
   <script src="{% static 'autocomplete_light/autocomplete.init.js' %}"></script>
   {{ form.media }}
   {{ form.as_p }}
   ```

### 高级用法
- **多选模式**：使用 `ModelSelect2Multiple` 来支持多选。
- **自定义模板**：通过 `choice_template` 参数自定义显示格式。
- **权限控制**：在 `get_queryset` 中添加用户权限过滤，如 `qs.filter(user=self.request.user)`。

更多细节请参考项目文档。