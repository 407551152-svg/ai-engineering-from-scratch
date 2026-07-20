import os
from openai import OpenAI


def create_client():
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")

    if not api_key:
        raise RuntimeError("请先设置 OPENAI_API_KEY 环境变量")

    return OpenAI(
        api_key=api_key,
        base_url=base_url,
    )


def ask_model(client, model, system_prompt, user_prompt, temperature, max_tokens):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content


def run_temperature_experiment(client, model):
    system_prompt = "你是一个清晰、简洁、可靠的 AI 学习助手。"
    user_prompt = "请用三句话解释什么是大语言模型。"

    temperatures = [0.1, 0.5, 0.9]

    print("=" * 60)
    print("Temperature Experiment")
    print("=" * 60)
    print("同一个问题，不同 temperature 会影响回答的稳定性和创造性。")
    print()

    for temperature in temperatures:
        print("-" * 60)
        print(f"temperature = {temperature}")
        print("-" * 60)

        answer = ask_model(
            client=client,
            model=model,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=temperature,
            max_tokens=300,
        )

        print(answer)
        print()


def run_max_tokens_experiment(client, model):
    system_prompt = "你是一个清晰、简洁、可靠的 AI 学习助手。"
    user_prompt = "请解释 Transformer、Attention 和 LLM 之间的关系。"

    max_tokens_list = [80, 200, 500]

    print("=" * 60)
    print("Max Tokens Experiment")
    print("=" * 60)
    print("同一个问题，不同 max_tokens 会影响回答长度。")
    print()

    for max_tokens in max_tokens_list:
        print("-" * 60)
        print(f"max_tokens = {max_tokens}")
        print("-" * 60)

        answer = ask_model(
            client=client,
            model=model,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.3,
            max_tokens=max_tokens,
        )

        print(answer)
        print()


def run_system_prompt_experiment(client, model):
    user_prompt = "请解释什么是 RAG。"

    system_prompts = [
        "你是一个适合新手学习的 AI 老师，请用通俗语言回答。",
        "你是一个严谨的机器学习工程师，请用专业术语回答。",
        "你是一个面试官，请用面试答案的方式回答。",
    ]

    print("=" * 60)
    print("System Prompt Experiment")
    print("=" * 60)
    print("同一个问题，不同 system prompt 会影响回答风格。")
    print()

    for index, system_prompt in enumerate(system_prompts, start=1):
        print("-" * 60)
        print(f"system_prompt #{index}")
        print(system_prompt)
        print("-" * 60)

        answer = ask_model(
            client=client,
            model=model,
            system_prompt=system_prompt,
            user_prompt=user_prompt,
            temperature=0.3,
            max_tokens=300,
        )

        print(answer)
        print()


def main():
    model = os.getenv("OPENAI_MODEL", "Qwen/Qwen2.5-7B-Instruct")

    client = create_client()

    print("LLM Playground")
    print("=" * 60)
    print("Model:", model)
    print()

    run_temperature_experiment(client, model)
    run_max_tokens_experiment(client, model)
    run_system_prompt_experiment(client, model)

    print("=" * 60)
    print("All experiments complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()