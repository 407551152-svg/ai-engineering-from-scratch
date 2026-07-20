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
        {"role": "system", "content": 
             "你是一个回答清晰、简洁、可靠的 AI 助手。"
            "请优先用用户提问的语言回答。"
            "如果用户用英文提问，就用简单英文回答。"
            "回答要分点，避免重复，不要输出乱码。"
            }       ## 系统消息，定义 AI 的行为和风格(不同类型的ai助手可以有不同的系统消息)
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
    ##优化请求部分的逻辑
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,    ##控制生成文本的随机性，值越高越随机
                max_tokens=500,     ##控制生成文本的长度，值越大生成的文本越长
            )

            assistant_reply = response.choices[0].message.content

            if not assistant_reply:
                assistant_reply = "抱歉，我这次没有生成有效回答，请再试一次。"

        except Exception as error:
            assistant_reply = f"请求失败：{error}"
        
        print(f"\nAI：{assistant_reply}")

        messages.append({"role": "assistant", "content": assistant_reply})

if __name__ == "__main__":
    main()