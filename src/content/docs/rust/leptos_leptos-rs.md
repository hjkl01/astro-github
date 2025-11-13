---
title: leptos
---


# Leptos (https://github.com/leptos-rs/leptos)

## 一、简介  
Leptos 是一款基于 Rust 的全栈 Web 框架。它把前后端统一到同一种语言，利用 Rust 的安全性与性能，提供了高效、可维护的 Web 开发体验。

## 二、主要特性  
- **双向绑定**：使用声明式语法轻松实现前端 UI 与后端数据的同步。  
- **响应式计算**：内置 Reactive 系统，可自动追踪数据变化并更新视图。  
- **SSR / CDN 缓存**：支持服务器端渲染和静态站点生成，提升 SEO 与首屏性能。  
- **TypeScript 友好**：前后端无缝编译，消除运行时类型错误。  
- **Rust 生态整合**：兼容 Diesel、SeaORM、grpc 等主流库，适配数据库与 gRPC。  
- **代码分割**：支持按需加载，降低 bundle 大小。  
- **服务器与客户端分离**：前端可以单独运行，也可与服务器共用同一代码库。

## 三、核心功能  
| 功能 | 说明 |
|------|------|
| `leptos::view!` | 声明式视图宏，类似 JSX。 |
| `Signal<T>` / `RwSignal<T>` | 响应式信号，用于共享状态。 |
| `create_effect` | 响应式副作用，监听信号变化执行代码。 |
| `Component` trait | 定义组件，支持 props 与状态。 |
| `create_server_action` | 服务器端请求钩子，支持 CSRF 保护。 |
| `Router` | 声明式路由，支持懒加载路由与守卫。 |
| `leptos_router::link` | 页面链接组件。 |
| `leptos_meta::Meta` | 动态更新 `<head>` 元素。 |

## 四、快速开始  

```bash
# 创建项目
cargo install cargo-leptos
cargo new my_lab -p my_lab -x
cd my_lab
cargo leptos new

# 运行开发服务器
cargo leptos watch
```

默认会在 `src` 中生成 `lib.rs` 与 `main.rs`，可直接编写组件。

### 示例

```rust
use leptos::*;
use leptos_meta::*;
use leptos_router::*;

#[component]
fn Home(cx: Scope) -> Element {
    view! { cx,
        <div class="home">
            <h1>"Hello, Leptos!"</h1>
        </div>
    }
}

#[component]
fn App(cx: Scope) -> Element {
    let (theme, set_theme) = create_signal(cx, "light");

    view! { cx,
        <Router>
            <Routes>
                <Route path="/" view=Home/>
            </Routes>
        </Router>
    }
}

fn main() {
    env_logger::init();
    mount_to_body(App);
}
```

## 五、常见使用方式  

| 场景 | 用法 | 示例 |
|------|------|------|
| **全栈 API** | 服务器端函数通过 `#[server]` 注解暴露 | `#[server(WhoAmI)]` |
| **公式渲染** | 结合 `yew` 或 `Leptos` 组件 | `use yew::mathml::Math`|
| **表单验证** | `create_form` 与 `subscribe_form` | `create_form(cx, validate_fn)` |
| **状态管理** | 使用 `Signal` 或 `RwSignal` | `let (counter, set_counter) = create_signal(cx, 0);` |

## 六、生态与扩展  

- **前端**：可与 yew、seed 等 Rust 前端框架共存。  
- **后端**：支持 Actix、Warp、Rocket 等 Web 后端框架。  
- **数据库**：可直接搭配 Diesel、SeaORM、sqlx。  
- **模板**：集成 `tera`、`handlebars` 等模板引擎。  
- **CI/CD**：与 GitHub Actions、GitLab CI 无缝集成。  

---
> 以上内容为 Leptos 框架的核心特性与使用方式介绍，供快速上手与实现全栈 Rust Web 开发。  
