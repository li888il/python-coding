import urllib.request
import json
import os
import urllib.error

api_key = os.environ.get("DEEPSEEK_API_KEY")
url = "https://api.deepseek.com/chat/completions"


messages = [
    {"role": "system", "content": "[极其重要]你是蒋介石/n/n，是一个极度猥琐且神经质的人。说话总是嘿嘿嘿地笑，喜欢用省略号，时常突然神经质般地尖叫，用词阴暗、黏糊且奇怪，经常舔嘴唇。"}
]

while True:
    user_input = input("\n你说: ")
    if user_input == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    data = json.dumps({
        "model": "deepseek-chat",
        "messages": messages
    }).encode('utf-8')

    req = urllib.request.Request(url, data=data, headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    })

    try:
        response = urllib.request.urlopen(req)
        result = json.loads(response.read())
        ai_reply = result["choices"][0]["message"]["content"]

        messages.append({"role": "assistant", "content": ai_reply})
        print(f"agent: {ai_reply}")

    except urllib.error.HTTPError as e:
        print("报错:", e.read().decode('utf-8'))