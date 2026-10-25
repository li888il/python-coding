# agent.py
import json
from pathlib import Path#固定格式

# 把 history.json 固定放在 agent.py 同目录，避免从别的目录运行时找不到
HISTORY_FILE = Path(__file__).with_name("history.json")


def load_history(path=HISTORY_FILE):
    """读取历史；文件不存在、空文件、坏 JSON 都返回空列表，保证不崩。"""
    if not path.exists():
        return []

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        # 只接受 list，防止文件内容格式不对导致后面 append 报错
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        # JSON 坏了或读失败：今天先降级为空历史，不中断程序
        return []


def save_history(history, path=HISTORY_FILE):
    """把历史写回 JSON；ensure_ascii=False 保留中文。"""
    with path.open("w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)


def main():
    history = load_history()
    print("echo agent v0.1，输入 exit 退出")

    while True:
        user_text = input("你> ").strip()

        # 空输入直接跳过，不写入历史
        if not user_text:
            continue

        # exit / quit 都退出；退出后到循环外统一保存
        if user_text.lower() in {"exit", "quit"}:
            break

        reply = f"echo: {user_text}"

        # 一次交互写两条：用户消息 + agent 回复
        history.append({"role": "user", "content": user_text})
        history.append({"role": "assistant", "content": reply})

        print(f"agent> {reply}")

    # 关键：保存放在循环外，exit 后才写回
    save_history(history)
    print("已保存历史，再见")


if __name__ == "__main__":
    main()