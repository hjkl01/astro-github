import os
import json
import re
from api_g4f import api_g4f


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


def task(url):
    if "github.com" not in url:
        return
    username, repository = extract_github_info(url)
    print(username, repository)

    astro_path = "./src/content/docs/github"
    if os.path.exists(astro_path) is False:
        os.makedirs(astro_path)
    filename = f"{astro_path}/{repository}_{username}.md"
    if os.path.exists(filename):
        print(f"文件已存在：{filename} {url}")
        return

    content = f"GitHub项目地址: {url}. 用中文描述该项目的主要特性、功能及其用法。我要以markdown格式保存为文件，包含项目地址，不需要其他的废话."
    response = api_g4f(content)
    print(response)
    md = response["choices"][0]["message"]["content"]
    title = f"""
---
title: {repository}
---

"""
    md = title + md

    with open(filename, "w") as f:
        f.write(md)


def main():
    # url = "https://github.com/apify/crawlee-python?tab=readme-ov-file"
    # username, repository = extract_github_info(url)
    # print(username, repository)
    # return
    with open("./github_bookmarks.json", "r") as file:
        data = json.loads(file.read())
    urls = [item["url"] for item in data["bookmarks"]]

    for url in urls:
        try:
            task(url)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
