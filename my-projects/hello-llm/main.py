import os
from openai import OpenAI


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    if not api_key:
        raise RuntimeError("请先设置 OPENAI_API_KEY 环境变量")

    client = OpenAI(
        api_key=api_key,
        base_url=base_url if base_url else None,
    )

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一个耐心、直白的 AI 学习助手。"},
            {"role": "user", "content": "用三句话解释什么是 AI Engineering。"},
        ],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()