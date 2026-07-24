import ast
import json
import operator
import os
from datetime import datetime

from openai import OpenAI


# ============================================================
# 第一部分：编写真正执行工作的 Python 工具
# ============================================================

def get_current_time():
    """返回当前本地时间。"""
    now = datetime.now().astimezone()

    return {
        "datetime": now.isoformat(timespec="seconds"),
        "timezone": str(now.tzinfo),
    }


WEATHER_DATA = {
    "北京": {
        "temperature": 28,
        "condition": "晴",
        "humidity": 42,
    },
    "上海": {
        "temperature": 31,
        "condition": "多云",
        "humidity": 68,
    },
    "广州": {
        "temperature": 33,
        "condition": "阵雨",
        "humidity": 79,
    },
}


def get_weather(city):
    """从本地模拟数据中查询天气。"""
    weather = WEATHER_DATA.get(city)

    if weather is None:
        return {
            "found": False,
            "city": city,
            "message": "没有该城市的数据，请尝试北京、上海或广州。",
        }

    return {
        "found": True,
        "city": city,
        **weather,
        "source": "本地模拟数据",
    }


# 允许使用的二元运算符
BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}


# 允许使用的正负号
UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def evaluate_node(node):
    """递归计算经过允许的 AST 节点。"""

    if isinstance(node, ast.Expression):
        return evaluate_node(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("表达式中只能包含数字")

    if isinstance(node, ast.BinOp):
        operation = BINARY_OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("包含不支持的运算符")

        left = evaluate_node(node.left)
        right = evaluate_node(node.right)

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        operation = UNARY_OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("包含不支持的一元运算符")

        return operation(evaluate_node(node.operand))

    raise ValueError("表达式中包含不允许的内容")


def calculate(expression):
    """安全计算基础数学表达式。"""

    if len(expression) > 100:
        raise ValueError("表达式不能超过100个字符")

    tree = ast.parse(expression, mode="eval")
    result = evaluate_node(tree)

    return {
        "expression": expression,
        "result": result,
    }


# ============================================================
# 第二部分：向模型描述可用工具
# ============================================================

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "查询当前本地日期、时间和时区。",
            "parameters": {
                "type": "object",
                "properties": {},
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": (
                "查询指定城市的当前模拟天气。"
                "只用于当前天气，不用于历史天气或天气预报。"
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "城市名称，例如北京",
                    }
                },
                "required": ["city"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "计算基础数学表达式。",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "数学表达式，例如 (18 + 2) * 5",
                    }
                },
                "required": ["expression"],
                "additionalProperties": False,
            },
        },
    },
]


# 工具名和真实 Python 函数的对应关系
TOOL_FUNCTIONS = {
    "get_current_time": get_current_time,
    "get_weather": get_weather,
    "calculate": calculate,
}


# ============================================================
# 第三部分：执行模型选择的工具
# ============================================================

def execute_tool(tool_name, arguments):
    """根据工具名称执行对应的Python函数。"""

    function = TOOL_FUNCTIONS.get(tool_name)

    if function is None:
        return {
            "ok": False,
            "error": f"未知工具：{tool_name}",
        }

    try:
        result = function(**arguments)

        return {
            "ok": True,
            "data": result,
        }

    except ZeroDivisionError:
        return {
            "ok": False,
            "error": "不能除以0",
        }

    except (SyntaxError, ValueError, TypeError) as error:
        return {
            "ok": False,
            "error": str(error),
        }

    except Exception as error:
        return {
            "ok": False,
            "error": f"工具执行失败：{error}",
        }


# ============================================================
# 第四部分：建立模型客户端
# ============================================================

def create_client():
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_BASE_URL")

    if not api_key:
        raise RuntimeError("请先设置 OPENAI_API_KEY 环境变量")

    return OpenAI(
        api_key=api_key,
        base_url=base_url if base_url else None,
    )


# ============================================================
# 第五部分：实现 Tool Calling 循环
# ============================================================

def handle_user_message(client, model, messages):
    """
    完成一次用户请求。

    模型可以连续调用工具，但是最多允许5轮，
    防止模型陷入无限调用。
    """

    for round_number in range(1, 6):
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0,
        )

        assistant_message = response.choices[0].message

        # 保存模型消息
        messages.append(
            assistant_message.model_dump(exclude_none=True)
        )

        # 如果没有工具调用，说明模型准备直接回答
        if not assistant_message.tool_calls:
            return assistant_message.content or "本次没有生成回答。"

        # 模型可能一次调用多个工具
        for tool_call in assistant_message.tool_calls:
            tool_name = tool_call.function.name

            try:
                arguments = json.loads(
                    tool_call.function.arguments
                )
            except json.JSONDecodeError as error:
                tool_result = {
                    "ok": False,
                    "error": f"工具参数不是合法JSON：{error}",
                }
            else:
                print(
                    f"\n[Decide 第{round_number}轮]"
                    f"\n工具：{tool_name}"
                    f"\n参数：{json.dumps(arguments, ensure_ascii=False)}"
                )

                tool_result = execute_tool(
                    tool_name,
                    arguments,
                )

            print(
                "[Execute]"
                f"\n结果：{json.dumps(tool_result, ensure_ascii=False)}"
            )

            # 把工具执行结果交回模型
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(
                        tool_result,
                        ensure_ascii=False,
                    ),
                }
            )

    return "已经达到最多5轮工具调用，本次任务已停止。"


# ============================================================
# 第六部分：命令行主程序
# ============================================================

def main():
    client = create_client()

    model = os.getenv(
        "OPENAI_MODEL",
        "Qwen/Qwen2.5-7B-Instruct",
    )

    messages = [
        {
            "role": "system",
            "content": (
                "你是一个简洁的中文AI助手。"
                "遇到时间、天气或数学计算问题时，"
                "必须优先使用提供的工具。"
                "工具执行失败时，要向用户说明失败原因。"
            ),
        }
    ]

    print("Tool Calling Demo 已启动")
    print(f"当前模型：{model}")
    print("可以询问时间、天气或数学计算。")
    print("输入 exit 退出。")

    while True:
        user_input = input("\n你：").strip()

        if user_input.lower() in {
            "exit",
            "quit",
            "q",
        }:
            print("Demo 已结束。")
            break

        if not user_input:
            continue

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        try:
            answer = handle_user_message(
                client,
                model,
                messages,
            )
        except Exception as error:
            answer = f"模型请求失败：{error}"

        print(f"\nAI：{answer}")


if __name__ == "__main__":
    main()