---
title: testify
---


# stretchr/testify

> 项目地址：<https://github.com/stretchr/testify>

## 简介
stretchr/testify 是一个 Go 语言的测试工具包，旨在提供简洁、易于使用且强大的断言、测试套件和 mock 功能。它广泛用于单元测试、集成测试，并在 Go 社区被视为最常用的测试工具之一。

## 主要特性

| 组件 | 说明 |
|------|------|
| **Assert** | 断言函数，支持判断值等价、布尔表达式、字符串相似度、JSON 比对等。 |
| **Require** | 与 Assert 类似，但遇到失败立即停止当前测试。 |
| **Mock** | 简单易用的 mock 实现，支持期望调用、返回值、方法计数等。 |
| **Suite** | 基于 testify/suite 的测试套件支持，能初始化、共享状态、自动注册子测试。 |
| **TestTemplate** | 通过自定义模板来复用测试代码，提升可读性与复用性。 |
| **Testify-run** | 适配 Go 1.7+ 的 `t.Run` 功能，实现子测试的断言与 mock。 |

## 典型用例

### 1. 断言 (Assertions)

```go
import (
    "testing"
    "github.com/stretchr/testify/assert"
)

func TestSum(t *testing.T) {
    result := Sum(2, 3)
    assert.Equal(t, 5, result, "Sum(2,3) should be 5")
}
```

### 2. 必需断言 (Require)

```go
import (
    "testing"
    "github.com/stretchr/testify/require"
)

func TestGetUser(t *testing.T) {
    user, err := GetUser(42)
    require.NoError(t, err, "should not return error")
    require.NotNil(t, user, "user should be non-nil")
}
```

### 3.  Mock

```go
import (
    "testing"
    "github.com/stretchr/testify/mock"
)

type FooClientMock struct {
    mock.Mock
}

func (m *FooClientMock) FetchValue(id int) (int, error) {
    args := m.Called(id)
    return args.Int(0), args.Error(1)
}

func TestService(t *testing.T) {
    mockClient := new(FooClientMock)
    mockClient.On("FetchValue", 42).Return(100, nil)

    service := NewService(mockClient)
    result := service.DoSomething(42)

    assert.Equal(t, 100, result)
    mockClient.AssertExpectations(t)
}
```

### 4. 测试套件 (Test Suite)

```go
import (
    "testing"
    "github.com/stretchr/testify/suite"
)

type MySuite struct {
    suite.Suite
    db *MockDB
}

func (suite *MySuite) SetupTest() {
    suite.db = NewMockDB()
}

func (suite *MySuite) TestInsert() {
    err := suite.db.Insert("table", map[string]interface{}{"name":"Alice"})
    suite.NoError(err)
}

func TestRunMySuite(t *testing.T) {
    suite.Run(t, new(MySuite))
}
```

## 如何安装

```bash
go get github.com/stretchr/testify
```

## 结语
stretchr/testify 通过提供丰富的断言、mock 与测试套件，极大地简化了 Go 单元/集成测试的开发流程，提升代码质量与可维护性。其 API 设计简洁直观，几乎可以无缝集成到现有的 Go 测试框架中。