
---
title: django-filter
---

# django-filter 项目

## 项目地址
[GitHub 项目地址](https://github.com/carltongibson/django-filter)

## 主要特性
django-filter 是一个 Django 的第三方库，提供了一个通用的、指定化的方式来过滤基于 Django QuerySet 的数据。它旨在简化视图中的过滤逻辑，支持多种过滤类型（如精确匹配、范围过滤、包含搜索等），并与 Django REST Framework 等框架无缝集成。主要特性包括：
- **声明式过滤器**：通过定义 FilterSet 类来指定过滤字段和类型，避免在视图中编写复杂的查询代码。
- **内置过滤器**：支持各种数据类型，如字符串（exact、icontains）、数字（lt、gt、range）、日期（date、gt、lt）、多选（MultipleChoiceFilter）等。
- **自定义过滤器**：允许用户扩展自定义过滤逻辑。
- **集成支持**：易于与 Django 的类视图（Class-Based Views）、DRF 的过滤后端结合使用。
- **表单集成**：自动生成过滤表单，支持客户端验证和分页。
- **性能优化**：使用 Django ORM 的高效查询，避免 N+1 问题。

## 主要功能
- **数据过滤**：基于用户输入（如 GET 参数）动态过滤 QuerySet，支持单字段或多字段组合过滤。
- **搜索功能**：内置搜索过滤器，可对多个字段进行全文搜索。
- **排序支持**：可选与 django-filter 的排序扩展结合，实现数据排序。
- **分页兼容**：与 Django 的 Paginator 或第三方分页库（如 django.core.paginator）兼容。
- **API 集成**：在 REST API 中作为过滤后端，提供查询参数过滤资源列表。
- **国际化**：支持 Django 的 i18n 框架，过滤器标签可本地化。

## 用法
### 安装
```bash
pip install django-filter
```

### 配置
在 `settings.py` 中添加 `'django_filters'` 到 `INSTALLED_APPS`：
```python
INSTALLED_APPS = [
    # ...
    'django_filters',
]
```

### 定义过滤器
创建一个 FilterSet 子类，指定模型和过滤字段：
```python
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter(lookup_expr='gte')
    published_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = ['title', 'price', 'published_date']
```

### 在视图中使用
#### 函数视图示例
```python
from django.shortcuts import render
from .models import Book
from .filters import BookFilter

def book_list(request):
    books = Book.objects.all()
    filter = BookFilter(request.GET, queryset=books)
    return render(request, 'books/list.html', {'filter': filter})
```

#### 类视图示例
```python
from django_filters.views import FilterView
from .models import Book
from .filters import BookFilter

class BookListView(FilterView):
    model = Book
    filterset_class = BookFilter
    template_name = 'books/list.html'
```

#### 模板渲染
在模板中渲染过滤表单：
```html
<form method="get">
    {{ filter.form.as_p }}
    <button type="submit">过滤</button>
</form>
<ul>
    {% for book in filter.qs %}
        <li>{{ book.title }}</li>
    {% endfor %}
</ul>
```

### DRF 集成
在 DRF 视图中：
```python
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    filter_backends = [DjangoFilterBackend]
```

更多细节请参考项目文档。