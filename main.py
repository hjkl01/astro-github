import os
import sys
import re
import asyncio
from pathlib import Path

from api.config import logger
from api.prompt import markdown_prompt
from api.api_ai import auto_category, api_ollama_generate, api_github_readme
from api.github_trending_scraper import main as github_trending_scraper


def clean_small_md_files(dirname="src/content/docs", min_size=500):
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if file.endswith(".md"):
                filepath = os.path.join(root, file)
                size = os.path.getsize(filepath)
                if size < min_size:
                    os.remove(filepath)
                    logger.info(f"Deleted small file: {filepath}")


def extract_github_info(github_url):
    """
    从GitHub URL中提取用户名和项目名

    Args:
        github_url (str): GitHub仓库URL

    Returns:
        tuple: (username, project_name) 或 (None, None) 如果匹配失败
    """

    # logger.debug(github_url)
    # GitHub仓库URL的正则表达式模式
    pattern = r"https?://github\.com/([^/]+)/([^/?#]+)(?:[/?#].*)?"

    match = re.search(pattern, github_url.strip())

    if match:
        username = match.group(1)
        project_name = match.group(2)
        # logger.debug(f"{username} {project_name}")
        return username, project_name
    else:
        return None, None


def list_files(dirname="src/content/docs"):
    files = []
    for root, dirs, filenames in os.walk(dirname):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files


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
                logger.info(f"{md_file}, {category}")
                if category in category_dirs:
                    new_dir = os.path.join(dirname, category)
                    os.makedirs(new_dir, exist_ok=True)
                    logger.debug(os.path.join(dirname, md_file))
                    logger.debug("src/content/docs/" + category + "/" + md_file)
                    os.rename(
                        os.path.join(dirname, md_file),
                        "src/content/docs/" + category + "/" + md_file,
                    )
    os.removedirs(dirname)


async def main(args=None):
    clean_small_md_files()
    if args == "cate":
        await category_md_files()
        return

    with open("urls.txt", "r", encoding="utf-8") as f:
        urls = f.readlines()

    md_files = list_files()
    md_files = [f.split("/")[-1] for f in md_files]

    for project_line in urls:
        project_line = project_line.strip()
        if not project_line:
            continue

        temp = project_line.split(" ")
        url = temp[0]

        username, repository = extract_github_info(url)
        if not username or not repository:
            logger.info(f"无法解析 GitHub URL: {url}")
            continue

        filename = f"{repository}_{username}.md"
        if filename in md_files:
            logger.debug(f"文件已存在：{filename}")
            continue

        logger.info(project_line)
        try:
            readme_content = api_github_readme(username, repository)
            if readme_content is None:
                continue
            prompt = markdown_prompt.replace("readme_content", readme_content)
            ai_resp = api_ollama_generate(prompt)
            if len(temp) == 1:
                category_dir = "00"
            elif len(temp) == 2:
                category_dir = temp[1]
            else:
                logger.info(f"无法解析：{temp}")

            title = """
         ---
         title: repository
         ---

         ### [username repository](https://github.com/username/repository)

         """

            text = title.replace("username", username).replace("repository", repository) + ai_resp

            if not os.path.exists(f"src/content/docs/{category_dir}"):
                os.makedirs(f"src/content/docs/{category_dir}")

            with open(f"src/content/docs/{category_dir}/{filename}", "w") as file:
                file.write(text)

        except Exception as e:
            logger.error(f"处理项目 {url} 时出错：{str(e)}")

    await category_md_files()


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) > 1 and argv[1] == "cate":
        asyncio.run(main("cate"))
    elif len(argv) > 1 and argv[1] == "crawl":
        github_trending_scraper()
    else:
        asyncio.run(main())
