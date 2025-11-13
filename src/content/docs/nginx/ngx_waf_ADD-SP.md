---
title: ngx
---

# ngx_waf 项目

## 项目地址
[https://github.com/ADD-SP/ngx_waf](https://github.com/ADD-SP/ngx_waf)

## 主要特性
- **模块化设计**：基于 OpenResty 和 Lua 实现的 Web 应用防火墙（WAF），支持高度自定义规则和配置，便于扩展和维护。
- **高性能**：利用 Nginx 的异步非阻塞 I/O 架构，确保低延迟和高吞吐量，适用于高并发环境。
- **规则引擎**：内置多种检测规则，支持 SQL 注入、XSS 攻击、路径遍历等常见 Web 漏洞防护，可通过 Lua 脚本动态加载规则。
- **日志与监控**：提供详细的攻击日志记录，支持实时监控和告警集成，便于安全分析。
- **易集成**：作为 Nginx 模块，无缝集成到现有 Nginx/OpenResty 部署中，支持容器化和云环境。

## 主要功能
- **威胁检测**：实时扫描 HTTP 请求和响应，识别并阻挡恶意流量，包括 OWASP Top 10 攻击类型。
- **白名单/黑名单管理**：支持 IP、User-Agent 等维度的访问控制，允许灵活的例外处理。
- **自定义规则**：用户可编写 Lua 脚本定义防护逻辑，支持正则表达式和模式匹配。
- **性能优化**：内置缓存机制和采样模式，减少对正常流量的影响。
- **报告生成**：自动生成安全事件报告，支持导出到外部系统如 ELK Stack。

## 用法
1. **安装**：
   - 确保已安装 OpenResty（Nginx + Lua）。
   - 通过 LuaRocks 或手动编译安装 ngx_waf 模块：`luarocks install lua-resty-waf`（或参考仓库的构建指南）。
   - 在 Nginx 配置中加载模块：`load_module modules/ngx_waf.so;`。

2. **配置**：
   - 编辑 `nginx.conf`，在 http 或 server 块中添加：
     ```
     waf on;
     waf_mode BLOCK;  # 或 MONITOR 模式
     waf_rules /path/to/rules.lua;  # 指定规则文件
     ```
   - 示例规则文件（rules.lua）：
     ```lua
     local rules = {
         { pattern = "'; DROP TABLE", action = "block" },  -- SQL 注入检测
         { pattern = "<script>", action = "block" }  -- XSS 检测
     }
     return rules
     ```

3. **启动与测试**：
   - 重载 Nginx：`nginx -s reload`。
   - 测试：使用工具如 curl 发送恶意请求，观察日志 `/var/log/nginx/waf.log` 中的阻挡记录。
   - 监控：集成 Prometheus 或其他工具查看 WAF 指标。

更多细节请参考仓库的 README 和示例配置。