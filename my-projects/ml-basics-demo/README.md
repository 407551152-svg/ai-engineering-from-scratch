# ML Basics Demo

这是一个机器学习基础演示项目。

项目通过两个小例子展示机器学习的基本流程：

1. 线性回归：预测连续值
2. 逻辑回归：完成二分类任务

## 项目目标


理解机器学习项目的基本闭环：准备数据 → 划分训练集和测试集 → 训练模型 → 预测结果 → 评估模型

## 项目功能

1. 线性回归
线性回归用于预测连续数值。
例如：
房价预测
销量预测
成绩预测
温度预测
本项目中，程序会生成一组模拟数据，然后训练一个线性回归模型，并输出预测结果和均方误差。
2. 逻辑回归
逻辑回归用于分类任务。
例如：
是否垃圾邮件
是否通过考试
是否点击广告
是否存在风险
本项目中，程序会生成一组二分类数据，然后训练一个逻辑回归模型，并输出预测类别、预测概率和准确率。

## 使用技术

Python
scikit-learn
LinearRegression
LogisticRegression
train_test_split
mean_squared_error
accuracy_score

## 运行方法

先安装依赖:
pip install scikit-learn
然后在项目根目录运行：
python my-projects\ml-basics-demo\main.py

## 示例输出

LINEAR REGRESSION DEMO
模型任务：根据一个特征预测连续数值
均方误差 MSE: ...

LOGISTIC REGRESSION DEMO
模型任务：根据两个特征判断类别 0 或 1
准确率 Accuracy: ...

## 我学到了什么

通过这个项目，我理解了：
    机器学习是让模型从数据中学习规律  
    训练集用于让模型学习
    测试集用于检查模型效果
    线性回归适合预测连续值
    逻辑回归适合做分类
    评估指标可以帮助我们判断模型好不好

## 和 AI Engineering 的关系

AI Engineering 不只是调用大模型 API，也包括理解模型训练、评估和部署的基本流程。
这个项目是后续学习模型评估、特征工程、Pipeline、RAG 和 Agent 评估的基础。