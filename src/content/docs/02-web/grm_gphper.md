---
title: grm
---

# GRM 项目介绍

## 项目地址
[GitHub 项目地址](https://github.com/gphper/grm)

## 主要特性
GRM 是一个基于 PHP 的轻量级路由管理框架，主要特性包括：
- **简单高效的路由系统**：支持 RESTful 路由定义，自动解析 URL 并匹配控制器方法。
- **中间件支持**：允许添加自定义中间件，用于处理请求前后的逻辑，如认证、日志记录等。
- **依赖注入**：内置容器，支持自动注入依赖，提高代码的可维护性。
- **错误处理**：统一的异常捕获和响应机制，提供 JSON 或 HTML 格式的错误输出。
- **轻量级设计**：无外部依赖，核心文件少，便于集成到现有 PHP 项目中。
- **支持 Composer**：易于安装和更新。

## 主要功能
- **路由定义**：通过注解或配置文件定义 GET、POST、PUT、DELETE 等 HTTP 方法的路由。
- **控制器管理**：支持 MVC 模式，控制器类处理业务逻辑。
- **请求与响应**：提供 Request 和 Response 对象，方便获取参数、设置头部和返回数据。
- **视图渲染**：集成简单模板引擎，支持渲染 HTML 视图。
- **CLI 工具**：内置命令行接口，用于开发和测试路由。

## 用法
### 安装
1. 通过 Composer 安装：
   ```
   composer require gphper/grm
   ```

2. 在项目根目录创建 `index.php` 作为入口文件：
   ```php
   <?php
   require 'vendor/autoload.php';

   use Grm\App;

   $app = new App();
   $app->run();
   ```

### 基本路由定义
在控制器中使用注解定义路由，例如：
```php
<?php
use Grm\Controller;

class UserController extends Controller
{
    /**
     * @route GET /user/{id}
     */
    public function getUser($id)
    {
        return json_encode(['id' => $id, 'name' => '示例用户']);
    }

    /**
     * @route POST /user
     */
    public function createUser()
    {
        $data = $this->request->getPost();
        // 处理逻辑
        return json_encode(['message' => '用户创建成功']);
    }
}
```

### 运行项目
- 将入口文件 `index.php` 部署到 Web 服务器（如 Apache 或 Nginx），访问对应 URL 即可测试路由。
- 对于开发环境，可使用 PHP 内置服务器：
  ```
  php -S localhost:8000 index.php
  ```
- 访问 `http://localhost:8000/user/123` 将调用 `getUser` 方法。

更多高级用法请参考项目 README 和示例代码。