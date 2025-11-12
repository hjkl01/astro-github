import os
import asyncio
from pathlib import Path
import httpx
from api_ai import api_g4f


async def update_file(filepath):
    filename = os.path.basename(filepath)
    if not filename.endswith(".md"):
        return
    parts = filename[:-3].rsplit("_", 1)
    if len(parts) != 2:
        return
    repo, owner = parts
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/README.md"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code != 200:
                url = f"https://raw.githubusercontent.com/{owner}/{repo}/master/README.md"
                response = await client.get(url)
                if response.status_code != 200:
                    print(f"Failed to fetch README for {owner}/{repo}")
                    return
            readme = response.text
        except:
            print(f"Error fetching {owner}/{repo}")
            return
    content = f"Based on this README content: {readme[:2000]}... 用中文描述该项目的主要特性、功能及其用法。包含项目地址 https://github.com/{owner}/{repo}. 以markdown格式输出，不需要其他的废话."
    try:
        response = await api_g4f(content)
        md = response.lstrip("```markdown").rstrip("```")
        title = f"---\ntitle: {repo}\n---\n\n"
        md = title + md
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Updated {filename}")
    except Exception as e:
        print(f"Error updating {filename}: {e}")


async def main():
    dir_path = Path("src/content/docs/03-android")
    tasks = []
    for file in dir_path.iterdir():
        if file.is_file():
            tasks.append(update_file(str(file)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
