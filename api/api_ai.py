import asyncio
import os
import subprocess
import requests
import json
import time

from .config import logger, OLLAMA_URL, OLLAMA_MODEL


def api_ollama_generate(
    prompt: str,
    model: str = OLLAMA_MODEL,
    host: str = OLLAMA_URL,
    stream: bool = False,
    timeout: float = 300.0,
    **extra_options,
) -> dict:
    """
    调用 Ollama /api/generate（非流式/流式均可）

    参数:
      model: 模型名，如 "llama3.1:8b"
      prompt: 提示词
      host: Ollama 地址（可带 http:// 与端口），默认读取环境变量 OLLAMA_HOST，未配置则用 http://127.0.0.1:11434
      stream: 是否流式返回
      timeout: 请求超时（秒），对流式表示整体耗时上限
      **extra_options: 其他可选项（会透传进 payload），例如：
         system="你是...",
         format="json",
         options={"temperature": 0.2, "num_predict": 1024},
         context=[1,2,3],
         suffix="",
         images=["/path/to/img1.jpg", ...]

    返回:
      非流式: {"text": 模型输出文本, "raw": 完整 JSON 对象}
      流式: {"text": 累积的输出文本, "raw": 最后一条 JSON 对象}
    """
    url = f"{host.rstrip('/')}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": bool(stream), **extra_options}
    logger.debug(url)
    logger.debug(payload['prompt'][:300])

    resp = requests.post(
        url,
        json=payload,
        stream=bool(stream),
        timeout=timeout,
    )
    if not resp.ok:
        raise RuntimeError(f"Ollama generate 请求失败: HTTP {resp.status_code} - {resp.text}")

    if not stream:
        # 非流式一次返回完整 JSON
        obj = resp.json()
        logger.debug(resp.text[:300])
        return {"text": obj.get("response", ""), "raw": obj}

    # 流式：服务端以逐行 JSON 返回（每行一个 JSON 对象）
    text_parts = []
    last_obj = None
    start_ts = time.time()
    for line in resp.iter_lines(decode_responses=True):
        # 超时保护
        if time.time() - start_ts > timeout:
            raise TimeoutError("Ollama 流式生成超时")
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            # 忽略无法解析的行
            continue
        if "response" in obj:
            text_parts.append(obj["response"])
        last_obj = obj
        # 可根据 obj.get("done", False) 提前结束
        if obj.get("done"):
            break

    return {"text": "".join(text_parts), "raw": last_obj or {}}


async def api_opencode(url=None, content=None, cache_dir=None, dirname="00", username=None, repository=None):
    if url and cache_dir:
        # Analyze the local cloned code with ollama
        prompt = f"用markdown的格式 介绍项目的功能和用法：{url}. 基于本地代码分析：{cache_dir}. \
注意事项： \
    1. 以项目名_用户名.md 为文件名, 写到 src/content/docs/{dirname} 文件夹下。\
    2. 开头保持astro模板starlight的格式： --- \n title: repository \n ---  \n \
    3. 用中文介绍。"
        print(f"{prompt=}")
        # Call ollama API
        try:
            response = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": False},
            )
            response.raise_for_status()
            md_content = response.json()["response"]
        except Exception as e:
            print(f"Ollama API error: {e}")
            return None
        # Generate markdown file
        filename = f"src/content/docs/{dirname}/{repository}_{username}.md"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(md_content)
        print(f"Markdown file created: {filename}")
        return md_content
    elif content:
        # For category, keep original logic
        command = 'opencode run "{}"'.format(content)
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        output, error = process.communicate()
        return output


async def auto_category(content, category_dirs):
    # 现在我想对其进行分类，已有的分类有Python、docker、Linux、tools、windows等，分析该项目应在哪个分类下，如不存在已有的分类，可以新建一个。
    content = f"""我收集了GitHub上的项目,以下是对项目的描述: {content}.
    现在我想对其进行分类，已有的分类有 {category_dirs} ，分析该项目应在哪个分类下，如不存在已有的分类，返回 github。 直接返回分类名称， 不需要其他的废话."""
    response = api_ollama_generate(content)
    # response = await api_opencode(content=content)
    logger.info(response)
    return response


if __name__ == "__main__":
    asyncio.run(api_opencode(url="https://github.com/withastro/astro"))
