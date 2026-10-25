import json
fake_ai_reply = '{"filename": "a.txt", "content": "hello"}'
data = json.loads(fake_ai_reply)
print("提取成功！文件名是：", data["filename"])