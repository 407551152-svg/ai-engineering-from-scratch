# CLI Chatbot

这是一个基于大语言模型 API 的命令行聊天机器人项目。

用户可以在终端中连续输入问题，程序会调用大模型生成回答，并保留当前会话的上下文历史。输入 `exit`、`quit` 或 `q` 可以退出程序。

## 项目功能

- 在命令行中与 AI 连续对话
- 使用 `messages` 保存对话历史
- 支持通过环境变量配置 API Key、模型和接口地址
- 输入退出指令后结束程序

## 使用技术

- Python
- OpenAI Python SDK
- OpenAI-compatible API
- SiliconFlow API

## 运行前准备

先安装依赖：

```powershell
pip install openai

设置环境变量
$env:OPENAI_API_KEY="你的APIKey"
$env:OPENAI_BASE_URL="https://api.siliconflow.cn/v1"
$env:OPENAI_MODEL="Qwen/Qwen2.5-7B-Instruct"

运行项目
python my-projects\cli-chatbot\main.py

运行后可以看到
CLI Chatbot 已启动。输入 exit 退出。

然后可以输入问题提问
例如：
你：你好，你是谁？
AI：我是一个 AI 编程助手，可以帮助你学习编程和 AI 工程。
