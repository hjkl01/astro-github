import os
import json
import re
from api_g4f import api_g4f, auto_category


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


def task(url: str, dirname: str = '01'):
    if "github.com" not in url:
        return
    username, repository = extract_github_info(url)
    print(username, repository)

    content = f"GitHub项目地址: {url}. 用中文描述该项目的主要特性、功能及其用法。我要以markdown格式保存为文件，包含项目地址，不需要其他的废话."
    response = api_g4f(content)
    print(response)
    md = response["choices"][0]["message"]["content"].lstrip("```markdown").rstrip("```")
    title = f"""
---
title: {repository}
---

"""
    md = title + md

    if dirname:
        astro_path = f"./src/content/docs/{dirname}"
        if os.path.exists(astro_path) is False:
            os.makedirs(astro_path)
        filename = f"{astro_path}/{repository}_{username}.md"
        if os.path.exists(filename):
            print(f"文件已存在：{filename} {url}")
            return
    with open(filename, "w") as f:
        f.write(md)


def list_files(dirname="src/content/docs"):
    files = []
    for root, dirs, filenames in os.walk(dirname):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files


def main():
    # url = "https://github.com/apify/crawlee-python?tab=readme-ov-file"
    # username, repository = extract_github_info(url)
    # print(username, repository)
    # return

    # with open("./github_bookmarks.json", "r") as file:
    #     data = json.loads(file.read())
    # urls = [item["url"] for item in data["bookmarks"]]
    #
    # for url in urls:
    #     try:
    #         task(url)
    #     except Exception as e:
    #         print(e)

    with open("urls.txt", "r") as f:
        urls = f.readlines()
    md_files = list_files()
    md_files = [f.split("/")[-1] for f in md_files]
    for project in urls:
        temp = project.strip().split("\n")

        username, repository = extract_github_info(temp[0])
        filename = f"{repository}_{username}.md"
        if filename in md_files:
            print(f"文件已存在：{filename}")
            continue

        if len(temp) == 1:
            task(temp[0])
        elif len(temp) == 2:
            try:
                task(temp[0], temp[1])
            except Exception as e:
                print(e)
        else:
            print(f"无法解析：{temp}")
            continue


if __name__ == "__main__":
    main()
