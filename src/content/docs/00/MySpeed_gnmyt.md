
---
title: MySpeed
---

# MySpeed
#### 项目地址: https://github.com/gnmyt/MySpeed

## 主要功能
- **网络测速**：测量下载速度、上传速度、Ping RTT、TTL、丢包率等关键指标。  
- **多线程并发测试**：支持自定义并发线程数，提升下载/。  
- **高精度计时**：利用 `Stopwatch` 进行毫秒级计时，保证结果可重复性。  
- **结果可视化**：在控制台输出图形化条形图（可选），直观展示速度变化。  
- **跨平台支持**：.NET 6+ 可在 Windows、Linux、macOS 上运行。  
- **输出文件**：默认以 CSV 或 JSON 格式保存测试结果，便于后期分析。  
- **自定义 URL**：可自行指定测速服务器 URL，或使用默认的公共测速站点。  
- **错误处理**：对各类网络异常做了细致处理，避免测速时程序崩溃。  

## 用法示例
```bash
# 直接运行，使用默认设置
dotnet run

# 指定下载/上传服务器地址
dotnet run --download-url https://speedtest.example.com --upload-url https://upload.example.com

# 自定义并发线程数
dotnet run -t 8

# 输出结果到 CSV
dotnet run --output csv

# 开启图形化条形图显示
dotnet run --graph```

## 参数说明
| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-d, --download-url` | 下载测速服务器地址 | `https://speed.hetzner.de/100MB.bin` |
| `-u, --upload-url` | 上传测速服务器地址 | `http://speedtest.bart.ca/upload` |
| `-t, --threads` | 并发线程数 | `4` |
| `-o, --output` | 输出格式（csv/json） | `csv` |
| `-g, --graph` | 是否显示图形化条形图 | `false` |
| `-h, --help` | 显示帮助信息 |  |

## 快速上手
1. 克隆仓库  
   ```bash
   git clone https://github.com/gnmyt/MySpeed.git
   cd MySpeed
   ```
2. 依赖插件自动会被 `dotnet restore` 安装。  
3. 直接执行 `dotnet run`，即刻开始测速。  

> **提示**：首次运行请确认网络可达性，若测速失败可尝试更换 `--download-url` / `--upload-url`。  

---