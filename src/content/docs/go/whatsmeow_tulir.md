---
title: whatsmeow
---

## 项目简介

whatsmeow 是一个用 Go 语言编写的库，用于与 WhatsApp Web 多设备 API 进行交互。它允许开发者通过编程方式与 WhatsApp 进行通信，实现自动化消息发送、接收和管理等功能。

## 主要功能

- **消息发送和接收**：支持向私聊和群组发送文本和媒体消息，并接收所有消息。
- **群组管理**：创建和管理群组，接收群组变更事件，通过邀请消息加入群组，使用和创建邀请链接。
- **通知和回执**：发送和接收打字通知、送达回执和已读回执。
- **应用状态管理**：读取和写入联系人列表、聊天置顶/静音状态等应用状态。
- **消息重试**：处理消息解密失败时的重试回执。
- **状态消息**：实验性支持发送状态消息（可能不适用于大型联系人列表）。

## 未实现功能

- 发送广播列表消息（WhatsApp Web 也不支持此功能）。
- 通话功能。

## 用法

1. **安装**：使用 Go 模块安装库。

   ```
   go get go.mau.fi/whatsmeow
   ```

2. **基本使用**：参考 [godoc 文档](https://pkg.go.dev/go.mau.fi/whatsmeow) 获取详细 API 文档。以下是一个简单的示例：

   ```go
   package main

   import (
       "context"
       "log"
       "os"
       "os/signal"
       "syscall"

       "go.mau.fi/whatsmeow"
       "go.mau.fi/whatsmeow/store/sqlstore"
       "go.mau.fi/whatsmeow/types/events"
       waLog "go.mau.fi/whatsmeow/util/log"
   )

   func main() {
       dbLog := waLog.Stdout("Database", "DEBUG", true)
       container, err := sqlstore.New("sqlite3", "file:examplestore.db?_foreign_keys=on", dbLog)
       if err != nil {
           panic(err)
       }
       deviceStore, err := container.GetFirstDevice()
       if err != nil {
           panic(err)
       }
       clientLog := waLog.Stdout("Client", "DEBUG", true)
       client := whatsmeow.NewClient(deviceStore, clientLog)
       client.AddEventHandler(func(evt interface{}) {
           switch v := evt.(type) {
           case *events.Message:
               log.Printf("Received message: %s", v.Message.GetConversation())
           }
       })

       if client.Store.ID == nil {
           qrChan, _ := client.GetQRChannel(context.Background())
           err = client.Connect()
           if err != nil {
               panic(err)
           }
           for evt := range qrChan {
               if evt.Event == "code" {
                   // 显示 QR 码
               } else {
                   log.Printf("QR channel result: %s", evt.Event)
               }
           }
       } else {
           err = client.Connect()
           if err != nil {
               panic(err)
           }
       }

       c := make(chan os.Signal, 1)
       signal.Notify(c, os.Interrupt, syscall.SIGTERM)
       <-c

       client.Disconnect()
   }
   ```

3. **讨论和支持**：加入 Matrix 房间 [#whatsmeow:maunium.net](https://matrix.to/#/#whatsmeow:maunium.net) 获取帮助，或在 GitHub Discussions 的 [WhatsApp protocol Q&A](https://github.com/tulir/whatsmeow/discussions/categories/whatsapp-protocol-q-a) 部分提问协议相关问题。

## 许可证

该项目采用 MPL-2.0 许可证。
