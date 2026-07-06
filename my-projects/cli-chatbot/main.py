import os
from openai import OpenAI


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    model = os.getenv("OPENAI_MODEL", "Qwen/Qwen2.5-7B-Instruct")

    if not api_key:
        raise RuntimeError("请先设置 OPENAI_API_KEY 环境变量")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    messages = [
        {"role": "system", "content": "你是一个耐心、直白、适合新手学习的 AI 编程助手。"}
    ]

    print("CLI Chatbot 已启动。输入 exit 退出。")

    while True:
        user_input = input("\n你：").strip()

        if user_input.lower() in ["exit", "quit", "q"]:
            print("AI：再见，今天的小项目完成得不错。")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=model,
            messages=messages,
        )

        assistant_reply = response.choices[0].message.content
        print(f"\nAI：{assistant_reply}")

        messages.append({"role": "assistant", "content": assistant_reply})


if __name__ == "__main__":
    main()