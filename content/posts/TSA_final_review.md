+++
date = '2026-05-18T13:00:00+09:00'
draft = false
title = 'TSA final review notes'
isCJKLanguage = true
math = true
categories = ['Course Notes']
+++


# Lecture 1: Basic Objects of Time Series

## Part A. 课堂内容还原

### Def 1.1 Time Series

一个 **time series** 是按时间顺序排列的一列随机变量，板书中写成

\[
\{X_n:n\in\mathbb Z\},\qquad X_1,X_2,\ldots .
\]

这里每一个 $X_t$ 都是随机变量，而不是一个确定数值。真正观测到的数据只是这个随机过程的一次 realization，例如

\[
x_1,x_2,\ldots,x_n.
\]

这说明时间序列分析的对象不是一串普通数字，而是背后的随机过程。它不仅关心每个时点自身的随机波动，还关心不同时点之间的依赖结构。

### Def 1.2 Mean Function

时间序列的 **mean function** 定义为

\[
\mu_t=E(X_t),\qquad t\in\mathbb Z.
\]

这里的 $\mu_t$ 可以随时间变化。板书中写 mean function，而不是只写 mean，是因为在时间序列里，均值本身可能是时间的函数。比如某个经济变量长期增长，那么 $E(X_t)$ 就不一定是常数。

### Def 1.3 Autocovariance Function

时间序列的 **autocovariance function** 定义为

\[
\gamma_{t,s}=\operatorname{Cov}(X_t,X_s).
\]

当 $t=s$ 时，

\[
\gamma_{t,t}=\operatorname{Cov}(X_t,X_t)=\operatorname{Var}(X_t).
\]

这个定义刻画两个不同时点之间的线性共同波动。若 $\gamma_{t,s}>0$，说明 $X_t$ 偏高时 $X_s$ 也倾向于偏高；若 $\gamma_{t,s}<0$，说明二者倾向于反向变化；若 $\gamma_{t,s}=0$，说明它们没有线性相关结构。

### Def 1.4 Autocorrelation Function

时间序列的 **autocorrelation function** 定义为

\[
\rho_{t,s}
=\operatorname{Corr}(X_t,X_s)
=\frac{\operatorname{Cov}(X_t,X_s)}
{\sqrt{\operatorname{Var}(X_t)\operatorname{Var}(X_s)}}
=\frac{\gamma_{t,s}}{\sqrt{\gamma_{t,t}\gamma_{s,s}}}.
\]

自相关函数是标准化后的自协方差。它不再受变量单位影响，所以更适合比较两个时间点之间的相关强度。

### Prop 1.5 Covariance of Linear Combinations

若 $a_i,b_j$ 是常数，则

\[
\operatorname{Cov}\left(\sum_i a_iX_i,\sum_j b_jX_j\right)
= \sum_i\sum_j a_i b_j\operatorname{Cov}(X_i,X_j).
\]

这个结论来自协方差的双线性性。它后面会反复使用，因为 random walk、moving average、linear process 都会把 $Y_t$ 写成 white noise 的线性组合。只要模型写成线性组合，计算 $\operatorname{Var}(Y_t)$ 和 $\operatorname{Cov}(Y_t,Y_s)$ 的基本工具就是 Prop 1.5。

### Def 1.6 White Noise

设 $\{e_t\}$ 是一列 **white noise**。在本讲计算中，它满足

\[
E(e_t)=0,\qquad 
\operatorname{Var}(e_t)=\sigma^2,\qquad
\operatorname{Cov}(e_t,e_s)=0\quad (t\ne s).
\]

这里 white noise 表示不同时点之间没有线性相关的随机扰动。它是后面构造 random walk、moving average、ARMA 模型的基本材料。

### Ex 1.7 Random Walk

定义 random walk 为

\[
Y_t=Y_{t-1}+e_t.
\]

若取 $Y_0=0$，递推展开得到

\[
Y_t=e_1+e_2+\cdots+e_t=\sum_{r=1}^t e_r.
\]

因为 $E(e_r)=0$，所以

\[
\mu_t=E(Y_t)
= E\left(\sum_{r=1}^t e_r\right)
= \sum_{r=1}^t E(e_r)
=0.
\]

接着计算自协方差。由 Prop 1.5，

\[
\gamma_{t,s}
= \operatorname{Cov}(Y_t,Y_s)
= \operatorname{Cov}\left(\sum_{r=1}^t e_r,\sum_{\ell=1}^s e_\ell\right)
= \sum_{r=1}^t\sum_{\ell=1}^s \operatorname{Cov}(e_r,e_\ell).
\]

由于 white noise 在不同时间点不相关，只有 $r=\ell$ 的项留下。共同出现的噪声项个数是 $\min(t,s)$，因此

\[
\gamma_{t,s}=\min(t,s)\sigma^2.
\]

特别地，

\[
\gamma_{t,t}=t\sigma^2,\qquad \gamma_{s,s}=s\sigma^2.
\]

所以

\[
\rho_{t,s}
= \frac{\gamma_{t,s}}{\sqrt{\gamma_{t,t}\gamma_{s,s}}}
= \frac{\min(t,s)}{\sqrt{ts}}.
\]

若 $t\ge s$，则

\[
\rho_{t,s}=\sqrt{\frac{s}{t}}.
\]

这个例子很重要。random walk 的均值虽然恒为 $0$，但它的方差

\[
\operatorname{Var}(Y_t)=t\sigma^2
\]

会随时间增长，因此它的二阶结构不是时间不变的。

### Ex 1.8 Moving Average of Order 1

板书中的 moving average 例子为

\[
Y_t=\frac{e_t+e_{t-1}}{2}.
\]

它的均值为

\[
\mu_t=E(Y_t)
= \frac{E(e_t)+E(e_{t-1})}{2}
=0.
\]

自协方差为

\[
\gamma_{t,s}
= \operatorname{Cov}(Y_t,Y_s)
= \operatorname{Cov}\left(
\frac{e_t+e_{t-1}}{2},
\frac{e_s+e_{s-1}}{2}
\right).
\]

由 Prop 1.5 展开，

\[
\gamma_{t,s}
= \frac{1}{4}
\left[
\operatorname{Cov}(e_t,e_s)
+
\operatorname{Cov}(e_t,e_{s-1})
+
\operatorname{Cov}(e_{t-1},e_s)
+
\operatorname{Cov}(e_{t-1},e_{s-1})
\right].
\]

由于 white noise 不同时点之间协方差为 $0$，只有下标相同的项留下。因此

\[
\gamma_{t,s}
= \frac{\sigma^2}{4}
\left[
2\mathbf 1_{\{t=s\}}
+
\mathbf 1_{\{t=s-1\}}
+
\mathbf 1_{\{t=s+1\}}
\right].
\]

也就是说，

\[
\gamma_{t,s}
= \begin{cases}
\dfrac{\sigma^2}{2}, & |t-s|=0,\\[4pt]
\dfrac{\sigma^2}{4}, & |t-s|=1,\\[4pt]
0, & \text{otherwise}.
\end{cases}
\]

因为 $\gamma_{t,t}=\sigma^2/2$，所以自相关函数为

\[
\rho_{t,s}
= \begin{cases}
1, & |t-s|=0,\\[4pt]
\dfrac{1}{2}, & |t-s|=1,\\[4pt]
0, & \text{otherwise}.
\end{cases}
\]

这说明 moving average 的相关性只存在于相邻时间点之间。超过一个 lag 以后，两个变量不再共享同一个 white noise 项，所以自协方差为 $0$。

### Rmk 1.9 Random Walk 与 Moving Average 的比较

比较 Ex 1.7 和 Ex 1.8，可以看到两种过程的核心区别。random walk 中

\[
\gamma_{t,s}=\min(t,s)\sigma^2,
\]

它不仅和时间差有关，还和具体时间位置有关。比如 $Y_{100}$ 的方差明显大于 $Y_1$ 的方差。

而 moving average 中，自协方差只取决于 $|t-s|$。它不关心两个时点具体出现在时间轴上的哪个位置，只关心它们相隔多远。

这就是板书从两个例子过渡到 **stationarity** 的原因。时间序列分析希望找到一种“结构稳定”的过程，使得我们可以用过去的数据学习未来的相关结构。

### Def 1.10 Strict Stationarity

若对任意 $m\ge 1$、任意时间点 $t_1,\ldots,t_m$ 和任意时间平移 $k$，都有

\[
(X_{t_1},X_{t_2},\ldots,X_{t_m})
\overset{d}{=}
(X_{t_1+k},X_{t_2+k},\ldots,X_{t_m+k}),
\]

则称 $\{X_t\}$ 是 **strictly stationary**。

这里 $\overset{d}{=}$ 表示两个随机向量具有相同的联合分布。严格平稳要求很强，它要求任意有限维联合分布在整体时间平移以后完全不变。

### Def 1.11 Weak Stationarity

若时间序列 $\{X_t\}$ 满足有限二阶矩，并且

\[
E(X_t)=\mu,\qquad \forall t,
\]

同时自协方差只依赖于时间差，即

\[
\gamma_{t,s}
= \operatorname{Cov}(X_t,X_s)
= \gamma_{t+k,s+k},
\qquad \forall t,s,k,
\]

等价地说，

\[
\gamma_{t,s}=\gamma(t-s),
\]

则称 $\{X_t\}$ 是 **weakly stationary**，也叫 **second-order stationary**。

弱平稳只要求均值和自协方差结构不随时间平移改变。它不要求完整分布不变，因此比 strict stationarity 弱。时间序列课程中大量模型先从 weak stationarity 出发，因为均值、自协方差、自相关函数正是前面 Def 1.2、Def 1.3、Def 1.4 建立起来的二阶工具。

### Ex 1.12 Stationarity Check for Moving Average

对 Ex 1.8 中的过程

\[
Y_t=\frac{e_t+e_{t-1}}{2},
\]

我们已经得到

\[
E(Y_t)=0,
\]

并且 $\gamma_{t,s}$ 只依赖于 $|t-s|$。因此它的均值不随 $t$ 改变，自协方差只依赖于 lag。由 Def 1.11，这个 moving average 过程是 **weakly stationary**。

相反，Ex 1.7 中 random walk 的方差为

\[
\operatorname{Var}(Y_t)=t\sigma^2,
\]

随时间 $t$ 增大而增大，所以它不是 weakly stationary。

## Part B. 复习视角

Lecture 1 开头真正要建立的是时间序列的 **二阶语言**。Def 1.1 先说明研究对象是一列按时间索引排列的随机变量。紧接着 Def 1.2、Def 1.3、Def 1.4 分别给出 **mean function、autocovariance function、autocorrelation function**。这三个对象构成后面整门课的基础。只要题目问到一个过程是不是平稳、ACF 怎么算、sample ACF 在估计什么，本质上都在回到这三个定义。

这一节最关键的思路是：**时间序列的难点不在单个 $X_t$，而在不同时间点之间的依赖结构**。如果只看均值，Ex 1.7 的 random walk 和 Ex 1.8 的 moving average 都有 $E(Y_t)=0$，看起来差不多。但一算自协方差，差异立刻出现。random walk 的方差是 $t\sigma^2$，随时间增长；moving average 的方差是 $\sigma^2/2$，不随时间改变。这说明均值信息远远不够，必须研究 autocovariance 和 autocorrelation。

紧接着，**Prop 1.5 是后面所有模型计算的基本工具**。Random walk 可以写成 $Y_t=\sum_{r=1}^t e_r$，moving average 可以写成两个 white noise 的线性组合。之后的 linear process、MA(q)、ARMA 模型都会沿着这个方向展开。每次计算 $\operatorname{Var}(Y_t)$ 或 $\operatorname{Cov}(Y_t,Y_s)$，本质上都是用 Prop 1.5 展开，再利用 Def 1.6 中 white noise 的不相关性删掉大部分交叉项。

最后，**stationarity 是为了让时间序列结构可以被稳定学习**。Rmk 1.9 说明 random walk 的二阶结构依赖具体时间位置，而 moving average 的二阶结构只依赖 lag。Def 1.10 的 strict stationarity 要求整个有限维联合分布在时间平移后不变；Def 1.11 的 weak stationarity 只要求均值和自协方差结构不变。后面 TSA 里大量 ACF、MA、AR 模型主要是在 weak stationarity 框架下展开。

复习这节时，最应该熟练掌握的是从模型定义推导 $\mu_t$、$\gamma_{t,s}$、$\rho_{t,s}$ 的流程。以 Ex 1.8 为例，先写出 $Y_t$ 的 white noise 线性组合，再用 Def 1.6 和 Prop 1.5 展开协方差，然后判断哪些噪声项共享同一个时间下标，最后把结果写成只依赖 lag 的形式。这个流程掌握以后，后面遇到 MA(1)、MA(q)、linear process 的 ACF 推导就会自然很多。

---

# Lecture 2: Stationarity, Estimator Properties, and Trend

## Part A. 课堂内容还原

### Rmk 2.1 Stationarity and Dependence across Time

Lecture 2 开头继续强调 TSA 的基本目标。时间序列分析面对的是按时间排列的随机变量，因此不仅要描述单个时点的分布，还要刻画时间点之间的依赖结构。Lecture 1 已经给出了 mean function、autocovariance 和 autocorrelation；现在进入平稳框架以后，这些对象会变得更可估计、更可比较。

对于 weakly stationary process，均值不随时间变化，自协方差只与 lag 有关。因此可以记

\[
\gamma_k=\operatorname{Cov}(Y_t,Y_{t+k}),\qquad k\in\mathbb Z.
\]

特别地，

\[
\gamma_0=\operatorname{Var}(Y_t).
\]

对应的 autocorrelation function 写成

\[
\rho_k
= \operatorname{Corr}(Y_t,Y_{t+k})
= \frac{\gamma_k}{\gamma_0}.
\]

这套 notation 很重要。只要过程 weakly stationary，原本带两个时间下标的 $\gamma_{t,s}$ 就可以压缩成只带一个 lag 下标的 $\gamma_k$。

### Def 2.2 Trend Decomposition

为了处理非平稳均值，板书引入趋势分解：

\[
Y_t=\mu_t+X_t,
\]

其中

\[
E(X_t)=0,
\]

并且 $X_t$ 通常被假设为 stationary process。这里 $\mu_t$ 表示 deterministic trend，也可以包含 seasonal 或 periodic component；$X_t$ 表示围绕趋势波动的 stationary residual。

这个分解的思想是：原始序列 $Y_t$ 可能不是 stationary，但减去 deterministic component 以后，剩下的随机扰动 $X_t$ 可能是 stationary。之后估计 trend、去趋势、再分析残差相关结构，都是沿着这个分解进行的。

### Ex 2.3 Constant Mean Model

最简单的趋势模型是假设均值为常数：

\[
\mu_t=\mu.
\]

此时模型为

\[
Y_t=\mu+X_t,\qquad E(X_t)=0.
\]

自然的估计量是样本均值：

\[
\hat{\mu}=\bar{Y}=\frac{1}{n}\sum_{t=1}^n Y_t.
\]

因为 $E(Y_t)=\mu$，所以

\[
E(\hat{\mu})
= E\left(\frac{1}{n}\sum_{t=1}^n Y_t\right)
= \frac{1}{n}\sum_{t=1}^n E(Y_t)
= \mu.
\]

因此 $\hat{\mu}$ 是 $\mu$ 的 unbiased estimator。

### Def 2.4 Unbiasedness

若估计量 $\hat{\theta}$ 满足

\[
E(\hat{\theta})=\theta,
\]

则称 $\hat{\theta}$ 是 $\theta$ 的 **unbiased estimator**。

unbiasedness 是有限样本意义下的性质。它说明估计量的期望正好等于目标参数，但这不意味着单次样本估计一定接近真值，也不意味着样本量增大时一定收敛到真值。

### Def 2.5 Consistency

若估计量 $\hat{\theta}_n$ 满足

\[
\hat{\theta}_n\overset{p}{\longrightarrow}\theta,\qquad n\to\infty,
\]

则称 $\hat{\theta}_n$ 是 $\theta$ 的 **consistent estimator**。

按定义，convergence in probability 表示对任意 $\varepsilon>0$，

\[
P(|\hat{\theta}_n-\theta|>\varepsilon)\to 0,\qquad n\to\infty.
\]

板书中还提到 strong convergence almost surely：

\[
\hat{\theta}_n\overset{a.s.}{\longrightarrow}\theta.
\]

strong convergence 比 convergence in probability 更强。TSA 中很多估计量先用二阶矩工具证明 mean-square convergence，再推出 convergence in probability。

### Lem 2.6 Markov Inequality and Chebyshev-type Argument

若随机变量 $Z\ge 0$，则 Markov inequality 给出

\[
P(Z>\varepsilon)\le \frac{E(Z)}{\varepsilon}.
\]

令

\[
Z=|\hat{\theta}_n-\theta|^k,\qquad k>0,
\]

则

\[
P(|\hat{\theta}_n-\theta|>\varepsilon)
= P(|\hat{\theta}_n-\theta|^k>\varepsilon^k)
\le
\frac{E|\hat{\theta}_n-\theta|^k}{\varepsilon^k}.
\]

特别地，当 $k=2$ 时，

\[
P(|\hat{\theta}_n-\theta|>\varepsilon)
\le
\frac{E(\hat{\theta}_n-\theta)^2}{\varepsilon^2}.
\]

因此，如果

\[
E(\hat{\theta}_n-\theta)^2\to 0,
\]

那么

\[
\hat{\theta}_n\overset{p}{\longrightarrow}\theta.
\]

若估计量无偏，则

\[
E(\hat{\theta}_n-\theta)^2
= \operatorname{Var}(\hat{\theta}_n).
\]

所以对于 unbiased estimator，只要

\[
\operatorname{Var}(\hat{\theta}_n)\to 0,
\]

就可以推出 consistency。

### Ex 2.7 Variance of the Sample Mean under Stationarity

继续 Ex 2.3。设 $Y_t$ weakly stationary，均值为 $\mu$，自协方差为 $\gamma_k$。样本均值为

\[
\bar{Y}=\frac{1}{n}\sum_{t=1}^n Y_t.
\]

它的方差为

\[
\operatorname{Var}(\bar{Y})
= \operatorname{Var}\left(\frac{1}{n}\sum_{t=1}^nY_t\right)
= \frac{1}{n^2}\sum_{t=1}^n\sum_{s=1}^n
\operatorname{Cov}(Y_t,Y_s).
\]

由于过程 stationary，$\operatorname{Cov}(Y_t,Y_s)=\gamma_{t-s}$。把双重求和按 lag 分组，得到

\[
\operatorname{Var}(\bar{Y})
= \frac{1}{n^2}
\left[
n\gamma_0
+
2\sum_{k=1}^{n-1}(n-k)\gamma_k
\right].
\]

写成 autocorrelation 的形式：

\[
\operatorname{Var}(\bar{Y})
= \frac{\gamma_0}{n}
\left[
1+
2\sum_{k=1}^{n-1}
\left(1-\frac{k}{n}\right)\rho_k
\right].
\]

这个公式说明样本均值的方差不仅取决于单点方差 $\gamma_0$，还取决于所有 lag 的相关性 $\rho_k$。如果正相关很强，样本均值的方差会比 independent case 更大。

### Ex 2.8 White Noise Case

若 $Y_t$ 是 white noise 或者没有 serial correlation，则

\[
\rho_k=0,\qquad k\ge 1.
\]

因此 Ex 2.7 的公式化为

\[
\operatorname{Var}(\bar{Y})=\frac{\gamma_0}{n}.
\]

于是

\[
\operatorname{Var}(\bar{Y})\to 0.
\]

结合 Ex 2.3 的 unbiasedness 和 Lem 2.6，得到

\[
\bar{Y}\overset{p}{\longrightarrow}\mu.
\]

所以在 white noise 情形下，样本均值是 $\mu$ 的 consistent estimator。

### Ex 2.9 Finite Dependence / Moving Average Case

若过程是 MA(q) 型，或者更一般地说只存在有限阶相关，即

\[
\rho_k=0,\qquad k>q,
\]

则

\[
\operatorname{Var}(\bar{Y})
= \frac{\gamma_0}{n}
\left[
1+
2\sum_{k=1}^{q}
\left(1-\frac{k}{n}\right)\rho_k
\right].
\]

括号中的项在 $n\to\infty$ 时保持有界，因此

\[
\operatorname{Var}(\bar{Y})=O\left(\frac{1}{n}\right).
\]

于是样本均值仍然 consistent。这解释了为什么短程相关不会破坏样本均值的一致性，但会改变它的 finite-sample variance。

### Ex 2.10 Geometrically Decaying Correlation

若

\[
\rho_k=\phi^k,\qquad |\phi|<1,
\]

则相关性以几何速度衰减。因为

\[
\sum_{k=1}^{\infty}|\phi|^k<\infty,
\]

所以

\[
\sum_{k=1}^{n-1}
\left(1-\frac{k}{n}\right)\rho_k
\]

保持有界，从而

\[
\operatorname{Var}(\bar{Y})=O\left(\frac{1}{n}\right).
\]

因此

\[
\bar{Y}\overset{p}{\longrightarrow}\mu.
\]

这个例子说明，只要 autocorrelation 衰减得足够快，样本均值仍然可以稳定估计总体均值。

### Def 2.11 Big-O and Little-o Notation

若存在常数 $C>0$ 和足够大的 $n$，使得

\[
|a_n|\le C|b_n|,
\]

则记作

\[
a_n=O(b_n).
\]

如果

\[
\frac{a_n}{b_n}\to 0,
\]

则记作

\[
a_n=o(b_n).
\]

特别地，

\[
a_n=O(1)
\]

表示 $a_n$ 有界，而

\[
a_n=o(1)
\]

表示 $a_n\to 0$。

这些 notation 用来压缩渐近阶数。比如在 Ex 2.9 和 Ex 2.10 中，$\operatorname{Var}(\bar{Y})=O(1/n)$ 表示样本均值方差以 $1/n$ 的阶下降。

### Ex 2.12 Linear Trend Model

现在考虑线性趋势模型：

\[
Y_t=\beta_0+\beta_1 t+X_t,\qquad E(X_t)=0.
\]

记

\[
Q(\beta_0,\beta_1)
= \sum_{t=1}^n
\left(Y_t-\beta_0-\beta_1t\right)^2.
\]

OLS estimator 通过最小化 $Q$ 得到。对 $\beta_0$ 求偏导并令其为 0：

\[
\frac{\partial Q}{\partial \beta_0}
= -2\sum_{t=1}^n
\left(Y_t-\beta_0-\beta_1t\right)
=0.
\]

于是

\[
\bar{Y}=\hat{\beta}_0+\hat{\beta}_1\bar{t}.
\]

对 $\beta_1$ 求偏导并令其为 0：

\[
\frac{\partial Q}{\partial \beta_1}
= -2\sum_{t=1}^n
t\left(Y_t-\beta_0-\beta_1t\right)
=0.
\]

结合第一条 normal equation，可以得到

\[
\hat{\beta}_1
= \frac{\sum_{t=1}^n(t-\bar{t})Y_t}
{\sum_{t=1}^n(t-\bar{t})^2},
\qquad
\hat{\beta}_0
= \bar{Y}-\hat{\beta}_1\bar{t}.
\]

因为

\[
Y_t=\beta_0+\beta_1t+X_t,
\]

且 $E(X_t)=0$，所以

\[
E(\hat{\beta}_1)=\beta_1,
\qquad
E(\hat{\beta}_0)=\beta_0.
\]

因此在线性趋势模型中，OLS estimator 是 unbiased 的。

### Prop 2.13 Order of the Linear Trend Estimator Variance

对 Ex 2.12 中的斜率估计量，记

\[
w_t=\frac{t-\bar{t}}{\sum_{s=1}^n(s-\bar{t})^2}.
\]

则

\[
\hat{\beta}_1-\beta_1=\sum_{t=1}^n w_t X_t.
\]

因此

\[
\operatorname{Var}(\hat{\beta}_1)
= \sum_{t=1}^n\sum_{s=1}^n
w_tw_s\operatorname{Cov}(X_t,X_s).
\]

如果 $X_t$ 是 weakly stationary 且相关性衰减足够快，则分母

\[
\sum_{t=1}^n(t-\bar{t})^2
\]

的阶为 $O(n^3)$，而协方差加权和可控，最终得到

\[
\operatorname{Var}(\hat{\beta}_1)=O(n^{-3}).
\]

这说明线性趋势的斜率估计比普通均值估计收敛更快，因为时间指标 $t$ 本身提供了越来越大的离散程度。

### Ex 2.14 Piecewise or Seasonal Trend Motivation

板书随后引入更复杂的 trend，例如某些趋势可能按月份、季度、阶段改变。直观上，常数均值和线性趋势都太简单；如果数据存在季节性，均值结构可能不是一条直线，而是按周期重复。

例如月度数据可以有 12 个季节均值：

\[
\mu_t=\beta_j,\qquad t=j, j+12, j+24,\ldots,\quad j=1,\ldots,12.
\]

也可以用三角函数表达周期项，例如

\[
\mu_t
= \beta_0+\beta_1t+
\beta_2\cos\left(\frac{2\pi t}{12}\right)
+
\beta_3\sin\left(\frac{2\pi t}{12}\right).
\]

这些模型都属于 deterministic trend 或 deterministic seasonal component 的估计问题。核心仍然是先估计 $\mu_t$，再把 $Y_t-\hat{\mu}_t$ 当作 residual process 研究。

## Part B. 复习视角

Lecture 2 的主线是从 **stationarity 的 notation** 进入 **趋势估计与估计量性质**。Rmk 2.1 把 weak stationarity 的自协方差写成 $\gamma_k$，这一步非常关键。它把 Lecture 1 的 $\gamma_{t,s}$ 压缩成只依赖 lag 的函数，使得后面讨论 $\bar{Y}$、sample autocovariance 和 sample ACF 成为可能。

这一讲的第一个关键点是 **unbiasedness 与 consistency 的区别**。Def 2.4 只关心 $E(\hat{\theta})=\theta$，它是“平均意义上不偏”。Def 2.5 关心 $\hat{\theta}_n\overset{p}{\to}\theta$，它是“大样本下越来越接近真值”。Lem 2.6 给出了课程里最常用的证明套路：先控制 $E(\hat{\theta}_n-\theta)^2$，再用 Markov/Chebyshev inequality 推出 convergence in probability。

第二个关键点是 **serial correlation 会进入样本均值方差**。Ex 2.7 的公式

\[
\operatorname{Var}(\bar{Y})
= \frac{\gamma_0}{n}
\left[
1+
2\sum_{k=1}^{n-1}
\left(1-\frac{k}{n}\right)\rho_k
\right]
\]

是这一讲最重要的公式之一。它直接说明：样本均值是否稳定，不只看样本量，还看时间序列的相关结构。如果相关性有限或者衰减够快，如 Ex 2.9 和 Ex 2.10，则 $\operatorname{Var}(\bar{Y})=O(1/n)$，样本均值仍然 consistent。

第三个关键点是 **trend estimation 的逻辑**。Def 2.2 把 $Y_t$ 拆成 $\mu_t+X_t$。如果 $\mu_t$ 是常数，就用 sample mean；如果 $\mu_t$ 是线性函数，就用 OLS；如果 $\mu_t$ 有季节性，就用 dummy variables 或 sine/cosine terms。无论形式多复杂，本质都是先估计 deterministic component，再分析剩下的 stationary residual。

---

# Lecture 3: Trend Models and Linear Regression Form

## Part A. 课堂内容还原

### Rmk 3.1 General Trend Framework

Lecture 3 继续围绕 trend 展开。基本模型仍然是

\[
Y_t=\mu_t+X_t,
\qquad
E(X_t)=0,
\]

其中 $X_t$ 是 stationary process。Lecture 2 已经讨论了常数均值和线性趋势，Lecture 3 进一步系统整理不同 $\mu_t$ 的估计方式。

### Ex 3.2 Constant Trend

若

\[
\mu_t=\mu,
\]

则

\[
Y_t=\mu+X_t.
\]

估计量仍然是

\[
\hat{\mu}=\bar{Y}=\frac{1}{n}\sum_{t=1}^nY_t.
\]

这对应 Lecture 2 的 Ex 2.3。它是 trend estimation 中最基础的情形。

### Ex 3.3 Linear Trend

若

\[
\mu_t=\beta_0+\beta_1t,
\]

则

\[
Y_t=\beta_0+\beta_1t+X_t.
\]

OLS estimator 为

\[
\hat{\beta}_1
= \frac{\sum_{t=1}^n(t-\bar{t})Y_t}
{\sum_{t=1}^n(t-\bar{t})^2},
\qquad
\hat{\beta}_0
= \bar{Y}-\hat{\beta}_1\bar{t}.
\]

这个模型用一条直线描述 deterministic trend。它适合长期均值随时间单调变化的数据，但不能描述周期性重复模式。

### Def 3.4 Seasonal Dummy Trend

若数据有周期 $p$，可以用 $p$ 个季节均值描述：

\[
\mu_t=\beta_j,\qquad t=j+kp,\quad j=1,\ldots,p,\quad k=0,1,\ldots .
\]

对于月度数据，常见情形是 $p=12$，于是

\[
\mu_t=\beta_j,\qquad t=j+12k,\quad j=1,\ldots,12.
\]

这里 $\beta_j$ 表示第 $j$ 个季节位置的平均水平。比如 $j=1$ 可以表示所有 1 月，$j=2$ 表示所有 2 月，以此类推。

### Ex 3.5 Estimator for Seasonal Dummy Means

设总共有 $N$ 个完整周期，因此样本量为

\[
n=Np.
\]

对第 $j$ 个季节位置，估计量是该位置跨所有周期的平均：

\[
\hat{\beta}_j
= \frac{1}{N}
\sum_{k=0}^{N-1}
Y_{j+kp},
\qquad j=1,\ldots,p.
\]

在 $p=12$ 的月度数据中，

\[
\hat{\beta}_j
= \frac{1}{N}
\sum_{k=0}^{N-1}
Y_{j+12k},
\qquad j=1,\ldots,12.
\]

因为

\[
E(Y_{j+kp})=\beta_j,
\]

所以

\[
E(\hat{\beta}_j)=\beta_j.
\]

因此 $\hat{\beta}_j$ 是 unbiased estimator。

若 $X_t$ 是 stationary residual，则

\[
\operatorname{Var}(\hat{\beta}_j)
= \frac{1}{N^2}
\sum_{r=0}^{N-1}
\sum_{s=0}^{N-1}
\operatorname{Cov}(X_{j+rp},X_{j+sp}).
\]

由 stationarity，

\[
\operatorname{Cov}(X_{j+rp},X_{j+sp})
= \gamma_{(r-s)p}.
\]

因此

\[
\operatorname{Var}(\hat{\beta}_j)
= \frac{1}{N^2}
\left[
N\gamma_0
+
2\sum_{h=1}^{N-1}(N-h)\gamma_{hp}
\right].
\]

这与 Lecture 2 中样本均值方差的结构完全相同，只是 lag 以周期 $p$ 为单位跳跃。

### Def 3.6 Sinusoidal Trend Model

除了 seasonal dummy，也可以用 sine/cosine 表示周期趋势。对周期 $p$，模型写成

\[
\mu_t
= \beta_0
+
\beta_1\cos\left(\frac{2\pi t}{p}\right)
+
\beta_2\sin\left(\frac{2\pi t}{p}\right).
\]

于是

\[
Y_t
= \beta_0
+
\beta_1\cos\left(\frac{2\pi t}{p}\right)
+
\beta_2\sin\left(\frac{2\pi t}{p}\right)
+
X_t.
\]

这个模型用一对正弦余弦函数刻画一个周期性波动。与 seasonal dummy 相比，它更平滑，参数更少；但如果真实季节效应形状很不规则，它可能不如 dummy model 灵活。

### Prop 3.7 Orthogonality Identities for Complete Periods

若样本覆盖完整周期，并且 $n$ 是 $p$ 的倍数，则三角函数项满足近似或精确的正交关系：

\[
\sum_{t=1}^n\cos\left(\frac{2\pi t}{p}\right)=0,
\qquad
\sum_{t=1}^n\sin\left(\frac{2\pi t}{p}\right)=0,
\]

\[
\sum_{t=1}^n
\cos\left(\frac{2\pi t}{p}\right)
\sin\left(\frac{2\pi t}{p}\right)
=0,
\]

\[
\sum_{t=1}^n
\cos^2\left(\frac{2\pi t}{p}\right)
= \frac{n}{2},
\qquad
\sum_{t=1}^n
\sin^2\left(\frac{2\pi t}{p}\right)
= \frac{n}{2}.
\]

这些正交关系使得 OLS estimator 可以写成非常简单的投影形式。

### Ex 3.8 Estimators in the Sinusoidal Trend Model

在 Def 3.6 的模型中，若使用 Prop 3.7 的完整周期正交关系，则 OLS estimator 为

\[
\hat{\beta}_0
= \bar{Y}
= \frac{1}{n}\sum_{t=1}^nY_t,
\]

\[
\hat{\beta}_1
= \frac{2}{n}
\sum_{t=1}^n
\cos\left(\frac{2\pi t}{p}\right)Y_t,
\]

\[
\hat{\beta}_2
= \frac{2}{n}
\sum_{t=1}^n
\sin\left(\frac{2\pi t}{p}\right)Y_t.
\]

这些式子可以理解为把 $Y_t$ 投影到常数项、cosine 项和 sine 项上。由于三者彼此正交，所以每个系数都可以单独用内积形式估计。

### Prop 3.9 Variance Order for Sinusoidal Estimators

以 $\hat{\beta}_0$ 为例，

\[
\operatorname{Var}(\hat{\beta}_0)
= \operatorname{Var}\left(\frac{1}{n}\sum_{t=1}^nY_t\right).
\]

若 residual process $X_t$ 的 autocorrelation 衰减足够快，则由 Lecture 2 的 Ex 2.7 推出

\[
\operatorname{Var}(\hat{\beta}_0)=O\left(\frac{1}{n}\right).
\]

对 $\hat{\beta}_1$，

\[
\operatorname{Var}(\hat{\beta}_1)
= \operatorname{Var}\left[
\frac{2}{n}
\sum_{t=1}^n
\cos\left(\frac{2\pi t}{p}\right)X_t
\right].
\]

展开后得到

\[
\operatorname{Var}(\hat{\beta}_1)
= \frac{4}{n^2}
\sum_{t=1}^n\sum_{s=1}^n
\cos\left(\frac{2\pi t}{p}\right)
\cos\left(\frac{2\pi s}{p}\right)
\gamma_{t-s}.
\]

在 white noise case 下，只有 $t=s$ 的项留下，因此

\[
\operatorname{Var}(\hat{\beta}_1)
= \frac{4}{n^2}
\sum_{t=1}^n
\cos^2\left(\frac{2\pi t}{p}\right)\sigma^2
= \frac{4}{n^2}\cdot \frac{n}{2}\sigma^2
= \frac{2\sigma^2}{n}.
\]

同理，

\[
\operatorname{Var}(\hat{\beta}_2)
= \frac{2\sigma^2}{n}.
\]

如果 residual 有短程相关或相关性衰减足够快，上述方差仍然是 $O(1/n)$ 的阶。

### Def 3.10 General Linear Trend Model

将前面的常数趋势、线性趋势、seasonal dummy 和 sinusoidal trend 统一起来，可以写成 general linear model：

\[
Y_t=\mu_t+X_t,
\qquad
\mu_t=\sum_{j=1}^{p}\beta_j z_{tj}.
\]

这里 $z_{tj}$ 是已知的 deterministic regressor，$\beta_j$ 是未知参数。写成矩阵形式：

\[
Y=X\beta+\varepsilon,
\]

其中

\[
Y=(Y_1,\ldots,Y_n)^T,
\qquad
\beta=(\beta_1,\ldots,\beta_p)^T,
\]

\[
X=
\begin{pmatrix}
z_{11} & z_{12} & \cdots & z_{1p}\\
z_{21} & z_{22} & \cdots & z_{2p}\\
\vdots & \vdots & \ddots & \vdots\\
z_{n1} & z_{n2} & \cdots & z_{np}
\end{pmatrix}.
\]

这个形式把“估计趋势”统一为一个线性回归问题。

### Prop 3.11 OLS Estimator in the General Linear Model

若 $X^TX$ 可逆，则 OLS estimator 为

\[
\hat{\beta}
= (X^TX)^{-1}X^TY.
\]

因为

\[
Y=X\beta+\varepsilon,
\]

所以

\[
\hat{\beta}
= (X^TX)^{-1}X^T(X\beta+\varepsilon)
= \beta+(X^TX)^{-1}X^T\varepsilon.
\]

若

\[
E(\varepsilon)=0,
\]

则

\[
E(\hat{\beta})=\beta.
\]

因此 OLS estimator 是 unbiased 的。

### Prop 3.12 Covariance Matrix of the OLS Estimator under Time-series Errors

令

\[
\Gamma=\operatorname{Var}(\varepsilon)
= \begin{pmatrix}
\gamma_0 & \gamma_1 & \cdots & \gamma_{n-1}\\
\gamma_1 & \gamma_0 & \cdots & \gamma_{n-2}\\
\vdots & \vdots & \ddots & \vdots\\
\gamma_{n-1} & \gamma_{n-2} & \cdots & \gamma_0
\end{pmatrix}
\]

表示 residual 的 covariance matrix。由于时间序列误差通常不是 independent，所以 $\Gamma$ 一般不是 $\sigma^2I_n$。

由

\[
\hat{\beta}-\beta=(X^TX)^{-1}X^T\varepsilon,
\]

可得

\[
\operatorname{Var}(\hat{\beta})
= (X^TX)^{-1}X^T\Gamma X(X^TX)^{-1}.
\]

如果误差是 white noise，则

\[
\Gamma=\sigma^2I_n,
\]

于是退化为普通线性回归中的公式

\[
\operatorname{Var}(\hat{\beta})
= \sigma^2(X^TX)^{-1}.
\]

板书在这里强调的重点是：**OLS 点估计公式不因为时间序列相关而改变，但方差公式会改变**。这也是 TSA 和普通回归课程之间最重要的连接点之一。

## Part B. 复习视角

Lecture 3 的主线是把 trend estimation 从具体例子提升到 **general linear model**。Ex 3.2 是常数均值，Ex 3.3 是线性趋势，Def 3.4 和 Ex 3.5 是 seasonal dummy，Def 3.6 到 Prop 3.9 是 sinusoidal trend。它们看起来形式不同，但 Def 3.10 说明它们都可以写成 $Y=X\beta+\varepsilon$。

这一讲最关键的概念是 **deterministic regressors 与 stationary residual 的分离**。趋势项不是随机建模的重点，它是我们先从数据里拿掉的 deterministic component。真正具有时间序列结构的是 residual $X_t$。所以这门课不是把回归当作终点，而是把回归当作去趋势工具。去掉 $\hat{\mu}_t$ 之后，才进入 stationary residual 的建模。

另一个关键点是 **orthogonality**。Prop 3.7 解释了为什么 sine/cosine 模型的估计量能写得那么简单。完整周期下，constant、cosine、sine 彼此正交，所以 OLS estimator 等价于把数据投影到这些基函数上。这和 Gram matrix、inner product 的思想是连在一起的：回归系数本质上是在一组基函数张成的空间里做投影。

最后要特别注意 Prop 3.12。普通回归里我们熟悉 $\sigma^2(X^TX)^{-1}$，但时间序列误差有 autocovariance，所以 covariance matrix 变成 Toeplitz 形式的 $\Gamma$。因此 OLS estimator 仍然 unbiased，但 standard error 不能直接照搬 independent error 的公式。这一点会影响后面所有关于 trend estimator precision 的讨论。

---

# Lecture 4: Linear Processes and Moving Average Models

## Part A. 课堂内容还原

### Def 4.1 Linear Process, Finite Approximation

Lecture 4 进入 stationary time series models。先从 finite linear process 出发：

\[
Y_{t,m}
= \sum_{j=0}^{m}\psi_j e_{t-j},
\]

其中 $\{e_t\}$ 是 white noise，满足

\[
E(e_t)=0,\qquad \operatorname{Var}(e_t)=\sigma^2,\qquad
\operatorname{Cov}(e_t,e_s)=0\quad (t\ne s).
\]

这里 $Y_{t,m}$ 是把当前和过去 $m$ 期 white noise 按权重 $\psi_j$ 线性组合起来。moving average model 是 linear process 的有限阶特例。

### Def 4.2 Convergence in $L^2$

随机变量序列 $X_m$ 在 $L^2$ 中收敛到 $X$，记作

\[
X_m\overset{L^2}{\longrightarrow}X,
\]

如果

\[
E|X_m-X|^2\to 0,\qquad m\to\infty.
\]

这是 mean-square convergence。它比 convergence in probability 更强，因为由 Markov inequality，

\[
P(|X_m-X|>\varepsilon)
\le
\frac{E|X_m-X|^2}{\varepsilon^2}.
\]

所以

\[
X_m\overset{L^2}{\longrightarrow}X
\quad\Longrightarrow\quad
X_m\overset{p}{\longrightarrow}X.
\]

### Lem 4.3 $L^2$-Cauchy Criterion for Linear Processes

考虑

\[
Y_{t,m}
= \sum_{j=0}^{m}\psi_j e_{t-j}.
\]

若

\[
\sum_{j=0}^{\infty}\psi_j^2<\infty,
\]

则 $Y_{t,m}$ 在 $L^2$ 中是 Cauchy sequence。因为当 $m>r$ 时，

\[
Y_{t,m}-Y_{t,r}
= \sum_{j=r+1}^{m}\psi_j e_{t-j}.
\]

于是

\[
E|Y_{t,m}-Y_{t,r}|^2
= E\left(
\sum_{j=r+1}^{m}\psi_j e_{t-j}
\right)^2.
\]

利用 white noise 的不相关性，交叉项消失，得到

\[
E|Y_{t,m}-Y_{t,r}|^2
= \sigma^2\sum_{j=r+1}^{m}\psi_j^2.
\]

由于 $\sum_{j=0}^{\infty}\psi_j^2<\infty$，尾和趋于 0，因此

\[
E|Y_{t,m}-Y_{t,r}|^2\to 0.
\]

所以有限截断 $Y_{t,m}$ 在 $L^2$ 中有极限。

### Def 4.4 General Linear Process

若

\[
\sum_{j=0}^{\infty}\psi_j^2<\infty,
\]

则定义 **general linear process** 为

\[
Y_t
= \sum_{j=0}^{\infty}\psi_j e_{t-j}.
\]

在很多书写中会取

\[
\psi_0=1.
\]

条件 $\sum \psi_j^2<\infty$ 是过程有意义的关键。它保证 infinite sum 在 $L^2$ 下收敛，从而 $Y_t$ 有有限方差。

### Prop 4.5 Mean and Variance of a Linear Process

对 Def 4.4 中的 linear process，

\[
Y_t = \sum_{j=0}^{\infty}\psi_j e_{t-j},
\]

因为 $E(e_{t-j})=0$，所以

\[
E(Y_t) = \sum_{j=0}^{\infty}\psi_jE(e_{t-j})
= 0.
\]

方差为

\[
\operatorname{Var}(Y_t)
= \operatorname{Var}
\left(
\sum_{j=0}^{\infty}\psi_j e_{t-j}
\right).
\]

利用 white noise 的不相关性，得到

\[
\operatorname{Var}(Y_t)
= \sigma^2\sum_{j=0}^{\infty}\psi_j^2.
\]

由于 $\sum_{j=0}^{\infty}\psi_j^2<\infty$，因此

\[
\operatorname{Var}(Y_t)<\infty.
\]

### Prop 4.6 Autocovariance Function of a Linear Process

对 Def 4.4 中的 process，计算 lag $\ell$ 的 autocovariance：

\[
\gamma_\ell
= \operatorname{Cov}(Y_t,Y_{t+\ell}).
\]

代入 linear process 表达式：

\[
\gamma_\ell
= \operatorname{Cov}
\left(
\sum_{j=0}^{\infty}\psi_j e_{t-j},
\sum_{k=0}^{\infty}\psi_k e_{t+\ell-k}
\right).
\]

展开协方差：

\[
\gamma_\ell
= \sum_{j=0}^{\infty}\sum_{k=0}^{\infty}
\psi_j\psi_k
\operatorname{Cov}(e_{t-j},e_{t+\ell-k}).
\]

由于 white noise 不同时点不相关，只有

\[
t-j=t+\ell-k
\]

即

\[
k=j+\ell
\]

时保留。于是对 $\ell\ge0$，

\[
\gamma_\ell
= \sigma^2
\sum_{j=0}^{\infty}\psi_j\psi_{j+\ell}.
\]

由 Cauchy-Schwarz inequality，

\[
\sum_{j=0}^{\infty}|\psi_j\psi_{j+\ell}|
\le
\left(\sum_{j=0}^{\infty}\psi_j^2\right)^{1/2}
\left(\sum_{j=0}^{\infty}\psi_{j+\ell}^2\right)^{1/2}
<\infty.
\]

因此 autocovariance 是 well-defined 的，并且只依赖 lag $\ell$，不依赖具体时间 $t$。这说明 general linear process 是 weakly stationary。

### Ex 4.7 MA(1) as a Linear Process

MA(1) 模型写作

\[
Y_t=e_t-\theta e_{t-1}.
\]

它对应的 linear process 系数为

\[
\psi_0=1,\qquad \psi_1=-\theta,\qquad \psi_j=0\quad (j\ge2).
\]

因此

\[
\sum_{j=0}^{\infty}\psi_j^2
= 1+\theta^2
<\infty.
\]

所以 MA(1) 是 well-defined 的 stationary linear process。

### Ex 4.8 MA(q) Model

MA(q) 模型写作

\[
Y_t=e_t-\theta_1e_{t-1}+\theta_2e_{t-2}+\cdots+\theta_qe_{t-q}.
\]

也可以统一写成

\[
Y_t
= \sum_{j=0}^{q}\psi_j e_{t-j},
\]

其中

\[
\psi_0=1,\qquad \psi_j=0\quad (j>q).
\]

由于只有有限个非零系数，

\[
\sum_{j=0}^{\infty}\psi_j^2<\infty.
\]

因此 MA(q) 一定是 stationary linear process。它的 autocovariance 在 $q$ 阶以后截尾，因为当 lag 大于 $q$ 时，两个线性组合不再共享任何 white noise 项。

### Ex 4.9 Geometric Linear Process

若

\[
\psi_j=\phi^j,\qquad |\phi|<1,
\]

则

\[
\sum_{j=0}^{\infty}\psi_j^2
= \sum_{j=0}^{\infty}\phi^{2j}
= \frac{1}{1-\phi^2}
<\infty.
\]

因此

\[
Y_t=\sum_{j=0}^{\infty}\phi^j e_{t-j}
\]

是 well-defined 的 stationary linear process。这个例子会在后面和 AR(1) 联系起来，因为 stationary AR(1) 可以写成这样的 infinite MA representation。

### Ex 4.10 Autocovariance and ACF of MA(1)

对 MA(1)：

\[
Y_t=e_t-\theta e_{t-1}.
\]

均值为

\[
E(Y_t)=0.
\]

方差为

\[
\gamma_0
= \operatorname{Var}(Y_t)
= \operatorname{Var}(e_t-\theta e_{t-1})
= (1+\theta^2)\sigma^2.
\]

lag 1 的 autocovariance 为

\[
\gamma_1
= \operatorname{Cov}(Y_t,Y_{t+1})
= \operatorname{Cov}(e_t-\theta e_{t-1}, e_{t+1}-\theta e_t).
\]

展开后，只有 $\operatorname{Cov}(e_t,e_t)$ 留下，因此

\[
\gamma_1=-\theta\sigma^2.
\]

当 $k\ge2$ 时，$Y_t$ 和 $Y_{t+k}$ 不共享任何同一个 white noise 项，所以

\[
\gamma_k=0,\qquad k\ge2.
\]

因此

\[
\gamma_k
= \begin{cases}
(1+\theta^2)\sigma^2, & k=0,\\
-\theta\sigma^2, & k=1,\\
0, & k\ge2.
\end{cases}
\]

对应的 ACF 为

\[
\rho_1
= \frac{\gamma_1}{\gamma_0}
= -\frac{\theta}{1+\theta^2},
\]

并且

\[
\rho_k=0,\qquad k\ge2.
\]

这就是 MA(1) 的典型特征：**ACF 在 lag 1 以后截尾**。

### Rmk 4.11 Range and Shape of the MA(1) First Autocorrelation

定义函数

\[
f(x)=-\frac{x}{1+x^2}.
\]

则 MA(1) 的 first autocorrelation 是

\[
\rho_1=f(\theta).
\]

其导数为

\[
f'(x)
= \frac{x^2-1}{(1+x^2)^2}.
\]

当 $|x|<1$ 时，

\[
f'(x)<0.
\]

因此在 $|\theta|<1$ 的区间内，$\rho_1$ 随 $\theta$ 单调递减。特别地，

\[
-\frac12<\rho_1<\frac12.
\]

这说明 MA(1) 的 first autocorrelation 不能任意取值。若 imposed invertibility condition $|\theta|<1$，则 $\rho_1$ 和 $\theta$ 之间一一对应。

### Ex 4.12 Sample Mean Consistency for MA(1)

对 MA(1)，

\[
Y_t=e_t-\theta e_{t-1}.
\]

样本均值为

\[
\bar{Y}=\frac{1}{n}\sum_{t=1}^nY_t.
\]

因为 $E(Y_t)=0$，所以

\[
E(\bar{Y})=0.
\]

由 Lecture 2 的样本均值方差公式，且 MA(1) 只有 lag 1 autocovariance 不为 0，

\[
\operatorname{Var}(\bar{Y})
= \frac{1}{n^2}
\left[
n\gamma_0+2(n-1)\gamma_1
\right].
\]

代入

\[
\gamma_0=(1+\theta^2)\sigma^2,\qquad
\gamma_1=-\theta\sigma^2,
\]

得到

\[
\operatorname{Var}(\bar{Y})
= \frac{1}{n^2}
\left[
n(1+\theta^2)\sigma^2-2(n-1)\theta\sigma^2
\right]
= O\left(\frac{1}{n}\right).
\]

因此

\[
\bar{Y}\overset{p}{\longrightarrow}0.
\]

这个例子具体说明了：即使序列有短程相关，样本均值仍然可以 consistent。

### Def 4.13 Sample Autocovariance at Lag 0

lag 0 的 sample autocovariance，也就是 sample variance 型估计量，写作

\[
\hat{\gamma}_0
= \frac{1}{n}\sum_{t=1}^{n}(Y_t-\bar{Y})^2.
\]

如果真实均值已知为 0，也可以考虑

\[
\tilde{\gamma}_0
= \frac{1}{n}\sum_{t=1}^{n}Y_t^2.
\]

板书这里的重点是比较“真实均值已知”和“均值需要用样本均值估计”两种情况下的差异。因为 $\bar{Y}$ 本身是随机的，所以 $\hat{\gamma}_0$ 会出现有限样本 bias，但该 bias 通常是 $O(1/n)$ 的阶。

### Prop 4.14 Expectation of the Naive Second Moment for MA(1)

对 MA(1)，

\[
Y_t=e_t-\theta e_{t-1},
\]

若暂时使用

\[
\tilde{\gamma}_0=\frac{1}{n}\sum_{t=1}^{n}Y_t^2,
\]

则

\[
E(\tilde{\gamma}_0)
= \frac{1}{n}\sum_{t=1}^{n}E(Y_t^2)
= \gamma_0.
\]

由于

\[
\gamma_0=(1+\theta^2)\sigma^2,
\]

所以

\[
E(\tilde{\gamma}_0)=(1+\theta^2)\sigma^2.
\]

这说明如果均值已知为 0，直接平均 $Y_t^2$ 可以无偏估计 $\gamma_0$。

### Lem 4.15 Quadratic Form Trace Identity

令

\[
X=(X_1,\ldots,X_n)^T,
\qquad E(X)=0,
\qquad \operatorname{Var}(X)=I_n.
\]

若 $A$ 是 $n\times n$ 矩阵，则

\[
E(X^TAX)=\operatorname{tr}(A).
\]

更一般地，若

\[
\operatorname{Var}(X)=\Sigma,
\]

则

\[
E(X^TAX)=\operatorname{tr}(A\Sigma).
\]

证明利用 trace 的循环性质：

\[
X^TAX=\operatorname{tr}(X^TAX)=\operatorname{tr}(AXX^T).
\]

取期望得

\[
E(X^TAX)
= \operatorname{tr}(A E(XX^T)).
\]

若 $E(XX^T)=I_n$，则得到

\[
E(X^TAX)=\operatorname{tr}(A).
\]

### Prop 4.16 Bias Order of the Sample Variance with Estimated Mean

写成向量形式。令

\[
Y=(Y_1,\ldots,Y_n)^T,
\qquad
\mathbf 1=(1,\ldots,1)^T.
\]

样本均值可以写成

\[
\bar{Y}=\frac{1}{n}\mathbf 1^T Y.
\]

去均值向量为

\[
Y-\bar{Y}\mathbf 1
= \left(I_n-P_1\right)Y,
\]

其中

\[
P_1=\frac{1}{n}\mathbf 1\mathbf 1^T.
\]

因此

\[
\hat{\gamma}_0
= \frac{1}{n}(Y-\bar{Y}\mathbf 1)^T(Y-\bar{Y}\mathbf 1)
= \frac{1}{n}Y^T(I_n-P_1)Y.
\]

取期望并用 Lem 4.15 的 trace identity：

\[
E(\hat{\gamma}_0)
= \frac{1}{n}
\operatorname{tr}\left[(I_n-P_1)\Gamma\right],
\]

其中

\[
\Gamma=\operatorname{Var}(Y).
\]

由于 $P_1$ 是 rank-one projection，$\operatorname{tr}(P_1\Gamma)$ 通常是 $O(1)$ 的阶，因此

\[
E(\hat{\gamma}_0)
= \gamma_0+O\left(\frac{1}{n}\right).
\]

对 MA(1)，$\Gamma$ 是带状 covariance matrix，只有主对角线和一阶副对角线不为零，因此这个 $O(1/n)$ 的 bias 可以直接算出来。结论是

\[
E(\hat{\gamma}_0)\to \gamma_0.
\]

因此 sample autocovariance at lag 0 虽然有限样本下有 bias，但渐近上仍然估计 $\gamma_0$。

## Part B. 复习视角

Lecture 4 的主线是从 **finite moving average** 推广到 **general linear process**。Def 4.1 先写有限截断 $Y_{t,m}$，Def 4.2 引入 $L^2$ 收敛，Lem 4.3 用 $\sum\psi_j^2<\infty$ 证明有限截断有 mean-square limit，最后 Def 4.4 才正式定义无限线性过程。这个顺序很重要，因为无限和不是随便写出来的，必须先说明它在概率意义上 well-defined。

这一讲第一个核心结论是 **$\sum\psi_j^2<\infty$ 是 linear process 的基本存在条件**。它保证方差有限，也保证 autocovariance 的求和收敛。Prop 4.5 和 Prop 4.6 分别说明了 linear process 的均值、方差和 autocovariance。尤其是

\[
\gamma_\ell
= \sigma^2
\sum_{j=0}^{\infty}\psi_j\psi_{j+\ell}
\]

这个公式是后面 MA、ARMA 和 AR 的 infinite MA representation 的核心工具。

第二个核心概念是 **MA(q) 的 ACF 截尾**。Ex 4.8 说明 MA(q) 只有有限个 white noise 项参与，因此当 lag 大于 $q$ 时，两个变量不再共享同一个噪声项，自协方差变成 0。Ex 4.10 对 MA(1) 做了完整计算，得到 $\rho_k=0$ for $k\ge2$。这是识别 MA 模型阶数时最常用的理论基础。

第三个核心概念是 **样本估计量的渐近性质**。Ex 4.12 用 MA(1) 说明样本均值仍然 consistent，因为它的 autocovariance 只有有限阶非零，$\operatorname{Var}(\bar{Y})=O(1/n)$。Def 4.13 到 Prop 4.16 则开始进入 sample autocovariance 的理论：用样本均值去中心化会引入有限样本 bias，但通过 quadratic form 和 trace 可以证明这个 bias 是 $O(1/n)$，所以渐近上不会影响一致性。

从复习角度看，Lecture 4 最应该掌握三条推导线。第一条是从 $\sum\psi_j^2<\infty$ 推出 $L^2$ 收敛和 finite variance。第二条是从 linear process 表达式推出 autocovariance formula。第三条是从 MA(1) 具体模型推出 $\gamma_0$、$\gamma_1$、$\rho_1$ 和 ACF 截尾。这三条线掌握以后，后面 AR 模型写成 infinite MA 形式时，逻辑会非常自然。



# Lecture 5: General Linear Process and Sample Autocovariance for MA Models

## Part A. 课堂内容还原

### Def 5.1 General Linear Process

Lecture 5 从 **general linear process** 开始。设 $\{e_t\}$ 是 white noise，满足

\[
E(e_t)=0, \qquad \operatorname{Var}(e_t)=\sigma^2, \qquad \operatorname{Cov}(e_t,e_s)=0 \quad (t\ne s).
\]

若系数序列 $\{\psi_j\}_{j\ge 0}$ 满足

\[
\sum_{j=0}^{\infty}\psi_j^2<\infty,
\]

则定义

\[
Y_t=\sum_{j=0}^{\infty}\psi_j e_{t-j}.
\]

板书中特别强调，$\sum_{j=0}^{\infty}\psi_j^2<\infty$ 是这个无限线性过程能良好定义的条件。它保证有限截断和的极限在 mean-square 意义下存在，也保证方差有限。

### Def 5.2 Finite Truncation of a Linear Process

为了让无限和有严格含义，先定义有限截断过程

\[
Y_{t,m}=\sum_{j=0}^{m}\psi_j e_{t-j}.
\]

若

\[
Y_t=\lim_{m\to\infty}Y_{t,m}
\]

在 $L^2$ 或 mean-square 意义下成立，就可以把 $Y_t$ 视为由 white noise 线性滤波得到的过程。

### Prop 5.3 Mean, Variance, and Autocovariance of a Linear Process

对 Def 5.1 中的 process，由 white noise 的零均值可得

\[
E(Y_t)=E\left(\sum_{j=0}^{\infty}\psi_j e_{t-j}\right)=\sum_{j=0}^{\infty}\psi_j E(e_{t-j})=0.
\]

方差为

\[
\operatorname{Var}(Y_t)
=\operatorname{Var}\left(\sum_{j=0}^{\infty}\psi_j e_{t-j}\right)
=\sigma^2\sum_{j=0}^{\infty}\psi_j^2.
\]

若记 lag-$k$ autocovariance 为

\[
\gamma_k=\operatorname{Cov}(Y_t,Y_{t+k}),
\]

则展开得到

\[
\gamma_k
=\operatorname{Cov}\left(\sum_{j=0}^{\infty}\psi_j e_{t-j},\sum_{\ell=0}^{\infty}\psi_\ell e_{t+k-\ell}\right).
\]

只有 $t-j=t+k-\ell$，也就是 $\ell=j+k$ 的项留下，因此

\[
\gamma_k=\sigma^2\sum_{j=0}^{\infty}\psi_j\psi_{j+k}.
\]

板书在这里写出 Cauchy--Schwarz 的控制：

\[
\sum_{j=0}^{\infty}|\psi_j\psi_{j+k}|
\le
\left(\sum_{j=0}^{\infty}\psi_j^2\right)^{1/2}
\left(\sum_{j=0}^{\infty}\psi_{j+k}^2\right)^{1/2}<\infty.
\]

这说明 $\gamma_k$ 是 well-defined 的。

### Ex 5.4 MA(1) as a Linear Process

板书把 MA(1) 写成

\[
Y_t=e_t-\theta e_{t-1}, \qquad |\theta|<1 \text{ is not required for stationarity here}.
\]

它对应的 linear process 系数为

\[
\psi_0=1,\qquad \psi_1=-\theta,
\qquad \psi_j=0 \quad (j\ge 2).
\]

因此

\[
\sum_{j=0}^{\infty}\psi_j^2=1+\theta^2<\infty.
\]

这里需要注意，MA(1) 的 weak stationarity 不要求 $|\theta|<1$；$|\theta|<1$ 通常出现在 **invertibility** 条件中，不是 MA(1) 平稳性的必要条件。板书旁边写到 “when $|\theta|<1$，不是 yet”，可以理解为老师提醒这里暂时不要把 invertibility 和 stationarity 混在一起。

### Ex 5.5 MA(q) as a Linear Process

一般的 moving average model 写成

\[
Y_t=e_t-\theta_1 e_{t-1}+\theta_2 e_{t-2}+\cdots+\theta_q e_{t-q}.
\]

也可以统一写成

\[
Y_t=\sum_{j=0}^{q}\psi_j e_{t-j},
\]

其中 $\psi_j=0$ for $j>q$。因此

\[
\sum_{j=0}^{\infty}\psi_j^2=\sum_{j=0}^{q}\psi_j^2<\infty.
\]

这说明 MA(q) 是 general linear process 的有限阶特例。由于它只含有限多个 white noise 项，所以一般很容易讨论其 stationarity 和 autocovariance function。

### Ex 5.6 Autocovariance and ACF of MA(1)

对

\[
Y_t=e_t-\theta e_{t-1},
\]

有

\[
E(Y_t)=0.
\]

计算方差：

\[
\gamma_0=\operatorname{Var}(Y_t)
=\operatorname{Var}(e_t)+\theta^2\operatorname{Var}(e_{t-1})
=(1+\theta^2)\sigma^2.
\]

计算 lag-1 autocovariance：

\[
\gamma_1=\operatorname{Cov}(Y_t,Y_{t+1}).
\]

由于

\[
Y_{t+1}=e_{t+1}-\theta e_t,
\]

所以

\[
\gamma_1
=\operatorname{Cov}(e_t-\theta e_{t-1},e_{t+1}-\theta e_t)
=-\theta \sigma^2.
\]

当 $k\ge 2$ 时，$Y_t$ 和 $Y_{t+k}$ 不共享任何同一个 white noise 项，因此

\[
\gamma_k=0,\qquad k\ge 2.
\]

所以 MA(1) 的 autocorrelation function 是

\[
\rho_k=\frac{\gamma_k}{\gamma_0},
\]

即

\[
\rho_1=-\frac{\theta}{1+\theta^2},
\qquad
\rho_k=0\quad(k\ge 2).
\]

板书中还画了函数

\[
f(\theta)=-\frac{\theta}{1+\theta^2},
\]

并讨论它在 $|\theta|<1$ 区间内的单调性。这个讨论服务于参数识别：如果限制 $|\theta|<1$，那么 $\rho_1$ 和 $\theta$ 之间是一一对应关系；若不限制，则同一个 $\rho_1$ 可能对应两个不同的 $\theta$。

### Def 5.7 Sample Autocovariance

对观测 $Y_1,\ldots,Y_n$，样本均值为

\[
\bar Y=\frac{1}{n}\sum_{t=1}^{n}Y_t.
\]

板书使用的 sample autocovariance 形式是

\[
\hat\gamma_k
=\frac{1}{n}\sum_{t=1}^{n-k}(Y_t-\bar Y)(Y_{t+k}-\bar Y).
\]

特别地，lag 0 的样本自协方差是

\[
\hat\gamma_0
=\frac{1}{n}\sum_{t=1}^{n}(Y_t-\bar Y)^2.
\]

这里分母使用 $n$，不是 $n-k$，这是时间序列教材中常见的定义。它会带来有限样本 bias，但更适合后面矩阵推导和正定性讨论。

### Lem 5.8 Projection Matrix for Demeaning

令

\[
Y=(Y_1,\ldots,Y_n)^T,\qquad \mathbf 1=(1,\ldots,1)^T,
\]

并定义

\[
P_1=\frac{1}{n}\mathbf 1\mathbf 1^T.
\]

则

\[
P_1Y=\bar Y\mathbf 1,
\]

所以去均值向量可以写成

\[
Y-\bar Y\mathbf 1=(I_n-P_1)Y.
\]

因此

\[
\hat\gamma_0
=\frac{1}{n}Y^T(I_n-P_1)Y.
\]

板书中强调 $P_1$ 是 projection matrix，满足

\[
P_1^T=P_1,\qquad P_1^2=P_1,
\]

因此 $I_n-P_1$ 也是 projection matrix。

### Lem 5.9 Quadratic Form Expectation

若 $X\in\mathbb R^n$ 满足 $E(X)=0$，$E(XX^T)=\operatorname{Var}(X)=\Sigma$，则对任意矩阵 $A$，有

\[
E(X^TAX)=\operatorname{tr}(A\Sigma).
\]

证明思路是

\[
X^TAX=\operatorname{tr}(X^TAX)=\operatorname{tr}(AXX^T),
\]

所以

\[
E(X^TAX)=\operatorname{tr}(AE(XX^T))=\operatorname{tr}(A\Sigma).
\]

这个 lemma 是后面处理 $E(\hat\gamma_0)$ 和 $E(\hat\gamma_k)$ 的关键工具。

### Prop 5.10 Bias Order of $\hat\gamma_0$ for MA(1)

对 MA(1) 过程 $Y_t=e_t-\theta e_{t-1}$，记

\[
\Sigma_Y=E(YY^T).
\]

由 Lem 5.8 和 Lem 5.9，

\[
E(\hat\gamma_0)
=\frac{1}{n}E\{Y^T(I_n-P_1)Y\}
=\frac{1}{n}\operatorname{tr}\{(I_n-P_1)\Sigma_Y\}.
\]

展开为

\[
E(\hat\gamma_0)
=\frac{1}{n}\operatorname{tr}(\Sigma_Y)-\frac{1}{n}\operatorname{tr}(P_1\Sigma_Y).
\]

对 MA(1)，$\Sigma_Y$ 只有主对角线和一阶副对角线非零。主对角线给出

\[
\frac{1}{n}\operatorname{tr}(\Sigma_Y)=\gamma_0.
\]

而 $P_1$ 是 rank-one projection，$\operatorname{tr}(P_1\Sigma_Y)$ 是 $O(1)$，因此

\[
E(\hat\gamma_0)=\gamma_0+O\left(\frac{1}{n}\right).
\]

于是

\[
E(\hat\gamma_0)\to\gamma_0.
\]

这个结论说明 $\hat\gamma_0$ 在有限样本下有 bias，但 bias 的阶是 $O(1/n)$。

### Prop 5.11 Variance Order of $\hat\gamma_0$ for MA(1)

板书接着试图证明

\[
\operatorname{Var}(\hat\gamma_0)=O\left(\frac{1}{n}\right).
\]

核心写法是把 MA(1) 写成矩阵形式。令

\[
\varepsilon=(e_1,e_0,\ldots,e_n)^T,
\]

存在一个带状矩阵 $A$，使得

\[
Y=A\varepsilon.
\]

于是

\[
\hat\gamma_0
=\frac{1}{n}\varepsilon^T A^T(I_n-P_1)A\varepsilon.
\]

若进一步假设 white noise 正态，标准化后可使用 quadratic form 的方差公式。板书中出现了类似

\[
\operatorname{Var}(X^TAX)=E(X^TAX)^2-[E(X^TAX)]^2
\]

以及 trace 展开，并最终将 variance 控制到 $O(1/n)$。

**【原笔记留白/中断】** 扫描件中这一部分从 $E(X^TAX)^2$ 的展开开始，后面多处有划掉、改写和边注，完整代数过程没有连续写完。可以可靠确认的板书结论是：通过 quadratic form、projection matrix、trace identity 和 matrix norm bound，可以得到

\[
\operatorname{Var}(\hat\gamma_0)=O\left(\frac{1}{n}\right)\to 0.
\]

**【根据前后文补充】** 标准闭合方式是：由于 MA(1) 的 covariance matrix 是带状矩阵，相关项只在有限个 lag 内存在，所以 $\hat\gamma_0$ 的方差中只有 $O(n)$ 个非零协方差贡献；再乘上 $1/n^2$，得到 $O(1/n)$。这与板书中的矩阵 trace bound 是同一个数量级结论。

### Cor 5.12 Consistency of $\hat\gamma_0$ for MA(1)

由 Prop 5.10 和 Prop 5.11，

\[
E(\hat\gamma_0)=\gamma_0+O\left(\frac{1}{n}\right),
\qquad
\operatorname{Var}(\hat\gamma_0)=O\left(\frac{1}{n}\right).
\]

因此

\[
\hat\gamma_0\xrightarrow{p}\gamma_0.
\]

证明可以用 Chebyshev inequality：对任意 $\varepsilon>0$，

\[
P(|\hat\gamma_0-\gamma_0|>\varepsilon)
\le
P(|\hat\gamma_0-E\hat\gamma_0|>\varepsilon/2)
+
P(|E\hat\gamma_0-\gamma_0|>\varepsilon/2),
\]

第一项由 variance 收敛到 0 控制，第二项由 bias 收敛到 0 控制。

## Part B. 复习视角

Lecture 5 的主线是从 **general linear process** 回到 **sample autocovariance 的一致性**。Def 5.1 到 Prop 5.3 重新强调，时间序列模型的许多对象都可以写成 white noise 的线性滤波。这个角度非常重要，因为只要 $Y_t$ 可以写成 $\sum_j\psi_j e_{t-j}$，我们就能用系数序列 $\{\psi_j\}$ 来计算均值、方差和 autocovariance。

这一讲第一个核心概念是 **平方可和条件**。$\sum_j\psi_j^2<\infty$ 不是一个随便加的技术条件，它直接保证 $Y_t$ 的方差有限，也保证 autocovariance formula 可以通过 Cauchy--Schwarz 收敛。后面 AR 模型能够转写成 infinite MA，也要重新回到这个条件。

第二个核心概念是 **MA(1) 的 ACF 截尾**。Ex 5.6 得到 $\gamma_0=(1+\theta^2)\sigma^2$，$\gamma_1=-\theta\sigma^2$，$\gamma_k=0$ for $k\ge2$。这个结论的直觉不是“公式刚好为零”，而是 $Y_t$ 和 $Y_{t+k}$ 当 $k\ge2$ 时不共享任何 white noise 项。

第三个核心概念是 **sample autocovariance 为什么能估计 population autocovariance**。Def 5.7 到 Cor 5.12 的思路是先写出 $\hat\gamma_0$，再把去均值写成 projection matrix $I_n-P_1$，然后通过 quadratic form 的 expectation 和 variance 控制 bias 与随机波动。最终得到 $\hat\gamma_0\xrightarrow{p}\gamma_0$。

复习时最需要掌握的是这条逻辑链：**模型写成线性过程 $\Rightarrow$ 计算 population $\gamma_k$ $\Rightarrow$ 定义 sample $\hat\gamma_k$ $\Rightarrow$ 用矩阵写出去均值 $\Rightarrow$ 证明 expectation 接近 $\gamma_k$ 且 variance 收敛到 0**。这条链会在 Lecture 6 和 Lecture 7 继续推广到一般 lag $k$ 和 AR 模型。

---

# Lecture 6: Consistency of Sample Autocovariance and Sample ACF

**【原笔记留白/中断】** 扫描件中没有清楚出现 “Lecture 6” 标题。由于下一处明确标题是 “Lec 7”，而中间几页继续完成 sample autocovariance / sample autocorrelation 的一致性证明，所以这里把这部分按内容整理为 Lecture 6。

## Part A. 课堂内容还原

### Def 6.1 Shift Matrix for Lag-$k$ Products

为了写出 lag-$k$ 的 sample autocovariance，引入矩阵 $Q_k$。它的作用是把向量 $Y$ 移动 $k$ 个位置，使得二次型能产生 $Y_tY_{t+k}$ 这样的项。

在不去均值时，核心项可以写成

\[
\frac{1}{n}Y^TQ_kY.
\]

去均值之后，结合 Lecture 5 的 projection matrix，得到

\[
\hat\gamma_k
=\frac{1}{n}Y^T(I_n-P_1)Q_k(I_n-P_1)Y.
\]

这里 $Q_k$ 不是 projection matrix，而是 lag-$k$ shift matrix。它通常不是对称矩阵；若要处理对称二次型，可以把 $Q_k$ 和 $Q_k^T$ 配合使用。

### Prop 6.2 Expectation of $\hat\gamma_k$

对 stationary process，记

\[
\Sigma_Y=E(YY^T).
\]

由 quadratic form expectation，

\[
E(\hat\gamma_k)
=\frac{1}{n}\operatorname{tr}\{(I_n-P_1)Q_k(I_n-P_1)\Sigma_Y\}.
\]

板书将其分成主要项和 projection correction。主要项是

\[
\frac{1}{n}\operatorname{tr}(Q_k\Sigma_Y).
\]

由于 $Q_k$ 只选出第 $k$ 条对角线上的 covariance，stationarity 给出

\[
\operatorname{tr}(Q_k\Sigma_Y)=(n-k)\gamma_k.
\]

因此

\[
\frac{1}{n}\operatorname{tr}(Q_k\Sigma_Y)
=\left(1-\frac{k}{n}\right)\gamma_k.
\]

projection correction 的阶为 $O(1/n)$，所以

\[
E(\hat\gamma_k)=\left(1-\frac{k}{n}\right)\gamma_k+O\left(\frac{1}{n}\right)
=\gamma_k+O\left(\frac{1}{n}\right).
\]

这说明 $\hat\gamma_k$ 的 bias 也会随 $n\to\infty$ 消失。

### Prop 6.3 Variance Control for $\hat\gamma_k$

板书接下来处理

\[
\operatorname{Var}(\hat\gamma_k).
\]

基本策略是将

\[
\hat\gamma_k
=\frac{1}{n}Y^T(I_n-P_1)Q_k(I_n-P_1)Y
\]

展开成一个主要项和若干由 $P_1$ 引入的 remainder terms。例如可以写成

\[
\hat\gamma_k
=\frac{1}{n}Y^TQ_kY+R_{1n}+R_{2n}+R_{3n}.
\]

板书的目标是证明这些 remainder terms 在概率意义下收敛到 0：

\[
R_{1n}\xrightarrow{p}0,
\qquad
R_{2n}\xrightarrow{p}0,
\qquad
R_{3n}\xrightarrow{p}0.
\]

其中一个典型 bound 是 Cauchy--Schwarz 型：

\[
|R_{1n}|
\le
\left(\frac{1}{n}Y^TP_1Y\right)^{1/2}
\left(\frac{1}{n}Y^TQ_k^TQ_kY\right)^{1/2}.
\]

由于

\[
\frac{1}{n}Y^TP_1Y=(\bar Y)^2\xrightarrow{p}0,
\]

而第二项在概率意义下有界，所以

\[
R_{1n}\xrightarrow{p}0.
\]

其他 correction terms 的处理方式类似。

**【原笔记留白/中断】** 这一部分扫描件中有多处矩阵展开和划掉内容，尤其是 $P_1Q_k$、$Q_kP_1$ 相关项的完整代数式没有完全保留。可以可靠确认的是，老师用 projection matrix、Cauchy--Schwarz inequality、trace bound 和 Markov/Chebyshev inequality 来证明 correction terms 消失。

### Prop 6.4 Consistency of $\hat\gamma_k$ for MA(1)

综合 Prop 6.2 和 Prop 6.3，对于 MA(1) 这样的短记忆 stationary process，有

\[
E(\hat\gamma_k)=\gamma_k+O\left(\frac{1}{n}\right),
\]

并且

\[
\operatorname{Var}(\hat\gamma_k)=O\left(\frac{1}{n}\right).
\]

因此

\[
\hat\gamma_k\xrightarrow{p}\gamma_k,
\qquad n\to\infty.
\]

板书在结论处写到：

\[
\hat\gamma_k \text{ is a consistent estimator of } \gamma_k.
\]

### Thm 6.5 Continuous Mapping Theorem

板书随后引入 continuous mapping theorem。若

\[
X_n\xrightarrow{p}a,
\]

且 $f$ 在 $a$ 的邻域内连续，则

\[
f(X_n)\xrightarrow{p}f(a).
\]

证明思路是：对任意 $\varepsilon>0$，由于 $f$ 在 $a$ 处连续，存在 $\delta>0$ 使得

\[
|x-a|<\delta \quad \Rightarrow \quad |f(x)-f(a)|<\varepsilon.
\]

于是

\[
P(|f(X_n)-f(a)|>\varepsilon)
\le
P(|X_n-a|>\delta)\to 0.
\]

### Cor 6.6 Consistency of Sample ACF

样本自相关函数定义为

\[
\hat\rho_k=\frac{\hat\gamma_k}{\hat\gamma_0}.
\]

由 Prop 6.4，

\[
\hat\gamma_k\xrightarrow{p}\gamma_k,
\qquad
\hat\gamma_0\xrightarrow{p}\gamma_0.
\]

若 $\gamma_0>0$，函数

\[
f(x_1,x_2)=\frac{x_2}{x_1}
\]

在 $x_1=\gamma_0$ 附近连续，所以由 Thm 6.5，

\[
\hat\rho_k=\frac{\hat\gamma_k}{\hat\gamma_0}
\xrightarrow{p}
\frac{\gamma_k}{\gamma_0}=\rho_k.
\]

这说明 sample ACF 是 population ACF 的 consistent estimator。

### Rmk 6.7 Homework on White Noise

板书最后留下 homework：若

\[
Y_t\sim WN(0,\sigma^2),
\]

证明对任意 $k>0$，

\[
\hat\gamma_k\xrightarrow{p}0.
\]

因为 white noise 的 population autocovariance 满足

\[
\gamma_k=0,
\qquad k>0,
\]

所以这个 homework 本质上是 Cor 6.6 的最简单特例。若直接证明，也可以展开

\[
\hat\gamma_k
=\frac{1}{n}\sum_{t=1}^{n-k}(Y_t-\bar Y)(Y_{t+k}-\bar Y),
\]

再用 $E(Y_tY_{t+k})=0$ 和方差阶数 $O(1/n)$ 得到 convergence in probability。

## Part B. 复习视角

Lecture 6 的主线是把 Lecture 5 中 lag 0 的一致性推广到 **任意固定 lag $k$**。Def 6.1 引入 shift matrix $Q_k$，它的作用是把 sample autocovariance 写成二次型。这个步骤非常关键，因为写成矩阵形式以后，expectation 可以用 trace，variance 可以用 quadratic form bound。

这一讲最重要的结论是 **$\hat\gamma_k\xrightarrow{p}\gamma_k$**。证明分成两层：先证明 $E(\hat\gamma_k)$ 和 $\gamma_k$ 的差是 $O(1/n)$，再证明 $\operatorname{Var}(\hat\gamma_k)$ 收敛到 0。第一层靠 trace；第二层靠 projection correction 的控制和有限依赖 / 短记忆结构。

紧接着，Thm 6.5 把 convergence in probability 从 sample autocovariance 推到 sample autocorrelation。因为

\[
\hat\rho_k=\frac{\hat\gamma_k}{\hat\gamma_0},
\]

只要 $\hat\gamma_0\to_p\gamma_0>0$，比值函数在极限点连续，就能得到 $\hat\rho_k\to_p\rho_k$。这就是 sample ACF 可以用来识别 MA 截尾和 AR 拖尾的理论基础。

复习时要抓住 **projection matrix + shift matrix + continuous mapping theorem** 这三个工具。$I_n-P_1$ 负责去均值，$Q_k$ 负责产生 lag-$k$ product，continuous mapping theorem 负责从 $\hat\gamma_k$ 推到 $\hat\rho_k$。这三步连起来，就是 sample ACF 理论的主线。

---

# Lecture 7: Autoregressive Models and AR(2) Stationarity

## Part A. 课堂内容还原

### Def 7.1 AR(p) Model

Lecture 7 从 autoregressive model 开始。一般的 AR(p) 模型写成

\[
Y_t=\phi_1Y_{t-1}+\phi_2Y_{t-2}+\cdots+\phi_pY_{t-p}+e_t,
\]

其中

\[
e_t\sim WN(0,\sigma^2),
\]

并且 $e_t$ 与过去的 $Y_{t-1},\ldots,Y_{t-p}$ 不相关，通常还要求 independent of the past。

这类模型要讨论的 properties 包括 **stationarity**、**ACF**、是否能写成 **general linear process**，以及 sample autocovariance / sample ACF 的一致性。

### Ex 7.2 AR(1) Model

最简单的 AR model 是

\[
Y_t=\phi Y_{t-1}+e_t.
\]

若 $|\phi|<1$，递推展开得到

\[
Y_t=e_t+\phi e_{t-1}+\phi^2 e_{t-2}+\cdots
=\sum_{j=0}^{\infty}\phi^j e_{t-j}.
\]

因为

\[
\sum_{j=0}^{\infty}\phi^{2j}<\infty
\quad \Longleftrightarrow \quad |\phi|<1,
\]

所以 AR(1) 在 $|\phi|<1$ 时可以写成 general linear process。

它的方差为

\[
\gamma_0
=\operatorname{Var}(Y_t)
=\sigma^2\sum_{j=0}^{\infty}\phi^{2j}
=\frac{\sigma^2}{1-\phi^2}.
\]

它的 autocorrelation function 为

\[
\rho_k=\phi^k,
\qquad k\ge0.
\]

因此 AR(1) 的 ACF 不是截尾，而是按照 $\phi^k$ 几何衰减。

### Rmk 7.3 Sample Mean for AR(1)

对 stationary AR(1)，有

\[
E(Y_t)=0.
\]

样本均值为

\[
\bar Y=\frac{1}{n}\sum_{t=1}^{n}Y_t.
\]

因为 AR(1) 的 autocovariance 以几何速度衰减，

\[
\operatorname{Var}(\bar Y)=O\left(\frac{1}{n}\right).
\]

所以

\[
\bar Y\xrightarrow{p}0.
\]

板书这里的作用是说明，即使 $Y_t$ 之间不独立，只要相关性衰减足够快，样本均值仍然 consistent。

### Rmk 7.4 Consistency of $\hat\gamma_k$ for General Linear Processes

Lecture 7 中间几页继续处理 Lecture 6 留下的 sample autocovariance 理论。对 general linear process

\[
Y_t=\sum_{j=0}^{\infty}\psi_j e_{t-j},
\]

若

\[
\sum_{j=0}^{\infty}\psi_j^2<\infty,
\]

则可以用截断过程

\[
Y_{t,m}=\sum_{j=0}^{m}\psi_j e_{t-j}
\]

逼近 $Y_t$。记 remainder 为

\[
R_{t,m}=Y_t-Y_{t,m}=\sum_{j=m+1}^{\infty}\psi_j e_{t-j}.
\]

由于

\[
E(R_{t,m}^2)=\sigma^2\sum_{j=m+1}^{\infty}\psi_j^2\to0,
\]

所以有限截断可以在 mean-square 意义下逼近无限线性过程。

**【根据前后文补充】** 板书的目标是把 finite MA 情况下已经证明的 $\hat\gamma_k\to_p\gamma_k$ 推广到 general linear process。做法是先对 $Y_{t,m}$ 使用有限依赖证明，再控制 remainder $R_{t,m}$。由于 tail square sum 收敛到 0，remainder 对 sample autocovariance 的影响也可以做小。因此可以得到

\[
\hat\gamma_k\xrightarrow{p}\gamma_k,
\qquad
\hat\rho_k\xrightarrow{p}\rho_k.
\]

**【原笔记留白/中断】** 这一部分扫描件中出现了 $Q_k$、$P_1$、$y_m+r_m$ 的展开，但个别矩阵项没有完全写完。可以可靠确认的是，老师用 truncation argument 把 general linear process 化归到 finite-order moving average。

### Def 7.5 AR(2) Model

AR(2) 模型写成

\[
Y_t=\phi_1Y_{t-1}+\phi_2Y_{t-2}+e_t,
\]

其中

\[
e_t\sim WN(0,\sigma^2),
\]

并且 $e_t$ 与 $Y_{t-1},Y_{t-2}$ 不相关。板书先假设 $Y_t$ 是 stationary process，然后从 stationarity 推出均值和 autocovariance 的约束。

### Prop 7.6 Mean of Stationary AR(2)

设

\[
\mu=E(Y_t).
\]

对 AR(2) 两边取期望，得到

\[
\mu=\phi_1\mu+\phi_2\mu.
\]

因此

\[
(1-\phi_1-\phi_2)\mu=0.
\]

若

\[
1-\phi_1-\phi_2\ne0,
\]

则

\[
\mu=0.
\]

所以在通常的 stationary AR(2) 情况下，若没有额外截距项，均值为 0。

### Prop 7.7 Variance and Lag-1 Autocovariance of Stationary AR(2)

设

\[
\gamma_k=\operatorname{Cov}(Y_t,Y_{t+k}).
\]

对

\[
Y_t=\phi_1Y_{t-1}+\phi_2Y_{t-2}+e_t
\]

计算方差，利用 $e_t$ 与过去不相关，得到

\[
\gamma_0
=\phi_1^2\gamma_0+
\phi_2^2\gamma_0+
2\phi_1\phi_2\gamma_1+
\sigma^2.
\]

再将模型与 $Y_{t-1}$ 取 covariance，得到

\[
\gamma_1=\phi_1\gamma_0+\phi_2\gamma_1.
\]

于是

\[
\gamma_1=\frac{\phi_1}{1-\phi_2}\gamma_0,
\]

因此

\[
\rho_1=\frac{\gamma_1}{\gamma_0}=\frac{\phi_1}{1-\phi_2}.
\]

把 $\gamma_1$ 代回方差方程，可以解得

\[
\gamma_0
=\frac{(1-\phi_2)\sigma^2}
{(1+\phi_2)\left[(1-\phi_2)^2-\phi_1^2\right]}.
\]

### Prop 7.8 Stationarity Region for AR(2)

板书根据均值、$\rho_1$ 和 $\gamma_0>0$ 推出 AR(2) 的平稳性约束。核心条件可以写成

\[
\phi_1+
\phi_2<1,
\]

\[
\phi_2-
\phi_1<1,
\]

以及

\[
-1<\phi_2<1.
\]

这三个不等式形成 AR(2) 参数平稳区域的三角形。板书上画出了以 $\phi_1$ 为横轴、$\phi_2$ 为纵轴的三角区域。

**【根据前后文补充】** 标准 AR(2) stationarity condition 也可以写成 characteristic polynomial

\[
1-\phi_1z-\phi_2z^2=0
\]

的根都在单位圆外。等价地，companion matrix 的 eigenvalues 都在单位圆内。板书这一页主要用 covariance 和 positivity 的方式推到同一个三角区域。

### Def 7.9 Vectorized AR(2)

为了把 AR(2) 写成一阶向量递推，定义

\[
Z_t=\begin{pmatrix}Y_t\\Y_{t-1}\end{pmatrix},
\qquad
E_t=\begin{pmatrix}e_t\\0\end{pmatrix},
\]

以及 companion matrix

\[
A=\begin{pmatrix}
\phi_1 & \phi_2\\
1 & 0
\end{pmatrix}.
\]

则 AR(2) 可以写成

\[
Z_t=AZ_{t-1}+E_t.
\]

继续递推得到

\[
Z_t=A^{m+1}Z_{t-m-1}+\sum_{k=0}^{m}A^kE_{t-k}.
\]

如果第一项满足

\[
A^{m+1}Z_{t-m-1}\to0,
\]

则 AR(2) 可以写成 vector moving-average form：

\[
Z_t=\sum_{k=0}^{\infty}A^kE_{t-k}.
\]

### Rmk 7.10 Matrix Norm and Eigenvalue Condition

板书给出一个 sufficient condition：若存在矩阵范数使得

\[
\|A\|<1,
\]

则

\[
\|A^{m+1}Z_{t-m-1}\|^2
\le
\|A\|^{2(m+1)}\|Z_{t-m-1}\|^2\to0,
\]

从而递推中的初值项消失。

矩阵 $A$ 的 eigenvalues 来自

\[
\det(\lambda I-A)=0,
\]

即

\[
\lambda^2-\phi_1\lambda-\phi_2=0.
\]

因此

\[
\lambda_{1,2}
=\frac{\phi_1\pm\sqrt{\phi_1^2+4\phi_2}}{2}.
\]

**【根据前后文补充】** 对 AR(2)，真正的 stationarity condition 是 spectral radius

\[
\rho(A)=\max_i |\lambda_i|<1.
\]

$\|A\|<1$ 是方便证明的充分条件，但不是必要条件。若 $\rho(A)<1$，可以通过 Jordan decomposition 或适当选择矩阵范数得到 $A^m\to0$。

## Part B. 复习视角

Lecture 7 的主线是从 **MA / linear process** 转向 **AR model**。MA 模型是把当前 $Y_t$ 写成当前和过去 noise 的线性组合；AR 模型则是把当前 $Y_t$ 写成过去 $Y$ 加当前 noise。表面上 AR 不是 linear process，但如果满足 stationarity 条件，它可以递推展开成 infinite MA representation。

这一讲第一个关键结论是 AR(1) 的平稳条件和 ACF：$|\phi|<1$ 时，

\[
Y_t=\sum_{j=0}^{\infty}\phi^j e_{t-j},
\qquad
\rho_k=\phi^k.
\]

这和 MA(1) 的 ACF 截尾形成非常重要的对比：**MA(1) 的 ACF 截尾，AR(1) 的 ACF 拖尾并几何衰减**。

第二个关键结论是 AR(2) 的 stationarity region。Prop 7.8 给出三角形区域：

\[
\phi_1+\phi_2<1,
\qquad
\phi_2-\phi_1<1,
\qquad
-1<\phi_2<1.
\]

从 covariance 角度看，这些条件保证 $\gamma_0>0$ 且相关结构稳定；从 linear algebra 角度看，它们等价于 companion matrix 的 eigenvalues 位于单位圆内。

第三个关键概念是 **vectorization**。Def 7.9 把 AR(2) 写成 $Z_t=AZ_{t-1}+E_t$，这一步很重要，因为它把高阶 AR 变成一阶向量递推。后面讨论 AR(p)、VAR、state-space model 时都会用这个思想。

复习 Lecture 7 时，不要只背三角区域。更好的路线是先理解 AR(1) 如何递推成 infinite MA，再理解 AR(2) 为什么要构造 companion matrix，最后把 $A^m\to0$ 和 stationarity 联系起来。这样 AR(p) 的一般理论就会自然很多。

---

# Lecture 8: Backshift Operator and Polynomial Representation

## Part A. 课堂内容还原

### Rmk 8.1 Continuation on AR(1) and Matrix Contraction

Lecture 8 开头写到 “AR(1) 续上一节课”，并讨论如何证明压缩映射。板书中的问题是：直接讨论某个矩阵范数 $\|A\|$ 有时不方便，因为某些常用范数下 $\|A\|<1$ 不一定成立，即使过程实际是 stationary。

**【原笔记留白/中断】** 这一页主要是思路性记录，写到 “讨论 $\|A\|$，$\|A\|$ 可以怎么加以计算，对角化，考虑能否 SVD? No. Jordan 分解 Yes. Why? 要换大。” 这里没有完整定理或证明。

**【根据前后文补充】** 可以确定的数学含义是：判断 AR(p) 是否 stationary，关键不是某个固定范数是否小于 1，而是 companion matrix 的 spectral radius 是否小于 1。若 $\rho(A)<1$，则 $A^m\to0$；证明可以用 Jordan decomposition，也可以构造一个合适的 equivalent matrix norm，使得 $\|A\|<1$。

### Def 8.2 Backshift Operator

定义 **backshift operator** $B$ 为

\[
BY_t=Y_{t-1}.
\]

它把时间序列向过去移动一期。

### Prop 8.3 Powers of the Backshift Operator

对任意非负整数 $k$，有

\[
B^kY_t=Y_{t-k}.
\]

证明直接来自反复应用 Def 8.2：

\[
B^2Y_t=B(Y_{t-1})=Y_{t-2},
\]

一般地，

\[
B^kY_t=Y_{t-k}.
\]

### Def 8.4 Polynomial in the Backshift Operator

若有一个普通多项式

\[
f(x)=\sum_{j=0}^{q}a_jx^j,
\]

则可以定义相应的 backshift polynomial：

\[
f(B)=\sum_{j=0}^{q}a_jB^j.
\]

作用在 $Y_t$ 上时，得到

\[
f(B)Y_t
=\sum_{j=0}^{q}a_jB^jY_t
=\sum_{j=0}^{q}a_jY_{t-j}.
\]

这个 notation 可以把 AR、MA、ARMA 模型写得非常紧凑。

### Ex 8.5 AR(k) in Backshift Form

AR(k) 模型为

\[
Y_t=\phi_1Y_{t-1}+\phi_2Y_{t-2}+\cdots+\phi_kY_{t-k}+e_t.
\]

把所有 $Y$ 项移到左边：

\[
Y_t-\phi_1Y_{t-1}-\phi_2Y_{t-2}-\cdots-\phi_kY_{t-k}=e_t.
\]

用 backshift operator 表示为

\[
(1-\phi_1B-\phi_2B^2-\cdots-\phi_kB^k)Y_t=e_t.
\]

记

\[
\Phi(B)=1-\phi_1B-\phi_2B^2-\cdots-\phi_kB^k,
\]

则

\[
\Phi(B)Y_t=e_t.
\]

若 $\Phi(B)$ 可以形式上取逆，就得到

\[
Y_t=\Phi(B)^{-1}e_t.
\]

这就是把 AR model 写成 infinite MA representation 的核心动机。

### Rmk 8.6 Why Inverting $\Phi(B)$ Matters

板书写到 “把 $L^{-1}$ 找出来”。这里的 $L$ 可以理解为 AR polynomial operator，例如

\[
L=1-\phi_1B-\cdots-\phi_kB^k.
\]

如果能写出

\[
L^{-1}=\sum_{j=0}^{\infty}\psi_jB^j,
\]

那么

\[
Y_t=L^{-1}e_t=
\sum_{j=0}^{\infty}\psi_jB^je_t
=\sum_{j=0}^{\infty}\psi_j e_{t-j}.
\]

这就把 AR(k) 转化为 Def 5.1 中的 general linear process。之后就可以使用 Lecture 5–7 中关于 linear process 的均值、方差、autocovariance 和 sample ACF consistency 的结论。

### Rmk 8.7 Sparse Notes on Estimating $\gamma_k$ and $\rho_k$

扫描件中有一页只写到“最后估计 $\rho_k,\gamma_k$ 的时候用上这”。

**【原笔记留白/中断】** 这一页几乎没有展开推导，因此不能可靠还原完整课堂内容。结合前后文，可以确定老师是在提示：估计 AR 或 general linear process 的 autocovariance / autocorrelation 时，前面关于 $\hat\gamma_k$ 和 $\hat\rho_k$ 的 consistency 会继续使用。

### Rmk 8.8 Mid-term List / Review Notes

扫描件末尾出现 “Mid-term list” 和若干复习项。这部分看起来不是 Lecture 8 的主线内容，而是期中复习 checklist。可辨认的项目包括 Jensen inequality、Chebyshev inequality、trace identity、projection matrix、quadratic form、spectral decomposition / matrix norm 等。

其中 Chebyshev inequality 写成

\[
P(|\hat\theta_n-\theta|>\varepsilon)
\le
\frac{E(|\hat\theta_n-\theta|^k)}{\varepsilon^k},
\]

或在二阶情形下写成

\[
P(|\hat\theta_n-\theta|>\varepsilon)
\le
\frac{\operatorname{Var}(\hat\theta_n)}{\varepsilon^2}.
\]

trace identity 包括

\[
\operatorname{tr}(AB)=\operatorname{tr}(BA),
\]

以及

\[
E(X^TAX)=\operatorname{tr}(A\Sigma)
\]

在 $E(X)=0$、$E(XX^T)=\Sigma$ 时成立。

Projection matrix 的复习重点是

\[
P_1=\frac{1}{n}\mathbf 1\mathbf 1^T,
\qquad
P_1^T=P_1,
\qquad
P_1^2=P_1,
\]

并且

\[
(I_n-P_1)Y=Y-\bar Y\mathbf 1.
\]

这些工具正是 Lecture 5–6 证明 sample autocovariance consistency 时反复用到的。

## Part B. 复习视角

Lecture 8 的主线是把 AR 模型改写成 **operator / polynomial form**。Def 8.2 的 backshift operator $B$ 看似只是一个记号，但它把时间下标移动变成了代数运算。这样 AR(k) 就可以写成

\[
\Phi(B)Y_t=e_t.
\]

这一讲最关键的思想是：**AR 模型的平稳解来自对 AR polynomial 的反演**。如果

\[
\Phi(B)^{-1}=\sum_{j=0}^{\infty}\psi_jB^j
\]

存在并且系数满足平方可和条件，那么

\[
Y_t=\sum_{j=0}^{\infty}\psi_j e_{t-j}
\]

就是一个 general linear process。于是 AR 模型又回到了 Lecture 5 的框架中。

Lecture 8 还把上一讲的 companion matrix 观点和 backshift polynomial 观点连接起来。对 AR(2)，companion matrix 的 eigenvalue condition 和 AR polynomial roots outside unit circle 是同一个平稳性问题的两种表达。矩阵方法适合处理向量递推，backshift 方法适合处理模型代数和 ARMA 表示。

复习时要抓住一条线：**AR recurrence $\Rightarrow$ backshift polynomial $\Rightarrow$ inverse polynomial $\Rightarrow$ infinite MA representation $\Rightarrow$ 使用 linear process 的 autocovariance 和 sample ACF 理论**。这条线把 Lecture 5–8 串成一个整体。前面证明 $\hat\gamma_k$ 和 $\hat\rho_k$ consistent，并不是孤立的技术练习，而是为了让我们在 AR/MA 模型中能够用样本 ACF 去识别和估计 population ACF。


# Lecture 9: AR(p), Backshift Operator, ARMA and Invertibility

## Part A. 课堂内容还原

### Rmk 9.1 Lecture 9 的扫描情况

Lecture 9 在扫描件中从 AR(2) 模型开始。前面若干页是空白页或只有横线页；正式内容从 AR(2)、Yule--Walker、backshift operator 和 AR(p) 的平稳性条件开始。后面进入 ARMA(p,q) 和 invertibility。

**【原笔记留白/中断】** 扫描件中 Lecture 9 前几页为空白，ARMA(1,1) 一页只写了标题，黑板照片中部分推导较暗，因此 ARMA(1,1) 的细节只能按前后文作有限补充。

### Ex 9.2 AR(2) Model

板书先回到 AR(2) 模型。设 $\{e_t\}$ 是 white noise，满足 $E(e_t)=0$、$\operatorname{Var}(e_t)=\sigma^2$，AR(2) 写成

\[
Y_t=\phi_1Y_{t-1}+\phi_2Y_{t-2}+e_t.
\]

对应的 AR polynomial 是

\[
\phi(x)=1-\phi_1x-\phi_2x^2.
\]

AR(2) 的平稳性条件写成：

\[
\phi(x)=0 \quad \Longrightarrow \quad |x|>1.
\]

也就是说，AR polynomial 的所有根都必须在单位圆外。这里的“单位圆外”是针对 $x$ 平面中的根而言。这个条件的直观含义是：如果把 AR 递推不断往过去展开，过去冲击的影响必须逐渐衰减，而不能爆炸。

### Prop 9.3 Yule--Walker Equations for AR(2)

对 AR(2) 模型，如果过程是 weakly stationary，并且均值为 0，则对两边同时乘以 $Y_{t-k}$ 再取期望，可得 Yule--Walker equations。对 $k\ge 1$，由于 $e_t$ 与过去的 $Y_{t-k}$ 不相关，

\[
\gamma_k=\phi_1\gamma_{k-1}+\phi_2\gamma_{k-2}.
\]

标准化以后得到

\[
\rho_k=\phi_1\rho_{k-1}+\phi_2\rho_{k-2}.
\]

特别地，当 $k=1$ 时，利用 $\rho_{-1}=\rho_1$，有

\[
\rho_1=\phi_1+\phi_2\rho_1.
\]

因此

\[
\rho_1=\frac{\phi_1}{1-\phi_2}.
\]

当 $k=0$ 时，方差方程包含 innovation variance：

\[
\gamma_0=\phi_1\gamma_1+\phi_2\gamma_2+\sigma^2.
\]

两边除以 $\gamma_0$ 得到

\[
1=\phi_1\rho_1+\phi_2\rho_2+\frac{\sigma^2}{\gamma_0}.
\]

这说明 Yule--Walker 方程分成两类：$k\ge1$ 的方程主要描述 autocorrelation 的递推结构；$k=0$ 的方程负责把整体方差 $\gamma_0$ 和噪声方差 $\sigma^2$ 联系起来。

### Def 9.4 Backshift Operator

**backshift operator** 记为 $B$，定义为

\[
BY_t=Y_{t-1}.
\]

因此

\[
B^jY_t=Y_{t-j}.
\]

使用 backshift operator 后，AR 模型可以写成多项式形式。比如 AR(2) 写成

\[
(1-\phi_1B-\phi_2B^2)Y_t=e_t.
\]

这种写法的好处是可以把 AR 模型看作对 $Y_t$ 施加一个线性滤波器，后面讨论 stationarity、ARMA、ARIMA 时都会用到这个记号。

### Def 9.5 AR(p) Model and AR Polynomial

一般的 AR(p) 模型写作

\[
Y_t=\phi_1Y_{t-1}+\phi_2Y_{t-2}+\cdots+\phi_pY_{t-p}+e_t.
\]

用 backshift operator 表示为

\[
\phi(B)Y_t=e_t,
\]

其中

\[
\phi(B)=1-\phi_1B-\phi_2B^2-\cdots-\phi_pB^p.
\]

对应的 AR polynomial 也可写成

\[
\phi(x)=1-\phi_1x-\phi_2x^2-\cdots-\phi_px^p.
\]

### Prop 9.6 Stationarity Condition for AR(p)

AR(p) 的平稳性条件是

\[
\phi(x)=0 \quad \Longrightarrow \quad |x|>1.
\]

也就是说，AR polynomial 的所有根都在单位圆外。板书旁边写到“逆算子可以展开成收敛幂级数”，这正是根在单位圆外条件的核心作用。

**【根据前后文补充】** 如果 $\phi(x)$ 的根都在单位圆外，那么 $\phi(B)^{-1}$ 可以展开成收敛的 power series，于是

\[
Y_t=\phi(B)^{-1}e_t=\sum_{j=0}^{\infty}\psi_j e_{t-j}.
\]

这说明平稳 AR(p) 可以写成 MA($\infty$) 形式。这个结论和 Lecture 5 中的 general linear process 接上了：AR 模型虽然表面上是 $Y_t$ 对过去 $Y$ 的回归，但在平稳条件下，它本质上也是 white noise 的无限线性组合。

### Prop 9.7 Mean Requirement under Stationarity

板书接着讨论平稳性的 requirements。假设 $\{Y_t\}$ 是 stationary，并记

\[
E(Y_t)=\mu.
\]

对 AR(p) 模型取期望：

\[
E(Y_t)=\phi_1E(Y_{t-1})+\cdots+\phi_pE(Y_{t-p})+E(e_t).
\]

由于 $E(e_t)=0$ 且平稳时所有 $E(Y_{t-j})$ 都等于 $\mu$，得到

\[
\mu=(\phi_1+\cdots+\phi_p)\mu.
\]

因此

\[
\left(1-\phi_1-\cdots-\phi_p\right)\mu=0.
\]

这说明要么

\[
\phi_1+\cdots+\phi_p=1,
\]

要么

\[
\mu=0.
\]

在 centered AR model 中，通常直接讨论 $\mu=0$ 的情形。若均值不为 0，则应先写成 $Y_t-\mu$ 的 AR 结构。

### Prop 9.8 Yule--Walker Equations for AR(p)

在 $\mu=0$ 的情况下，AR(p) 模型为

\[
Y_t=\phi_1Y_{t-1}+\cdots+\phi_pY_{t-p}+e_t.
\]

对两边乘以 $Y_{t-k}$ 并取期望，得到

\[
E(Y_tY_{t-k})
=\phi_1E(Y_{t-1}Y_{t-k})+\cdots+
\phi_pE(Y_{t-p}Y_{t-k})+E(e_tY_{t-k}).
\]

当 $k\ge1$ 时，$Y_{t-k}$ 属于过去信息，$e_t$ 与过去不相关，因此

\[
E(e_tY_{t-k})=0.
\]

于是

\[
\gamma_k=\phi_1\gamma_{k-1}+\phi_2\gamma_{k-2}+\cdots+\phi_p\gamma_{k-p}.
\]

标准化得到

\[
\rho_k=\phi_1\rho_{k-1}+\phi_2\rho_{k-2}+\cdots+\phi_p\rho_{k-p}.
\]

这里使用了 $\rho_{-j}=\rho_j$。当 $k=1,\ldots,p$ 时，这组方程可以写成矩阵形式。

### Prop 9.9 Yule--Walker Equations in Matrix Form

定义

\[
\boldsymbol{\rho}=(\rho_1,\rho_2,\ldots,\rho_p)^T,
\qquad
\boldsymbol{\phi}=(\phi_1,\phi_2,\ldots,\phi_p)^T.
\]

令

\[
R_p=\begin{pmatrix}
1 & \rho_1 & \rho_2 & \cdots & \rho_{p-1}\\
\rho_1 & 1 & \rho_1 & \cdots & \rho_{p-2}\\
\rho_2 & \rho_1 & 1 & \cdots & \rho_{p-3}\\
\vdots & \vdots & \vdots & \ddots & \vdots\\
\rho_{p-1} & \rho_{p-2} & \rho_{p-3} & \cdots & 1
\end{pmatrix}.
\]

则 Yule--Walker equations 可以写成

\[
\boldsymbol{\rho}=R_p\boldsymbol{\phi}.
\]

矩阵 $R_p$ 是 Toeplitz matrix，因为它的元素只依赖于行列指标之差。这个结构来自 stationarity：autocorrelation 只依赖 lag。

### Prop 9.10 Variance Equation for AR(p)

当 $k=0$ 时，不能直接把 $E(e_tY_t)$ 丢掉，因为 $Y_t$ 本身包含 $e_t$。由

\[
Y_t=\phi_1Y_{t-1}+\cdots+\phi_pY_{t-p}+e_t
\]

两边乘以 $Y_t$ 并取期望，得到

\[
\gamma_0=\phi_1\gamma_1+\cdots+\phi_p\gamma_p+E(e_tY_t).
\]

由于

\[
Y_t=\phi_1Y_{t-1}+\cdots+\phi_pY_{t-p}+e_t,
\]

且 $e_t$ 与过去的 $Y_{t-j}$ 不相关，所以

\[
E(e_tY_t)=E(e_t^2)=\sigma^2.
\]

因此

\[
\gamma_0=\phi_1\gamma_1+\cdots+\phi_p\gamma_p+\sigma^2.
\]

两边除以 $\gamma_0$，得到

\[
1=\phi_1\rho_1+\cdots+\phi_p\rho_p+\frac{\sigma^2}{\gamma_0}.
\]

这个方程可用于从 $\rho_1,
\ldots,\rho_p$ 和 $\phi_1,
\ldots,\phi_p$ 推出 $\gamma_0$ 与 $\sigma^2$ 的关系。

### Prop 9.11 Stationary AR(p) as MA($\infty$)

板书用 backshift operator 说明 AR(p) 的平稳解可以表示成 MA($\infty$)。由

\[
\phi(B)Y_t=e_t,
\]

若

\[
\phi(B)=(1-G_1B)(1-G_2B)\cdots(1-G_pB),
\]

并且所有 $|G_i|<1$，则

\[
\frac{1}{1-G_iB}=\sum_{j=0}^{\infty}G_i^jB^j.
\]

因此

\[
\phi(B)^{-1}
=\prod_{i=1}^p(1-G_iB)^{-1}
\]

可以展开为收敛幂级数，进而

\[
Y_t=\phi(B)^{-1}e_t
=\sum_{j=0}^{\infty}\psi_jB^je_t
=\sum_{j=0}^{\infty}\psi_j e_{t-j}.
\]

这正是 MA($\infty$) 表示。注意 $G_i$ 与根 $x_i$ 的关系是 $x_i=1/G_i$，所以 $|G_i|<1$ 等价于 $|x_i|>1$。

### Def 9.12 ARMA(p,q) Model

Lecture 9 后半部分开始推广到 ARMA。一般的 ARMA(p,q) 模型写成

\[
\phi(B)Y_t=\theta(B)e_t,
\]

其中

\[
\phi(B)=1-\phi_1B-\cdots-\phi_pB^p,
\]

而 MA polynomial 可写成

\[
\theta(B)=1-\theta_1B-\cdots-\theta_qB^q.
\]

不同教材对 MA 部分的正负号约定可能不同；本笔记沿用板书中 $Y_t=e_t-\theta e_{t-1}$ 的符号习惯。

### Prop 9.13 Stationarity and Invertibility of ARMA(p,q)

ARMA(p,q) 同时涉及两个条件。平稳性由 AR polynomial 决定：

\[
\phi(x)=0 \quad \Longrightarrow \quad |x|>1.
\]

可逆性由 MA polynomial 决定：

\[
\theta(x)=0 \quad \Longrightarrow \quad |x|>1.
\]

平稳性保证 $Y_t$ 可以写成过去 shocks 的收敛线性组合；可逆性保证 shocks $e_t$ 可以由当前与过去的 observations $Y_t,Y_{t-1},\ldots$ 恢复出来。

### Rmk 9.14 Motivation for Invertibility

板书用 AR(1) 和 MA(1) 对比说明 invertibility。对 AR(1)

\[
Y_t=\phi Y_{t-1}+e_t,
\]

噪声可以直接由观测决定：

\[
e_t=Y_t-\phi Y_{t-1}.
\]

但对 MA(1)

\[
Y_t=e_t-\theta e_{t-1},
\]

当前噪声 $e_t$ 不能立即只由 $Y_t$ 和有限个过去观测写出来。由

\[
Y_t=(1-\theta B)e_t,
\]

如果 $|\theta|<1$，则

\[
e_t=(1-\theta B)^{-1}Y_t
=\sum_{j=0}^{\infty}\theta^jY_{t-j}.
\]

这就说明 $e_t$ 可以由当前和过去的观测 $Y_t,Y_{t-1},\ldots$ 以收敛方式表示。这个性质就是 MA 模型的 invertibility。

### Ex 9.15 ARMA(1,1)

**【原笔记留白/中断】** 扫描件中 ARMA(1,1) 一页基本只有标题，具体推导没有写出。根据 Lecture 9 前后文，ARMA(1,1) 应当是 ARMA(p,q) 的最小非平凡例子。

**【根据前后文补充】** 按板书符号，ARMA(1,1) 可写成

\[
Y_t-\phi Y_{t-1}=e_t-\theta e_{t-1},
\]

也就是

\[
(1-\phi B)Y_t=(1-\theta B)e_t.
\]

其 stationarity condition 是

\[
|\phi|<1,
\]

因为 AR polynomial $1-\phi x=0$ 的根为 $x=1/\phi$，根在单位圆外等价于 $|\phi|<1$。其 invertibility condition 是

\[
|\theta|<1.
\]

若这两个条件都成立，则 ARMA(1,1) 同时有 MA($\infty$) 表示和 invertible AR($\infty$) 表示。

## Part B. 复习视角

Lecture 9 的核心是把前面 AR(1)、AR(2) 的具体例子提升到 **AR(p) 和 ARMA(p,q) 的算子语言**。Ex 9.2 和 Prop 9.3 先用 AR(2) 复习 characteristic polynomial 与 Yule--Walker 方程。紧接着 Def 9.4 引入 backshift operator，把模型从递推形式改写成 polynomial operator 形式。这个记号一开始看起来只是形式变化，但它实际上是后面所有 ARMA 和 ARIMA 推导的统一语言。

这节最重要的第一条线是 **AR polynomial 的根决定 stationarity**。Def 9.5 和 Prop 9.6 说明，对于 AR(p)，只要 $\phi(x)=0$ 的所有根都在单位圆外，$\phi(B)^{-1}$ 就能展开成收敛幂级数。Prop 9.11 进一步说明，平稳 AR(p) 可以写成 MA($\infty$)。所以平稳性不是孤立的判别规则，它的数学本质是“过去 shock 的权重可以衰减并形成收敛线性过程”。

第二条线是 **Yule--Walker 方程把模型参数和 ACF 联系起来**。Prop 9.8 和 Prop 9.9 告诉我们，AR(p) 的 autocorrelation 不是随便的，它满足一个由 $\phi_1,\ldots,\phi_p$ 决定的递推关系。这个递推关系后面会解释为什么 AR 模型的 ACF 通常是 tailing off，而不是像 MA(q) 那样在有限阶截尾。

第三条线是 **ARMA 同时需要 stationarity 和 invertibility**。Prop 9.13 把两个条件分开：AR polynomial 管 stationarity，MA polynomial 管 invertibility。Rmk 9.14 的意义很大：可逆性不是为了让 $Y_t$ 平稳，而是为了让 innovation $e_t$ 能被观测序列恢复出来。后面做 MLE、残差诊断、forecasting 时，我们都需要从数据中重建或估计 innovations，因此 invertibility 是统计推断中的核心条件。

---

# Lecture 10: Differencing, ARIMA and Transformations

## Part A. 课堂内容还原

### Rmk 10.1 From Stationary Models to Non-stationary Processes

Lecture 10 开头先总结 Chapter 5 中的线性平稳时间序列模型：MA model、AR model 和 ARMA model。对 ARMA 模型，板书强调“要看模型平稳 + 可逆”。若

\[
\phi(B)Y_t=\theta(B)e_t,
\]

则 stationarity 由

\[
\phi(x)=0\quad \Longrightarrow \quad |x|>1
\]

决定，invertibility 由

\[
\theta(x)=0\quad \Longrightarrow \quad |x|>1
\]

决定。

接着课程转入 non-stationary process。板书列出两个常见来源：第一，mean function 非常数；第二，ACF not constant，或者说二阶结构不稳定。非平稳均值可以是线性趋势

\[
\mu_t=a+bt,
\]

也可以是周期项

\[
\mu_t=\beta_0+\beta_1\cos(2\pi ft)+\beta_2\sin(2\pi ft).
\]

### Ex 10.2 Non-stationary AR(1): Explosive Case and Unit Root Case

考虑 AR(1)

\[
Y_t=\phi Y_{t-1}+e_t.
\]

当 $|\phi|<1$ 时，它是 stationary 的。板书接着讨论 $|\phi|>1$ 的情况。以 $\phi=3$ 为例，并设 $Y_0=0$，则

\[
Y_t=e_t+3Y_{t-1}
=e_t+3e_{t-1}+3^2e_{t-2}+\cdots+3^{t-1}e_1.
\]

因此

\[
\operatorname{Var}(Y_t)
=\sigma^2\sum_{k=0}^{t-1}3^{2k}
=\sigma^2\frac{3^{2t}-1}{3^2-1}.
\]

当 $t\to\infty$ 时，方差发散：

\[
\operatorname{Var}(Y_t)\to\infty.
\]

这就是 explosive process。越古早的 shock 经过递推以后影响越大，所以过程不可能平稳。

再看 unit root case，即 $\phi=1$。此时

\[
Y_t=Y_{t-1}+e_t.
\]

若 $Y_0=0$，则

\[
Y_t=\sum_{k=1}^t e_k,
\]

所以

\[
\operatorname{Var}(Y_t)=t\sigma^2\to\infty.
\]

这也是非平稳过程。板书随后问：“如何让它平稳？”答案是对它做差分。

### Def 10.3 Difference Operator

**difference operator** 记为 $\nabla$，定义为

\[
\nabla Y_t=Y_t-Y_{t-1}.
\]

二阶差分为

\[
\nabla^2Y_t=\nabla(\nabla Y_t).
\]

一般地，

\[
\nabla^dY_t=\nabla(\nabla^{d-1}Y_t).
\]

由于 $BY_t=Y_{t-1}$，所以

\[
\nabla=1-B.
\]

因此

\[
\nabla Y_t=(1-B)Y_t=Y_t-Y_{t-1}.
\]

差分算子的作用是消除 unit root 类型的非平稳性。例如 random walk 满足

\[
Y_t=Y_{t-1}+e_t,
\]

于是

\[
\nabla Y_t=e_t,
\]

差分后变成 white noise。

### Def 10.4 ARIMA(p,d,q)

若

\[
\nabla^dY_t\sim ARMA(p,q),
\]

则称 $Y_t$ 服从 **ARIMA(p,d,q)** 模型。

用 backshift operator 写，就是

\[
\phi(B)\nabla^dY_t=\theta(B)e_t.
\]

因为

\[
\nabla^d=(1-B)^d,
\]

也可以写成

\[
\phi(B)(1-B)^dY_t=\theta(B)e_t.
\]

这里的 $d$ 表示需要差分多少次才能得到 stationary ARMA process。

### Ex 10.5 Integrated White Noise

板书给出一个简单例子。若

\[
\nabla Y_t=W_t,
\]

并设边界条件

\[
Y_t=0,\qquad t<-m,
\]

则

\[
Y_t-Y_{t-1}=W_t.
\]

从 $-m$ 开始递推，得到

\[
Y_{-m}=W_{-m},
\]

\[
Y_{-m+1}=W_{-m}+W_{-m+1},
\]

继续递推可得

\[
Y_t=\sum_{k=-m}^{t}W_k.
\]

这说明如果一阶差分是 stationary process，那么原序列通常是它的累积和，因此会呈现非平稳的随机游走式波动。

### Ex 10.6 Second-order Integrated Process

板书继续考虑

\[
\nabla Y_t=M_t,
\]

其中

\[
M_t=\sum_{k=-m}^{t}W_k.
\]

于是

\[
Y_t=\sum_{j=-m}^{t}M_j
=\sum_{j=-m}^{t}\sum_{k=-m}^{j}W_k.
\]

**【根据前后文补充】** 这对应二阶积分过程。也就是说，如果 $\nabla^2Y_t=W_t$，那么 $Y_t$ 是 white noise 的二重累积。相比一阶积分过程，它的趋势会更“弯曲”，方差增长更快。

### Ex 10.7 IMA(1,1)

板书写到 IMA(1,1)：

\[
\nabla Y_t\sim MA(1).
\]

按照板书符号，设

\[
\nabla Y_t=e_t-\theta e_{t-1},\qquad t\ge -m.
\]

因此

\[
Y_t=\sum_{j=-m}^{t}(e_j-\theta e_{j-1}).
\]

把求和展开，得到

\[
Y_t=e_t+(1-\theta)e_{t-1}+\cdots+(1-\theta)e_{-m}-\theta e_{-m-1}.
\]

于是

\[
\operatorname{Var}(Y_t)
=\sigma^2\left[1+(1-\theta)^2(t+m)+\theta^2\right].
\]

这个方差随着 $t$ 增长，因此 $Y_t$ 非平稳，但它的一阶差分是 MA(1)，所以 $Y_t$ 是 IMA(1,1)。

**【原笔记留白/中断】** 板书中关于 $\operatorname{Cov}(Y_t,Y_{t+k})$ 的推导有多处划线和改写，最终表达式没有完全清楚写完。

**【根据前后文补充】** 可以确定的是，$Y_t$ 和 $Y_{t+k}$ 会共享大量过去的 innovation，因此 covariance 不会只依赖于 lag $k$，而会随着时间位置变化。这正是 IMA(1,1) 不平稳的二阶表现。

### Ex 10.8 ARI(1,1)

Lecture 10 还写到 ARI(1,1)，即

\[
\nabla Y_t=\phi\nabla Y_{t-1}+e_t.
\]

用 backshift operator 写为

\[
(1-B)Y_t=\phi B(1-B)Y_t+e_t.
\]

整理得到

\[
(1-B)(1-
\phi B)Y_t=e_t.
\]

因此

\[
Y_t=(1-B)^{-1}(1-
\phi B)^{-1}e_t.
\]

**【原笔记留白/中断】** 板书对边界条件 $Y_t=0$ for $t<-m$ 的递推只写了开头几步，并未完整展开一般形式。

**【根据前后文补充】** 这个例子的核心并不是要背完整展开式，而是看清：ARI(1,1) 经过一阶差分后变成 AR(1)。如果 $|\phi|<1$，则 $\nabla Y_t$ 平稳；但 $Y_t$ 自身由于含有 $(1-B)^{-1}$，通常仍是非平稳的 integrated process。

### Def 10.9 ARIMA(p,d,q) with Mean Adjustment

板书随后把 ARIMA 写回一般形式。若 $d=1$，则

\[
\phi(B)\nabla Y_t=\theta(B)e_t.
\]

如果差分后的序列有非零均值 $\mu$，可以写成

\[
\phi(B)(\nabla Y_t-\mu)=\theta(B)e_t.
\]

更一般地，

\[
\phi(B)(\nabla^dY_t-\mu)=\theta(B)e_t.
\]

这里 $\mu$ 是差分后 stationary process 的 mean，而不是原始 $Y_t$ 的 constant mean。

### Rmk 10.10 Other Ways to Stabilize Non-stationarity

差分主要处理 unit root 或 stochastic trend。板书接着问：“其它的平稳手段？”然后引入 Box--Cox transform。这个过渡很重要，因为有些序列非平稳不是因为均值趋势本身，而是因为波动幅度随水平变化。

假设 $Y_t>0$，且

\[
E(Y_t)=\mu_t,
\]

并且波动大小和均值水平有关，例如

\[
\operatorname{Var}(Y_t)^{1/2}=\mu_t\sigma.
\]

对 $\log Y_t$ 做 Taylor expansion：

\[
\log Y_t
\approx
\log \mu_t+
\frac{Y_t-\mu_t}{\mu_t}.
\]

因此

\[
\operatorname{Var}(\log Y_t)
\approx
\frac{1}{\mu_t^2}\operatorname{Var}(Y_t)
=\sigma^2.
\]

这说明 log transform 可以把“均值越大、方差越大”的数据变成近似 constant variance 的数据。

### Rmk 10.11 Log Difference and Return Data

板书还给出收益率数据的直觉。若

\[
Y_t=(1+X_t)Y_{t-1},
\]

则

\[
\log Y_t=
\log(1+X_t)+\log Y_{t-1}.
\]

因此

\[
\nabla\log Y_t=
\log Y_t-
\log Y_{t-1}
= \log(1+X_t).
\]

当 $X_t$ 很小时，

\[
\log(1+X_t)\approx X_t.
\]

所以

\[
\nabla\log Y_t\approx X_t.
\]

这就是为什么金融里的收益率数据常常使用 log difference。

### Def 10.12 Box--Cox Transform

对正值序列 $Y_t>0$，Box--Cox transform 定义为

\[
Y_t^{(\lambda)}=
\begin{cases}
\dfrac{Y_t^\lambda-1}{\lambda}, & \lambda\ne0,\\[6pt]
\log Y_t, & \lambda=0.
\end{cases}
\]

当 $\lambda\to0$ 时，利用极限

\[
\lim_{\lambda\to0}\frac{Y_t^\lambda-1}{\lambda}
=\log Y_t,
\]

因此 log transform 是 Box--Cox transform 的极限情形。

### Rmk 10.13 Estimating the Box--Cox Parameter by MLE

板书最后提到可以通过 MLE 估计 Box--Cox 参数。设

\[
X_1,X_2,\ldots,X_n \overset{iid}{\sim} f(x;\theta),
\]

并令变换

\[
g_\lambda:X\mapsto Y.
\]

若变换后的变量近似服从 normal model，例如

\[
g_\lambda(X)\sim N(\mu,\sigma^2),
\]

则可以写出关于 $\mu,\sigma^2,\lambda$ 的 likelihood，并最大化它。

**【原笔记留白/中断】** Box--Cox 的 likelihood 推导在扫描件中只写了开头，包括 monotone one-to-one transform、normal density 和部分 Jacobian 项，但没有完整收尾。

**【根据前后文补充】** 标准做法需要在 likelihood 中加入 Jacobian factor。若

\[
z_i=g_\lambda(y_i),
\]

则原始数据的 likelihood 不是简单地把 $z_i$ 放进正态密度，还要乘以

\[
\left|\frac{d}{dy_i}g_\lambda(y_i)\right|.
\]

对 Box--Cox transform，该 Jacobian 会产生与 $\lambda$ 有关的项。因此估计 $\lambda$ 时不能忽略变量变换带来的密度尺度变化。

## Part B. 复习视角

Lecture 10 的主线是：**当原始序列不平稳时，怎样把它变成适合 ARMA 建模的序列**。Rmk 10.1 先从 Chapter 5 的 stationary MA、AR、ARMA 模型转向 non-stationary process。Ex 10.2 说明，AR(1) 中 $|\phi|>1$ 会 explosive，$\phi=1$ 会产生 random walk；它们共同的问题是方差随时间发散。

Def 10.3 和 Def 10.4 是这一讲的核心。差分算子 $\nabla=1-B$ 的作用是消除 unit root。ARIMA(p,d,q) 的含义不是“比 ARMA 更复杂的模型”，而是“差分 $d$ 次以后得到 ARMA(p,q)”。因此 ARIMA 的建模逻辑一定是先问：原序列是否需要差分？差分几次之后看起来平稳？差分后的序列再用 ARMA(p,q) 描述。

Ex 10.5、Ex 10.6、Ex 10.7 和 Ex 10.8 共同说明 integrated process 的结构。若 $\nabla Y_t$ 是 white noise，原序列就是累积和；若 $\nabla Y_t$ 是 MA(1)，原序列就是 IMA(1,1)；若 $\nabla Y_t$ 是 AR(1)，原序列就是 ARI(1,1)。这些例子的共同点是：**差分后的序列可以平稳，但原序列本身仍然会因为累积效应而非平稳**。

后半部分的 Box--Cox 和 log transform 解决的是另一种问题：**variance 随 level 改变**。Rmk 10.10 说明，如果 $\operatorname{Var}(Y_t)$ 大致和 $\mu_t^2$ 成正比，那么 $\log Y_t$ 的方差可以近似稳定。Rmk 10.11 进一步说明，对于乘法增长过程，log difference 近似等于收益率。因此差分处理的是趋势或 unit root，变换处理的是尺度和方差不稳定；实际建模时两者可以同时出现。

---

# Lecture 11: Statistical Inference Overview, CLT Review and Sample ACF Asymptotics

## Part A. 课堂内容还原

### Rmk 11.1 Course Roadmap: From ARMA Models to Statistical Inference

Lecture 11 开头把课程分成两个部分。Section 1 是 ARMA(p,q)，大致对应前 1--5 章；Section 2 是 statistical inference，大致对应 6--9 章。后续章节包括 model specification、parameter estimation、diagnostic checking 和 forecasting。

### Rmk 11.2 Chapter 6: Model Specification

Chapter 6 的主题是 **model specification**。对 ARIMA(p,d,q)，核心问题是：

\[
\text{How to select }p,d,q?
\]

板书列出四种工具：ACF、PACF、EACF、AIC/BIC。Lecture 11--12 主要开始讲 ACF 和 PACF。

### Rmk 11.3 Chapter 7: Parameter Estimation

Chapter 7 的主题是 **parameter estimation**。若

\[
\nabla^dY_t\sim ARMA(p,q),
\]

则要估计的参数包括

\[
\boldsymbol{\phi}=(\phi_1,\ldots,\phi_p)^T,
\]

\[
\boldsymbol{\theta}=(\theta_1,
\ldots,\theta_q)^T,
\]

以及

\[
\sigma^2,
\qquad
\mu.
\]

板书列出的估计方法包括 method of moments、OLS 和 MLE。

### Rmk 11.4 Chapter 8 and Chapter 9

Chapter 8 是 **diagnostic checking**，包括假设检验，例如残差是否满足

\[
e_t\sim N(0,\sigma^2).
\]

Chapter 9 是 **forecasting**。给定观测

\[
Y_1,
\ldots,Y_n,
\]

目标是预测

\[
\widehat{Y}_{n+1},
\ldots,
\widehat{Y}_{n+k}.
\]

### Thm 11.5 CLT Review

板书开始复习 central limit theorem。设

\[
X_1,
\ldots,X_n \overset{iid}{\sim} X,
\]

并且

\[
E(X)=\mu,
\qquad
\operatorname{Var}(X)=\sigma^2.
\]

令

\[
T_n=\frac{1}{n}\sum_{i=1}^{n}X_i.
\]

则

\[
\frac{T_n-E(T_n)}{\sqrt{\operatorname{Var}(T_n)}}
=\frac{\sqrt n(T_n-
\mu)}{\sigma}
\xrightarrow{d}N(0,1).
\]

等价地，

\[
\sqrt n(T_n-\mu)
\xrightarrow{d}N(0,\sigma^2).
\]

### Def 11.6 Characteristic Function

随机变量 $X$ 的 characteristic function 定义为

\[
\varphi_X(t)=E(e^{itX}).
\]

Characteristic function 与 distribution function 一一对应。也就是说，若一列随机变量的 characteristic functions 收敛到某个随机变量的 characteristic function，则可以推出分布收敛。

特别地，如果

\[
X\sim N(0,1),
\]

则

\[
\varphi_X(t)=e^{-t^2/2}.
\]

如果

\[
X\sim N(0,\sigma^2),
\]

则

\[
\varphi_X(t)=e^{-\sigma^2t^2/2}.
\]

### Prop 11.7 Characteristic-function Proof Sketch for CLT

令

\[
S_n=\sqrt n(T_n-\mu)=\frac{1}{\sqrt n}\sum_{i=1}^{n}(X_i-\mu).
\]

由于 $X_i$ 独立同分布，

\[
\varphi_{S_n}(t)
=E\left[\exp\left(it\frac{1}{\sqrt n}\sum_{i=1}^{n}(X_i-
\mu)\right)\right]
=\prod_{i=1}^{n}E\left[\exp\left(it\frac{X_i-
\mu}{\sqrt n}\right)\right].
\]

因此

\[
\varphi_{S_n}(t)
=\left[
E\left[\exp\left(it\frac{X-
\mu}{\sqrt n}\right)\right]
\right]^n.
\]

对指数函数作 Taylor expansion：

\[
\exp(x)=1+x+\frac{x^2}{2}+o(x^2).
\]

取

\[
x=it\frac{X-
\mu}{\sqrt n}.
\]

由于

\[
E(X-
\mu)=0,
\qquad
E[(X-
\mu)^2]=\sigma^2,
\]

得到

\[
E\left[\exp\left(it\frac{X-
\mu}{\sqrt n}\right)\right]
=1-
\frac{t^2\sigma^2}{2n}+o\left(\frac1n\right).
\]

于是

\[
\varphi_{S_n}(t)
=\left[1-
\frac{t^2\sigma^2}{2n}+o\left(\frac1n\right)\right]^n
\to e^{-t^2\sigma^2/2}.
\]

这正是 $N(0,\sigma^2)$ 的 characteristic function。因此

\[
S_n\xrightarrow{d}N(0,\sigma^2).
\]

**【原笔记留白/中断】** 板书中的 characteristic-function 推导写得较跳跃，中间有“复杂了”的旁注；上面这一版是根据板书方向补齐的标准推导。

### Lem 11.8 Quadratic Form Facts for Normal Vectors

Lecture 11 后面复习 normal quadratic forms。若

\[
X\sim N(0,I_n),
\]

并且 $A$ 是对称矩阵，则

\[
E(X^TAX)=\operatorname{tr}(A),
\]

并且

\[
\operatorname{Var}(X^TAX)=2\operatorname{tr}(A^2).
\]

更一般地，若

\[
X\sim N(0,\Sigma),
\]

则

\[
E(X^TAX)=\operatorname{tr}(A\Sigma),
\]

并且

\[
\operatorname{Var}(X^TAX)=2\operatorname{tr}(A\Sigma A\Sigma).
\]

**【根据前后文补充】** 这些公式服务于 sample autocovariance 和 sample ACF 的渐近分布推导，因为样本自协方差可以写成类似 $Y^TA Y$ 的二次型。

### Def 11.9 Sample Autocovariance and Sample Autocorrelation in Matrix Form

设

\[
\mathbf Y=(Y_1,
\ldots,Y_n)^T.
\]

样本均值去除可以通过 projection matrix 表示。令

\[
P=\frac{1}{n}\mathbf 1\mathbf 1^T,
\]

则

\[
(I-P)\mathbf Y
\]

就是去均值后的向量。对 lag $k$，样本自协方差可以写成近似的二次型：

\[
\hat\gamma_k
\approx
\frac1n\mathbf Y^T(I-P)Q_k(I-P)\mathbf Y,
\]

其中 $Q_k$ 是把向量向后移动 $k$ 阶的矩阵。

**【原笔记留白/中断】** 板书中 $Q_k$、$P$ 和二次型的精确定义夹在黑板照片中，部分不可完全辨认；但推导目标非常明确：把 $\hat\gamma_k$ 写成 normal quadratic form，从而使用 Lem 11.8。

### Prop 11.10 Asymptotic Distribution of Sample ACF under White Noise

板书给出 white noise 的例子。若

\[
Y_t=e_t,
\qquad
 e_t\overset{iid}{\sim}N(0,\sigma^2),
\]

则理论 autocovariance 满足

\[
\gamma_k=0,
\qquad k\ge1,
\]

理论 autocorrelation 也满足

\[
\rho_k=0,
\qquad k\ge1.
\]

对固定的 $k$，有渐近结论

\[
\sqrt n(\hat\rho_k-
\rho_k)
\xrightarrow{d}N(0,1).
\]

由于 $\rho_k=0$，这等价于

\[
\sqrt n\hat\rho_k
\xrightarrow{d}N(0,1).
\]

对固定的多个 lag，可以写成向量形式：

\[
\sqrt n(\hat\rho_1,
\ldots,
\hat\rho_m)^T
\xrightarrow{d}N(0,I_m).
\]

这就是白噪声样本 ACF 图中常见置信带 $\pm 1.96/\sqrt n$ 的理论来源。

### Rmk 11.11 Alternative Bounds for Sample ACF

扫描件中出现一张 sample ACF 的图，标题大意是 “Alternative Bounds for the Sample ACF for the MA(3) Process”。这说明后面不只关心 white noise 的 ACF 置信带，也会关心 MA(q) 情形下样本 ACF 的渐近方差。

**【原笔记留白/中断】** 该页主要是图和黑板照片，图中具体数值和公式不完整；本笔记暂时只标记它作为 Lecture 12 的过渡。

## Part B. 复习视角

Lecture 11 的任务是把课程从“模型结构”推进到“统计推断”。Rmk 11.1 到 Rmk 11.4 先搭出 Section 2 的路线图：Chapter 6 选模型，Chapter 7 估参数，Chapter 8 做诊断，Chapter 9 做预测。也就是说，前面学的 ARMA/ARIMA 只是模型族，后面要解决的是如何从数据中选择、估计、检验和预测。

这节课的技术核心是 **渐近分布**。Thm 11.5 到 Prop 11.7 复习 CLT 和 characteristic function，因为之后样本 ACF、参数估计量、残差诊断统计量都需要用到“样本统计量在大样本下近似正态”这个思想。这里不是为了重新学概率论，而是为了给时间序列推断提供工具。

Lem 11.8 到 Prop 11.10 把普通 CLT 推向时间序列中的二次型。样本自协方差不是简单的样本均值，而是可以写成 $\mathbf Y^TA\mathbf Y$ 的二次型，所以需要 normal quadratic form 的期望和方差。最后得到白噪声下 $\sqrt n\hat\rho_k\to N(0,1)$，这直接解释了 ACF 图中的显著性判断。

这节复习时最关键的是把“ACF 图上的线”理解成统计推断对象。样本 ACF 中某一根柱子不等于理论 ACF，它有抽样波动。只有当 $\hat\rho_k$ 明显超过理论波动范围时，我们才把它视为显著相关。Lecture 12 会用这个想法来做 order selection。

---

# Lecture 12: Order Selection by ACF and PACF

## Part A. 课堂内容还原

### Rmk 12.1 Order Selection for MA(q)

Lecture 12 从 **order selection for MA(q)** 开始。设模型是 ARMA(p,q)，但先考虑 MA(q) 的识别。核心思想是：MA(q) 的理论 ACF 在 $q$ 阶之后截尾，即

\[
\rho_k=0,
\qquad k>q.
\]

因此可以通过 sample ACF 判断 $q$ 的大小。

### Ex 12.2 White Noise as MA(0)

white noise 可以看成 MA(0)：

\[
Y_t=e_t,
\qquad
 e_t\overset{iid}{\sim}N(0,\sigma^2).
\]

此时

\[
\rho_k=0,
\qquad k=1,2,\ldots.
\]

对每个 lag $k$，可以考虑假设

\[
H_{0,k}:\rho_k=0.
\]

由 Lecture 11 的结论，

\[
\sqrt n\hat\rho_k\xrightarrow{d}N(0,1).
\]

因此在白噪声情形下，若样本 ACF 的绝对值大致超过

\[
\frac{1.96}{\sqrt n},
\]

就可以认为该 lag 的相关性显著偏离 0。

### Prop 12.3 Asymptotic Distribution of Sample ACF for MA(q)

对 MA(q) 过程，当 $k>q$ 时，理论上

\[
\rho_k=0.
\]

但是样本 ACF 仍然有抽样波动。板书写出渐近结论：

\[
\sqrt n\hat\rho_k
\xrightarrow{d}N(0,c_{kk}),
\qquad k>q.
\]

其中对角方差项可写成 Bartlett formula 的形式：

\[
c_{kk}=1+2\rho_1^2+2\rho_2^2+\cdots+2\rho_q^2.
\]

**【根据前后文补充】** 这说明 MA(q) 后面那些理论为 0 的 lag，其样本波动方差通常不是 1，而是受前 $q$ 阶 autocorrelations 的影响。white noise 是 $q=0$ 的特例，此时 $c_{kk}=1$。

### Rmk 12.4 How to Select q by ACF

选择 MA(q) 阶数时，核心不是看某一个 lag 是否为 0，而是看样本 ACF 是否呈现 **cut-off**。如果理论上 $k>q$ 后 $\rho_k=0$，那么样本 ACF 在 $q$ 阶之后应该大致落在置信带内。

板书写到：“核心考虑：选 which $k$；$H_{0,k}:\rho_k=0$；但我们不知道 $q$，需要 check。”这句话的意思是：实际分析时 $q$ 未知，所以需要观察从哪个 lag 之后 ACF 不再显著。

### Rmk 12.5 When MA(q) May Not Be Appropriate

扫描件中有一张 ACF 图，旁注写到“若线性递减，可能不适合使用 MA 模型”。这是非常重要的模型识别直觉。

MA(q) 的 ACF 理论上应当在有限阶后截尾。如果 sample ACF 不是截尾，而是缓慢衰减、线性递减、指数衰减或呈振荡衰减，那么它更可能来自 AR 或 ARMA 结构，而不是低阶 MA 模型。

**【根据前后文补充】** 简单记忆是：MA(q) 的 ACF cut off，AR(p) 的 ACF tail off。真正的数据有抽样波动，所以不要机械地要求每一根柱子完全为 0，而是看整体形状。

### Rmk 12.6 Order Selection for AR(p): Why ACF Is Not Enough

Lecture 12 接着转向 AR(p) 的阶数选择。板书先写 AR(1)：

\[
Y_t=\phi Y_{t-1}+e_t.
\]

它的 autocorrelation function 为

\[
\rho_k=\phi^k,
\qquad k\ge0.
\]

只要 $\phi\ne0$，所有 $\rho_k$ 通常都不等于 0。因此 AR(1) 的 ACF 不会像 MA(q) 一样在有限阶截尾。

对 AR(2)：

\[
Y_t=\phi_1Y_{t-1}+\phi_2Y_{t-2}+e_t.
\]

由 Yule--Walker equation，

\[
\rho_k=\phi_1\rho_{k-1}+\phi_2\rho_{k-2}.
\]

因此 AR(2) 的 ACF 也是递推产生的，通常不会在 lag 2 后直接变为 0。板书旁注指出：由于所有 $\rho_k$ 不一定为 0，无法像 MA(q) 一样用 ACF 直接选择。

### Def 12.7 Partial Autocorrelation Function

为了解决 AR(p) 的阶数选择问题，引入 **partial autocorrelation function**，简称 PACF。

对 $k\ge2$，定义

\[
\phi_{kk}=\operatorname{Corr}(Y_t,Y_{t-k}\mid Y_{t-1},Y_{t-2},\ldots,Y_{t-k+1}).
\]

对 $k=1$，定义

\[
\phi_{11}=\operatorname{Corr}(Y_t,Y_{t-1})=\rho_1.
\]

这里的 conditional correlation 可以理解为：先把 $Y_t$ 中能被中间变量 $Y_{t-1},\ldots,Y_{t-k+1}$ 线性解释的部分拿掉，再把 $Y_{t-k}$ 中能被这些中间变量线性解释的部分拿掉，然后计算两个 residual 的 correlation。

### Prop 12.8 PACF of AR(1)

对 AR(1)

\[
Y_t=\phi Y_{t-1}+e_t,
\]

有

\[
\phi_{11}=\rho_1=\phi.
\]

当 $k\ge2$ 时，考虑

\[
\phi_{kk}=\operatorname{Corr}(Y_t,Y_{t-k}\mid Y_{t-1},\ldots,Y_{t-k+1}).
\]

因为

\[
Y_t=\phi Y_{t-1}+e_t,
\]

在给定 $Y_{t-1}$ 后，$Y_t$ 中除去可预测部分后只剩 innovation $e_t$。而 $e_t$ 与过去的 $Y_{t-k}$ 以及 $Y_{t-1},\ldots,Y_{t-k+1}$ 都不相关。因此

\[
\phi_{kk}=0,
\qquad k\ge2.
\]

所以 AR(1) 的 PACF 在 lag 1 后截尾：

\[
\phi_{11}=\rho_1,
\qquad
\phi_{kk}=0\quad(k\ge2).
\]

### Prop 12.9 PACF of AR(p)

一般的 AR(p) 模型为

\[
Y_t=\phi_1Y_{t-1}+\phi_2Y_{t-2}+\cdots+\phi_pY_{t-p}+e_t.
\]

当 $k\ge p+1$ 时，条件集合

\[
Y_{t-1},Y_{t-2},\ldots,Y_{t-k+1}
\]

已经包含了 AR(p) 的全部直接预测变量 $Y_{t-1},\ldots,Y_{t-p}$。因此，在给定这些变量后，$Y_t$ 剩下的不可预测部分就是 $e_t$，而 $e_t$ 与更早的 $Y_{t-k}$ 不相关。于是

\[
\phi_{kk}=0,
\qquad k\ge p+1.
\]

这就是 AR(p) 的 PACF 截尾性质。

**【原笔记留白/中断】** 扫描件最后一页对 AR(p) 情形的推导停在“$k\ge p+1$ 时相关项为 0；$k\le p$ 时仍有剩余项”的位置，没有继续给出 $\phi_{kk}$ 在 $k\le p$ 时的完整表达式。

**【根据前后文补充】** 做阶数选择时，我们主要需要的就是截尾结论：AR(p) 的 PACF 在 lag $p$ 后为 0。$k\le p$ 时的具体数值通常不需要手算完整闭式，而是由 Yule--Walker 或线性预测方程估计。

### Rmk 12.10 ACF/PACF Pattern Summary

根据 Lecture 12 的讨论，可以形成如下识别直觉。

MA(q) 的理论 ACF 在 $q$ 阶后截尾，而 PACF 通常拖尾。AR(p) 的理论 PACF 在 $p$ 阶后截尾，而 ACF 通常拖尾。ARMA(p,q) 一般 ACF 和 PACF 都拖尾，因此单靠 ACF/PACF 不一定能精确选出 p 和 q，需要结合 EACF、AIC/BIC 以及残差诊断。

**【根据前后文补充】** 这段是对板书中 ACF 与 PACF 识别逻辑的总结。扫描件里已经分别推了 MA(q) 的 ACF 截尾和 AR(p) 的 PACF 截尾，但没有完整写成表格式总结。

## Part B. 复习视角

Lecture 12 的主线是 **model specification**，也就是怎样从数据的相关结构里初步判断模型阶数。Lecture 11 先给出 sample ACF 的渐近分布，Lecture 12 立刻把它用于 order selection。这里的逻辑很自然：理论 ACF/PACF 是模型性质，sample ACF/PACF 是数据估计；只有知道估计量的抽样波动，才能判断某个 lag 的 spike 是真实结构还是随机误差。

前半节讲 MA(q)。Rmk 12.1 到 Prop 12.3 的关键是：MA(q) 的理论 ACF 在 $q$ 阶后为 0，但样本 ACF 不会真的完全等于 0，所以需要用渐近正态近似判断显著性。white noise 是 MA(0)，它的 sample ACF 置信带大致是 $\pm 1.96/\sqrt n$；一般 MA(q) 的后续 lag 波动还会受 $\rho_1,\ldots,\rho_q$ 影响。

后半节讲 AR(p)。Rmk 12.6 说明 ACF 对 AR 模型不够用，因为 AR(1) 的 $\rho_k=\phi^k$ 通常所有 lag 都非零，AR(2) 的 ACF 也通过 Yule--Walker 递推延续下去。因此必须引入 Def 12.7 的 partial autocorrelation。PACF 的本质是控制中间 lag 之后，考察 $Y_t$ 和 $Y_{t-k}$ 的直接线性关系。

Prop 12.8 和 Prop 12.9 是这节课最关键的结论：AR(1) 的 PACF 在 lag 1 后截尾，一般 AR(p) 的 PACF 在 lag p 后截尾。这和 MA(q) 的 ACF 截尾形成对偶关系。复习时要把这句话背后的原因讲清楚：AR(p) 中 $Y_t$ 的直接父节点只有 $Y_{t-1},\ldots,Y_{t-p}$，一旦条件集合已经包含这些变量，额外更远的 $Y_{t-k}$ 就只通过这些中间变量间接相关；控制掉中间变量后，它和 $Y_t$ 的 innovation 不再相关。

最终，Lecture 12 给出的不是机械选阶公式，而是一套看图逻辑。ACF 截尾支持 MA(q)，PACF 截尾支持 AR(p)，两者都拖尾则考虑 ARMA(p,q)。但实际数据有随机波动，所以还要结合 EACF、AIC/BIC 和 residual diagnostics。这个逻辑会继续连接到后面的 parameter estimation 和 diagnostic checking。


-
# Lecture 13: MA/AR Order Selection and PACF

## Part A. 课堂内容还原

### Rmk 13.1 继续模型选择：MA(q) 的 ACF 截尾

前面已经建立了 MA(q) 模型的基本结构。若

\[
Y_t=\theta(B)e_t,
\]

其中

\[
\theta(B)=1-\theta_1B-\cdots-\theta_qB^q,
\]

则 $Y_t$ 可以写成有限个 white noise 的线性组合。于是，当两个时间点相隔超过 $q$ 个 lag 时，它们不再共享同一个 white noise 项，所以理论自相关函数满足

\[
\rho_k=0,\qquad k>q.
\]

更完整地说，若把 MA(q) 写成

\[
Y_t=\sum_{j=0}^q \psi_j e_{t-j},\qquad \psi_0=1,
\]

则

\[
\gamma_k=\sigma^2\sum_{j=0}^{q-k}\psi_j\psi_{j+k},\qquad 0\le k\le q,
\]

并且

\[
\gamma_k=0,\qquad k>q.
\]

因此

\[
\rho_k=\frac{\gamma_k}{\gamma_0}
= \frac{\sum_{j=0}^{q-k}\psi_j\psi_{j+k}}
{\sum_{j=0}^q\psi_j^2},
\qquad 0\le k\le q,
\]

而

\[
\rho_k=0,\qquad k>q.
\]

这就是 MA(q) 模型最重要的识别特征：**ACF 在 q 阶以后截尾**。

### Prop 13.2 Sample ACF 在 MA(q) 阶数选择中的渐近分布

设 $\hat\rho_k$ 是 sample ACF。对于 MA(q) 过程，当

\[
k>q
\]

时，理论上有

\[
\rho_k=0.
\]

板书中给出的渐近结论是

\[
\sqrt n\,\hat\rho_k \xrightarrow{D} N(0,c_{kk}),
\]

其中

\[
c_{kk}=1+2\rho_1^2+\cdots+2\rho_q^2.
\]

因此可以考虑假设检验

\[
H_{0,k}:\rho_k=0.
\]

如果使用近似正态临界值，那么拒绝域可以写成

\[
W_k=
\left\{
|\hat\rho_k|>
z_{\alpha/2}\sqrt{\frac{c_{kk}}{n}}
\right\}.
\]

在实际画图时，常见的样本 ACF 图会画出上下置信界。如果原假设是 white noise，即 $q=0$，那么

\[
c_{kk}=1,
\]

对应的近似置信界就是

\[
\pm \frac{z_{\alpha/2}}{\sqrt n}.
\]

常用的粗略规则是用

\[
\pm\frac{1.96}{\sqrt n}
\]

判断 sample ACF 是否显著偏离 0。

### Rmk 13.3 从 sample ACF 选择 MA(q) 的经验规则

对于 MA(q)，理论 ACF 在 $q$ 阶以后为 0。因此看 sample ACF 图时，核心不是看前几个 lag 是否都显著，而是看从某个 lag 之后是否基本落入置信界。

如果从某个 $q+1$ 开始，后面的 sample ACF 大体都不显著，那么 $q$ 可以作为候选 MA 阶数。板书中画出了 ACF 图，并强调从右往左看“最后一个显著 lag”。这对应的直觉是：如果最右侧仍然显著，说明 MA 阶数可能还不够；如果某个 lag 之后都不显著，那么截尾位置可能就在它前面。

【根据前后文补充】严格地说，真实 MA(q) 的置信界并不总是简单的 $\pm1.96/\sqrt n$，因为 $c_{kk}$ 中含有 $\rho_1,\ldots,\rho_q$。但在初步识别阶段，软件和教材常常先使用 white-noise 近似置信界作为可视化参考，再结合后续 AIC、BIC 或残差诊断确认模型。

### Rmk 13.4 AR(p) 不能直接用 ACF 截尾选阶

对于 AR(p)，情形不同。AR(p) 模型可以写成

\[
\phi(B)Y_t=e_t,
\]

也就是

\[
Y_t=\phi(B)^{-1}e_t.
\]

在平稳条件下，逆算子可以展开为无穷阶 MA：

\[
Y_t=\sum_{j=0}^{\infty}\psi_j e_{t-j}.
\]

因此 AR(p) 的 ACF 通常不会在有限阶后严格变成 0。比如 AR(1) 的 ACF 具有形式

\[
\rho_k=\phi^k,\qquad k\ge 0,
\]

它是指数衰减，而不是截尾。AR(2) 的 ACF 由 Yule-Walker recursion 决定，一般也不会有限阶截尾。

这说明：**MA(q) 可以主要看 ACF 截尾，AR(p) 不能靠 ACF 截尾选阶**。这就引出下一步的工具：PACF。

### Def 13.5 Partial Autocorrelation Function

对于平稳时间序列，k 阶偏自相关函数定义为

\[
\phi_{kk}
= \operatorname{Corr}
\left(
Y_t,Y_{t-k}
\mid
Y_{t-1},Y_{t-2},\ldots,Y_{t-k+1}
\right),
\qquad k\ge 2.
\]

一阶偏自相关没有中间变量需要控制，因此定义为

\[
\phi_{11}
= \operatorname{Corr}(Y_t,Y_{t-1})
= \rho_1.
\]

PACF 的含义是：在已经控制中间 lag $Y_{t-1},\ldots,Y_{t-k+1}$ 以后，$Y_t$ 与 $Y_{t-k}$ 之间还剩多少线性相关。它不是普通相关，而是**条件线性相关**。

### Lem 13.6 多元正态向量的线性条件分布

板书在引入 PACF 后，先回顾了多元正态的条件分布。设

\[
Y= \begin{pmatrix}
Y_1\\
Y_2
\end{pmatrix}
\sim
N\left(
0,
\begin{pmatrix}
\Sigma_{11} & \Sigma_{12}\\
\Sigma_{21} & \Sigma_{22}
\end{pmatrix}
\right).
\]

我们希望用 $Y_2$ 线性预测 $Y_1$，即找矩阵 $A$ 使得

\[
E\|Y_1-AY_2\|^2
\]

最小。对 $A$ 求一阶条件，得到

\[
\Sigma_{12}=A\Sigma_{22},
\]

因此

\[
A=\Sigma_{12}\Sigma_{22}^{-1}.
\]

于是可以分解为

\[
Y_1=\Sigma_{12}\Sigma_{22}^{-1}Y_2+\varepsilon,
\]

其中

\[
\operatorname{Cov}(\varepsilon,Y_2)=0.
\]

若联合分布是正态，则不相关进一步推出独立，因此

\[
Y_1\mid Y_2
\sim
N\left(
\Sigma_{12}\Sigma_{22}^{-1}Y_2,\,
\Sigma_{11}-\Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}
\right).
\]

【根据前后文补充】扫描件中这一段推导符号比较密集，最后一行条件方差公式有局部涂改。上式是标准多元正态条件分布，也是板书推导 PACF 的必要工具。

### Ex 13.7 二阶 PACF 的条件相关写法

二阶 PACF 是

\[
\phi_{22}
= \operatorname{Corr}(Y_t,Y_{t-2}\mid Y_{t-1}).
\]

若过程平稳且方差标准化为

\[
\gamma_0=1,
\]

则

\[
\operatorname{Cov}(Y_t,Y_{t-1})=\rho_1,
\qquad
\operatorname{Cov}(Y_t,Y_{t-2})=\rho_2.
\]

对三维向量

\[
(Y_t,Y_{t-2},Y_{t-1})^T
\]

使用 Lem 13.6，可以得到条件协方差

\[
\operatorname{Cov}(Y_t,Y_{t-2}\mid Y_{t-1})
= \rho_2-\rho_1^2,
\]

条件方差为

\[
\operatorname{Var}(Y_t\mid Y_{t-1})=1-\rho_1^2,
\]

以及

\[
\operatorname{Var}(Y_{t-2}\mid Y_{t-1})=1-\rho_1^2.
\]

因此

\[
\phi_{22}
= \frac{\rho_2-\rho_1^2}{1-\rho_1^2}.
\]

这就是后面用 sample ACF 估计 sample PACF 时最常见的低阶公式。

### Def 13.8 PACF 的线性投影定义

PACF 也可以通过线性预测来定义。考虑用前 $k$ 个 lag 线性预测 $Y_t$：

\[
Y_t
= \phi_{k1}Y_{t-1}
+
\phi_{k2}Y_{t-2}
+\cdots+
\phi_{kk}Y_{t-k}
+
\varepsilon_t^{(k)}.
\]

其中

\[
\phi_k=
(\phi_{k1},\ldots,\phi_{kk})^T
\]

由 Yule-Walker 型方程确定：

\[
\Gamma_k\phi_k=\rho_k,
\]

其中

\[
\Gamma_k=
\begin{pmatrix}
1 & \rho_1 & \cdots & \rho_{k-1}\\
\rho_1 & 1 & \cdots & \rho_{k-2}\\
\vdots & \vdots & \ddots & \vdots\\
\rho_{k-1} & \rho_{k-2} & \cdots & 1
\end{pmatrix},
\qquad
\rho_k=
\begin{pmatrix}
\rho_1\\
\rho_2\\
\vdots\\
\rho_k
\end{pmatrix}.
\]

因此

\[
\phi_k=\Gamma_k^{-1}\rho_k.
\]

PACF 的第 $k$ 阶值就是最后一个系数：

\[
\phi_{kk}=e_k^T\phi_k,
\]

其中

\[
e_k=(0,\ldots,0,1)^T.
\]

这个定义和 Def 13.5 的条件相关定义在高斯/线性预测框架下是一致的。

### Prop 13.9 AR(p) 的 PACF 截尾性质

若 $Y_t$ 是 AR(p) 过程：

\[
Y_t=
\phi_1Y_{t-1}
+\cdots+
\phi_pY_{t-p}
+
e_t,
\]

则 PACF 满足

\[
\phi_{kk}=0,\qquad k>p.
\]

原因是：一旦已经控制了 $Y_{t-1},\ldots,Y_{t-p}$，更远的 $Y_{t-k}$ 对 $Y_t$ 不再提供新的线性预测信息。对 AR(1) 来说，

\[
Y_t=\phi Y_{t-1}+e_t.
\]

因此

\[
\phi_{11}=\rho_1=\phi,
\]

而对所有

\[
k\ge 2
\]

都有

\[
\phi_{kk}=0.
\]

更一般地，对 AR(p)，PACF 在 $p$ 阶以后截尾。因此 AR(p) 的阶数识别主要看 PACF，而不是 ACF。

### Prop 13.10 Sample PACF 的渐近分布

令 $\hat\phi_{kk}$ 是由 sample ACF 代入 Yule-Walker 方程得到的 sample PACF。板书中给出结论：若真实模型为 AR(p)，则当

\[
k>p
\]

时，

\[
\sqrt n\,\hat\phi_{kk}
\xrightarrow{D}
N(0,1).
\]

因此在 PACF 图中，对于超过真实 AR 阶数的 lag，近似置信界可以取

\[
\pm\frac{1.96}{\sqrt n}.
\]

这和 MA(q) 看 ACF 的逻辑平行：MA(q) 是 ACF 在 q 阶后近似落入置信界；AR(p) 是 PACF 在 p 阶后近似落入置信界。

【根据前后文补充】扫描件后半部分用 block matrix inverse 和 Yule-Walker 方程说明这个结论，但黑板照片较模糊，局部推导无法完整辨认。这里保留老师的结论，并补充标准表述：AR(p) 之后的 sample PACF 渐近服从 $N(0,1/n)$。

### Ex 13.11 White Noise 下二阶 PACF 的 Delta Method

若

\[
Y_t=e_t\sim MA(0),
\]

则

\[
\rho_1=\rho_2=0.
\]

对于前两个 sample ACF，有

\[
\sqrt n
\begin{pmatrix}
\hat\rho_1-\rho_1\\
\hat\rho_2-\rho_2
\end{pmatrix}
\xrightarrow{D}
N(0,I_2).
\]

又由 Ex 13.7，

\[
\phi_{22}=f(\rho_1,\rho_2)
= \frac{\rho_2-\rho_1^2}{1-\rho_1^2}.
\]

因此

\[
\hat\phi_{22}
= f(\hat\rho_1,\hat\rho_2).
\]

对 $f$ 在 $(0,0)$ 处做 Taylor expansion。梯度为

\[
\nabla f(0,0)=
\begin{pmatrix}
0\\
1
\end{pmatrix}.
\]

所以由 Delta Method，

\[
\sqrt n(\hat\phi_{22}-0)
\xrightarrow{D}
N(0,1).
\]

这与 Prop 13.10 在 white noise 情形下的结论一致。

## Part B. 复习视角

Lecture 13 的主线非常清楚：前面已经知道 **MA(q) 看 ACF 截尾**，但 AR(p) 的 ACF 不截尾，所以需要引入 **PACF** 来选择 AR 阶数。Rmk 13.1 到 Rmk 13.4 完成了这个逻辑转折：MA 的有限记忆直接反映在 ACF 上，AR 的递推结构会产生无限尾部，因此普通 ACF 不能直接告诉我们 p。

PACF 的关键直觉是 **控制中间 lag 以后再看远端 lag 是否仍有额外贡献**。Def 13.5 直接把这个想法写成条件相关；Def 13.8 则把它写成线性投影的最后一个系数。实际做题时，后者更常用，因为 sample PACF 往往就是通过 Yule-Walker 型线性方程从 sample ACF 递推出来的。

这一讲的技术核心是 Lem 13.6。PACF 说的是条件相关，而条件相关需要知道给定中间变量以后剩余的协方差结构。多元正态条件分布给出一个标准公式：条件均值是线性投影，条件方差是 Schur complement。Ex 13.7 的二阶 PACF 公式就是最直观的例子：

\[
\phi_{22}
= \frac{\rho_2-\rho_1^2}{1-\rho_1^2}.
\]

这说明 PACF 不是单纯的 $\rho_2$，而是从 $\rho_2$ 中扣掉通过 $Y_{t-1}$ 传递的那部分相关。

复习时最重要的是记住两个并列结论。**MA(q) 的 ACF 截尾，AR(p) 的 PACF 截尾**。因此如果 ACF 在 q 阶以后掉进置信界，而 PACF 拖尾，优先考虑 MA(q)；如果 PACF 在 p 阶以后掉进置信界，而 ACF 拖尾，优先考虑 AR(p)。若二者都拖尾，则要进入后面的 ARMA 和 EACF。

---

# Lecture 14: Midterm Exam

## Part A. 课堂内容还原

Lecture 14 没有新课内容，用于期中考试。

## Part B. 复习视角

这一讲没有新的定义、定理或例题。按照课程结构，它位于 **AR/MA/ARMA 基础模型** 与 **模型选择和统计推断** 之间。期中前的核心复习对象应当包括 stationarity、linear process、MA(q)、AR(p)、ARMA(p,q)、ARIMA、ACF、PACF、Yule-Walker equation、backshift operator、差分算子与样本 ACF/PACF 的基本性质。

---

# Lecture 15: Extended ACF for ARMA Model Selection

## Part A. 课堂内容还原

### Rmk 15.1 Chapter 6 的模型选择问题

进入 Chapter 6 之后，问题从“模型是什么”转向“模型怎么选”。对 ARIMA(p,d,q) 来说，模型选择至少包含三个层次：

\[
p,\qquad d,\qquad q.
\]

前面已经建立了两个基本识别工具。对于 MA(q)，ACF 在 q 阶后截尾：

\[
\rho_k=0,\qquad k>q.
\]

并且当

\[
k>q
\]

时，

\[
\sqrt n\,\hat\rho_k
\xrightarrow{D}
N(0,c_{kk}).
\]

对于 AR(p)，PACF 在 p 阶后截尾：

\[
\phi_{kk}=0,\qquad k>p,
\]

并且当

\[
k>p
\]

时，

\[
\sqrt n\,\hat\phi_{kk}
\xrightarrow{D}
N(0,1).
\]

但是对一般 ARMA(p,q)，ACF 和 PACF 通常都会拖尾，单独看 ACF 或 PACF 不足以同时识别 p 和 q。于是引入 **Extended ACF**，记作 EACF。

### Rmk 15.2 ARMA(1,1) 中直接用 AR 回归会出现的问题

考虑 ARMA(1,1)：

\[
Y_t=\phi Y_{t-1}+e_t-\theta e_{t-1}.
\]

如果 $\theta=0$，模型退化为 AR(1)：

\[
Y_t=\phi Y_{t-1}+e_t.
\]

此时用 $Y_t$ 对 $Y_{t-1}$ 做回归，OLS 估计会收敛到

\[
\phi.
\]

但如果 $\theta\ne 0$，误差项

\[
e_t-\theta e_{t-1}
\]

与回归变量 $Y_{t-1}$ 之间通常存在相关性，因为 $Y_{t-1}$ 本身包含 $e_{t-1}$。这时直接把 ARMA(1,1) 当 AR(1) 回归，回归系数的极限不再是 $\phi$，而是与自相关 $\rho_1$ 有关。

【根据前后文补充】扫描件第 1–4 页围绕这个问题推导：若忽略 MA 部分，直接回归得到的系数不能稳定识别 AR 参数；因此需要构造一种方法，使得在假设不同 AR 阶和 MA 阶时，能够看“过滤后的序列”是否表现为有限阶 MA。这就是 EACF 的出发点。

### Def 15.3 Extended ACF 的基本想法

EACF 的目标是同时识别 ARMA(p,q) 中的 p 和 q。设真实模型为

\[
Y_t
= \phi_1Y_{t-1}
+\cdots+
\phi_pY_{t-p}
+
e_t
-\theta_1e_{t-1}
-\cdots
-\theta_qe_{t-q}.
\]

如果 AR 阶数 p 已经正确过滤掉，那么剩下的残差应当像一个 MA(q)。因此 EACF 的基本想法是：对一系列候选 AR 阶数 k 做过滤，再检查过滤后序列的 ACF 是否在某个 MA 阶数 j 后截尾。

用符号表示，先根据候选 AR 阶数 k 构造过滤后序列

\[
W_{t,k}
= Y_t-\hat\phi_1^{(k)}Y_{t-1}
-\cdots-
\hat\phi_k^{(k)}Y_{t-k}.
\]

然后考察 $W_{t,k}$ 的 sample ACF。若在某个 j 之后近似为 0，则说明在 AR 阶数 k 下，剩余部分可能是 MA(j)。

【根据标准 TSA 结论补充】实际 EACF 算法通常会对不同的 k 和 j 构造一个二维表格，并对某些 residual autocorrelation 做显著性判断。若某个格子对应的 residual autocorrelation 不显著，就记为 “O”；若显著，就记为 “X”。真实 ARMA(p,q) 的 EACF 表中通常会从位置 $(p,q)$ 开始出现一个由 “O” 构成的三角形区域。

### Def 15.4 EACF 表格

EACF 表格的行对应候选 AR 阶数 k，列对应候选 MA 阶数 j。每一个格子大致检验：

\[
H_0:\text{在 AR 阶数 }k\text{ 过滤后，某个对应 lag 的残差自相关为 }0.
\]

若检验不拒绝，记为

\[
O.
\]

若检验拒绝，记为

\[
X.
\]

对于 ARMA(p,q)，理想情况下 EACF 表格中会出现如下模式：当候选 AR 阶数至少达到 p，候选 MA 阶数至少达到 q 时，残差自相关开始不显著。于是表格中会出现一个从 $(p,q)$ 开始的 “O” 三角形。

### Prop 15.5 ARMA(p,q) 的 EACF 识别模式

若真实模型是 ARMA(p,q)，则 EACF 的典型识别模式是：

\[
(k,j)=(p,q)
\]

附近开始出现系统性的零区域。具体说，当

\[
k\ge p,\qquad j\ge q
\]

时，经过足够的 AR 过滤后，剩余结构中不应再有超过 q 阶的 MA 相关，因此相应 EACF entry 倾向于不显著。

反过来，如果

\[
k<p
\]

则 AR 部分没有过滤干净，残差仍可能保留 AR 型拖尾结构；如果

\[
j<q
\]

则 MA 部分没有充分解释，残差对应 lag 仍可能显著。

【原笔记留白/中断】扫描件中有一张 EACF 表格和 ARMA(1,1) 示意图，但照片局部较暗，表格中每个 “O/X” 的具体位置不完全可辨认。这里保留 EACF 的标准识别结论：找从某个格点开始形成的 “O triangle”，其顶点作为 ARMA(p,q) 的候选阶数。

### Ex 15.6 ARMA(1,1) 的 EACF 示意

对 ARMA(1,1)：

\[
Y_t=\phi Y_{t-1}+e_t-\theta e_{t-1}.
\]

如果候选 AR 阶数

\[
k=0,
\]

则没有过滤掉 AR(1) 部分，残差仍带有 AR 结构，ACF 可能拖尾。

如果候选 AR 阶数

\[
k=1,
\]

则 AR 部分被正确过滤，剩余部分应近似为 MA(1)。这时在 EACF 表中，从候选 MA 阶数

\[
j=1
\]

开始，后续残差自相关应逐渐不显著。

因此对 ARMA(1,1)，理想 EACF 图像应当在

\[
(k,j)=(1,1)
\]

附近出现 “O triangle”。

### Rmk 15.7 EACF 与 ACF/PACF 的关系

ACF、PACF、EACF 的角色可以合在一起理解。ACF 最适合识别 MA(q)，因为 MA(q) 的 ACF 截尾。PACF 最适合识别 AR(p)，因为 AR(p) 的 PACF 截尾。EACF 是在 ARMA(p,q) 下使用的扩展工具，因为 ARMA 的 ACF 和 PACF 通常都不截尾，需要同时尝试不同的 AR 过滤阶数和 MA 截尾阶数。

实际建模时，EACF 不是唯一标准。它通常和 AIC、BIC、残差诊断一起使用。如果 EACF、AIC/BIC 和残差 white noise 检验指向相同阶数，模型选择就比较稳。

## Part B. 复习视角

Lecture 15 的核心是从 **单独选 p 或 q** 过渡到 **同时选 p 和 q**。MA(q) 看 ACF，AR(p) 看 PACF，这是两条很清楚的截尾规律。但一旦进入 ARMA(p,q)，普通 ACF 和 PACF 都可能拖尾，所以不能简单从图上读出阶数。

EACF 的想法其实非常自然：如果我们猜了一个 AR 阶数 k，那么可以先把 AR 部分过滤掉；如果 k 猜得足够大，剩下的应该主要像一个 MA 过程。于是再看过滤后序列的 ACF 是否在某个 j 阶后截尾。这样就把“同时选 p 和 q”的问题变成了一个二维表格搜索问题。

这节课最需要掌握的是 **O triangle** 的意义。EACF 表中行是候选 AR 阶数，列是候选 MA 阶数。真实 ARMA(p,q) 的信息通常表现为：从某个格点开始，后面形成一片不显著的零区域。这个格点的顶点就是候选的 $(p,q)$。如果只记一个结论，就是：**EACF 是为 ARMA(p,q) 的联合阶数识别服务的，而不是替代 ACF/PACF 的全部用途**。

---

# Lecture 16: Choosing the Differencing Order and Unit Root Tests

## Part A. 课堂内容还原

### Rmk 16.1 ARIMA 的非平稳性与差分阶数 d

ARIMA(p,d,q) 的一般形式是

\[
\phi(B)\nabla^dY_t=\theta(B)e_t.
\]

其中

\[
\nabla=1-B
\]

是差分算子，d 是差分阶数。如果原序列 $Y_t$ 非平稳，但经过 d 次差分以后变成平稳 ARMA(p,q)，就可以使用 ARIMA(p,d,q) 建模。

因此 ARIMA 的模型选择不仅要选 p 和 q，还要先决定 d。ACF、PACF、EACF 主要用于平稳序列或差分后的平稳序列；如果 d 没有选对，后面的 p、q 识别会受到影响。

### Def 16.2 Difference Operator

差分算子定义为

\[
\nabla Y_t=Y_t-Y_{t-1}.
\]

因为 backshift operator 满足

\[
BY_t=Y_{t-1},
\]

所以

\[
\nabla Y_t=(1-B)Y_t.
\]

高阶差分定义为递推：

\[
\nabla^dY_t=\nabla(\nabla^{d-1}Y_t).
\]

例如二阶差分为

\[
\nabla^2Y_t
= \nabla(Y_t-Y_{t-1})
= Y_t-2Y_{t-1}+Y_{t-2}.
\]

若

\[
\nabla^dY_t
\]

是平稳 ARMA(p,q)，则称

\[
Y_t
\]

是 ARIMA(p,d,q)。

### Ex 16.3 最简单的 unit root 问题：AR(1)

考虑

\[
Y_t=\alpha Y_{t-1}+e_t,
\]

其中 $e_t$ 是 white noise。若

\[
|\alpha|<1,
\]

则这是平稳 AR(1)。若

\[
\alpha=1,
\]

则

\[
Y_t=Y_{t-1}+e_t,
\]

是 random walk，非平稳。

因此可以把是否需要差分的问题转化为检验

\[
H_0:\alpha=1
\]

对比

\[
H_1:|\alpha|<1.
\]

令

\[
\beta=\alpha-1.
\]

则

\[
\nabla Y_t=Y_t-Y_{t-1}
= (\alpha-1)Y_{t-1}+e_t
= beta Y_{t-1}+e_t.
\]

于是 unit root 检验可以写成

\[
H_0:\beta=0
\]

对比

\[
H_1:\beta<0.
\]

### Def 16.4 Dickey-Fuller Test

Dickey-Fuller test 的基本回归形式是

\[
\nabla Y_t=\beta Y_{t-1}+e_t.
\]

其中

\[
H_0:\beta=0
\]

表示存在 unit root，序列是 random walk 型非平稳过程；而

\[
H_1:\beta<0
\]

表示序列是平稳 AR(1) 型过程。

OLS 估计量为

\[
\hat\beta= \frac{\sum_{t}Y_{t-1}\nabla Y_t}
{\sum_{t}Y_{t-1}^2}.
\]

形式上可以写出 t 统计量：

\[
\tau= \frac{\hat\beta}{SE(\hat\beta)}.
\]

但板书特别提醒：这里的 t 统计量在原假设下 **不是普通 t 分布**。因为在

\[
H_0:\beta=0
\]

下，$Y_t$ 是 random walk，回归变量 $Y_{t-1}$ 本身非平稳，经典线性回归 t 检验的渐近分布不再适用。因此需要使用 Dickey-Fuller / Fuller distribution 的临界值。

### Def 16.5 Augmented Dickey-Fuller Test

如果误差项不是 white noise，而是存在自相关，就需要使用 Augmented Dickey-Fuller test。板书写成

\[
Y_t=\alpha Y_{t-1}+X_t,
\qquad
X_t\sim AR(p).
\]

令

\[
\beta=\alpha-1.
\]

则

\[
\nabla Y_t=\beta Y_{t-1}+X_t.
\]

若

\[
\phi(B)X_t=e_t,
\]

则可以把 $X_t$ 的 AR 结构展开到差分回归中，得到 ADF 回归：

\[
\nabla Y_t
= \beta Y_{t-1}
+
\delta_1\nabla Y_{t-1}
+\cdots+
\delta_p\nabla Y_{t-p}
+
e_t.
\]

【根据前后文补充】扫描件中写到

\[
\beta=(1-\phi_1-\cdots-\phi_p)(\alpha-1),
\]

这表达的是：在带 AR 误差结构时，单位根对应的核心仍然是 $\alpha=1$，但回归中 $\beta$ 的系数会受误差 AR 多项式影响。实际 ADF 检验仍然检验

\[
H_0:\beta=0
\]

对比

\[
H_1:\beta<0.
\]

### Rmk 16.6 ADF 检验的作用

ADF 检验的目的不是直接选择 p 和 q，而是判断是否需要差分，也就是判断 d。若原序列无法拒绝 unit root 原假设，可以考虑对序列做一次差分：

\[
\nabla Y_t.
\]

然后再检验差分后的序列是否平稳。若一次差分后平稳，就考虑

\[
d=1.
\]

若仍不平稳，可能继续考虑二阶差分：

\[
\nabla^2Y_t.
\]

但过度差分会引入不必要的 MA 结构，因此 d 不能盲目取大。

### Rmk 16.7 本讲末尾提到的完整检查流程

板书末尾把若干工具放在一起：ACF、PACF、EACF，以及 unit root / differencing。可以整理成如下流程。先判断原序列是否明显非平稳，包括均值趋势、方差变化、ACF 是否缓慢衰减。若怀疑 unit root，则使用 DF 或 ADF 检验。决定 d 以后，对

\[
\nabla^dY_t
\]

继续使用 ACF、PACF、EACF 选择 p 和 q。

【原笔记留白/中断】扫描件最后一页底部出现 “Box-Cox” 和后续下节内容提示，但没有展开推导。Box-Cox 变换主要用于处理方差随均值变化的问题，Lecture 10 中已经出现过类似内容。本讲这里主要是提醒：非平稳不只有均值非平稳，也可能有方差不稳定；差分主要处理 unit root 或趋势型均值非平稳，方差不稳定常需要变换。

## Part B. 复习视角

Lecture 16 的核心问题是：**ARIMA 里的 d 怎么选**。前面的 ACF、PACF、EACF 都假设我们已经在处理平稳序列，或者至少是在处理差分后的平稳序列。如果原序列本身是 random walk，那么直接看 ACF/PACF 选 p、q 很容易误判。因此在 ARIMA 建模中，d 的选择通常要放在 p、q 之前。

这一讲最重要的模型是最简单的 AR(1)：

\[
Y_t=\alpha Y_{t-1}+e_t.
\]

当 $|\alpha|<1$ 时，序列平稳；当 $\alpha=1$ 时，序列变成 random walk。把它改写成

\[
\nabla Y_t=\beta Y_{t-1}+e_t
\]

以后，unit root 检验就变成检验 $\beta=0$。这里最容易误解的地方是：虽然形式上像普通回归，但在原假设下 $Y_{t-1}$ 是非平稳变量，所以 t 统计量不服从普通 t 分布。Def 16.4 里的 Dickey-Fuller test 正是为这个问题设计的。

ADF 是 DF 的扩展。它在回归中加入若干滞后差分项：

\[
\nabla Y_t
= \beta Y_{t-1}
+
\delta_1\nabla Y_{t-1}
+\cdots+
\delta_p\nabla Y_{t-p}
+
e_t.
\]

这样做的目的是吸收残差自相关，使得最后的 $e_t$ 更接近 white noise。复习时要抓住一点：**DF/ADF 不是用来选 ARMA 的 p、q，而是用来判断是否需要差分，也就是选择 d 的重要依据**。

最终建模流程可以理解为三层。先用图像、ADF 和必要的变换处理非平稳，决定 d；再对差分后的序列用 ACF、PACF、EACF 形成 p、q 的候选；最后用 AIC/BIC、残差诊断和预测表现进一步确认模型。这样 Lecture 13–16 的逻辑就闭合了：Lecture 13 解决 AR 与 MA 的单独识别，Lecture 15 解决 ARMA 的联合识别，Lecture 16 解决 ARIMA 中差分阶数 d 的识别。





# Lecture 17: Chapter 7 Estimation I — Moment Estimation and Least Squares

## Part A. 课堂内容还原

### Rmk 17.1 From Model Specification to Parameter Estimation

前面几讲主要围绕模型识别和模型选择。对 MA(q)，核心工具是 ACF；对 AR(p)，核心工具是 PACF；对 ARMA(p,q)，进一步引入 EACF；此外还出现了 AIC 与 BIC 作为信息准则。进入 Chapter 7 以后，问题从“如何选模型阶数”转向“模型阶数给定以后，如何估计参数”。

本讲板书把 estimation 方法分为三类：**moment estimation**、**ordinary least squares** 和 **maximum likelihood estimation**。Lecture 17 主要讲前两类，MLE 在后面继续展开。

### Ex 17.2 Method of Moments for MA(1)

考虑 MA(1) 模型

\[
Y_t=e_t-\theta e_{t-1},
\qquad e_t\sim WN(0,\sigma^2).
\]

由 white noise 的性质可得

\[
E(Y_t)=0.
\]

理论自相关函数满足

\[
\rho_1=\frac{\gamma_1}{\gamma_0}
      =\frac{-\theta\sigma^2}{(1+\theta^2)\sigma^2}
      =-\frac{\theta}{1+\theta^2},
\]

并且

\[
\rho_k=0,\qquad k\ge 2.
\]

moment estimation 的思想是把 sample moments 与 population moments 对齐。因为 sample ACF 满足

\[
r_k \xrightarrow{p} \rho_k,
\]

所以用 $r_1$ 代替 $\rho_1$，得到

\[
r_1=-\frac{\theta}{1+\theta^2}.
\]

整理可得二次方程

\[
r_1\theta^2+\theta+r_1=0.
\]

因此

\[
\theta
= \frac{-1\pm\sqrt{1-4r_1^2}}{2r_1}.
\]

由于 MA(1) 的 invertibility 通常要求

\[
|\theta|<1,
\]

所以应选择落在单位圆内的根。板书中取

\[
\hat\theta_M
= \frac{-1+\sqrt{1-4r_1^2}}{2r_1}.
\]

这里的下标 $M$ 表示 moment estimator。

### Rmk 17.3 Why MoM for MA Models Can Be Unstable

MA(1) 的 MoM 估计已经暴露出一个问题：由 $r_1$ 反解 $\theta$ 时需要开根号

\[
\sqrt{1-4r_1^2}.
\]

理论上可逆 MA(1) 的 $\rho_1$ 满足 $|\rho_1|\le 1/2$，但有限样本中的 $r_1$ 可能因为抽样误差而出现 $|r_1|>1/2$，此时反解公式直接失效。即使 $|r_1|<1/2$，靠近边界时估计也可能非常不稳定。

**【根据前后文补充】** 这解释了为什么板书在 MA(2) 处写“反解也会有问题”。MA(q) 的 moment equations 通常是非线性的，多个参数之间互相纠缠，反解可能有多个根，也可能出现不满足 invertibility 的根。因此 MoM 对 MA(q) 与 ARMA(p,q) 往往不是最稳健的主方法。

### Prop 17.4 Asymptotic Properties of the MA(1) Moment Estimator

若 $|\theta|<1$，则 $\rho_1=-\theta/(1+\theta^2)$ 位于可逆区域内部。由于

\[
r_1 \xrightarrow{p} \rho_1,
\]

并且

\[
\theta=f(\rho_1)
\]

在内部点连续，由 continuous mapping theorem 可得

\[
\hat\theta_M \xrightarrow{p} \theta.
\]

这就是 MA(1) moment estimator 的 consistency。

若进一步已知

\[
\sqrt n(r_1-\rho_1)\xrightarrow{d}N(0,c_1),
\]

其中板书给出

\[
c_1=1-3\rho_1^2+4\rho_1^4,
\]

则由 delta method，

\[
\sqrt n(\hat\theta_M-\theta)
\xrightarrow{d}
N\left(0,\left[f'(\rho_1)\right]^2c_1\right).
\]

**【原笔记中断】** 板书在这里写了 “why?”，说明 $c_1=1-3\rho_1^2+4\rho_1^4$ 的来源没有在笔记中完整推导。这个常数来自 sample ACF 的渐近方差公式，若后续复习要严格证明，需要回看 sample ACF asymptotic normality 的对应部分。

### Ex 17.5 Moment Estimation for MA(2)

考虑

\[
Y_t=e_t-\theta_1e_{t-1}-\theta_2e_{t-2}.
\]

理论自协方差为

\[
\gamma_0=(1+\theta_1^2+\theta_2^2)\sigma^2,
\]

\[
\gamma_1=(-\theta_1+\theta_1\theta_2)\sigma^2,
\]

\[
\gamma_2=-\theta_2\sigma^2,
\]

并且 $\gamma_k=0$ for $k>2$。所以

\[
\rho_1=\frac{-\theta_1+\theta_1\theta_2}{1+\theta_1^2+\theta_2^2},
\qquad
\rho_2=\frac{-\theta_2}{1+\theta_1^2+\theta_2^2}.
\]

MoM 会用 $r_1,r_2$ 替代 $\rho_1,\rho_2$，再反解 $\theta_1,\theta_2$。

**【原笔记中断】** 板书只写出 MA(2) 的 $\rho_1,\rho_2$ 形式，并标注“反解也会有问题”，没有继续给出完整反解。这里不建议强行补完整代数反解，因为 MA(2) 的根选择、invertibility 约束和多解问题会使公式很不适合手算复习。复习重点应放在“MoM 对 MA/ARMA 不稳定”这一方法论结论上。

### Ex 17.6 Moment Estimation for AR(1)

考虑平稳 AR(1)

\[
Y_t=\phi Y_{t-1}+e_t,
\qquad |\phi|<1.
\]

它的自相关函数为

\[
\rho_k=\phi^k,\qquad k\ge 1.
\]

取 $k=1$，得到

\[
\rho_1=\phi.
\]

因此 moment estimator 很自然地写成

\[
\hat\phi_M=r_1.
\]

由于 $r_1\xrightarrow{p}\rho_1$，所以

\[
\hat\phi_M\xrightarrow{p}\phi.
\]

进一步若

\[
\sqrt n(r_1-\rho_1)\xrightarrow{d}N(0,c_1),
\]

且对 AR(1) 有

\[
c_1=1-\phi^2,
\]

则

\[
\sqrt n(\hat\phi_M-\phi)
\xrightarrow{d}
N(0,1-\phi^2).
\]

### Rmk 17.7 Why High-lag Moment Estimation for AR(1) Is Bad

由于 AR(1) 满足

\[
\rho_k=\phi^k,
\]

也可以用

\[
\hat\phi_{M,k}=r_k^{1/k}
\]

估计 $\phi$。但板书指出，当 $k$ 很大时这个估计不好。

原因是函数

\[
f(x)=x^{1/k}
\]

的导数为

\[
f'(x)=\frac{1}{k}x^{1/k-1}.
\]

在 $x=\rho_k=\phi^k$ 处，

\[
f'(\rho_k)
= \frac{1}{k}(\phi^k)^{1/k-1}
= \frac{1}{k}\phi^{1-k}.
\]

若 $|\phi|<1$，则 $\phi^{1-k}$ 会随 $k$ 增大而迅速放大。因此高阶 sample ACF 的误差经过 $k$ 次根号反变换后会被放大。这就是板书中“故 $k$ 大时不好，用低阶矩进行估计”的含义。

### Prop 17.8 Yule–Walker Moment Estimation for AR(p)

考虑 AR(p)

\[
Y_t=\phi_1Y_{t-1}+\cdots+\phi_pY_{t-p}+e_t.
\]

Yule–Walker equations 为

\[
\rho_k
= \phi_1\rho_{k-1}
+\phi_2\rho_{k-2}
+\cdots
+\phi_p\rho_{k-p},
\qquad k\ge 1.
\]

取 $k=1,\ldots,p$，可写成矩阵形式

\[
\begin{pmatrix}
\rho_1\\
\rho_2\\
\vdots\\
\rho_p
\end{pmatrix}
= \begin{pmatrix}
1 & \rho_1 & \cdots & \rho_{p-1}\\
\rho_1 & 1 & \cdots & \rho_{p-2}\\
\vdots & \vdots & \ddots & \vdots\\
\rho_{p-1} & \rho_{p-2} & \cdots & 1
\end{pmatrix}
\begin{pmatrix}
\phi_1\\
\phi_2\\
\vdots\\
\phi_p
\end{pmatrix}.
\]

令

\[
\mathbf r_p=(r_1,\ldots,r_p)^T,
\]

并用 sample autocorrelations 代替 population autocorrelations，就得到 Yule–Walker moment estimator

\[
\hat{\boldsymbol\phi}_{YW}
= \hat R_p^{-1}\mathbf r_p.
\]

由于 $r_k\xrightarrow{p}\rho_k$，所以在矩阵可逆且模型平稳的条件下，

\[
\hat\phi_j\xrightarrow{p}\phi_j,\qquad j=1,\ldots,p.
\]

### Ex 17.9 Moment Equations for ARMA(1,1)

考虑

\[
Y_t=\phi Y_{t-1}+e_t-\theta e_{t-1}.
\]

板书给出关于自协方差的方程组

\[
\hat\gamma_1=\phi\hat\gamma_0-\theta\hat\sigma^2,
\]

\[
\hat\gamma_0=\phi^2\hat\gamma_0+\hat\sigma^2+\theta^2\hat\sigma^2-2\phi\theta\hat\sigma^2,
\]

\[
\hat\gamma_2=\phi\hat\gamma_1.
\]

由第三个式子可以得到

\[
\hat\phi=\frac{\hat\gamma_2}{\hat\gamma_1}.
\]

**【原笔记中断】** 这里板书写了 “$\theta$ 不合适” 和 “reason”，但没有完整推导 $\theta$ 的解为何不稳定。根据前后文，老师想强调的是：ARMA 模型中 AR 部分可以通过高阶自协方差递推估计，但 MA 参数仍会进入非线性方程，MoM 估计容易不稳定。因此 ARMA(p,q) 一般不把 MoM 当作首选方法，而转向 OLS/CSS/MLE。

### Def 17.10 Ordinary Least Squares

在线性回归

\[
Y_i=\beta_0+\beta_1X_i+\varepsilon_i
\]

中，OLS 通过最小化 residual sum of squares

\[
S(\beta)=\sum_i (Y_i-\beta_0-\beta_1X_i)^2
\]

得到

\[
\hat\beta=\arg\min_\beta S(\beta).
\]

在时间序列模型中，也可以把模型改写成“观测值等于预测部分加误差”的形式，然后最小化误差平方和。

### Def 17.11 Conditional Sum of Squares for MA(1)

对 MA(1)

\[
Y_t=e_t-\theta e_{t-1},
\]

可递推写成

\[
e_t=Y_t+\theta e_{t-1}.
\]

若给定初值

\[
e_0=0,
\]

则

\[
e_1=Y_1,
\]

\[
e_2=Y_2+\theta Y_1,
\]

一般地，

\[
e_t=Y_t+\theta Y_{t-1}+\theta^2Y_{t-2}+\cdots+\theta^{t-1}Y_1.
\]

conditional sum of squares 定义为

\[
S(\theta)=\sum_{t=1}^n e_t(\theta)^2.
\]

于是 conditional least squares estimator 为

\[
\hat\theta_{CLS}=\arg\min_\theta S(\theta).
\]

### Rmk 17.12 Numerical Optimization for MA Models

对于 MA(1)，由于

\[
e_t=(1-\theta B)^{-1}Y_t
=\sum_{j=0}^{\infty}\theta^jB^jY_t,
\]

$S(\theta)$ 通常不是一个简单的二次函数，所以一阶条件

\[
\frac{\partial S(\theta)}{\partial\theta}=0
\]

不一定能解析求解。板书因此转向数值方法，例如 Newton method。

**【根据前后文补充】** Newton method 的基本迭代为

\[
\theta^{(m+1)}
= \theta^{(m)} - \frac{f(\theta^{(m)})}{f'(\theta^{(m)})},
\]

其中

\[
f(\theta)=\frac{\partial S(\theta)}{\partial\theta}.
\]

这个补充与板书中的切线示意图一致。这里不要求手算完整迭代，重点是知道 MA/ARMA 的 least squares 通常需要数值优化。

### Ex 17.13 OLS for AR(1)

考虑 AR(1)

\[
Y_t=\phi Y_{t-1}+e_t.
\]

令

\[
S(\phi)=\sum_{t=2}^n (Y_t-\phi Y_{t-1})^2.
\]

对 $\phi$ 求导，

\[
\frac{\partial S(\phi)}{\partial \phi}
= -2\sum_{t=2}^n Y_{t-1}(Y_t-\phi Y_{t-1}).
\]

令导数为零，得到

\[
\sum_{t=2}^nY_tY_{t-1}
= \phi\sum_{t=2}^nY_{t-1}^2.
\]

所以

\[
\hat\phi_{OLS}
= \frac{\sum_{t=2}^nY_tY_{t-1}}
{\sum_{t=2}^nY_{t-1}^2}.
\]

板书进一步写出它与 sample autocovariance ratio 的关系：

\[
\hat\phi_{OLS}
= \frac{\hat\gamma_1}{\hat\gamma_0}+o_p(1)
= r_1+o_p(1).
\]

因此对于 AR(1)，OLS estimator 与 Yule–Walker/moment estimator 渐近等价。

### Prop 17.14 OLS for AR(p)

对 AR(p)

\[
Y_t=\phi_1Y_{t-1}+\phi_2Y_{t-2}+\cdots+\phi_pY_{t-p}+e_t,
\]

定义

\[
S(\boldsymbol\phi)
= \sum_{t=p+1}^n
\left(Y_t-\phi_1Y_{t-1}-\cdots-\phi_pY_{t-p}\right)^2.
\]

一阶条件为

\[
\frac{\partial S(\boldsymbol\phi)}{\partial \boldsymbol\phi}=0.
\]

写成矩阵形式，如果

\[
\mathbf x_t=(Y_{t-1},\ldots,Y_{t-p})^T,
\]

则

\[
\hat{\boldsymbol\phi}_{OLS} = \left(
    \sum_{t=p+1}^n\mathbf x_t\mathbf x_t^T\right)^{-1} \left(\sum_{t=p+1}^n\mathbf x_tY_t
    \right).
\]

**【原笔记中断】** Lecture 17 后半部分黑板照片中继续推导了 AR(p) 的 OLS 渐近性质，但可辨识信息不足。根据 Lecture 18 和 Lecture 19 的衔接，老师后面会把 AR(p) 的 OLS 与 conditional MLE、moment estimator 联系起来，因此这里暂时保留核心公式，不强行补完整渐近证明。

## Part B. 复习视角

Lecture 17 的主线是从 **model specification** 进入 **parameter estimation**。在模型选择阶段，我们关心 ACF、PACF、EACF、AIC 和 BIC；进入估计阶段后，我们假设模型阶数大致已经定下，开始估计 $\phi,\theta,\sigma^2$ 这些参数。

这一讲最重要的对比是 **MA/ARMA 的 MoM 不如 AR 的 MoM 稳定**。MA(1) 已经需要从 $r_1=-\theta/(1+\theta^2)$ 反解 $\theta$，会出现根选择和 invertibility 问题；MA(2) 与 ARMA(1,1) 更复杂。相比之下，AR(1) 有 $\rho_1=\phi$，AR(p) 有 Yule–Walker equations，因此 AR 模型的 moment estimation 结构非常自然。

第二条主线是 **least squares 的可计算性**。AR(1) 和 AR(p) 的 OLS 是标准二次最小化问题，能写出闭式解；MA(q) 与 ARMA(p,q) 的误差项要递推生成，所以 objective function 通常需要数值优化。这是 Lecture 18 继续讲 conditional likelihood 和 MLE 的铺垫。

---

# Lecture 18: Chapter 7 Estimation II — Conditional MLE and Markov Factorization

## Part A. 课堂内容还原

### Rmk 18.1 Review of Estimation Methods

Lecture 18 开头复习了三类估计方法。对 MA(1)，MoM 可以写出来，但并不好；对 AR(p)，Yule–Walker equations 给出自然的 moment estimator；对 ARMA(p,q)，当 $k>q$ 时有递推关系

\[
\rho_k=\phi_1\rho_{k-1}+\cdots+\phi_p\rho_{k-p},
\]

这可以帮助估计 AR 参数，但 MA 参数仍不容易由 moments 稳定估计。因此板书总结为：AR(p) 的 MoM 较自然，而 MA/ARMA 的 MoM 不好。

对 AR(p)，OLS objective 为

\[
L(\boldsymbol\phi)
= \sum_{t=p+1}^n
\left(Y_t-\phi_1Y_{t-1}-\cdots-\phi_pY_{t-p}\right)^2.
\]

一阶条件对应 Yule–Walker 型方程，所以板书写出

\[
OLS \Longleftrightarrow Moment\ estimation
\]

这一关系。这里的“等价”更准确地说是 **在 AR 模型中，OLS 正规方程和 sample moment/Yule–Walker 方程具有同类结构，并且渐近上给出相同目标参数**。

### Def 18.2 Likelihood and Log-likelihood

设

\[
X_1,\ldots,X_n\stackrel{iid}{\sim}f_\theta(x),
\qquad \theta\in\Theta.
\]

likelihood function 定义为

\[
L(\theta)=f_\theta(X_1,\ldots,X_n).
\]

在 iid 情形下，

\[
L(\theta)=\prod_{i=1}^n f_\theta(X_i).
\]

log-likelihood 为

\[
\ell(\theta)=\log L(\theta).
\]

MLE 定义为

\[
\hat\theta_{MLE}
= \arg\max_{\theta\in\Theta} L(\theta)
= \arg\max_{\theta\in\Theta}\ell(\theta).
\]

### Ex 18.3 Exact Likelihood for Gaussian MA(1)

考虑 Gaussian MA(1)

\[
Y_t=e_t-\theta e_{t-1},
\qquad e_t\sim N(0,\sigma^2).
\]

令

\[
\mathbf Y=(Y_1,\ldots,Y_n)^T.
\]

由于 $\mathbf Y$ 是 Gaussian white noise 的线性组合，$\mathbf Y$ 服从多元正态分布

\[
\mathbf Y\sim N(0,\Sigma_Y).
\]

其中协方差矩阵为 Toeplitz 型：

\[
\operatorname{Var}(Y_t)=(1+\theta^2)\sigma^2,
\]

\[
\operatorname{Cov}(Y_t,Y_{t-1})=-\theta\sigma^2,
\]

\[
\operatorname{Cov}(Y_t,Y_s)=0,\qquad |t-s|\ge 2.
\]

因此

\[
\Sigma_Y
= \sigma^2
\begin{pmatrix}
1+\theta^2 & -\theta & 0 & \cdots & 0\\
-\theta & 1+\theta^2 & -\theta & \cdots & 0\\
0 & -\theta & 1+\theta^2 & \cdots & 0\\
\vdots & \vdots & \vdots & \ddots & -\theta\\
0 & 0 & 0 & -\theta & 1+\theta^2
\end{pmatrix}.
\]

Gaussian likelihood 为

\[
L(\theta,\sigma^2)
= (2\pi)^{-n/2}|\Sigma_Y|^{-1/2}
\exp\left\{-\frac12\mathbf Y^T\Sigma_Y^{-1}\mathbf Y\right\}.
\]

MLE 是

\[
(\hat\theta,\hat\sigma^2)
= \arg\max_{\theta,\sigma^2}L(\theta,\sigma^2).
\]

### Rmk 18.4 Why Exact MLE Is Hard for MA Models

板书在 exact likelihood 旁边写了“很难算”和“why? log 处理？”。困难主要来自两个地方。第一，$\Sigma_Y$ 依赖 $\theta$，所以 $|\Sigma_Y|$ 和 $\Sigma_Y^{-1}$ 都是参数的复杂函数。第二，MA(q) 与 ARMA(p,q) 的协方差矩阵虽然有结构，但直接最大化 exact likelihood 仍然不方便。

**【根据前后文补充】** 这就是后面转向 **conditional likelihood** 的原因。条件化以后，不再直接处理 $\mathbf Y$ 的整体协方差矩阵，而是通过递推残差 $e_t(\theta)$ 把 likelihood 写成 residual squares 的形式。

### Def 18.5 Conditional MLE for MA(q)

考虑 MA(q)

\[
Y_t=e_t-\theta_1e_{t-1}-\theta_2e_{t-2}-\cdots-\theta_qe_{t-q}.
\]

反过来有递推式

\[
e_t=Y_t+\theta_1e_{t-1}+\theta_2e_{t-2}+\cdots+\theta_qe_{t-q}.
\]

conditional likelihood 的做法是设定初值

\[
e_0=e_{-1}=\cdots=e_{-q}=0.
\]

这样给定 $\theta$ 后，每个 $e_t(\theta)$ 都可以由观测 $Y_1,\ldots,Y_t$ 递推得到。

若 $e_t\sim N(0,\sigma^2)$，conditional likelihood 写成

\[
L_c(\theta,\sigma^2)
= \prod_{t=1}^n
\frac{1}{\sqrt{2\pi}\sigma}
\exp\left\{-\frac{e_t(\theta)^2}{2\sigma^2}\right\}.
\]

因此最大化 conditional likelihood 等价于最小化

\[
S(\theta)=\sum_{t=1}^n e_t(\theta)^2
\]

当 $\sigma^2$ 已知或被 profile out 时。这就是板书中写的

\[
MLE \Longleftrightarrow OLS
\]

在 MA(q) conditional setting 下的含义。

### Lem 18.6 Jacobian in the MA(q) Transformation

由

\[
Y_t=e_t-\theta_1e_{t-1}-\cdots-\theta_qe_{t-q}
\]

并设 $e_0,\ldots,e_{-q}=0$，可得

\[
\frac{\partial Y_t}{\partial e_j}
= \begin{cases}
1, & j=t,\\
0, & j>t,\\
-\theta_{t-j}, & 1\le t-j\le q,\\
0, & t-j>q.
\end{cases}
\]

因此 Jacobian matrix 是下三角矩阵，主对角线全为 1，所以

\[
|J|=1.
\]

这解释了为什么从 $\mathbf e$ 到 $\mathbf Y$ 的变量变换不会带来额外复杂 Jacobian factor。

### Ex 18.7 Conditional Likelihood for AR(1)

考虑 AR(1)

\[
Y_t=\phi Y_{t-1}+e_t.
\]

条件化在 $Y_1$ 上，对 $t=2,\ldots,n$，

\[
e_t=Y_t-\phi Y_{t-1}.
\]

因此

\[
f(Y_2,\ldots,Y_n\mid Y_1)
= |J|f(e_2,\ldots,e_n).
\]

这里从 $(e_2,\ldots,e_n)$ 到 $(Y_2,\ldots,Y_n)$ 的 Jacobian 也是下三角且对角线为 1，因此

\[
|J|=1.
\]

若 $e_t\sim N(0,\sigma^2)$，则 conditional log-likelihood 等价于最小化

\[
\sum_{t=2}^n(Y_t-\phi Y_{t-1})^2.
\]

所以 AR(1) 的 conditional MLE 与 OLS 相同。

### Prop 18.8 Markov Property of AR(1)

AR(1) 具有 Markov property，即

\[
f(y_n\mid y_1,\ldots,y_{n-1})
= f(y_n\mid y_{n-1}).
\]

因此 joint density 可分解为

\[
f(y_1,\ldots,y_n)
= f(y_1)f(y_2\mid y_1)f(y_3\mid y_2)\cdots f(y_n\mid y_{n-1}).
\]

在 Gaussian AR(1) 下，

\[
Y_t\mid Y_{t-1}
\sim
N(\phi Y_{t-1},\sigma^2).
\]

这个性质使得 AR 模型的 likelihood 比 MA 模型更直接。AR(p) 也有类似的 p 阶 Markov property。

### Def 18.9 Conditional Likelihood for ARMA(p,q)

考虑 ARMA(p,q)

\[
Y_t=\phi_1Y_{t-1}+\cdots+\phi_pY_{t-p}
+e_t-\theta_1e_{t-1}-\cdots-\theta_qe_{t-q}.
\]

conditional likelihood 的标准处理是条件化在初始观测

\[
Y_1,\ldots,Y_p
\]

上，并设

\[
e_t=0,\qquad t\le 0.
\]

于是对 $t=p+1,\ldots,n$，残差 $e_t$ 可以递推表示为参数和观测的函数。conditional likelihood 为

\[
L_c(\phi,\theta,\sigma^2)
= \prod_{t=p+1}^n
\frac{1}{\sqrt{2\pi}\sigma}
\exp\left\{-\frac{e_t(\phi,\theta)^2}{2\sigma^2}\right\}.
\]

因此估计 $\phi,\theta$ 等价于最小化 conditional residual sum of squares

\[
S(\phi,\theta)=\sum_{t=p+1}^n e_t(\phi,\theta)^2.
\]

**【原笔记中断】** Lecture 18 最后一页黑板照片进入一般 MLE consistency 和 regularity conditions，但笔记只记录了部分关键词，如 consistency、CLT、$\hat\theta=\arg\max L(\theta)$、regularity conditions。完整内容在 Lecture 19 继续展开，因此这里不强行补写完整 theorem，只保留承上启下信息。

## Part B. 复习视角

Lecture 18 的主线是：**exact likelihood 太难，所以引入 conditional likelihood**。对 Gaussian MA(1)，精确 likelihood 需要处理 $\Sigma_Y^{-1}$ 和 $|\Sigma_Y|$，这在手算和推导上都很不友好。conditional likelihood 通过设初始 residual 为 0，把问题改写成递推 residual 的平方和最小化。

这一讲要抓住两个技术点。第一，**Jacobian 为什么等于 1**。无论 MA(q) 还是 AR(1)，从 innovations 到 observations 的变换矩阵都是三角矩阵，主对角线是 1，所以变量变换不改变密度的体积因子。第二，**AR 模型为什么更自然**。AR(1) 具有 Markov property，给定上一期，当前期只依赖上一期和新噪声，因此 conditional likelihood 直接变成 OLS。

这一讲的空白和中断明显集中在 exact MLE 到 conditional MLE 的转换，以及一般 MLE regularity conditions 的开头。这不是孤立缺口，它正好连接 Lecture 19 的 MLE consistency 和 asymptotic normality。复习时要把 Lecture 18 和 Lecture 19 连成一块看。

---

# Lecture 19: MLE Consistency and Asymptotic Normality

## Part A. 课堂内容还原

### Def 19.1 Conditional Likelihood for Gaussian ARMA

若

\[
Y_t\sim ARMA(p,q),
\qquad e_t\sim N(0,\sigma^2),
\]

conditional likelihood function 可写为

\[
L(\theta)
= \prod_{t=p+1}^n
\frac{1}{\sqrt{2\pi}\sigma}
\exp\left\{-\frac{e_t(\theta)^2}{2\sigma^2}\right\},
\]

其中 $e_t(\theta)$ 由 ARMA 递推关系决定。

MLE 定义为

\[
\hat\theta_{MLE}
= \arg\max_{\theta}L(\theta).
\]

### Thm 19.2 Consistency of MLE: Heuristic Argument

设

\[
X_1,\ldots,X_n\stackrel{iid}{\sim}f_{\theta_0}(x),
\]

其中 $\theta_0$ 是真实参数。likelihood 为

\[
L(\theta)=\prod_{i=1}^n f_\theta(X_i),
\]

log-likelihood 为

\[
\ell_n(\theta)=\sum_{i=1}^n\log f_\theta(X_i).
\]

对任意固定 $\theta$，

\[
\frac{1}{n}\ell_n(\theta)
= \frac{1}{n}\sum_{i=1}^n \log f_\theta(X_i)
\xrightarrow{a.s.}
E_{\theta_0}\log f_\theta(X).
\]

若模型可识别，并且 $\theta_0$ 是唯一最大化

\[
E_{\theta_0}\log f_\theta(X)
\]

的参数，则 sample log-likelihood 的最大点应收敛到 $\theta_0$，即

\[
\hat\theta_{MLE}\xrightarrow{a.s.}\theta_0.
\]

### Rmk 19.3 Why the Population Criterion Is Maximized at the True Parameter

关键不等式来自 Kullback–Leibler divergence。注意

\[
E_{\theta_0}\log f_{\theta_0}(X)-E_{\theta_0}\log f_\theta(X)
= E_{\theta_0}\log\frac{f_{\theta_0}(X)}{f_\theta(X)}
\ge 0.
\]

等号成立当且仅当

\[
f_\theta=f_{\theta_0}
\]

几乎处处成立。若模型 identifiable，则推出

\[
\theta=\theta_0.
\]

所以真实参数 $\theta_0$ 是 population log-likelihood 的唯一最大点。

**【根据前后文补充】** 板书中写了 continuity、dominated condition、unique maximum 等条件。完整严格证明需要 uniform law of large numbers，而板书主要给出直观证明路线：pointwise LLN 给出极限 criterion，regularity conditions 保证 argmax 收敛。

### Rmk 19.4 Regularity Conditions Mentioned in Class

板书中列出了一般 MLE consistency 所需的 regularity conditions，大意包括：参数空间中 $\theta_0$ 是内点；support 不依赖于 $\theta$；log density 对参数足够光滑；存在可积 envelope function 控制导数；population criterion 有唯一最大值。

**【原笔记中断】** 这部分在 Lecture 18 末尾和 Lecture 19 开头分散出现，笔记未完整抄下所有条件。这里不强行整理成严格 theorem，因为不同教材的 regularity conditions 形式略有差异。复习时应掌握它们的作用：让 sample log-likelihood 能稳定逼近 population criterion，并允许后面做 Taylor expansion。

### Ex 19.5 Conditional MLE for AR(p)

考虑 AR(p)

\[
Y_t=\phi_1Y_{t-1}+\cdots+\phi_pY_{t-p}+e_t,
\qquad e_t\sim N(0,\sigma^2).
\]

令

\[
\boldsymbol\phi=(\phi_1,\ldots,\phi_p)^T.
\]

conditional likelihood 为

\[
L(\boldsymbol\phi)
= \prod_{t=p+1}^n
\frac{1}{\sqrt{2\pi}\sigma}
\exp\left\{
-\frac{e_t(\boldsymbol\phi)^2}{2\sigma^2}
\right\},
\]

其中

\[
e_t(\boldsymbol\phi)
= Y_t-\phi_1Y_{t-1}-\cdots-\phi_pY_{t-p}.
\]

log-likelihood 为

\[
\ell_n(\boldsymbol\phi)
= \sum_{t=p+1}^n
\left[
\log\left(\frac{1}{\sqrt{2\pi}\sigma}\right)
-\frac{e_t(\boldsymbol\phi)^2}{2\sigma^2}
\right].
\]

如果 $\sigma^2$ 已知，最大化 $\ell_n(\boldsymbol\phi)$ 等价于最小化

\[
\sum_{t=p+1}^n
\left(Y_t-\phi_1Y_{t-1}-\cdots-\phi_pY_{t-p}\right)^2.
\]

因此 Gaussian AR(p) 的 conditional MLE 与 OLS 相同。

### Thm 19.6 Asymptotic Normality of MLE

在适当 regularity conditions 下，

\[
\sqrt n(\hat\theta-\theta_0)
\xrightarrow{d}
N\left(0,I(\theta_0)^{-1}\right),
\]

其中 $I(\theta_0)$ 是 Fisher information。

证明思路来自 score equation 与 Taylor expansion。因为 MLE 满足

\[
\frac{\partial \ell_n(\hat\theta)}{\partial\theta}=0,
\]

对 $\theta_0$ 附近展开：

\[
0
= \frac{\partial \ell_n(\theta_0)}{\partial\theta}
+
\frac{\partial^2 \ell_n(\theta_0)}{\partial\theta\partial\theta^T}
(\hat\theta-\theta_0)
+
R_n.
\]

两边除以 $n$ 并整理，得到

\[
\sqrt n(\hat\theta-\theta_0)
= -
\left[
\frac{1}{n}
\frac{\partial^2\ell_n(\theta_0)}
{\partial\theta\partial\theta^T}
+o_p(1)
\right]^{-1}
\left[
\frac{1}{\sqrt n}
\frac{\partial\ell_n(\theta_0)}{\partial\theta}
\right].
\]

在 regularity conditions 下，

\[
\frac{1}{\sqrt n}
\frac{\partial\ell_n(\theta_0)}{\partial\theta}
\xrightarrow{d}
N(0,I(\theta_0)),
\]

并且

\[
-\frac{1}{n}
\frac{\partial^2\ell_n(\theta_0)}
{\partial\theta\partial\theta^T}
\xrightarrow{p}
I(\theta_0).
\]

由 Slutsky theorem 得到

\[
\sqrt n(\hat\theta-\theta_0)
\xrightarrow{d}
N(0,I(\theta_0)^{-1}).
\]

### Lem 19.7 Information Identity

板书推导了两个常用结论。第一，

\[
E_{\theta_0}
\left[
\frac{\partial}{\partial\theta}\log f_{\theta}(X)
\bigg|_{\theta=\theta_0}
\right]
=0.
\]

因为

\[
E_{\theta_0}
\left[
\frac{\partial}{\partial\theta}\log f_\theta(X)
\bigg|_{\theta=\theta_0}
\right]
= \int
\frac{\partial_\theta f_\theta(x)|_{\theta=\theta_0}}
{f_{\theta_0}(x)}
f_{\theta_0}(x)\,dx
= \frac{\partial}{\partial\theta}
\int f_\theta(x)\,dx\bigg|_{\theta=\theta_0}
=0.
\]

第二，在 regularity conditions 下，

\[
I(\theta_0)
= E_{\theta_0}\left[
s_{\theta_0}(X)s_{\theta_0}(X)^T
\right]
= -
E_{\theta_0}
\left[
\frac{\partial^2}{\partial\theta\partial\theta^T}
\log f_\theta(X)
\bigg|_{\theta=\theta_0}
\right],
\]

其中

\[
s_{\theta_0}(X)=
\frac{\partial}{\partial\theta}\log f_\theta(X)
\bigg|_{\theta=\theta_0}
\]

是 score function。

### Rmk 19.8 AR(p) MLE Asymptotic Normality

对于 Gaussian AR(p)，由于 conditional MLE 等价于 OLS，最终结论可写成

\[
\sqrt n(\hat{\boldsymbol\phi}-\boldsymbol\phi)
\xrightarrow{d}
N(0,\sigma^2\Gamma_p^{-1}),
\]

其中

\[
\Gamma_p=E(\mathbf X_t\mathbf X_t^T),
\qquad
\mathbf X_t=(Y_{t-1},\ldots,Y_{t-p})^T.
\]

若用 normalized autocovariance matrix 表示，也可把 $\Gamma_p$ 写成由 $\gamma_0,\gamma_1,\ldots,\gamma_{p-1}$ 组成的 Toeplitz matrix。

**【原笔记中断】** Lecture 19 最后一页把 AR(2) 的 asymptotic covariance 留成 homework：计算

\[
Y_t=\phi_1Y_{t-1}+\phi_2Y_{t-2}+e_t,
\qquad
\sqrt n(\hat{\boldsymbol\phi}-\boldsymbol\phi)
\xrightarrow{d}
N(0, ?).
\]

这里没有完整答案，建议后续单独作为一道推导题整理。它是非常重要的复习点，因为它要求把 Yule–Walker、Toeplitz covariance matrix 和 OLS/MLE asymptotic normality 接起来。

## Part B. 复习视角

Lecture 19 是本轮最理论化的一讲，核心是 **MLE 为什么相合、为什么渐近正态**。这节不是只服务于 ARMA，而是在补统计推断的大框架。先用 iid 模型解释 MLE consistency，再用 score equation 和 Taylor expansion 推出 asymptotic normality，最后再回到 AR(p) conditional MLE。

这一讲非常值得花额外时间。原因是它把前面很多“会算 estimator”的内容提升成“知道 estimator 的分布”。后面如果要做 confidence interval、hypothesis testing、AIC/BIC、diagnostics，最终都离不开 consistency 和 asymptotic normality。

这一讲的空白信号也最强。笔记里有多个黑板照片式页面，推导密度很高，尤其是 Fisher information identity 和 AR(p) asymptotic covariance。这通常意味着课堂强度较大，容易跟不上。建议复习时不要一次性硬啃整讲，而是先把 MLE 的三步逻辑背熟：sample log-likelihood 收敛到 population criterion；score equation 在真值附近 Taylor 展开；score 的 CLT 与 Hessian 的 LLN 合起来得到渐近正态。

---

# Lecture 20: Estimation Summary and Transition

## Part A. 课堂内容还原

### Rmk 20.1 Lecture 20 Note Status

Lecture 20 的扫描件内容非常少。笔记中写到日期 5/13，并总结：

\[
Conditional\ OLS,\quad MLE.
\]

接着写：

\[
AR:\quad OLS \Longleftrightarrow MLE,
\]

并提到对于 moment estimator，今天主要讲了如何处理相关内容。

**【原笔记中断】** 上传文件中 Lecture 20 只保留了一页摘要式笔记，没有完整板书推导。根据 Lecture 19 结尾的 homework 和 Lecture 20 的摘要，Lecture 20 很可能是在总结 Chapter 7 estimation 的三条线：MoM、OLS/CSS、MLE，并强调在 Gaussian AR 模型中 OLS 与 conditional MLE 的等价关系。若课堂回放中有更多板书，建议优先补充这一节。

### Rmk 20.2 Safe Reconstruction of the Likely Lecture 20 Thread

**【根据前后文补充】** 从 Lecture 17–19 的承接关系看，Lecture 20 很可能围绕以下主线收束：对 AR(p)，Yule–Walker moment estimator、OLS estimator 和 Gaussian conditional MLE 都估计同一个 $\boldsymbol\phi$，并且在大样本下具有相同或相近的渐近行为；对 MA(q) 和 ARMA(p,q)，moment estimator 不稳定，OLS/CSS 与 MLE 更常用，但通常需要数值优化；MLE 的理论性质由 Lecture 19 的 consistency 和 asymptotic normality 支撑。

对于 Gaussian AR(p)，可以安全写出

\[
\hat{\boldsymbol\phi}_{OLS}
= \hat{\boldsymbol\phi}_{CMLE},
\]

因为二者都等价于最小化

\[
\sum_{t=p+1}^n
\left(Y_t-\phi_1Y_{t-1}-\cdots-\phi_pY_{t-p}\right)^2.
\]

同时，moment/Yule–Walker estimator 与 OLS/CMLE 在大样本下会有相同目标，但小样本公式并不完全一样。

## Part B. 复习视角

Lecture 20 在现有笔记中不像一节完整新课，更像 Chapter 7 estimation 的收束。你真正需要从这里带走的结论是：**不同估计方法不是孤立的，它们在 AR 模型中会汇合，在 MA/ARMA 模型中会分化**。AR 模型有线性回归结构，因此 OLS、conditional MLE、Yule–Walker 都很自然；MA/ARMA 的误差需要递推，导致 objective function 非线性，MLE/CSS 往往要靠数值算法。
