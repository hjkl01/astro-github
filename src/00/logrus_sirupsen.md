# Logrus

## 功能介绍

Logrus 是一个结构化日志库，用于 Go (golang)，它与标准库日志器完全 API 兼容。Logrus 提供了多种日志级别（Trace、Debug、Info、Warn、Error、Fatal、Panic）、基于字段的结构化日志记录、自定义格式化器（JSON 和 Text）、以及可扩展的钩子用于与外部服务集成。该库默认是线程安全的，并提供灵活的配置选项，用于输出目的地、日志级别和格式化样式。

该库目前处于维护模式，专注于错误修复、安全补丁和性能改进，同时保持向后兼容性。它在 Go 生态系统中推广结构化日志方面发挥了重要作用，并继续在生产应用程序中广泛使用。Logrus 通过促进基于字段的日志记录而不是字符串插值来鼓励最佳实践，使日志更易于解析和发现，用于日志聚合系统。

## 基本用法

### 包级函数的基本日志记录

使用标准日志器实例进行快速结构化日志记录，并将字段附加到日志条目。

```go
package main

import (
	log "github.com/sirupsen/logrus"
)

func main() {
	// 简单消息日志记录
	log.Info("Application started")

	// 带字段的结构化日志记录
	log.WithFields(log.Fields{
		"animal": "walrus",
		"size":   10,
	}).Info("A group of walrus emerges from the ocean")

	// 添加错误字段
	err := performOperation()
	if err != nil {
		log.WithError(err).Error("Operation failed")
	}

	// 多种日志级别
	log.Debug("Debugging information")
	log.Warn("Warning message")
	log.Error("Error occurred but continuing")
	// log.Fatal("Critical error") // 调用 os.Exit(1)
	// log.Panic("Panic level")    // 调用 panic()
}

func performOperation() error {
	return nil
}
```

### 创建自定义日志器实例

创建和配置独立的日志器实例，为应用程序的不同部分设置自定义设置。

```go
package main

import (
	"os"
	"github.com/sirupsen/logrus"
)

func main() {
	// 创建新的日志器实例
	logger := logrus.New()

	// 配置输出目的地
	logger.SetOutput(os.Stdout)

	// 设置日志级别（仅记录此级别或以上的日志）
	logger.SetLevel(logrus.DebugLevel)

	// 配置格式化器
	logger.SetFormatter(&logrus.JSONFormatter{
		TimestampFormat: "2006-01-02 15:04:05",
		PrettyPrint:     true,
	})

	// 启用调用者报告（添加文件:行信息）
	logger.SetReportCaller(true)

	// 使用日志器
	logger.WithFields(logrus.Fields{
		"component": "database",
		"action":    "connect",
	}).Info("Database connection established")

	logger.Debug("This debug message will be logged")
	logger.Trace("This trace message will NOT be logged (below DebugLevel)")
}
```

### 日志级别和级别检查

设置和检查日志级别以控制详细程度，并有条件地执行昂贵的日志记录操作。

```go
package main

import (
	"github.com/sirupsen/logrus"
)

func main() {
	logger := logrus.New()
	logger.SetLevel(logrus.WarnLevel)

	// 这些将被记录（Warn、Error、Fatal、Panic）
	logger.Warn("This is a warning")
	logger.Error("This is an error")

	// 这些不会被记录（低于 WarnLevel）
	logger.Info("This won't appear")
	logger.Debug("Neither will this")

	// 在执行昂贵操作之前检查级别是否启用
	if logger.IsLevelEnabled(logrus.DebugLevel) {
		complexData := gatherDebugInfo() // 仅在启用调试时调用
		logger.WithField("debug_data", complexData).Debug("Debug info")
	}

	// 使用 LogFunction 进行延迟评估
	logger.DebugFn(func() []interface{} {
		// 此函数仅在启用 Debug 级别时执行
		return []interface{}{"Expensive debug computation:", expensiveOperation()}
	})

	// 获取当前级别
	currentLevel := logger.GetLevel()
	logger.Info("Current log level:", currentLevel.String())
}

func gatherDebugInfo() map[string]interface{} {
	return map[string]interface{}{"cpu": "90%", "memory": "2GB"}
}

func expensiveOperation() string {
	return "result"
}
```

### 使用上下文字段重用条目

创建带有持久字段的日志条目，以避免在多个日志语句中重复。

```go
package main

import (
	"context"
	"github.com/sirupsen/logrus"
	"time"
)

func main() {
	logger := logrus.New()

	// 创建带有公共字段的条目
	requestLogger := logger.WithFields(logrus.Fields{
		"request_id": "abc-123",
		"user_id":    "user-456",
		"ip":         "192.168.1.1",
	})

	// 重用条目 - 所有日志将包含公共字段
	requestLogger.Info("Request received")
	requestLogger.Debug("Parsing request body")
	requestLogger.Info("Processing request")
	requestLogger.Info("Request completed")

	// 向现有条目添加更多字段
	requestLogger.WithField("duration_ms", 150).Info("Response sent")

	// 向条目添加上下文
	ctx := context.Background()
	contextLogger := logger.WithContext(ctx)
	contextLogger.Info("Log with context")

	// 覆盖时间戳
	customTimeLogger := logger.WithTime(time.Date(2023, 10, 9, 10, 0, 0, 0, time.UTC))
	customTimeLogger.Info("Log with custom timestamp")
}
```

### JSON 格式化器配置

为日志聚合系统配置 JSON 输出，具有自定义字段名称和格式化选项。

```go
package main

import (
	"os"
	"github.com/sirupsen/logrus"
)

func main() {
	logger := logrus.New()

	// 基本 JSON 格式化器
	logger.SetFormatter(&logrus.JSONFormatter{
		TimestampFormat:   "2006-01-02T15:04:05.000Z07:00",
		DisableTimestamp:  false,
		DisableHTMLEscape: true,
		PrettyPrint:       false,
	})

	// 具有自定义字段名称的 JSON 格式化器（用于 ELK、Splunk 等）
	logger.SetFormatter(&logrus.JSONFormatter{
		FieldMap: logrus.FieldMap{
			logrus.FieldKeyTime:  "@timestamp",
			logrus.FieldKeyLevel: "@level",
			logrus.FieldKeyMsg:   "@message",
			logrus.FieldKeyFunc:  "@caller",
		},
	})

	// 具有嵌套数据键的 JSON 格式化器
	logger.SetFormatter(&logrus.JSONFormatter{
		DataKey: "fields", // 所有自定义字段嵌套在 "fields" 下
	})

	logger.WithFields(logrus.Fields{
		"user":   "john",
		"action": "login",
	}).Info("User logged in")

	// 带调用者美化器的 JSON 格式化器
	logger.SetReportCaller(true)
	logger.SetFormatter(&logrus.JSONFormatter{
		CallerPrettyfier: func(f *logrus.Frame) (string, string) {
			return f.Function, fmt.Sprintf("%s:%d", f.File, f.Line)
		},
	})
}
```

### Text 格式化器配置

配置人类可读的文本输出，具有颜色、时间戳和字段排序选项。

```go
package main

import (
	"github.com/sirupsen/logrus"
	"os"
)

func main() {
	logger := logrus.New()
	logger.SetOutput(os.Stdout)

	// 禁用颜色的基本文本格式化器
	logger.SetFormatter(&logrus.TextFormatter{
		DisableColors:   true,
		FullTimestamp:   true,
		TimestampFormat: "2006-01-02 15:04:05",
	})

	// 带颜色自定义的文本格式化器
	logger.SetFormatter(&logrus.TextFormatter{
		ForceColors:            true,  // 即使没有 TTY 也强制颜色
		DisableTimestamp:       false,
		DisableLevelTruncation: true,  // 显示完整级别名称（不截断为 4 个字符）
		PadLevelText:           true,  // 填充级别文本以对齐
		DisableSorting:         false, // 按字母顺序排序字段
		QuoteEmptyFields:       true,  // 引用空字段值
	})

	// 自定义字段排序
	logger.SetFormatter(&logrus.TextFormatter{
		SortingFunc: func(keys []string) {
			// 自定义排序逻辑
			sort.Strings(keys)
		},
	})

	// 带自定义字段名称的文本格式化器
	logger.SetFormatter(&logrus.TextFormatter{
		FieldMap: logrus.FieldMap{
			logrus.FieldKeyTime:  "timestamp",
			logrus.FieldKeyLevel: "severity",
			logrus.FieldKeyMsg:   "message",
		},
	})

	logger.WithFields(logrus.Fields{
		"component": "api",
		"method":    "GET",
		"path":      "/users",
	}).Info("API request processed")
}
```

### 创建和使用钩子

实现自定义钩子，根据日志级别将日志发送到外部服务。

```go
package main

import (
	"fmt"
	"github.com/sirupsen/logrus"
)

// 将错误发送到警报服务的自定义钩子
type AlertHook struct {
	alertService *AlertService
}

func (hook *AlertHook) Levels() []logrus.Level {
	// 仅为 Error、Fatal 和 Panic 级别触发
	return []logrus.Level{
		logrus.ErrorLevel,
		logrus.FatalLevel,
		logrus.PanicLevel,
	}
}

func (hook *AlertHook) Fire(entry *logrus.Entry) error {
	// 发送警报到外部服务
	message := fmt.Sprintf("[%s] %s", entry.Level, entry.Message)
	return hook.alertService.SendAlert(message, entry.Data)
}

type AlertService struct{}

func (a *AlertService) SendAlert(msg string, fields logrus.Fields) error {
	fmt.Printf("ALERT: %s (fields: %v)\n", msg, fields)
	return nil
}

func main() {
	logger := logrus.New()

	// 添加自定义钩子
	alertService := &AlertService{}
	logger.AddHook(&AlertHook{alertService: alertService})

	// Info 不会触发钩子
	logger.Info("This is just info")

	// Error 将触发钩子
	logger.WithFields(logrus.Fields{
		"error_code": "DB_CONNECTION_FAILED",
		"retry":      3,
	}).Error("Database connection failed")

	// 可以添加多个钩子
	logger.AddHook(&MetricsHook{})
}

type MetricsHook struct{}

func (h *MetricsHook) Levels() []logrus.Level {
	return logrus.AllLevels
}

func (h *MetricsHook) Fire(entry *logrus.Entry) error {
	// 增加指标计数器
	fmt.Printf("Metrics: logged at level %s\n", entry.Level)
	return nil
}
```

### 使用日志器作为 io.Writer

将日志器转换为 io.Writer，以与标准库和第三方包集成。

```go
package main

import (
	"log"
	"net/http"
	"github.com/sirupsen/logrus"
)

func main() {
	logger := logrus.New()
	logger.SetFormatter(&logrus.JSONFormatter{})

	// 获取 INFO 级别的写入器
	writer := logger.Writer()
	defer writer.Close()

	// 替换标准库日志器
	stdLogger := log.New(writer, "", 0)
	stdLogger.Println("This goes through logrus")

	// 与 HTTP 服务器错误日志一起使用
	server := &http.Server{
		Addr:     ":8080",
		ErrorLog: stdLogger,
	}

	// 获取特定级别的写入器
	errorWriter := logger.WriterLevel(logrus.ErrorLevel)
	defer errorWriter.Close()

	errorWriter.Write([]byte("Error message\n"))
	errorWriter.Write([]byte("Another error\n"))

	// 带字段
	entry := logger.WithFields(logrus.Fields{
		"service": "http-server",
		"port":    8080,
	})
	serverWriter := entry.WriterLevel(logrus.WarnLevel)
	defer serverWriter.Close()

	customServer := &http.Server{
		Addr:     ":8080",
		ErrorLog: log.New(serverWriter, "", 0),
	}

	_ = server
	_ = customServer
}
```

### 使用空日志器和测试钩子进行测试

使用测试钩子在单元测试中捕获和断言日志输出。

```go
package main

import (
	"testing"
	"github.com/sirupsen/logrus"
	"github.com/sirupsen/logrus/hooks/test"
	"github.com/stretchr/testify/assert"
)

func processUserLogin(logger *logrus.Logger, username string) error {
	if username == "" {
		logger.Error("Username cannot be empty")
		return fmt.Errorf("invalid username")
	}

	logger.WithField("username", username).Info("User logged in")
	return nil
}

func TestUserLoginSuccess(t *testing.T) {
	// 创建带测试钩子的空日志器
	logger, hook := test.NewNullLogger()

	// 调用函数
	err := processUserLogin(logger, "john")

	// 断言无错误
	assert.NoError(t, err)

	// 断言日志条目
	assert.Equal(t, 1, len(hook.Entries))
	assert.Equal(t, logrus.InfoLevel, hook.LastEntry().Level)
	assert.Equal(t, "User logged in", hook.LastEntry().Message)
	assert.Equal(t, "john", hook.LastEntry().Data["username"])

	// 为下一次测试重置
	hook.Reset()
	assert.Nil(t, hook.LastEntry())
}

func TestUserLoginFailure(t *testing.T) {
	logger, hook := test.NewNullLogger()

	err := processUserLogin(logger, "")

	assert.Error(t, err)
	assert.Equal(t, 1, len(hook.Entries))
	assert.Equal(t, logrus.ErrorLevel, hook.LastEntry().Level)
	assert.Equal(t, "Username cannot be empty", hook.LastEntry().Message)
}

func TestWithExistingLogger(t *testing.T) {
	logger := logrus.New()
	hook := test.NewLocal(logger)

	logger.Info("Test message")

	assert.Equal(t, 1, len(hook.Entries))
	assert.Equal(t, "Test message", hook.LastEntry().Message)
}
```

### 致命处理程序和退出行为

注册处理程序以在 Fatal 级别退出应用程序之前执行清理任务。

```go
package main

import (
	"fmt"
	"github.com/sirupsen/logrus"
	"os"
	"time"
)

var shutdownComplete = make(chan bool)

func main() {
	logger := logrus.New()

	// 为清理注册致命处理程序
	logrus.RegisterExitHandler(func() {
		fmt.Println("Graceful shutdown initiated...")

		// 关闭数据库连接
		closeDatabaseConnections()

		// 刷新指标
		flushMetrics()

		// 等待飞行中的请求
		time.Sleep(1 * time.Second)

		fmt.Println("Shutdown complete")
		shutdownComplete <- true
	})

	// 注册多个处理程序（以相反顺序执行）
	logrus.RegisterExitHandler(func() {
		fmt.Println("Final cleanup handler")
	})

	// 为高性能场景禁用锁定
	logger.SetNoLock() // 仅当不需要线程安全时

	// Fatal 将调用注册的处理程序，然后 os.Exit(1)
	// logger.Fatal("Critical error occurred")

	// 用于测试的自定义退出函数
	logger.ExitFunc = func(code int) {
		fmt.Printf("Would exit with code: %d\n", code)
		// 在测试中不实际退出
	}

	logger.Fatal("Test fatal without exit")
}

func closeDatabaseConnections() {
	fmt.Println("Closing database connections...")
}

func flushMetrics() {
	fmt.Println("Flushing metrics...")
}
```

### 线程安全和性能优化

为高吞吐量场景配置线程安全和性能设置。

```go
package main

import (
	"bytes"
	"github.com/sirupsen/logrus"
	"os"
	"sync"
)

// 性能自定义缓冲池
type CustomBufferPool struct {
	pool *sync.Pool
}

func (p *CustomBufferPool) Get() *bytes.Buffer {
	return p.pool.Get().(*bytes.Buffer)
}

func (p *CustomBufferPool) Put(buf *bytes.Buffer) {
	buf.Reset()
	p.pool.Put(buf)
}

func main() {
	logger := logrus.New()

	// 场景 1：使用默认互斥锁的线程安全（默认）
	logger.Info("Thread-safe logging")

	// 场景 2：为单线程或预同步场景禁用锁定
	// 安全条件：无钩子 OR 写入 O_APPEND 文件 < 4KB OR 自定义同步
	file, _ := os.OpenFile("app.log", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
	logger.SetOutput(file)
	logger.SetNoLock() // 禁用内部互斥锁

	// 场景 3：自定义缓冲池以减少分配
	customPool := &CustomBufferPool{
		pool: &sync.Pool{
			New: func() interface{} {
				return new(bytes.Buffer)
			},
		},
	}
	logger.SetBufferPool(customPool)

	// 场景 4：使用 LogFn 的延迟日志评估（仅在启用级别时评估）
	logger.SetLevel(logrus.WarnLevel)

	logger.InfoFn(func() []interface{} {
		// 此昂贵操作不会执行（Info < Warn）
		data := expensiveDataGathering()
		return []interface{}{"Expensive data:", data}
	})

	logger.WarnFn(func() []interface{} {
		// 此操作会执行（Warn >= Warn）
		return []interface{}{"Warning with lazy evaluation"}
	})

	// 场景 5：原子替换钩子
	newHooks := make(logrus.LevelHooks)
	oldHooks := logger.ReplaceHooks(newHooks)
	_ = oldHooks // 如需要恢复
}

func expensiveDataGathering() map[string]interface{} {
	// 模拟昂贵操作
	return map[string]interface{}{"key": "value"}
}
```

## 总结和集成模式

Logrus 专为需要结构化、可解析日志的生产应用程序而设计，具有最小的配置开销。常见用例包括具有一致字段格式的微服务日志记录、通过 JSON 格式化器与日志聚合平台（ELK、Splunk、Datadog）集成，以及通过钩子将关键日志发送到监控服务。库在需要上下文日志记录的场景中表现出色，其中请求 ID、用户 ID 或跟踪 ID 需要附加到请求生命周期内的所有日志条目，使分布式系统调试显著更容易。

集成模式通常涉及在应用程序启动时创建配置有适当格式化器、钩子和输出目的地的单例日志器实例。对于 HTTP 服务，中件可以创建带有跟踪字段的每请求日志器条目，然后通过请求上下文传递。使用空日志器和测试钩子简化测试，以验证日志输出而无需实际 I/O。性能关键应用程序可以禁用锁定并使用自定义缓冲池，而钩子通过将不同日志级别路由到不同后端（错误到 Sentry、指标到 StatsD、调试日志到文件）来实现关注点分离，而不会用基础设施问题污染业务逻辑。
