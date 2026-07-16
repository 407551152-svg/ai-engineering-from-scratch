# Phase 07 Transformers 学习笔记

## Attention 是什么

Attention 是一种让模型判断“当前 token 应该关注哪些 token”的机制。

它不是平均看所有内容，而是根据相关性分配不同权重。

## Self-Attention 是什么

Self-Attention 是让一句话中的每个 token 互相关注。

比如：

text
I love AI
其中 love 可能会更关注 I 和 AI，因为它们共同决定句子的含义。
## Query / Key / Value 是什么

Query
Query 表示当前 token 想找什么。

Key
Key 表示每个 token 有什么特征可以被匹配。

Value
Value 表示每个 token 真正提供的信息。

## 简单理解：

Query = 我想找什么
Key = 我有什么标签
Value = 我能提供什么内容
Attention Scores 是什么
Attention Scores 表示 token 之间的相关程度。

## 计算方式：

scores = Q x K.T
如果分数高，说明两个 token 更相关。
Softmax 的作用
Softmax 把 attention scores 转换成权重。
转换后每一行加起来等于 1。

## 这样模型就知道：

当前 token 应该从每个 token 那里拿多少信息。
Multi-Head Attention 是什么
Multi-Head Attention 是同时做多组 Attention。
不同 head 可以关注不同关系，例如：
语法关系
主谓关系
指代关系
语义关系

## Positional Encoding 是什么

Transformer 本身不天然知道 token 的顺序。
Positional Encoding 用来告诉模型：
每个 token 在句子中的位置。
否则模型只知道有哪些 token，不知道它们的先后顺序。
Transformer Block 由什么组成
一个 Transformer Block 通常包含：
Self-Attention
LayerNorm
Feed Forward Network
Residual Connection
它的作用是不断更新 token 的表示，让每个 token 融合更多上下文信息。

## GPT 架构是什么

GPT 是基于 Transformer Decoder 的语言模型。
它的核心特点是：
根据前面的 token 预测下一个 token。
所以 GPT 很适合做文本生成。

## 今天跑通了哪些官方代码

今天运行了 Phase 07 Transformers 中的官方代码，包括：
01-attention-mechanism
02-self-attention
03-multi-head-attention
04-positional-encoding
05-transformer-block
07-gpt-architecture

## 今天完成的项目

今天完成了：
my-projects/transformer-attention-demo
项目实现了：
手动定义 token embedding
计算 Query / Key / Value
计算 Attention Scores
使用 Softmax 得到 Attention Weights
加权 Value 得到 Attention Output
打印每个 token 最关注谁

## 今日总结

Transformer 的核心是 Attention，它让模型在处理一个 token 时，能够动态关注上下文中最相关的其他 token。