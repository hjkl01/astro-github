
---
title: boltz
---


# Boltz（jwohlwend 的 Boltz 项目）

**项目地址**：<https://github.com/jwohlwend/boltz>

---

## 主要特性

- **Boltzmann 加权构象搜索**  
  通过蒙特卡罗或随机采样产生大量分子构象，并根据能量计算其 Boltzmann 权重，得到对应的热力学权重分布。

- **多种能量评价方法**  
  支持 RDKit 内置的 UFF / MMFF94 能量模型；可通过插件接口绑定外部力场（例如 OpenBabel、MMFF 等）。

- **高效重排与能量最小化**  
  利用 RDKit 的最小化算法对生成的构象进行能量优化，同时可设置能量阈值进行筛选。

- **输出多种格式**  
  支持 SDF、PDB、XYZ 等常见分子文件格式的导出，方便后续可视化或进一步计算。

- **Python API 与命令行工具并存**  
  可以在脚本中直接调用 `boltz` 的函数完成构象搜索，也可以通过命令行一次性完成整个流程。

---

## 主要功能

| 功能 | 说明 |
|------|------|
| `boltz.generate_conformers` | 生成并能量最小化指定原子式的构象集合，返回 `list[Mol]` 与对应能量列表 |
| `boltz.compute_boltzmann_weights` | 根据能量列表计算 Boltzmann 权重 |
| `boltz.filter_by_energy` | 依据阈值或前 N 名过滤构象 |
| `boltz.conformers_to_file` | 将构象集写入文件（支持 SDF/PDB/XYZ） |
| `boltz.cli` | 命令行入口，支持 `-i/--input`, `-n/--num_conformers`, `-o/--output`, `-f/--forcefield` 等选项 |

---

## 用法示例

### 1. Python API 方式

```python
from boltz import (
    generate_conformers,
    compute_boltzmann_weights,
    conformers_to_file
)

# 读取分子
mol = Chem.MolFromMolFile("target.mol")

# 生成 200 个构象
confs, energies = generate_conformers(mol, n_confs=200, forcefield="UFF")

# 计算 Boltzmann 权重
weights = compute_boltzmann_weights(energies, temperature=298.15)

# 保存前 10 个重要构象
top_indices = sorted(range(len(weights)), key=lambda i: weights[i], reverse=True)[:10]
top[i] for i in top_indices]
conformers_to_file(top_confs, "top_conformers.sdf")
```

### 2. 命令行方式

```bash
python -m boltz \
    -i input.sdf \          # 输入文件
    -n 150 \                # 生成 150 个构象
    -o.sdf \         # 输出文件
    -f UFF \                # 使用 UFF 力场
    --temperature 310      # 温度（单位 K）
```

执行后将在 `output.sdf` 中得到按 Boltzmann 权重排序的构象列表。

---

## 安装

```bash
pip install git+https://github.com/jwohlwend/boltz.git
```

---

> 欢迎尝试 Boltz，若对构象搜索或热力学模型有进一步需求，欢迎使用其可扩展的 Python API 或自行编写插件。祝使用愉快！