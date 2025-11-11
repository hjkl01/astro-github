import os
import re
import sys
import asyncio
from pathlib import Path
from api_ai import auto_category, api_opencode


def extract_github_info(github_url):
    """
    从GitHub URL中提取用户名和项目名

    Args:
        github_url (str): GitHub仓库URL

    Returns:
        tuple: (username, project_name) 或 (None, None) 如果匹配失败
    """
    # GitHub仓库URL的正则表达式模式
    pattern = r"https?://github\.com/([^/]+)/([^/?#]+)(?:[/?#].*)?"

    match = re.search(pattern, github_url.strip())

    if match:
        username = match.group(1)
        project_name = match.group(2)
        return username, project_name
    else:
        return None, None


async def task(url: str, dirname: str = "00"):
    if "github.com" not in url:
        return

    username, repository = extract_github_info(url)
    if not username or not repository:
        print(f"无法解析 GitHub URL: {url}")
        return

    print("start: ", username, repository)

    try:
        await api_opencode(url=url)
    except Exception as err:
        print(err)
    return

    # filename = None


#     try:
#         content = f"GitHub项目地址: {url}. 用中文描述该项目的主要特性、功能及其用法。我要以markdown格式保存为文件, 路径为src/content/docs/{dirname}/{repository}_{username}.md，包含项目地址，不需要其他的废话."
#         content = f"GitHub项目地址: {url}. 用中文描述该项目的主要特性、功能及其用法。包含项目地址.不需要其他的废话."
#         response = await api_g4f(content)
#         # response = await api_opencode(content)
#         print(response)
#
#         # if "choices" not in response or not response["choices"]:
#         #     print(f"API 响应格式错误: {url}")
#         #     return
#
#         md = response.lstrip("```markdown").rstrip("```")
#         if len(md) < 50:
#             print(f"API 响应内容太短：{url}")
#             return
#         title = f"""
# ---
# title: {repository}
# ---
#
# """
#         md = title + md
#
#         if dirname:
#             astro_path = f"./src/content/docs/{dirname}"
#             os.makedirs(astro_path, exist_ok=True)
#             filename = f"{astro_path}/{repository}_{username}.md"
#
#         if filename:
#             with open(filename, "w", encoding="utf-8") as f:
#                 f.write(md)
#             print(f"文件创建成功：{filename}")
#
#     except Exception as e:
#         print(f"处理项目时出错 {url}: {str(e)}")
#         if filename:
#             print(f"问题文件：{filename}")


def list_files(dirname="src/content/docs"):
    files = []
    for root, dirs, filenames in os.walk(dirname):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files


def clean_small_md_files(dirname="src/content/docs", min_size=500):
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                size = os.path.getsize(filepath)
                if size < min_size:
                    # os.remove(filepath)
                    print(f"Deleted small file: {filepath}")


async def category_md_files(dirname="src/content/docs/00"):
    category_dirs = [
        str(child).lstrip("src/content/docs/").rstrip("/")
        for child in Path("src/content/docs").iterdir()
        if child.is_dir()
    ]

    md_files = os.listdir(dirname)
    for md_file in md_files:
        if md_file.endswith(".md"):
            with open(os.path.join(dirname, md_file), "r", encoding="utf-8") as f:
                content = f.read()
                category = await auto_category(content, category_dirs)
                print(md_file, category)
                if category in category_dirs:
                    new_dir = os.path.join(dirname, category)
                    os.makedirs(new_dir, exist_ok=True)
                    os.rename(os.path.join(dirname, md_file), "src/content/docs/" + category + "/" + md_file)


async def main(args=None):
    if args == "cate":
        await category_md_files()
        return

    clean_small_md_files()
    try:
        with open("urls.txt", "r", encoding="utf-8") as f:
            urls = f.readlines()

        md_files = list_files()
        md_files = [f.split("/")[-1] for f in md_files]

        for project_line in urls:
            project_line = project_line.strip()
            if not project_line:
                continue

            temp = project_line.split("\n")
            url = temp[0]

            username, repository = extract_github_info(url)
            if not username or not repository:
                print(f"无法解析 GitHub URL: {url}")
                continue

            filename = f"{repository}_{username}.md"
            if filename in md_files:
                print(f"文件已存在：{filename}")
                continue

            try:
                if len(temp) == 1:
                    await task(url)
                elif len(temp) == 2:
                    await task(url, temp[1])
                else:
                    print(f"无法解析：{temp}")
            except Exception as e:
                print(f"处理项目 {url} 时出错：{str(e)}")

    except FileNotFoundError:
        print("错误：找不到 urls.txt 文件")
    except Exception as e:
        print(f"主程序出错：{str(e)}")


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) > 1 and argv[1] == "cate":
        asyncio.run(main("cate"))
    else:
        asyncio.run(main())
