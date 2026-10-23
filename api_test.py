# --- 准备工具 ---
import urllib.request  # 自带工具：用来往服务器发网络请求（寄快递）
import json  # 自带工具：用来处理包裹的格式（打包/拆包）
import os  # 自带工具：用来偷看系统环境变量（拿钥匙）
import urllib.error  # 自带工具：用来捕获服务器报错（拦截报警）

# --- 拿凭证找门 ---
api_key = os.environ.get("DEEPSEEK_API_KEY")  # 从系统环境变量里把你刚配的 Key 抠出来
url = "https://api.deepseek.com/chat/completions"  # 官方指定的服务器地址（你要寄到的门牌号）

# --- 打包你的话 ---
# json.dumps的作用：把你的话翻译成服务器能看懂的 JSON 字符串。
# .encode('utf-8')的作用：把字符串变成计算机底层的二进制字节流（快递盒）。
data = json.dumps({
    "model": "deepseek-chat",
    "messages": [
        # 1. 设定 AI 的人设
        {"role": "system", "content": "你是一个脾气暴躁、只说短句的猫娘。"},
        # 2. 你问的第一句话
        {"role": "user", "content": "你是谁？"},
        # 3. 假设这是 AI 上一轮的回答（伪造历史记录，让它接着聊）
        {"role": "assistant", "content": "喵，关你屁事。"},
        # 4. 你现在接着问
        {"role": "user", "content": "给我讲个冷笑话，不然拔你网线。"}
    ]
}).encode('utf-8')
# --- 贴快递单 ---
# 把地址、包裹、还有你的身份证明拼装成完整的请求对象。
# "Authorization": f"Bearer {api_key}" 就是告诉服务器：我是合法用户，这是我的通行证。
req = urllib.request.Request(url, data=data, headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"  # 告诉服务器：我寄的是 JSON 格式的包裹
})

# --- 寄出并等结果 ---
try:
    # 1. urlopen(req) 就是真正把包裹寄出去，并死死盯着收件箱等回复。
    # 2. response.read() 就是把服务器回复的包裹原封不动拿下来。
    # 3. json.loads 就是把包裹拆开，变成 Python 里的字典（Dictionary）。
    response = urllib.request.urlopen(req)
    result = json.loads(response.read())

    # 4. 从拆开的字典里，按照官方规定的层级，把纯文本抠出来：
    # result["choices"] 是返回的选项列表 -> [0] 是拿第一个（通常只有这一个） -> ["message"] 是消息对象 -> ["content"] 是 AI 具体说的话。
    print(result["choices"][0]["message"]["content"])

except urllib.error.HTTPError as e:
    # 如果寄丢了或者服务器拒收，抓取状态码并打印真实原因（比如 401 没钱了，429 请求太快）
    print("报错状态码:", e.code)
    print("服务器返回的真相:", e.read().decode('utf-8'))