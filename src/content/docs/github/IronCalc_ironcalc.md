---
title: IronCalc_ironcalc
---

# IronCalc

IronCalc 是一个现代化的电子表格引擎和工具集，用于在各种环境中处理电子表格。该项目使用 Rust 编程，支持多种编程语言绑定，包括 Python、JavaScript (WASM)、Node.js 等。

## 主要功能

- **电子表格引擎**：提供完整的电子表格计算和数据处理功能
- **多语言支持**：支持 Python、JavaScript、Node.js、R、Julia、Go 等多种编程语言
- **多种界面**：支持终端界面、桌面应用程序和 Web 应用程序
- **XLSX 支持**：完整的 Excel 文件读写功能
- **高性能**：基于 Rust 的高性能实现

## 安装和使用

### Docker 方式

如果已安装 Docker，可以直接运行：

```bash
docker compose up --build
```

然后访问 [http://localhost:2080](http://localhost:2080) 测试应用程序。

### 从源码构建

```bash
cargo build --release
```

### 测试和代码覆盖率

运行所有测试（包括单元测试、集成测试、代码检查和格式化测试）：

```bash
make tests
```

生成代码覆盖率报告：

```bash
make coverage
cd target/coverage/html/
python -m http.server
```

## API 文档

文档发布在：[https://docs.rs/ironcalc/latest/ironcalc/](https://docs.rs/ironcalc/latest/ironcalc/)

本地生成文档：

```bash
make docs
cd target/doc
python -m http.server
```

然后访问 [http://0.0.0.0:8000/ironcalc/](http://0.0.0.0:8000/ironcalc/)

## 使用示例

在 `Cargo.toml` 中添加依赖：

```toml
[dependencies]
ironcalc = { git = "https://github.com/ironcalc/IronCalc", version = "0.5" }
```

在 `main.rs` 中使用：

```rust
use ironcalc::{
    base::{expressions::utils::number_to_column, Model},
    export::save_to_xlsx,
};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let mut model = Model::new_empty("hello-calc.xlsx", "en", "UTC")?;

    // 在第一个工作表中添加数字平方
    for row in 1..100 {
        for column in 1..100 {
            let value = row * column;
            model.set_user_input(0, row, column, format!("{}", value));
        }
    }

    // 添加新工作表
    model.add_sheet("Calculation")?;
    let last_column = number_to_column(100).unwrap();
    let formula = format!("=SUM(Sheet1!A1:{}100)", last_column);
    model.set_user_input(1, 1, 1, formula);

    // 评估公式
    model.evaluate();

    // 保存到磁盘
    save_to_xlsx(&model, "hello-calc.xlsx")?;
    Ok(())
}
```

## 在线预览

可以在浏览器中体验早期预览版本：[https://app.ironcalc.com](https://app.ironcalc.com)

## 贡献和社区

项目正在积极开发中，欢迎各种形式的贡献。如果您对高质量代码、开放基础设施的电子表格感兴趣，可以：

- 加入 [Discord 频道](https://discord.gg/zZYWfh3RHJ)
- 发送邮件至 [hello@ironcalc.com](mailto:hello@ironcalc.com)

## 许可证

项目采用双重许可证：

- [MIT 许可证](https://github.com/ironcalc/IronCalc/blob/main/LICENSE-MIT)
- [Apache 2.0 许可证](https://github.com/ironcalc/IronCalc/blob/main/LICENSE-Apache-2.0)

您可以选择其中任一许可证使用。

## 项目状态

- ⭐ GitHub Stars: 2.9k+
- 🍴 Forks: 98+
- 📝 Issues: 121+
- 🔀 Pull Requests: 16+
- 👥 贡献者: 19+

## 技术栈

- **Rust** (84.0%) - 核心引擎
- **TypeScript** (14.8%) - Web 界面
- **JavaScript** (0.7%) - 辅助脚本
- **Docker** (0.1%) - 容器化
- **Python** (0.1%) - 绑定和工具

## 相关链接

- [官方网站](https://www.ironcalc.com)
- [GitHub 仓库](https://github.com/ironcalc/IronCalc)
- [在线演示](https://app.ironcalc.com)
- [API 文档](https://docs.rs/ironcalc)
- [Discord 社区](https://discord.gg/zZYWfh3RHJ)
