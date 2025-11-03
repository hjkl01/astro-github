import asyncio
import subprocess

from g4f.client import AsyncClient


async def api_opencode(content):
    command = 'opencode run "{}"'.format(content)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output


async def api_g4f(content):
    try:
        client = AsyncClient(timeout=60)
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            # model="gpt-4.1",
            # model="gpt-4o",
            # model="gpt-3.5-turbo",
            # model="gemini",
            # model="grok",
            messages=[{"role": "user", "content": content}],
        )
        result = response.choices[0].message.content
        return result
    except Exception as err:
        print(err)
        return await api_g4f(content)


async def auto_category(content, category_dirs):
    # 现在我想对其进行分类，已有的分类有Python、docker、Linux、tools、windows等，分析该项目应在哪个分类下，如不存在已有的分类，可以新建一个。
    content = f"""我收集了GitHub项目,以下是对项目的描述: {content}.
    现在我想对其进行分类，已有的分类有{category_dirs}，分析该项目应在哪个分类下，如不存在已有的分类，放到默认的GitHub目录下。
    直接返回分类名称， 不需要其他的废话."""
    response = await api_g4f(content)
    print(response)
    return response


if __name__ == "__main__":
    # 运行基本示例
    # main()
    asyncio.run(api_g4f("请详细解释什么是人工智能"))

    # 运行流式示例（取消注释）
    # streaming_example()
