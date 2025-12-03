import requests
import json
import re
import time

from .config import logger, OLLAMA_URL, OLLAMA_MODEL
from .prompt import category_prompt


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
    logger.debug(payload["prompt"][:300])

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
        text = re.sub(r"<think>.*</think>", "", obj.get("response", ""), flags=re.DOTALL)
        logger.debug(text[:300])
        return text.strip()

        # return {"text": obj.get("response", ""), "raw": obj}

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


async def auto_category(content, category_dirs):
    content = f"""我收集了GitHub上的项目,以下是对项目的描述: {content}.
    现在我想对其进行分类，已有的分类有 {category_dirs} ，分析该项目应在哪个分类下，如不存在已有的分类，返回 github。 直接返回分类名称， 不需要其他的废话."""
    prompt = category_prompt.replace("content", content).replace("category_dirs", ",".join(category_dirs))
    response = api_ollama_generate(prompt)
    logger.info(response)
    return response


if __name__ == "__main__":
    pass
