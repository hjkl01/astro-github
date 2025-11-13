---
title: langchain
---


# LangChain 说明

## 项目地址
- [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)

## 主要特性
- **链（Chain）**  
  将LLM、工具或其他模块按顺序组合，形成可重复使用、可组合的工作流。
- **提示模板（PromptTemplate）**  
  支持可扩展、可重用的提示生成，兼容多种语言模型。
- **记忆（Memory）**  
  提供会记忆（ConversationBufferMemory/TokenBufferMemory）与外部检索记忆，保证上下文连贯。
- **检索与向量存储**  
  与多种向量数据库（FAISS、Chroma、Pinecone 等）和检索器（VectorStoreRetriever）无缝集成。
- **工具与代理（Agents）**  
  通过 Agent + Tool 组合实现自动化决策、查询执行、超文本解析等。
- **多模型支持**  
  原生支持 OpenAI、anthropic、gpt‑4、LLM 本地推理、以及自定义 LLM。
- **自定义组件与插件化**  
  通过 `Base*` 类可轻松实现自定义 Prompt、LLM、Memory、Retriever 等。
- **调试与可视化**  
  提供 `langchain-tracing` 和 `langchain-visualization` 等工具，方便排查链执行流程。

## 核心功能

| 模块 | 作用 |
|------|------|
| `langchain.llms` | 封装多种 LLM 适配器 |
| `langchain.prompts` | 统一提示词管理 |
| `langchain.chains` | 定义链(Runnable)实现 |
| `langchain.agents` | 自动推理、工具调用 |
| `langchain.memory` | 会话上下文存储 |
| `langchain.vectorstores` | 向量检索接口 |
| `langchain.embeddings` | 文本嵌入接口 |
| `langchain.output_parsers` | 结果解析器 |
| `langchain.tools` | 外部工具集成 |

## 用法示例

```python
from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

# 1. 初始化模型
llm = OpenAI(temperature=0.7, model="gpt-4")

# 2. 定义提示模板
template = PromptTemplate(
    input_variables=["question"],
    template="回答以下问题：{question}"
)

# 3. 创建链
chain = LLMChain(llm=llm, prompt=template)

# 4. 调用链
response = chain.run({"question": "Python 的作用域规则是什么？"})
print(response)

# 5. 向量检索示例
embeddings = OpenAIEmbeddings()
docstore = FAISS.from_texts(
    ["Python 是一种解释型语言", "Java 也是一种编程语言"],
    embeddings
)
retriever = docstore.as_retriever()
docs = retriever.retrieve("Python")
print([doc.page_content for doc in docs])

# 6. 代理调用工具
from langchain.agents import initialize_agent, Tool

calculator_tool = Tool(
    name="Calculator",
    func=lambda x: str(eval(x)),
    description="Use for arithmetic calculations"
)

agent = initialize_agent([calculator_tool], llm, agent_type="zero-shot-react-description")
result = agent.run("2+2*5")
print(result)
```

## 如何开始

1. **安装**  
   ```bash
   pip install langchain
   ```

2. **配置 API Key**  
   ```bash
   export OPENAI_API_KEY="your-key"
   ```

3. **快速实验**  
   运行上面提供的示例代码，即可看到 LangChain 的强大功能。

4. **参考文档**  
   - 官方文档: https://langchain.readthedocs.io  
   - 代码示例: https://github.com/langchain-ai/langchain/tree/master/examples

> **提示**：在大型项目中建议使用 `langchain` 的 `Runnable` 接口来替代传统链类，以更好地支持多任务并行与可组合性。

--- 

> 若需进一步定制或拓展，请查阅对应模块的详细 API 文档或源代码。
