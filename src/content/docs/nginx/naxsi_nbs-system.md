---
title: naxsi
---

# NAXSI 项目

## 项目地址
[https://github.com/nbs-system/naxsi](https://github.com/nbs-system/naxsi)

## 主要特性
NAXSI（Nginx Anti XSS & SQL Injection）是一个开源的Web应用防火墙（WAF）模块，专为Nginx设计，主要用于防范SQL注入（SQLi）和跨站脚本攻击（XSS）。其核心特性包括：
- **学习模式**：自动分析正常流量，生成规则集，避免手动配置的复杂性。
- **黑白名单机制**：基于规则的白名单过滤，结合黑名单阻挡已知攻击模式，支持自定义规则。
- **低误报率**：通过分数系统评估请求风险，只有高分请求才被阻挡，减少对合法流量的干扰。
- **实时日志和监控**：提供详细的攻击日志，支持与外部工具集成进行监控。
- **轻量级集成**：作为Nginx模块，无需额外进程，性能开销小，适用于高流量环境。
- **开源与社区支持**：基于BSD许可，社区活跃，提供规则更新和扩展。

## 主要功能
- **XSS防护**：检测并阻挡常见的XSS payload，如脚本注入、HTML标签滥用。
- **SQLi防护**：识别SQL注入尝试，包括经典注入、盲注等变体。
- **规则管理**：支持静态规则文件和动态学习，支持Lua脚本扩展高级功能。
- **模式切换**：学习模式（记录而不阻挡）、保护模式（实时阻挡），便于部署和测试。
- **自定义响应**：可配置返回自定义错误页面或重定向。
- **兼容性**：支持Nginx 0.7.x及以上版本，适用于各种Web应用场景，如PHP、Node.js等后端。

## 用法
1. **安装**：
   - 从GitHub克隆仓库：`git clone https://github.com/nbs-system/naxsi.git`。
   - 编译Nginx时添加NAXSI模块：`./configure --add-module=/path/to/naxsi/naxsi_src`。
   - 或使用预编译包（如Debian/Ubuntu的nginx-extras）。

2. **配置Nginx**：
   - 在nginx.conf中加载模块：`load_module modules/ngx_http_naxsi_module.so;`。
   - 在server块中启用NAXSI：
     ```
     location / {
         include /etc/nginx/naxsi.rules;
         naxsi_rules /etc/nginx/naxsi.rules;
     }
     ```
   - 创建规则文件（naxsi.rules），示例：
     ```
     ## 基本规则
     SecRuleEngine On
     SecDefaultAction "phase:2,log,deny,status:403"
     SecRule REQUEST_URI "@beginsWith /admin" "id:1000,phase:1,nolog,pass"
     ```

3. **学习模式部署**：
   - 设置`SecRuleEngine DetectionOnly`以记录流量而不阻挡。
   - 运行一段时间后，使用`naxsi_ui`工具分析日志生成规则：`naxsi_ui -f /var/log/nginx/access.log`。

4. **保护模式**：
   - 切换到`SecRuleEngine On`启用阻挡。
   - 监控日志`/var/log/nginx/naxsi.log`查看攻击事件。

5. **高级用法**：
   - 自定义分数阈值：`SecRule REQUEST_HEADERS:Content-Type "@contains application/x-www-form-urlencoded" "id:2000,phase:2,score:10"`.
   - 集成外部工具如Fail2Ban进行IP封禁。
   - 更新规则：定期从社区获取新规则集。

更多细节请参考项目文档和示例配置。