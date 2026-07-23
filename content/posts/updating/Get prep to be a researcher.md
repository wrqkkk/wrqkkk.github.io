+++
date = '2026-07-03T20:20:00+08:00'
draft = true
title = 'Weekly Notes'
isCJKLanguage = true
math = true
+++



# Update Plans

- Report：准备记录/汇报后复盘，一般一周2次汇报，见组会周记
- Exploring：1 Questions/day，学会提出高质量的问题并思考，辅以AI
- Paper reading：粗读文献，两天一篇




# Report

## 0701

Start


# Exploring

## 0703
 Done


# Paper Reading

## 0703

### xxx is all you need ？ —— 标题党开山者

Start


### 

## 0718

### 关于CKA，《Similarity of Neural Network Representations Revisited》 ICML 2019,Google Brain


我们作训练，学习，是想要学习到数据中的某种结构，这个结构存在于一个子空间中。

神经网络训练是很黑盒的，不同的initialization，不同的样本数据顺序，不同的网络深度和宽度，都会给结果带来很大的扰动。我们需要一些指标来衡量训练结果/神经网络中的layer训练出来的weights是否是“相似”的。之前很多指标都要求对于可逆线性变换具有不变性（invariance），但这篇论文认为这在样本量远小于特征数的时候就不成立了。

因此我们introduce CKA（Centered Kernel Alignment），对于正交变换具有不变性。另外还讨论了更宽的随机网络的在不同的随机初始化下学到的模型，在同一层的表示上更相似；讨论了早期层比later layer更早饱和，以及同一个神经网络，早期层在不同数据集上能学到更相似的表示（representation）等等。


（未完待续）




## 0722

### 从PCA出发复习线性代数。






