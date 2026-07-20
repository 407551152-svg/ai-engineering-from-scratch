# LLM Playground

这是一个大语言模型推理参数实验项目。

项目目标是理解不同推理参数如何影响模型输出。

## 项目功能

本项目会进行三组实验：

1. Temperature Experiment
2. Max Tokens Experiment
3. System Prompt Experiment

通过这些实验观察：

- temperature 如何影响回答随机性
- max_tokens 如何影响回答长度
- system prompt 如何影响回答风格

## 使用技术

- Python
- OpenAI Python SDK
- OpenAI-compatible API
- SiliconFlow API

## 运行前准备

先安装依赖：

pip install openai

设置环境变量，此处以siliconflow为例

 $env:OPENAI_API_KEY="你的 API Key"
 $env:OPENAI_API_BASE="https://api.siliconflow.cn/v1"
 $env:OPENAI_MODEL="Qwen/Qwen2.5-7B-Instruct"

运行方法

 python my-projects\llm-playground\main.py

## 核心概念

Token
Token 是大语言模型处理文本的基本单位。
一段文本会先被 tokenizer 切成 token，然后模型基于 token 进行预测。

Inference
Inference 指模型训练好之后，根据输入 prompt 生成回答的过程。

Temperature
temperature 控制模型输出的随机性。
temperature 低：回答更稳定、更保守
temperature 高：回答更发散、更有创造性

Max Tokens
max_tokens 控制模型最多生成多少 token。
它可以影响：
回答长度
响应时间
API 成本

System Prompt
system prompt 用来设定模型的角色、语气和回答规则。
不同 system prompt 会让同一个问题产生不同风格的回答。

## 我学到了什么

通过这个项目，我理解了：
同一个模型在不同参数下会产生不同输出
temperature 会影响回答的稳定性和创造性
max_tokens 会影响回答长度
system prompt 会影响回答风格
LLM 应用开发需要合理控制模型参数