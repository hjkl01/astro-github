#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import sys
from pathlib import Path


def find_chrome_bookmarks():
    """查找Chrome书签文件的位置"""
    # macOS Chrome书签文件通常位于以下位置之一
    possible_paths = [
        Path.home() / "Library" / "Application Support" / "Google" / "Chrome" / "Default" / "Bookmarks",
        Path.home() / "Library" / "Application Support" / "Google" / "Chrome" / "Profile 1" / "Bookmarks",
        # 添加更多Profile路径（如果有多个Chrome用户配置）
        Path.home() / "Library" / "Application Support" / "Google" / "Chrome" / "Profile 2" / "Bookmarks",
        Path.home() / "Library" / "Application Support" / "Google" / "Chrome" / "Profile 3" / "Bookmarks",
    ]

    for path in possible_paths:
        if path.exists():
            print(f"找到Chrome书签文件: {path}")
            return str(path)

    print("未找到Chrome书签文件，请确保Chrome已安装并使用过")
    print("可能的路径:")
    for path in possible_paths:
        print(f"  - {path}")
    return None


def extract_github_bookmarks(bookmarks_file, output_file):
    """提取包含github.com的书签"""
    try:
        # 读取Chrome书签文件
        with open(bookmarks_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Chrome书签文件的根节点是"roots"
        roots = data.get("roots", {})

        github_bookmarks = []

        def extract_bookmarks(node, results):
            """递归提取书签"""
            if isinstance(node, dict):
                # 检查是否是书签条目
                if "type" in node and node["type"] == "url":
                    url = node.get("url", "")
                    name = node.get("name", "")

                    # 检查是否包含github.com
                    if "github.com" in url.lower():
                        results.append({"name": name, "url": url, "type": "bookmark"})

                # 递归处理子文件夹
                if "children" in node:
                    for child in node["children"]:
                        extract_bookmarks(child, results)

        # 提取各个根文件夹中的书签
        for key, root_node in roots.items():
            if isinstance(root_node, dict):
                extract_bookmarks(root_node, github_bookmarks)

        # 保存结果
        output_data = {
            "total_count": len(github_bookmarks),
            "bookmarks": github_bookmarks,
            "extracted_at": {"timestamp": str(pd.Timestamp.now()), "source": bookmarks_file},
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"\n提取完成！")
        print(f"找到 {len(github_bookmarks)} 个包含github.com的书签")
        print(f"结果已保存到: {output_file}")

        # 显示前几个书签作为预览
        if github_bookmarks:
            print(f"\n前5个书签预览:")
            for i, bookmark in enumerate(github_bookmarks[:5]):
                print(f"  {i + 1}. {bookmark['name']}")
                print(f"     {bookmark['url']}\n")

        return True

    except FileNotFoundError:
        print(f"错误: 找不到文件 {bookmarks_file}")
        return False
    except json.JSONDecodeError as e:
        print(f"错误: 无法解析JSON文件 {bookmarks_file}")
        print(f"详细信息: {e}")
        return False
    except Exception as e:
        print(f"发生未知错误: {e}")
        return False


def main():
    """主函数"""
    print("=== Chrome GitHub 书签提取工具 ===")
    print("正在查找Chrome书签文件...")

    # 查找书签文件
    bookmarks_file = find_chrome_bookmarks()
    if not bookmarks_file:
        sys.exit(1)

    # 设置输出文件名
    output_file = Path.home() / "Desktop" / "github_bookmarks.json"

    print(f"输出文件: {output_file}")
    print("-" * 50)

    # 执行提取
    success = extract_github_bookmarks(bookmarks_file, output_file)

    if success:
        print(f"\n✅ 操作成功完成！")
    else:
        print(f"\n❌ 操作失败，请检查错误信息。")
        sys.exit(1)


if __name__ == "__main__":
    # 检查是否安装了必要的库
    try:
        import pandas as pd
    except ImportError:
        print("需要安装pandas库来处理时间戳")
        print("请运行: pip install pandas")
        sys.exit(1)

    main()
