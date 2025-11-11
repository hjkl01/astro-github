---
title: luci-app-easytier
---

# luci-app-easytier

## 项目简介

luci-app-easytier 是 OpenWrt 系统中的 EasyTier 安装包，提供 IPK 和 APK 格式的安装包。它是一个 LuCI 应用，用于在 OpenWrt 路由器上安装和配置 EasyTier VPN 工具。

## 功能

- 提供 OpenWrt 路由器上的 EasyTier VPN 集成
- 支持通过 LuCI 界面进行配置和管理
- 兼容多种 OpenWrt 版本和架构
- 提供自动编译和发布工作流

## 用法

### 依赖

在使用前，需要先安装 `kmod-tun` 内核模块。

### 快速开始

1. Fork 并克隆本项目到你的 GitHub 账户。
2. 修改 `.github/workflows/build.yml` 文件，在 `jobs.build.strategy` 中配置所需的架构 (arch) 和 SDK 版本。
   - 建议只保留需要的架构以加速编译。
   - SDK 可以选择 SNAPSHOT 后缀的 APK 包或 openwrt-22.03 的 IPK 包，根据你的 OpenWrt 版本调整。
3. 在 Actions 中手动触发编译流程，确保填写 release 信息以发布构建结果。

### 安装方法

#### 使用 IPK 包 (适用于旧版 OpenWrt)

```bash
# 上传 IPK 文件到 OpenWrt 的 /tmp/tmp 目录
opkg install /tmp/tmp/luci-app-easytier_all.ipk
```

#### 使用 APK 包 (适用于新版 OpenWrt)

```bash
# 如果出现证书验证问题，使用 --allow-untrusted 选项
apk add --allow-untrusted /tmp/tmp/luci-app-easytier.apk
```

#### 卸载

```bash
opkg remove luci-app-easytier
```

#### 更新版本

1. 先卸载旧版本：`opkg remove luci-app-easytier`
2. 安装新版本 IPK 包
3. 在 LuCI 管理界面中关闭插件，修改参数后重新应用并保存
4. 如果安装后 LuCI 界面不显示 EasyTier，请注销登录或重新打开浏览器窗口

**注意**：此 LuCI 应用不包含 EasyTier 二进制程序，需要在 LuCI 界面中手动上传二进制文件。

### 编译方法

#### 下载 OpenWrt SDK

```bash
# 下载并解压 SDK (以 rockchip/armv8 为例)
wget -qO /opt/sdk.tar.xz https://downloads.openwrt.org/releases/22.03.5/targets/rockchip/armv8/openwrt-sdk-22.03.5-rockchip-armv8_gcc-11.2.0_musl.Linux-x86_64.tar.xz
tar -xJf /opt/sdk.tar.xz -C /opt
```

#### 编译步骤

```bash
cd /opt/openwrt-sdk*/package
# 克隆项目到 SDK 的 package 目录
git clone https://github.com/EasyTier/luci-app-easytier.git /opt/luci-app-easytier
cp -R /opt/luci-app-easytier/luci-app-easytier .

cd /opt/openwrt-sdk*
# 更新 feeds 并创建默认配置
./scripts/feeds update -a
make defconfig

# 编译 luci-app-easytier 包
make package/luci-app-easytier/compile V=s -j1

# 编译完成后，IPK 文件位于 /opt/openwrt-sdk*/bin/packages/aarch64_generic/base
cd /opt/openwrt-sdk*/bin/packages/aarch64_generic/base
mv *.ipk /opt/luci-app-easytier_all.ipk
```

#### 故障排除

如果在系统日志中出现 `luci.util.pcdata() has been replaced by luci.xml.pcdata()` 错误，可以使用以下命令修复：

```bash
sed -i 's/util.pcdata/xml.pcdata/g' /usr/lib/lua/luci/model/cbi/easytier.lua
```

## 相关链接

- [GitHub 仓库](https://github.com/EasyTier/luci-app-easytier)
- [EasyTier 主项目](https://github.com/EasyTier/EasyTier)
