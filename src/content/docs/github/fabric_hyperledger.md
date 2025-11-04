
---
title: fabric
---

# Hyperledger Fabric

> 官方项目地址: <https://github.com/hyperledger/fabric>

## 一、项目概述  
Hyperledger Fabric 是一个模块化、可插拔的企业级区块链框架，专为需要隐私保护、可扩展性和高性能的分布式账本解决方案而设计。它提供了多通道、链码（智能合约）以及可插拔权限模型，支持在私有网络中安全进行业务交易。

## 二、主要特性  

| 特性 | 说明 |
|------|------|
| **院区隔离（Channels）** | 独立的账本子网络，每个通道只对授权成员可见，保证业务数据隔离 |
| **可插拔排序/共识** | 默认采用 Raft、Kafka；可自行实现 PBFT、Solo 等共识机制 |
| **链码模型** | Chaincode 采用 Go/Java/Node.js 等多语言支持，支持链码生命周期管理（安装、批准、提交) |
| **隐私与配额** | 私有数据集合（Private Data Collections）可对特定成员可见，支持配额门限 |
| **多租户（MSp）** | 对等节点可加入不同组织，CSP、TLS 证书实现身份验证 |
| **智能合约事件** | 通过质询/订阅机制告知链码状态变更，支持链码版本回滚 |
| **命令行工具** | `peer`, `configtxgen`, `cryptogen` 等，为链码部署和网络配置提供 CLI |
| **安全性** | 对等节点、管理员和链码均使用 x.509 证书，内置 TLS 与访问控制 |
| **多版本并行** | 支持链码的多版本并发（Peer 兼容）以实现无缝升级 |
| **桌面调试** | Dev Sandbox, Minifabric 等工具实现快速本地实验 |
| **高级特性** | Lifecycles v2.0、水平链码扩展、Chaincode Lifecycle、Fabric SDK 等 |

## 三、核心功能模块  

1. **核心区块链结构**  
   - `orderer/`：排序服务实现，可选 Raft / Kafka  
   - `peer/`：区块生产者，支持链码执行、日志节点、隐私集合管理  
2. **数据管理**  
   - `ledger/`：LevelDB/Go-PoV 等实现，支持区块、状态树  
3. **身份认证**  
   - `msp/`：多方身份管理与证书颁发，支持 ECDSA、RSA 等  
4. **链码生命周期**  
   - `chaincode/`：链码安装、批准、提交的完整流程  
5. **通道配置**  
   - `configtx/`：通道配置文件与链码更新工具  
6. **SDK**  
   - Go / Node.js / Java / .NET、Kotlin 等 SDK，支持应用程序快速集成  

## 四、用法

### 1. 环境准备  
```bash
# 安装 Docker 与 Docker Compose
sudo apt-get install docker docker-compose
docker --version
docker-compose --version
```

### 2. 获取源码  
```bash
git clone https://github.com/hyperledger/fabric.git
cd fabric
```

### 3. 生成网络材料  
```bash
# 生成 MSP 与证书（示例）
cd ./cryptogen
./cryptogen generate --config=./crypto-config.yaml
```

### 4. 创建通道  
```bash
cd ..
# 生成通道配置
./configtxgen -profile ThreeOrgsOrdererGenesis -outputBlock genesis.block
./configtxgen -profile TwoOrgsChannel -outputCreateChannelTx channel.tx -channelID mychannel

# 覆盖 recovery  
./orderer genesis.block mychannel
```

### 5. 启动网络  
```bash
# 通过 docker-compose 启动
set -x
export FABRIC_CFG_PATH=${PWD}/config/
./byfn.sh up
```

### 6. 安装并实例化链码  
```bash
# 通过 CLI
peer chaincode install -n mycc -v 1.0 -p github.com/chaincode/chaincode_example02/go
peer chaincode instantiate -o orderer.example.com:7050 -C mychannel -n mycc -v 1.0 -c '{"Args":["init","a","100","b","50"]}' -P "AND ('Org1.peer','Org2.peer')"
```

### 7. 调用与查询  
```bash
peer chaincode invoke -o orderer.example.com:7050 -C mychannel -n mycc -c '{"Args":["invoke","a","b","10"]}'
peer chaincode query -C mychannel -n mycc -c '{"Args":["query","a"]}'
```

### 8. 升级链码（v2.x 流程）  
```bash
# 1. 提交链码
peer lifecycle chaincode package mycc.tar.gz --path github.com/chaincode/chaincode_example02/go --lang golang --label mycc_1
peer lifecycle chaincode install mycc.tar.gz
# 2. 评议批准
peer lifecycle chaincode approvefcn ...
```

## 五、快速入门资源  

- 官方学习资料: [Hyperledger Fabric Docs](https://hyperledger-fabric.readthedocs.io/zh-cn/latest/index.html)  
- 样例项目: [FabCar](https://github.com/hyperledger/fabric-samples/tree/master/chaincode-go/example02)  
- 社区支持: #fabric 之 Slack 频道、邮件列表，GitHub Discussions  

以上内容构成了 Hyperledger Fabric 的主要特性、功能与基本使用流程，足以帮助你快速开始构建私有链网络与智能合约。