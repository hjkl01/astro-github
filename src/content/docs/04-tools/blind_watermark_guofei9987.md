---
title: blind
---

# blind_watermark

项目地址: <https://github.com/guofei9987/blind_watermark>

## 概述
**blind_watermark** 是一个基于 Python 的图像盲水印工具，能够在图像中嵌入不可见水印，并在不损坏视觉质量的前提下实现对水印的安全存储与检测。该工具支持对多种常见图像格式（如 JPEG、PNG）进行嵌入与提取，适用于数字版权保护、内容验证等场景。

## 主要特性
- **盲水印嵌入**：通过改动像素的 LSB 或频域系数，将水印信息隐藏在图像中，几乎不影响视觉效果。  
- **鲁棒检测**：支持对已嵌入水印的图像进行检测，能够在一定程度上抵抗压缩、裁剪、噪声、颜色空间转换等常见操作。  
- **可配置参数**：提供多种嵌入强度、嵌入区域和随机种子等参数，便于根据不同安全需求进行自定义。  
- **跨平台**：纯 Python 实现，兼容 Windows、macOS、Linux 系统。  

## 功能
| 功能模块 | 描述 |
| -------- | ---- |
| `embed` | 读取源图像与水印图像，按设定参数嵌入水印并保存输出图像。 |
| `extract` | 从嵌入水印的图像中提取原始水印或判断其完整性。 |
| `config` | 通过配置文件或命令行参数定制嵌入/检测策略。 |

## 用法

### 1. 安装

```bash
# 克隆仓库
git clone https://github.com/guofei9987/blind_watermark.git
cd blind_watermark

# 创建并激活虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 嵌入水印

```bash
python embed.py \
  --image  src/sample.jpg \          # 原始图像路径
  --watermark watermark.png \        # 水印图像路径
  --output out_with_watermark.jpg \  # 输出图像路径
  --strength 0.2 \                  # 嵌入强度（0~1）
  --seed 42                          # 随机种子
```

> **说明**  
> - `--strength` 控制水印对图像可视化影响的程度，值越大，鲁棒性越强但可视化影响也越明显。  
> - `--seed` 用于生成嵌入掩码的随机数种子，保证同一张图片可重复生成相同的水印位置。

### 3. 检测/提取水印

```bash
python extract.py \
  --image out_with_watermark.jpg \  # 含水印图像路径
  --threshold 0.7 \                # 判定阈值，越高判定更严格
  --report report.txt               # 检测结果报告
```

> **输出**  
> - `report.txt` 包含检测置信度、错误率等信息，可用于后续验证或记录。  

## 示例代码

- **embed.py**（入口脚本示例）

  ```python
  from blind_watermark import embed

  if __name__ == "__main__":
      embed(
          image_path="src/sample.jpg",
          watermark_path="watermark.png",
          output_path="out_with_watermark.jpg",
          strength=0.2,
          seed=42
      )
  ```

- **extract.py**（入口脚本示例）

  ```python
  from blind_watermark import extract

  if __name__ == "__main__":
      result = extract(
          image_path="out_with_watermark.jpg",
          threshold=0.7
      )
      print(result)
  ```

## 参考文献
- GitHub Repository: <https://github.com/guofei9987/blind_watermark>

---