# Tiny Neural Network

这是一个使用 NumPy 从零实现的最小神经网络项目。

项目目标是让一个简单的神经网络学习 AND 逻辑：

[0, 0] -> 0
[0, 1] -> 0
[1, 0] -> 0
[1, 1] -> 1

## 项目目标

通过这个项目理解深度学习的基本流程：输入数据 -> 前向传播 -> 计算损失 -> 反向传播 -> 更新参数 -> 预测结果

## 使用技术

Python
NumPy
Sigmoid 激活函数
Binary Cross Entropy 损失函数
Gradient Descent 梯度下降

## 项目结构

tiny-neural-network/
  main.py
  README.md

## 运行方法

在项目根目录执行：python my-projects\tiny-neural-network\main.py

## 核心概念

前向传播
前向传播负责从输入计算预测结果。
X -> hidden layer -> output layer -> prediction


## 损失函数

损失函数用来衡量模型预测错了多少。
本项目使用 Binary Cross Entropy，因为 AND 逻辑是二分类问题。

## 反向传播

反向传播用来计算每个参数对错误的影响。
模型根据这些影响调整权重和偏置。

## 梯度下降

梯度下降负责不断更新参数，让损失逐渐变小。

## 我学到了什么

通过这个项目，我理解了：
神经网络由权重和偏置组成
前向传播负责得到预测结果
损失函数衡量预测错误
反向传播计算参数应该如何调整
梯度下降让模型逐渐学会规律
训练过程就是不断降低 loss 的过程
