import json
import os
from openai import OpenAI
def write_note(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    return "add suceessfully"
client = OpenAI(
    api_key=os.environ.get("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
system_msg={"role":"system","content":'如果你被要求记录或写笔记，必须输出严格的JSON格式：{“file_name”:"笔记.txt","content":"内容“}，如果是普通聊天，就正常输出'}
user_msg={"role":"user","content":"user_text"}
response = client.chat.completions.create(model="deepseek-chat", messages=[system_msg, user_msg])
ai_reply=response.choices[0].message.content
try:
    data=json.loads(ai_reply)
    filename=data.get("filename")
    content=data.get("content")
    if filename and content:
        result=write_note(filename,content)
        print(result)
    else :
        print("agent:",ai_reply)
except json.decoder.JSONDecodeError:
    print("agent:",ai_reply)