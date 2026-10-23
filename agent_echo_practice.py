#import json
#import os
#
#
#
#def load_history():
#    if os.path.exists("history.json"):
#        with open("history.json", "r", encoding="utf-8") as f:
#
#
#            return json.load(f)
#    else:
#        return []
#def save_history(history):
#    with open("history.json", "w", encoding="utf-8") as f:
#        json.dump(history, f, ensure_ascii=False, indent=2)
#
import json
import os


# 1. 你的 EchoAgent 类放这里
class EchoAgent:
    def __init__(self, name):
        self.name = name
        self.history = []

    def reply(self, text):
        answer = f"[{self.name}] echo: {text}"
        self.history.append({"user": text, "agent": answer})
        return answer


# 2. 你刚写对的这两个函数放这里
def load_history():
    if os.path.exists("history.json"):
        with open("history.json", "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []


def save_history(history):
    with open("history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


# 3. 核心：把它们串起来的启动代码
if __name__ == "__main__":
    # 先读历史
    history = load_history()

    # 创建机器人，并把历史塞给它
    agent = EchoAgent("demo")
    agent.history = history

    print("Agent 已启动，输入 exit 退出。")

    while True:
        user_input = input("你: ")

        if user_input == "exit":
            # 退出前保存历史
            save_history(agent.history)
            print("历史已保存，拜拜！")
            break

        # 正常对话
        response = agent.reply(user_input)
        print("Agent:", response)