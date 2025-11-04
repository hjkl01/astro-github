
---
title: domain-list-community
---

# `domain-list-community`（V2Fly 领域列表社区版）

**项目地址**：<https://github.com/v2fly/domain-list-community>  

> 该项目旨在提供可供 V2Fly/V2Ray 等代理工具使用的域名列表，支持广告追踪、恶意域名、热门站点等分类，并通过社区维护保持高准确率和实时更新。

## 主要特性

| 特性 | 描述 |
|------|------|
| **多分类列表** | - `ad.txt`：广告与追踪域名<br>- `bypass.txt`：需要直连或特殊路由的域名<br>- `whitelist.txt`：白名单域名<br>- `abused.txt`：被滥用或识别为恶意的域名 |
| **实时更新** | 通过 GitHub Actions 自动检测更新，将最新域名同步到项目根目录，保持数据的及时性。 |
| **兼容 V2Fly/V2Ray** | 采用 `plain text` 格式，可直接在配置文件中引用，无需额外转换。 |
| **可统计与自定义** | 通过自带脚本 `count.sh` 可快速查看每个列表的域名数量，亦可根据需要自行编辑或添加 `custom.txt` |
| **社区维护** | 任何有兴趣的贡献者可 fork 本项目，提交 PR 或 Issue，以持续完善列表质量。 |

## 文件结构

```
domain-list-community/
├── ad/
│   ├── ad.txt     # 广告/跟踪域名列表
│   └── *.txt ...
├── banned/
│   ├── banned.txt # 被阻止域名
│   └── *.txt ...
├── bypass/
│   ├── bypass.txt # 直连或特殊路由域名
│   └── *.txt ...
├── whitelist/
│   ├── whitelist.txt   # 白名单域名
│   └── *.txt ...
├── README.MD
├── LICENSE
└── ...
```

> 每个 `.txt` 文件均为纯文本，每行一个域名，支持注释（以 `#` 开头）。

## 如何使用

1. **下载列表**  
   ```bash
   git clone https://github.com/v2fly/domain-list-community.git
   ```
   或者直接下载需要的单个文件，例如 `ad/ad.txt`。

2. **配置 V2Fly/V2Ray**  
   在 V2Fly/V2Ray 的 `config.json`（或 `config.yaml`）中，添加 DomainSet 或 DomainRule 相关字段，指向下载的列表文件。  
   **示例**（JSON）：
   ```json
   {
     "dns": {
       "enabled": true,
       "servers": [
         "8.8.8.8",
         "8.8.4.4"
       ],
       "listen": ":53",
       "useHosts": true,
       "cacheSize": 1000,
       "addHosts": true,
       "exclude": ["geoip:cn"],
       "domainStrategy": "IPIfNonMatch",
       "domains": [
         "geoip:cn",
         "geosite:category-ads",
         "proxy",      // 直连
         "direct"
       ]
     }
   }
   ```
   这里 `geosite:category-ads` 就会自动使用 `ad/ad.txt` 中的内容。

   **示例**（YAML）：
   ```yaml
   dns:
     enabled: true
     servers:
       - 8.8.8.8
       - 8.8.4.4
     try-hold: false
     domainStrategy: IPIfNonMatch
     domains:
       - "geosite:category-ads"
       - "direct"
   ```

   > - `geosite:<category>` 会根据 `geosite` 的 yaml 配置文件自动匹配相应的 `.txt` 列表。  
   > - 你也可以自行指定完整路径，例如 `[]/path/to/ad/ad.txt`。

3. **自定义列表**  
   如果需要添加自己的规则，只需新建 `custom.txt`（或任何你想要的名字），编辑后在配置文件中添加对应引用即可。

4. **维护与更新**  
   - 若你使用 Git 安装：执行 `git pull origin main` 更新列表。  
   - 若你下载单文件，则需要手动更新。可以每周检查一次官方仓库的 Commit。

5. **统计列表信息（可选）**  
   ```bash
   cd domain-list-community
   ./count.sh
   ```
   输出每个列表的域名数量，帮助你了解列表规模。

## 联系与贡献

- **Issue**：提交错误报告或功能建议。  
- **Pull Request**：提交新的域名或修正错误，项目会通过 CI 自动合并。  
- **讨论**：可在仓库 `Discussions` 进行社区交流。

> 该列表已被多款 V2Fly 兼容插件（如 Qv2ray、V2RayN、sing-box）广泛使用并持续更新，确保在不同网络环境下能获得最佳路由效果。