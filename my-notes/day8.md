# Phase 10 LLMs from Scratch 学习笔记

## Tokenizer 是什么

Tokenizer 是把文本切分成 token 的工具。

大语言模型不是直接处理完整句子，而是处理 token。

## Token 是什么

Token 是模型处理文本的基本单位。

一个 token 可能是：

- 一个单词
- 一个词的一部分
- 一个汉字
- 一个标点符号

## Language Modeling 是什么

Language Modeling 的核心任务是：
根据前面的 token，预测下一个 token。

## Inference 是什么

Inference 指模型训练完成后，根据输入生成输出的过程。
我们调用 API 让模型回答问题，就是在做 inference。

## Sampling Strategies 是什么

Sampling Strategies 是模型选择下一个 token 的策略。
不同采样策略会影响回答是否稳定、随机、发散。

## Temperature 是什么

temperature 控制模型输出的随机性。
temperature 越低，模型越稳定
temperature 越高，模型越发散

## Top-p 是什么

top_p 也是控制采样范围的参数。

它会限制模型只从累计概率最高的一部分 token 中选择。

## Max Tokens 是什么

max_tokens 控制模型最多生成多少 token。
它影响：
回答长度
响应时间
成本
是否容易输出过长内容

## Context Window 是什么

Context Window 是模型一次能看到的最大上下文长度。
如果对话历史超过上下文窗口，模型就无法完整看到前面的内容。

## System Prompt 是什么

System Prompt 用来设定模型角色和回答规则。
例如：
你是一个适合新手学习的 AI 老师。
它会影响模型的回答风格。

## 今天跑通了哪些官方代码

今天运行了 Phase 10 LLMs from Scratch 中的官方代码，包括：
01-tokenizer
03-language-modeling
10-inference
12-sampling-strategies
13-context-window

## 今天完成的项目

今天完成了：
my-projects/llm-playground

## 项目实现了：

对比不同 temperature 的输出
对比不同 max_tokens 的输出
对比不同 system prompt 的输出风格
观察推理参数如何影响模型回答

## 今日总结
LLM 应用开发不只是把 prompt 发给模型，还要理解 token、上下文窗口和推理参数如何影响输出。