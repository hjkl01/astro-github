
---
title: blender-mcp
---


# Blender MCP Add‑on (ahujasid)

**GitHub 项目地址**  
<https://github.com/ahujasid/blender-mcp>

## 主要特性

| 功能 | 说明 |
|------|------|
| **MCP 导入/导出** | 支持 `.mcp` 模型文件的导入与导出，便于与 Minecraft Mod 生态集成。 |
| **UV 与材质映射** | 保留 UV 坐标与材质信息，导出时自动生成对应的材质表。 |
| **顶点颜色 & 颜色通道** | 支持顶点颜色通道，导出时保持颜色信息。 |
| **骨骼权重** | 读取并写出骨骼权重，兼容 Blender 骨骼体系。 |
| **自定义属性映射** | 通过属性映射表将 Blender 自定义属性映射到 MCP 字段。 |
| **批量处理** | 可一次性导入/导出多个对象，支持批量命名与分组。 |
| **命令行接口** | 通过 `bpy` 脚本或命令行批量转换，适合自动化工作流。 |

## 安装与使用

1. **下载插件**  
   ```bash
   git clone https://github.com/ahujasid/blender-mcp.git
   ```

2. **安装插件**  
   - 打开 Blender → `Edit > Preferences > Add-ons > Install…`  
   - 选择 `blender_mcp/__init__.py`（或压缩包）  
   - 勾选插件以启用

3. **导入 MCP**  
   - 选择 `File > Import > MCP (.mcp)`  
   - 选择文件 → 预览 → `Import MCP`

4. **导出 MCP**  
   - 选择对象 → `File > Export > MCP (.mcp)`  
   - 配置导出选项（UV、材质、权重等） → `Export MCP`

5. **命令行批量转换**  
   ```bash
   blender --background --python - <<'PY'
   import bpy
   bpy.ops.import_mcp(filepath="model.mcp")
   bpy.ops.export_mcp(filepath="model_exported.mcp")
   PY
   ```

## 示例代码

```python
import bpy

# 导入
bpy.ops.import_mcp(filepath="/path/to/model.mcp")

# 设置导出路径
bpy.ops.export_mcp(filepath="/path/to/exported.mcp",
                   use_uv=True,
                   use_vertex_colors=True,
                   use_bone_weights=True)
```

## 贡献

如需提交 PR 或 issue，遵循项目的贡献指南。  
查看 `CONTRIBUTING.md` 与 `LICENSE` 了解更多细节。