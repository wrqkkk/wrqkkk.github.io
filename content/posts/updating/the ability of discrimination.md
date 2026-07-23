+++
date = '2026-06-08T11:20:00+08:00'
draft = false
title = '*the ability of discrimination'
isCJKLanguage = true
math = true
+++





# 初探条件期望

## 条件期望的定义

我们在概率空间上定义随机变量 \(X\)，然后对于 \(X\) 和某个 σ-代数 \(\mathcal{F}\)（问：这个 \(\mathcal{F}\) 一定是三元组中的F吗），存在且唯一存在一个随机变量 \(Y\) 满足以下条件：

- 首先是这个随机变量  \(\mathcal{F}\)-measurable
- 其次有，对于 \(\forall A \in \mathcal{F}\)：
  \[
    \int_{A}YdP=\int_{A}XdP
  \]

那么我们把 \(Y\) 记作 \(\mathbb{E}[X|\mathcal{F}]\)，称 \(X\) 关于 \(\mathcal{F}\)的条件期望



> 注：另一种概率论中讲的理解是，条件期望就是条件分布的期望。（待讨论）
> - 它们的区别在于？
> - 什么场合下用什么？
> - 概率论语境下，我们讨论了哪些有关条件期望的事情？
> - 贝叶斯中涉及了哪些条件期望的内容？






