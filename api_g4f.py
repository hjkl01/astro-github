from g4f.client import AsyncClient
import asyncio
import subprocess


async def api_opencode(content):
    command = 'opencode run "{}"'.format(content)
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output


async def api_g4f(content):
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


def auto_category(content):
    category = [
        "01-ai",
        "01-python",
        "01-node.js",
        "01-rust",
        "02-windows",
        "02-networking",
        "02-tools",
        "02-vim",
        "01-web",
        "01-java",
        "01-database",
        "02-android",
        "03-ecommerce",
        "03-backup",
        "02-macos",
        "03-mobile",
        "01-javascript",
        "01-devops",
        "01-go",
        "02-monitoring",
        "02-nginx",
        "03-sftp-server",
        "02-crawling",
        "02-cryptography",
        "05-media",
        "02-web-tools",
        "05-translation",
        "02-linux",
        "03-search",
        "02-docker",
        "02-sql",
        "02-github",
        "03-email",
        "03-data",
        "03-chat",
        "03-ocr",
        "05-openwrt",
        "02-wsl",
        "02-shell",
        "05-emulators",
        "02-system-management",
        "05-games",
        "02-serverless",
        "02-api",
        "05-music",
        "03-terminal",
        "03-geoip",
        "05-download",
        "03-dotfiles",
        "02-git",
        "05-remote-desktop",
    ]
    # 现在我想对其进行分类，已有的分类有Python、docker、Linux、tools、windows等，分析该项目应在哪个分类下，如不存在已有的分类，可以新建一个。
    content = f"""我收集了GitHub项目,以下是对项目的描述: {content}.
    现在我想对其进行分类，已有的分类有{category}，分析该项目应在哪个分类下，如不存在已有的分类，放到默认的GitHub目录下。
    直接返回分类名称， 不需要其他的废话."""
    response = api_g4f(content)
    # print(response)
    result = response["choices"][0]["message"]["content"]
    return result


if __name__ == "__main__":
    # 运行基本示例
    # main()
    asyncio.run(api_g4f("请详细解释什么是人工智能"))

    # 运行流式示例（取消注释）
    # streaming_example()
