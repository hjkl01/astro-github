---
title: miniob
---


# MiniOB - OceanBase 轻量化实现

**项目地址**  
<https://github.com/oceanbase/miniob>

## 主要特性
- **内存数据库**：所有数据以内存方式存储，启动速度快，适合快速原型和单元测试。  
- **完整 SQL 语法支持**：基本的 `SELECT / INSERT / UPDATE / DELETE / CREATE / DROP / ALTER` 等 DDL/DML。  
- **事务与并发**：提供 `BEGIN/COMMIT/ROLLBACK`，并行查询的读写隔离保证。  
- **与 OceanBase 兼容**：通过兼容的网络协议与 OceanBase 进行互操作，可在不改动客户端的前提下切换到 MiniOB 进行调试。  
- **简易配置**：不需要安装数据库引擎，直接运行 jar 包即可。  
- **可嵌入应用**：提供 Java API，可在应用内嵌入 MiniOB 模块进行单元测试或开发。  

## 功能概览
| 功能 | 简述 |
|------|------|
| **内存表与索引** | 支持普通表、主键索引、唯一索引等。 |
| **事务管理** | 支持多事务隔离级别（Read Uncommitted / Read Committed / Repeatable Read / Serializable）。 |
| **日志与恢复** | 仅限内存，重启后数据清空，但可配置磁盘 WAL（Write‑Ahead Log）以实现持久化。 |
| **网络协议** | 支持 [OceanBase Binary Protocol](https://docs.oceanbase.com/) 规格，可被 OceanBase 官方客户端直接访问。 |
| **CLI 调试工具** | 通过命令行交互，执行 SQL 并查看结果。 |
| **API 接口** | 提供 JDBC、RESTful API 两种访问方式。 |

## 用法示例

### 1. 运行 MiniOB
```bash
# 下载并解压
wget https://github.com/oceanbase/miniob/releases/latest/download/miniob.jar

# 启动服务器（默认端口 2881）
java -jar miniob.jar
```

### 2. 通过 JDBC 连接
```java
String url = "jdbc:oceanbase://localhost:2881/testdb";
Connection conn = DriverManager.getConnection(url, "root", "");

Statement stmt = conn.createStatement();
stmt.execute("CREATE TABLE t_user(id INT PRIMARY KEY, name VARCHAR(50));");
stmt.execute("INSERT INTO t_user VALUES(1, 'Alice'), (2, 'Bob');");
ResultSet rs = stmt.executeQuery("SELECT * FROM t_user;");
while (rs.next()) {
    System.out.printf("id=%d, name=%s%n", rs.getInt("id"), rs.getString("name"));
}
conn.close();
```

### 3. 使用 REST Client（可选）
```bash
# 终端执行
curl -X POST http://localhost:2881/restapi \
     -H "Content-Type: application/json" \
     -d '{"sql":"SELECT * FROM t_user"}'
```

## 快速开始

1. **创建数据库**  
   ```
   CREATE DATABASE testdb;
   USE testdb;
   ```

2. **定义表**  
   ```
   CREATE TABLE t_book (
       id INT PRIMARY KEY,
       title VARCHAR(100),
       author VARCHAR(50),
       published_year INT
   );
   ```

3. **插入数据**  
   ```
   INSERT INTO t_book VALUES (1, 'The Little Prince', 'Antoine de Saint-Exupéry', 1943);
   INSERT INTO t_book VALUES (2, '1984', 'George Orwell', 1949);
   ```

4. **查询**  
   ```
   SELECT * FROM t_book WHERE published_year >= 1940;
   ```

5. **事务操作**  
   ```
   BEGIN TRANSACTION;
   UPDATE t_book SET title = 'Animal Farm' WHERE id = 2;
   ROLLBACK;   -- 或 COMMIT;
   ```

---
**注意**  
- MiniOB 目前仅适用于开发与测试阶段，**不建议**在生产环境中使用。  
- 由于是内存数据库，重启后所有数据将丢失（除非开启 WAL 持久化）。  
- 对 OceanBase 的协议实现虽已兼容但仍处于*稳定*测试阶段，出现细节不一致时请参考官方文档。  
> 了解更多信息请访问项目主页并查看 README 和官方 Wiki。  
```  
(保存为 `src/content/docs/00/miniob_oceanbase.md`)