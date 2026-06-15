+++
date = '2026-06-15T23:20:00+08:00'
draft = false
title = '*CNN learning'
isCJKLanguage = true
math = true
+++



# 什么是CNN

卷积神经网络，convolution neural network

关于卷积：“卷”形式的一种乘积，我们在概率论中有接触过卷积：

**独立随机变量和的分布**里，我们假设

\[
Z=X+Y
\]

那么要得到 (Z=z)，可以有如下组合：

\[
X=t,\quad Y=z-t
\]

我们会发现 \(Z\) 的密度不是简单地 \(f_X(z)f_Y(z)\) 就能得到，而是要把所有可能的 \(t\) 都扫一遍：

\[
f_Z(z)=\int_{-\infty}^{\infty} f_X(t)f_Y(z-t),dt
\]

这里的核心是：**一个变量取 (t)，另一个变量必须取 (z-t)，然后把所有 (t) 对应的贡献加起来**。这就是普通意义上的**卷积 convolution**。


CNN 里的卷积，intuitively，共享同一个“滑动乘积再求和”的结构：

CNN 里的卷积和概率论里的卷积不是同一个应用场景，但数学形式上有类似。给定一张图像或一个二维矩阵，卷积核会在局部区域上做：

\[
\text{output}*{i,j}=\sum*{a,b} \text{kernel}*{a,b}\cdot \text{input}*{i+a,j+b}
\]

这一步的关键在于**局部乘积再求和**。也就是说，卷积核会关注一个小窗口的结果，例如 \(3\times 3\) 区域。它把这九个输入值分别乘上九个权重，然后加起来，得到输出 feature map 上的一个元素。

它和概率论里的卷积相似之处在于，它们都不是孤立地处理一个点，而是把一组局部相关的组合汇总成一个结果。


# 一些术语

## Neural Network
### Head
### Neck
### Backbone

### MLP（Multi Layer Perceptron）


## CNN
### padding

### stride