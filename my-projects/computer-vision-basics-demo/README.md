# Computer Vision Basics Demo

这是一个计算机视觉基础演示项目。

项目目标是理解图片在计算机中的表示方式，以及卷积操作如何提取图像特征。

## 项目功能

本项目完成了以下操作：

1. 创建一张示例 RGB 图片
2. 查看图片的尺寸和通道信息
3. 将 RGB 图片转换为灰度图
4. 使用卷积核进行边缘检测
5. 使用卷积核进行模糊处理
6. 保存处理后的图片结果

## 使用技术

- Python
- NumPy
- Pillow
- 图像数组
- 灰度化
- 卷积操作

## 项目结构

computer-vision-basics-demo/
  main.py
  README.md
  outputs/
    original.png
    gray.png
    edge.png
    blur.png

## 运行方法

先安装依赖：pip install pillow numpy
然后运行：python my-projects\computer-vision-basics-demo\main.py

## 输出结果

运行后会生成四张图片：
original.png：原始示例图
gray.png：灰度图
edge.png：边缘检测结果
blur.png：模糊处理结果

## 核心概念

图像是什么:

在计算机中，图片本质上是一个数字数组。
RGB 图片通常可以表示为：
height x width x channels

灰度图是什么:

灰度图只有一个通道，每个像素表示亮度。
常见转换公式：
gray = 0.299 * R + 0.587 * G + 0.114 * B

卷积是什么:

卷积就是用一个小矩阵在图片上滑动，并对局部区域做计算。
不同卷积核可以产生不同效果：
边缘检测
模糊
锐化
特征提取

CNN 为什么适合图像：

CNN 中的卷积核可以自动学习图像中的局部特征，例如：
边缘
角点
纹理
形状
物体局部结构

## 我学到了什么

通过这个项目，我理解了：
图片在计算机中就是数字矩阵
RGB 图片有 3 个颜色通道
灰度图只有 1 个亮度通道
卷积核可以提取图像特征
CNN 的核心思想就是通过卷积提取视觉特征