---
title: Logrus
---

# Logrus

Logrus 是一个结构化的 Go (golang) 日志库，完全兼容标准库日志器。

## 功能

- **结构化日志**：鼓励通过字段进行仔细的结构化日志记录，而不是冗长的不可解析的错误消息。
- **兼容性**：完全 API 兼容标准库日志器，可以轻松替换现有的 `log` 导入。
- **多种格式化器**：内置 TextFormatter 和 JSONFormatter，支持自定义格式化器。
- **钩子系统**：允许添加钩子来处理不同级别的日志，例如发送错误到异常跟踪服务或记录到多个位置。
- **日志级别**：支持 Trace、Debug、Info、Warning、Error、Fatal 和 Panic 七个级别。
- **字段支持**：使用 `WithFields` 添加结构化字段。
- **默认字段**：可以设置始终附加到日志语句的字段。
- **线程安全**：默认通过互斥锁保护并发写入，可以禁用以提高性能。
- **测试支持**：内置设施用于断言日志消息的存在。

## 用法

### 基本用法

最简单的使用方式是使用包级导出的日志器：

```go
package main

import "github.com/sirupsen/logrus"

func main() {
  logrus.WithFields(logrus.Fields{
    "animal": "walrus",
  }).Info("A walrus appears")
}
```

### 自定义配置

```go
package main

import (
  "os"
  log "github.com/sirupsen/logrus"
)

func init() {
  // 设置为 JSON 格式而不是默认的 ASCII 格式
  log.SetFormatter(&log.JSONFormatter{})

  // 输出到 stdout 而不是默认的 stderr
  log.SetOutput(os.Stdout)

  // 只记录警告级别或以上的日志
  log.SetLevel(log.WarnLevel)
}

func main() {
  log.WithFields(log.Fields{
    "animal": "walrus",
    "size":   10,
  }).Info("A group of walrus emerges from the ocean")

  log.WithFields(log.Fields{
    "omg":    true,
    "number": 122,
  }).Warn("The group's number increased tremendously!")

  log.WithFields(log.Fields{
    "omg":    true,
    "number": 100,
  }).Fatal("The ice breaks!")
}
```

### 创建日志器实例

```go
package main

import (
  "os"
  "github.com/sirupsen/logrus"
)

var logger = logrus.New()

func main() {
  logger.Out = os.Stdout

  logger.WithFields(logrus.Fields{
    "animal": "walrus",
    "size":   10,
  }).Info("A group of walrus emerges from the ocean")
}
```

### 使用字段

```go
logrus.WithFields(logrus.Fields{
  "event": event,
  "topic": topic,
  "key": key,
}).Fatal("Failed to send event")
```

### 默认字段

```go
requestLogger := logger.WithFields(logrus.Fields{"request_id": request_id, "user_ip": user_ip})
requestLogger.Info("something happened on that request")
```

### 钩子

```go
import (
  "log/syslog"
  "github.com/sirupsen/logrus"
  airbrake "gopkg.in/gemnasium/logrus-airbrake-hook.v2"
  logrus_syslog "github.com/sirupsen/logrus/hooks/syslog"
)

func init() {
  logrus.AddHook(airbrake.NewHook(123, "xyz", "production"))

  hook, err := logrus_syslog.NewSyslogHook("udp", "localhost:514", syslog.LOG_INFO, "")
  if err != nil {
    logrus.Error("Unable to connect to local syslog daemon")
  } else {
    logrus.AddHook(hook)
  }
}
```

### 日志级别

```go
logrus.Trace("Something very low level.")
logrus.Debug("Useful debugging information.")
logrus.Info("Something noteworthy happened!")
logrus.Warn("You should probably take a look at this.")
logrus.Error("Something failed but I'm not quitting.")
logrus.Fatal("Bye.")  // 调用 os.Exit(1)
logrus.Panic("I'm bailing.")  // 调用 panic()
```

设置级别：

```go
logrus.SetLevel(logrus.InfoLevel)
```

### 格式化器

- **TextFormatter**：在 TTY 上以颜色记录，否则为纯文本。
- **JSONFormatter**：以 JSON 格式记录字段。

自定义格式化器：

```go
type MyJSONFormatter struct{}

func (f *MyJSONFormatter) Format(entry *logrus.Entry) ([]byte, error) {
  serialized, err := json.Marshal(entry.Data)
  if err != nil {
    return nil, fmt.Errorf("Failed to marshal fields to JSON, %w", err)
  }
  return append(serialized, '\n'), nil
}

logrus.SetFormatter(new(MyJSONFormatter))
```

### 作为 io.Writer

```go
w := logger.Writer()
defer w.Close()

srv := http.Server{
  ErrorLog: log.New(w, "", 0),
}
```

### 测试

```go
import (
  "testing"
  "github.com/sirupsen/logrus"
  "github.com/sirupsen/logrus/hooks/test"
  "github.com/stretchr/testify/assert"
)

func TestSomething(t *testing.T) {
  logger, hook := test.NewNullLogger()
  logger.Error("Helloerror")

  assert.Equal(t, 1, len(hook.Entries))
  assert.Equal(t, logrus.ErrorLevel, hook.LastEntry().Level)
  assert.Equal(t, "Helloerror", hook.LastEntry().Message)
}
```
