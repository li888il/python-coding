import os
from openai import OpenAI
import json

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'), 
    base_url="https://api.deepseek.com"
)

# 核心：设计一段极其严格的提示词（Prompt），逼模型吐出 JSON
system_prompt = """
你是一个文件助手。请根据用户的话，提取出操作。
你必须只输出一个 JSON，不要包含任何诸如 ```json 的代码块标记，不要任何多余的废话。
JSON 格式如下：{"filename": "文件名.txt", "content": "要写入的内容"}
"""

user_input = "帮我建一个日记本.txt，里面写上今天天气真好。"

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ],
    stream=False
)

answer = response.choices[0].message.content
print("--- 模型的原始输出 ---")
print(answer)

# 最硬核的一步：在 Python 里直接把这个 JSON 转成字典
try:
    tool_call = json.loads(answer)
    print("\n--- 解析成功 ---")
    print("提取到的文件名:", tool_call["filename"])
    print("提取到的内容:", tool_call["content"])
except Exception as e:
    print("\n--- 解析失败，模型说了废话 ---")
    print("报错原文:", e)