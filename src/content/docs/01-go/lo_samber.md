
---
title: lo
---

下面为您提供需要保存到 `src/content/docs/00/lo_samber.md` 的 Markdown 内容。请直接复制后保存。

```markdown
# samber/lo

- **项目地址**: https://github.com/samber/lo  
- **仓库状态**: 2018-2025 已持续维护，支持 Go 1.14+  
- **许可证**: MIT

## 简介

`samber/lo` 是一套功能丰富、类型安全且兼容 Go 泛型（Go 1.18+）的工具库，灵感来自于 JavaScript 的 Lodash。它提供了多种集合、数组、字符串、对象、函数、数学等实用函数，帮助开发者轻松完成常见任务。

## 主要特性

| 领域 | 典型功能 |
|-----|----------|
| **数组/切片** | `Filter`, `Map`, `Reduce`, `Flatten`, `Chunk`, `Zip`, `Concat`, `Unique` |
| **集合** | `Values`, `Keys`, `CountBy`, `GroupBy`, `SortedUniq`, `Intersection`, `Difference` |
| **字符串** | `Trim`, `TrimPrefix`, `TrimSuffix`, `Lpad`, `Rpad`, `Ascii`, `Contains`, `StartsWith`, `EndsWith` |
| **对象** | `Pick`, `Omit`, `Has`, `Merge`, `Clone`, `DeepClone`, `ValueBy` |
| **函数** | `Once`, `OnceAsync`, `Throttle`, `Debounce`, `Memoize`, `Currying` |
| **数学** | `Min`, `Max`, `Clamp`, `InRange`, `Random`, `Sum`, `Avg` |
| **日期/时间** | `Now`, `Format`, `Add`, `Sub`, `UnixToTime` |
| **类型工具** | `IsNil`, `IsZero`, `As`, ` *所列功能仅为核心示例，实际 API 完整度超出 100+ 函数。*

## 使用方式

1. **安装**

   ```bash
   go get -u github.com/samber/lo
   ```

2. **引入**

   ```go
   import "github.com/samber/lo"
   ```

3. **典型示例**

   ```go
   // 过滤、映射、求和
   nums := []int{1, 2, 3, 4, 5}
   result := lo.Reduce(
       lo.Filter(lo.Map(nums, func(n int, _ int) int { return n * n }), func(n int, _ int) bool { return n%2 == 0 }),
       func(total, v int, _ int) int { return total + v }, 0,
   )   // result == 20  (4 + 16)

   // 字符串处理
   s := lo.CamelCase("hello world example")   // "helloWorldExample"

   // 对象合并
   type User struct{ Name string; Age int }
   u1 := User{Name: "Alice", Age: 30}
   u2 := User{Name: "Bob"}
   merged := lo.Merge(u1, u2)   // User{Name: "Bob", Age: 30}
   ```

4. **泛型支持**

   ```go
   type Point[T any] struct{ X, Y T }
   pts := []Point[int]{{1, 2}, {3, 4}}
   xs := lo.Map(pts, func(p Point[int], _ int) int { return p.X })
   // xs == []int{1, 3}
   ```

5. **异步与容错**

   ```go
   // 只执行一次
   once := lo.Once(func() { fmt.Println("executed") })
   once()
   once()  // 无输出
   ```

## 文档与参考

- 官方文档: https://pkg.go.dev/github.com/samber/lo  
- 代码示例: https://github.com/samber/lo/tree/main/examples  
- 贡献指南: https://github.com/samber/lo/blob/master/CONTRIBUTING.md  
- 许可证: MIT

---

> 如果在使用中遇到任何问题，欢迎提交 issue 或 PR。祝编码愉快！
