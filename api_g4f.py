import httpx
import json
import time
import random
from typing import Dict, Any, Optional


class APIClient:
    def __init__(self):
        # 公共请求头
        self.common_headers = {
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "content-type": "application/json",
            "dnt": "1",
            "origin": "https://ai.zdht.hjkl01.cn:65432",
            "priority": "u=1, i",
            "referer": "https://ai.zdht.hjkl01.cn:65432/",
            "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
        }

    def post_chat_completion(self, url: str, data: Dict[str, Any], model: Optional[str] = None) -> httpx.Response:
        """发送聊天完成请求"""
        payload = data.copy()
        if model:
            payload["model"] = model

        response = httpx.post(url, headers=self.common_headers, json=payload, timeout=30.0)
        return response

    def get_models(self, url: str) -> httpx.Response:
        """获取模型列表"""
        response = httpx.get(url, headers=self.common_headers, timeout=30.0)
        return response

    def options_request(self, url: str, method: str = "POST") -> httpx.Response:
        """发送OPTIONS预检请求"""
        headers = self.common_headers.copy()
        headers.update(
            {
                "access-control-request-headers": "content-type",
                "access-control-request-method": method,
            }
        )

        response = httpx.options(url, headers=headers, timeout=30.0)
        return response


# 使用示例


def api_g4f(content):
    sleep_time = random.randint(1, 3)
    print(sleep_time, content)
    time.sleep(sleep_time)
    client = APIClient()

    # 基础数据
    base_payload = {
        "messages": [{"role": "user", "content": content}],
        # "stream": True,
        "stream": False,
        "stream_options": {"include_usage": True},
    }

    grok_response = client.post_chat_completion(
        "https://gpt4free.pro/v1/chat/completions",
        base_payload,
        # model="grok-4",
        model="gpt-5-chat",
        # "https://g4f.dev/api/grok/chat/completions", base_payload, model="grok-4-fast-non-reasoning"
    )
    print(f"Status: {grok_response.status_code}")
    if grok_response.status_code != 200:
        return api_g4f(content)
    # print(f"Response: {grok_response.text[:200]}...")
    print(f"Response: {grok_response.text[:100]}...")
    return grok_response.json()


# 流式响应处理示例


def handle_streaming_response(response: httpx.Response):
    """处理流式响应"""
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                try:
                    # 解析SSE格式（Server-Sent Events）
                    if line.startswith("data: "):
                        data = line[6:]  # 移除 "data: " 前缀
                        if data == "[DONE]":
                            break
                        json_data = json.loads(data)
                        # 处理响应数据
                        if "choices" in json_data and json_data["choices"]:
                            content = json_data["choices"][0].get("delta", {}).get("content", "")
                            if content:
                                print(content, end="", flush=True)
                except json.JSONDecodeError:
                    continue
        print()  # 换行
    else:
        print(f"Error: {response.status_code} - {response.text}")


# 流式请求示例


def streaming_example():
    client = APIClient()
    payload = {
        "messages": [{"role": "user", "content": "请详细解释什么是人工智能"}],
        "stream": True,
        "stream_options": {"include_usage": True},
    }

    print("=== Streaming Response Example ===")
    response = client.post_chat_completion(
        "https://g4f.dev/api/openrouter/chat/completions", payload, model="alibaba/tongyi-deepresearch-30b-a3b:free"
    )

    handle_streaming_response(response)


def auto_category(content):
    category = [
        "windows",
        "python",
        "tools",
        "vim",
        "kubernetes",
        "web",
        "java",
        "database",
        "android",
        "ecommerce",
        "backup",
        "macos",
        "ai",
        "networking",
        "node.js",
        "rust",
        "mobile",
        "javascript",
        "windows",
        "devops",
        "go",
        "monitoring",
        "nginx",
        "sftp-server",
        "crawling",
        "cryptography",
        "media",
        "web-tools",
        "translation",
        "linux",
        "search",
        "docker",
        "sql",
        "github",
        "email",
        "data",
        "chat",
        "ocr",
        "openwrt",
        "wsl",
        "shell",
        "emulators",
        "system-management",
        "games",
        "serverless",
        "api",
        "music",
        "terminal",
        "geoip",
        "download",
        "dotfiles",
        "nodejs",
        "git",
        "remote-desktop",
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
    api_g4f("请详细解释什么是人工智能")

    # 运行流式示例（取消注释）
    # streaming_example()
