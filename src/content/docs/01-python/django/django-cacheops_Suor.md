---
title: django-cacheops
---

# django-cacheops 项目

## 项目地址
[GitHub 项目地址](https://github.com/Suor/django-cacheops)

## 主要特性
django-cacheops 是一个高效的 Django 缓存后端，专注于透明的查询缓存和自动失效机制。主要特性包括：
- **透明缓存**：无需修改模型或查询代码，即可自动缓存 QuerySet 查询结果。
- **自动失效**：基于模型变更自动失效相关缓存，支持细粒度控制（如按字段或关系失效）。
- **支持多种后端**：兼容 Redis、Memcached 等流行缓存系统，Redis 为默认推荐。
- **事务安全**：与 Django 事务系统无缝集成，确保缓存一致性。
- **高级功能**：支持缓存失效模式（如 invalidate_on_commit）、缓存键前缀、分布式锁，以及对复杂查询（如聚合、注解）的优化。
- **轻量高效**：最小化数据库查询，减少负载，支持缓存预热和批量操作。

## 主要功能
- **查询缓存**：自动缓存 SELECT 查询，支持缓存时间（timeout）和条件失效。
- **对象缓存**：缓存单个模型实例，支持 get_or_set 等原子操作。
- **失效机制**：监听模型信号（post_save, post_delete 等）自动清除缓存，支持手动失效。
- **配置灵活**：通过 settings.py 配置缓存操作，如启用/禁用特定模型的缓存、自定义键生成。
- **集成工具**：提供管理命令（如 cacheops_clear）用于缓存清理和调试。

## 用法
1. **安装**：
   ```
   pip install django-cacheops
   ```

2. **配置 settings.py**：
   ```python
   INSTALLED_APPS = [
       # ... 其他 app
       'cacheops',
   ]

   CACHES = {
       'default': {
           'BACKEND': 'cacheops.backends.redis',  # 或其他后端
           'LOCATION': 'redis://127.0.0.1:6379/1',
           'TIMEOUT': 60 * 15,  # 缓存超时时间
       },
       'cacheops': {  # 专用缓存
           'BACKEND': 'cacheops.backends.redis',
           'LOCATION': 'redis://127.0.0.1:6379/1',
       }
   }

   # 启用缓存模型，例如：
   CACHEOPS = {
       'myapp.*': {'ops': 'all', 'timeout': 60*15},  # 缓存所有操作
       'auth.user': {'ops': {'fetch', 'get'}, 'timeout': 60*5},  # 仅缓存 fetch 和 get
   }
   ```

3. **使用示例**：
   - 自动缓存查询：
     ```python
     from myapp.models import Article

     # 这将自动缓存结果
     articles = Article.objects.all()
     ```
   - 手动缓存对象：
     ```python
     from cacheops import cached_as

     @cached_as(Article.objects.get(id=1), timeout=60)
     def get_article():
         return Article.objects.get(id=1)
     ```
   - 失效缓存：
     ```python
     from cacheops import invalidate_obj

     invalidate_obj(article_instance)  # 失效单个对象
     Article.objects.invalidate_all()  # 失效所有
     ```

更多细节请参考项目文档。