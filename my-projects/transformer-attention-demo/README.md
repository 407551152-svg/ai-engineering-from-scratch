# Transformer Attention Demo

这是一个 Transformer 注意力机制演示项目。

项目目标是用最简单的 NumPy 代码理解 Self-Attention 的核心流程。

## 项目功能

本项目演示了：

1. Token 如何表示成向量
2. 如何从 Embedding 得到 Query、Key、Value
3. 如何计算 Attention Scores
4. 如何用 Softmax 得到 Attention Weights
5. 如何用 Attention Weights 加权 Value
6. 如何解释每个 Token 关注了谁

## 核心流程

text
Token 向量
-> Query / Key / Value
-> Attention Scores
-> Softmax
-> Attention Weights
-> 加权 Value
-> Attention Output

## 使用技术

Python
NumPy
Matrix Multiplication
Softmax
Scaled Dot-Product Attention

## 运行方法

python my-projects\transformer-attention-demo\main.py

## 核心概念

Query：当前 token 想寻找什么信息。
Key:每个 token 有什么特征可以被别人匹配。
Value:每个 token 真正提供的信息内容。
Attention Score:一个 token 和另一个 token 的相关程度。
计算方式：Q x K.T
Attention Weight：Attention Weight 是经过 softmax 后的注意力权重。表示当前 token 应该从其他 token 中拿多少信息。
Attention Output：Attention Output 是用注意力权重加权 Value 得到的新表示。它已经融合了上下文信息。

## 我学到了什么

通过这个项目，我理解了：

Transformer 的核心是 Attention
Attention 让 token 可以关注上下文中的其他 token
Q/K/V 是从同一个 embedding 变换出来的不同表示
Softmax 把相关性分数变成权重
Self-Attention 的输出是上下文混合后的新向量
LLM 能理解上下文，离不开 Attention