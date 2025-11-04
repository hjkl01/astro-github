
---
title: guihua.lua
---


# guihua.lua

项目地址: https://github.com/ray-x/guihua.lua

## 项目简介
guihua.lua 是一个为 Love2D 设计的 **轻量级 GUI 库**。  
它采用高内聚、低耦合的模块化架构，支持自定义控件、布局、主题与事件系统，使 Lua 代码可以像原生组件一样灵活地管理界面。

## 主要特性
- **简洁的 API**：几行代码即可创建窗口、按钮、文本框等常用控件。  
- **模块化布局**：支持水平、垂直、网格与自由布局，方便实现响应式 UI。  
- **事件驱动**：统一的事件分发机制，支持点击、键盘、鼠标滚轮、拖拽等。  
- **主题与皮肤**：可通过 JSON 或 Lua 表一次性定义全局主题，快速切换 UI 颜色、字体与边框样式。  
- **数据绑定**：支持两向绑定，UI 与游戏状态同步更直观。  
- **扩展性**：可自行注册自定义控件，继承基础 Widget 或实现自定义渲染。

## 核心功能
| 功能 | 说明 |
|------|------|
| `Window` | 具备拖拽、缩放、关闭、标题栏的窗口控件，适合弹窗与工具面板。 |
| `Button` | 单击、双击、长按、禁用态三态按钮。 |
| `Label` | 文本显示与可换行文本框。 |
| `InputBox` | 支持单行/多行输入、自动匹配宽高、光标控制。 |
| `Slider` | 线性滚动条，滑块可自定义大小。 |
| `Checkbox / Radio` | 带图标的勾选/单选框。 |
| `ListView` | 列表视图，可对滚动条实现懒加载。 |
| `ScrollPane` | 支持垂直/水平滚动的容器。 |
| `ThemeManager` | 动态切换主题文件，支持热更新。 |

## 使用方法

1. **安装**  
   将 `libs/guihua.lua` 目录放入你的项目中，或使用 LuaRocks（如果官方已发布）：

   ```bash
   luarocks install guihua
   ```

2. **导入与初始化**  

   ```lua
   local guihua = require("guihua.gui")
   local Gui = guihua.new()   -- 创建 GUI 实例
   ```

3. **创建控件**  

   ```lua
   local win = Gui:addWindow{
       title = "示例窗口",
       x = 100, y = 80,
       w = 400, h = 300,
   }

   win:addButton{
       text = "点击我",
       w = 100,
       onClick = function() print("按钮被点击") end,
   }

   win:addSlider{
       min = 0, max = 100,
       value = 50,
       w = 200,
   }
   ```

4. **渲染 & 事件**  
   在 Love2D 的回调中调用 GUI 的渲染与事件分发：

   ```lua
   function love.draw()
       Gui:draw()
   end

   function love.update(dt)
       Gui:update(dt)
   end

   function love.mousepressed(x, y, button)
       Gui:mousepressed(x, y, button)
   end

   function love.mousereleased(x, y, button)
       Gui:mousereleased(x, y, button)
   end

   function love.mousemoved(x, y, dx, dy)
       Gui:mousemoved(x, y, dx, dy)
   end

   function love.keypressed(key)
       Gui:keypressed(key)
   end

   function love.textinput(t)
       Gui:textinput(t)
   end
   ```

5. **主题自定义**  

   ```lua
   local myTheme = {
       backgroundColor = {255, 255, 255, 255},
       textColor       = {0, 0, 0, 255},
       button = {
           background = {70, 130, 180, 255},
           foreground = {255, 255, 255, 255},
           hover = {100, 149, 237, 255},
       },
   }

   Gui:setTheme(myTheme)
   ```

## 示例代码

```lua
local guihua = require("guihua.gui")
local Gui = guihua.new()

function love.load()
    Gui:addWindow{
        title = "Hello GUI",
        x = 200, y = 150,
        w = 320, h = 240,
    }:addButton{
        text = "Greet",
        w = 80,
        onClick = function() print("你好，世界!") end,
    }:addLabel{
        text = "请输入名字：",
        x = 20, y = 80,
    }:addInputBox{
        w = 180,
        onReturn = function(txt) print("姓名:", txt) end,
    }
end

function love.update(dt)
    Gui:update(dt)
end

function love.draw()
    Gui:draw()
end

function love.mousepressed(x, y, button)
    Gui:mousepressed(x, y, button)
end

function love.mousereleased(x, y, button)
    Gui:mousereleased(x, y, button)
end

function love.textinput(t)
    Gui:textinput(t)
end

function love.keypressed(key)
    Gui:keypressed(key)
end
```

## 结语
guihua.lua 通过简洁的 API 与良好的可扩展性，帮助 Love2D 开发者快速搭建游戏 UI 或工具面板。无论是单机游戏还是复杂的编辑器，它都能满足常规 GUI 开发需求。

---
