---
title: yaak
---
---

## 使用示例  

```bash
# 1. 通过模板创建新项目
yaak init python-web my-sample-app

# 2. 进入项目目录
cd my-sample-app

# 3. 安装依赖（示例：pip, npm 等）
yaak run install.sh

# 4. 运行项目
yaak run run.py

# 5. 批量执行所有测试脚本
yaak batch tests --filter "test_*.py"

# 6. 安装自定义插件
yaak plugin install my-custom-plugin

# 7. 查看日志
yaak log --tail
```

---
## 贡献与文档  
- **源码**: <https://github.com/mountain-loop/yaak>
- **Issue**: <https://github.com/mountain-loop/yaak/issues>
- **Wiki**: 详细文档请见仓库 Wiki 页面。
> 以上内容为 `yaak` 项目的核心特性、功能与基本使用方法，协助快速上手与集成。