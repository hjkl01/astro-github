import os
from api_ai import api_opencode
import asyncio

# @01-go/  检查md文件 哪些和项目的描述不相符的 更新功能和用法


async def main():
    default_dir = "./src/content/docs"
    dirs = [f'{default_dir}/{d}' for d in os.listdir(default_dir)]
    print(dirs)

    for d in dirs:
        content = f'@{d}  检查md文件 哪些和项目的描述不相符的, 更新功能和用法.如果是用英文描述的，则替换为中文。'
        await api_opencode(content=content)

if __name__ == "__main__":
    asyncio.run(main())
