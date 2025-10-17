
---
title: minio-py
---

# MinIO Python客户端示例：获取对象

## 项目地址
[GitHub项目地址](https://github.com/minio/minio-py/blob/master/examples/get_object.py)

## 主要特性
- **MinIO Python客户端集成**：基于minio-py库，提供与MinIO对象存储服务的无缝交互，支持S3兼容的API。
- **对象获取功能**：专注于从MinIO存储桶中下载或读取对象，支持流式处理和元数据访问。
- **简单易用**：示例代码简洁，适合初学者快速上手MinIO的Python集成。
- **错误处理**：包含基本的异常捕获机制，确保操作的鲁棒性。

## 功能
- **连接MinIO服务**：通过端点、访问密钥和密钥初始化MinIO客户端。
- **获取对象**：从指定存储桶下载对象到本地文件，支持指定对象键（key）和存储桶名称。
- **流式读取**：允许以字节流形式获取对象内容，便于处理大文件或内存优化。
- **元数据支持**：可访问对象的元数据，如大小、修改时间等。

## 用法
1. **安装依赖**：首先安装minio-py库，使用pip命令：
   ```
   pip install minio
   ```

2. **代码示例**（基于项目文件）：
   ```python
   from minio import Minio
   from minio.error import S3Error

   # 初始化客户端
   client = Minio(
       "play.min.io",  # MinIO端点
       access_key="Q3AM3UQ867SPQQA43P2F",  # 访问密钥
       secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",  # 密钥
   )

   try:
       # 获取对象并保存到本地文件
       client.fget_object("my-bucket", "my-object", "local-file")
       print("对象下载成功")
   except S3Error as err:
       print(err)
   ```

3. **自定义用法**：
   - 替换端点、密钥和存储桶/对象名称以适应你的MinIO部署。
   - 对于流式获取，使用`client.get_object()`返回Response对象，然后读取其数据。
   - 适用于上传、删除等扩展操作，通过minio-py的其他方法实现。

此示例适用于开发环境测试，生产环境需配置安全的凭证。