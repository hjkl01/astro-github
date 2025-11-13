---
title: gumroad
---

# Gumroad

## 功能

Gumroad 是一个电子商务平台，使创作者能够直接向消费者销售产品。该平台允许用户销售数字产品、物理商品等，并提供销售分析和客户管理功能。

主要功能包括：

- 产品销售和分发
- 支付处理
- 客户管理和订阅
- 销售分析和报告
- 自定义商店页面

## 用法

### 安装和设置

1. 克隆仓库：

   ```
   git clone https://github.com/antiwork/gumroad.git
   cd gumroad
   ```

2. 安装依赖：
   - Ruby 和 Node.js 版本见 `.ruby-version` 和 `.node-version`
   - 安装 Ruby gems：`bundle install`
   - 安装 Node.js 依赖：`npm install`

3. 配置环境：
   - 复制 `.env.example` 到 `.env` 并填写必要凭据
   - 设置 S3 存储桶（可选，用于文件上传）

4. 启动服务：
   - 启动 Docker 服务：`make local`
   - 设置数据库：`bin/rails db:prepare`
   - 启动应用：`bin/dev`

5. 访问应用：`https://gumroad.dev`

### 开发

- 登录测试账户：`seller@gumroad.com` / `password`（2FA 码：000000）
- 重置 Elasticsearch 索引：运行 `DevTools.delete_all_indices_and_reindex_all` 在 Rails 控制台中
- 推送通知：`INITIALIZE_RPUSH_APPS=true bundle exec rpush start -e development -f`

更多详情见 [GitHub 仓库](https://github.com/antiwork/gumroad)。
