---
title: ratatui
---


# ratatui

> **GitHub 项目地址**: <https://github.com/ratatui/ratatui>

## 项目简介
ratatui 是一个用 Rust 编写的跨平台终端用户界面（TUI）框架，旨在帮助开发者快速构建可扩展、可维护且高性能的终端应用程序。它基于 `crossterm`，支持 Windows、Linux、macOS，并兼容多种终端尺寸与颜色方案。

## 主要特性
- **模块化组件**：提供常用 UI 组件（如 `Block`, `Paragraph`, `Table`, `List`, `Tabs`, `Chart` 等），可自由组合。
- **主题与样式**：支持自定义颜色、字体样式、边框样式，易于实现深色/浅色主题切换。
- **事件驱动**：统一事件系统，支持键盘、鼠标、定时器等多种事件，方便实现交互逻辑。
- **布局与渲染**：基于 `Rect` 的布局系统，可实现网格、垂直/水平分割、弹性布局等。
- **高性能**：采用最小化重绘策略，仅在必要时更新屏幕，确保流畅体验。
- **可扩展**：支持自定义组件、渲染器与事件处理器，满足特殊需求。

## 快速上手

### 1. 添加依赖
```toml
[dependencies]
ratatui = "0.27"   # 请根据官方文档选择最新版本
crossterm = "0.27"
```

### 2. 示例代码
```rust
use ratatui::{
    prelude::*,
    widgets::{Block, Borders, Paragraph},
};
use crossterm::{
    event::{self, Event, KeyCode},
    execute,
    terminal::{disable_raw_mode, enable_raw_mode, EnterAlternateScreen, LeaveAlternateScreen},
};
use std::{error::Error, io};

fn main() -> Result<(), Box<dyn Error>> {
    // 初始化终端
    enable_raw_mode()?;
    let mut stdout = io::stdout();
    execute!(stdout, EnterAlternateScreen)?;
    let backend = CrosstermBackend::new(stdout);
    let mut terminal = Terminal::new(backend)?;

    // 主循环
    loop {
        terminal.draw(|f| {
            let size = f.size();
            let block = Block::default()
                .title("Hello, ratatui!")
                .borders(Borders::ALL);
            f.render_widget(block, size);

            let paragraph = Paragraph::new("Press 'q' to exit.")
                .style(Style::default().fg(Color::Yellow));
            f.render_widget(paragraph, size);
        })?;

        if event::poll(std::time::Duration::from_millis(100))? {
            if let Event::Key(key) = event::read()? {
                if key.code == KeyCode::Char('q') {
                    break;
                }
            }
        }
    }

    // 清理终端
    disable_raw_mode()?;
    execute!(terminal.backend_mut(), LeaveAlternateScreen)?;
    terminal.show_cursor()?;
    Ok(())
}
```

### 3. 运行
```bash
cargo run
```

按 `q` 退出程序。

## 进一步阅读
- 官方文档: <https://ratatui.rs/>  
- 示例项目: <https://github.com/ratatui/ratatui/tree/master/examples>  

--- 

> **文件路径**: `src/content/docs/00/ratatui_ratatui.md`  
> **保存方式**: 将上述内容复制到该路径下的 Markdown 文件即可。