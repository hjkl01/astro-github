import asyncio
import subprocess

import dashscope
from dashscope import Generation

from config import logger, QWEN_KEY


def api_qianwen(prompt):
    logger.debug(prompt[:100])
    # 设置 API Key
    dashscope.api_key = QWEN_KEY

    # 调用 Qwen-Max 模型
    model = "qwen-max"
    # model = "qwen3-max-2025-09-23"
    response = Generation.call(model=model, prompt=prompt)

    # 输出结
    logger.info(response.output)
    return response.output.text


async def api_opencode(url=None, content=None):
    if url:
        content = f"用markdown的格式 介绍项目的功能和用法：{url}.  \
注意事项： \
    1. 以项目名_用户名.md 为文件名, 写到 src/content/docs/ 对应的文件夹下,如01-neovim文件夹下.不要新建文件夹，如没有合适的文件夹，则放到默认的github文件夹下。  \
    2. 开头保持astro模板starlight的格式： --- \n title: repository \n ---  "
    print(f"{content=}")
    command = 'opencode run "{}"'.format(content)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output


async def auto_category(content, category_dirs):
    # 现在我想对其进行分类，已有的分类有Python、docker、Linux、tools、windows等，分析该项目应在哪个分类下，如不存在已有的分类，可以新建一个。
    content = f"""我收集了GitHub上的项目,以下是对项目的描述: {content}.
    现在我想对其进行分类，已有的分类有 {category_dirs} ，分析该项目应在哪个分类下，如不存在已有的分类，返回 github。 直接返回分类名称， 不需要其他的废话."""
    response = api_qianwen(content)
    # response = await api_opencode(content=content)
    logger.info(response)
    return response


if __name__ == "__main__":
    asyncio.run(api_opencode(url="https://github.com/withastro/astro"))
