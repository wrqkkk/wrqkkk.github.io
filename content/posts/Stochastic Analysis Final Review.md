+++
date = '2026-06-4T21:00:00+08:00'
draft = false
title = 'Stochastic Analysis Final Review'
isCJKLanguage = true
math = true
+++


# 金融随机分析课堂笔记整理讲义：Lecture 1–5

> 本版按照 PDF 页序和 lecture 原始顺序整理。由于原件为手写扫描与课堂照片，文中保留了若干 **【原笔记留白】**、**【推导中断】**、**【条件缺失】**、**【板书无法识别】** 与 **【根据前后文补充】** 标记。  

> 覆盖范围：Lecture 1 约 PDF 第 2–7 页；Lecture 2 约第 9–14 页；Lecture 3 约第 15–22 页；Lecture 4 约第 23–26 页；Lecture 5 约第 27–32 页。第 1、8、33 页基本为空白或封面式页面。

---

# Lecture 1. 概率空间、随机变量、σ-代数流与随机过程

## Part A. 课堂内容还原

### Rmk 1.1 概率空间的基本结构回顾

本讲从 **probability space** 的复习开始。一个概率空间写作 $(\Omega,\mathcal F,\mathbb P)$.

这里 **$\Omega$** 是样本空间，表示所有可能结果的集合；**$\mathcal F$** 是定义在 $\Omega$ 上的 **σ-代数**，表示我们允许讨论其概率的事件集合；**$\mathbb P$** 是概率测度，把事件映到实数概率值。板书中特别强调了一个映射关系：概率不是直接定义在所有 $\Omega$ 的子集上，而是定义在 $\mathcal F$ 上，即 $\mathbb P:\mathcal F\to \mathbb R$.

这一步非常关键。后面定义随机变量、随机过程、适应过程时，所有“可测”条件本质上都在问：某个集合是不是属于对应的 σ-代数，因此能不能被当前信息系统识别为事件。

### Def 1.2 σ-代数

设 $\Omega$ 是样本空间。若 $\mathcal F$ 是 $\Omega$ 的若干子集构成的集合，并且满足以下性质，则称 $\mathcal F$ 是 $\Omega$ 上的一个 **σ-代数**：$\Omega\in \mathcal F$.

若 $A\in\mathcal F$，则 $A^c\in\mathcal F$.

若 $A_1,A_2,\dots,A_n,\dots\in\mathcal F$，则

\[
\bigcup_{i=1}^{\infty}A_i\in\mathcal F.
\]

第三个条件是 **可列并封闭性**。由补集封闭和可列并封闭可以推出可列交封闭，因为

\[
\bigcap_{i=1}^{\infty}A_i
= \left(\bigcup_{i=1}^{\infty}A_i^c\right)^c.
\]

在概率论中，$A\in\mathcal F$ 表示 $A$ 是一个可以被讨论概率的随机事件。板书写到“$A\in\mathcal F$ 是随机事件，是 $\Omega$ 的子集”，核心含义是：**不是每个集合都天然是事件，只有落在 $\mathcal F$ 中的集合才是事件**。

### Def 1.3 概率测度

设 $\mathcal F$ 是 $\Omega$ 上的 σ-代数。映射 $\mathbb P:\mathcal F\to \mathbb R$称为概率测度，如果它满足：$\mathbb P(\Omega)=1$,对任意 $A\in\mathcal F$，有 $\mathbb P(A)\ge 0$,

若 $A_1,A_2,\dots\in\mathcal F$ 两两不交，则

\[
\mathbb P\left(\bigcup_{i=1}^{\infty}A_i\right)
= \sum_{i=1}^{\infty}\mathbb P(A_i).
\]

第一条是 **规范性**，第二条是 **非负性**，第三条是 **可列可加性**。因此三元组 $(\Omega,\mathcal F,\mathbb P)$称为一个概率空间。

### Ex 1.4 有限样本空间上的 σ-代数

课堂中取 $\Omega=\{1,2,\dots,6\}$.

最小的 σ-代数是 $\mathcal F_0=\{\Omega,\varnothing\}$.

最大的 σ-代数是幂集 $\mathcal F_1=2^\Omega$,

也就是 $\Omega$ 的所有子集构成的集合。若 $|\Omega|=6$，则 $|2^\Omega|=2^6$.

板书中还写了一个中间例子，类似于 $\mathcal F_2=\{\{1\},\{2,3,4,5,6\},\Omega,\varnothing\}$.

这个例子表达的是：一个 σ-代数可以比最小 σ-代数更细，但不一定达到幂集那么细。它把 $\Omega$ 分成一些“信息块”，例如知道结果是否为 $1$，但不能区分 $2,3,4,5,6$ 之间的差异。

**【原笔记留白】** 板书中提出了一个思考题：“若 $|\Omega|=n$，最多构成多少个 σ-代数？”这里没有继续展开。这个问题本质上和有限集合的 **partition** 有关：有限样本空间上的每个 σ-代数都由一个划分生成。需要回看老师是否要求掌握计数公式，还是只要求理解“σ-代数对应信息粗细”。

### Def 1.5 生成的 σ-代数

设 $\mathcal R$ 是 $\Omega$ 的某些子集构成的集合。称包含 $\mathcal R$ 的最小 σ-代数为由 $\mathcal R$ 生成的 σ-代数，记作 $\sigma(\mathcal R)$.

也就是说，$\sigma(\mathcal R)$ 是所有包含 $\mathcal R$ 的 σ-代数中最小的一个。它至少包含 $\mathcal R$，并且为了满足 σ-代数的封闭性，还必须包含 $\mathcal R$ 中集合的补集、可列并、可列交，以及反复进行这些操作之后得到的集合。

数学上，**生成 σ-代数**解决的问题是：从一批最基本的可观测事件出发，自动补全所有由这些事件逻辑推出的事件。金融上，它对应“由某些可观测变量产生的信息”。例如只观察到股票价格 $S_t$，那么由 $S_t$ 生成的 σ-代数就是“仅凭 $S_t$ 当前值能够判断的全部事件”。

### Def 1.6 Borel σ-代数

当 $\Omega=\mathbb R$时，最大的 σ-代数是 $2^{\mathbb R}$.

但在实数轴上通常不直接使用 $2^{\mathbb R}$，而是使用 **Borel σ-代数**。课堂中先列出了实数轴上的常见区间：

\[
(-\infty,\infty),\quad (a,\infty),\quad (-\infty,b),\quad (a,b),
\] $[a,b],\quad (a,b],\quad [a,b)$.

令 $\mathcal G$ 表示实数轴上所有区间构成的集合。区间集合 $\mathcal G$ 本身不是 σ-代数，因为它对可列并等操作不封闭。包含 $\mathcal G$ 的最小 σ-代数称为 $\mathbb R$ 上的 **Borel σ-代数**，记为 $\mathcal B(\mathbb R)$.

这里的核心是：**Borel 集是从区间出发，通过补集、可列并、可列交等操作生成出来的集合**。后面随机变量的定义会要求 $X^{-1}(A)\in\mathcal F,\qquad A\in\mathcal B(\mathbb R)$,所以 Borel σ-代数是随机变量可测性的目标 σ-代数。

### Prop 1.7 Borel σ-代数的若干性质

课堂中给出以下性质。对任意 $x\in\mathbb R$，单点集 $\{x\}\in\mathcal B(\mathbb R)$.

**【根据前后文补充】** 证明思路是

\[
\{x\}=\bigcap_{n=1}^{\infty}\left(x-\frac1n,x+\frac1n\right),
\]

右侧是 Borel 集的可列交，因此 $\{x\}$ 是 Borel 集。

任意有理数集属于 $\mathcal B(\mathbb R)$。更准确地说，由于 $\mathbb Q$ 是可数集，且每个单点集 $\{q\}$ 都是 Borel 集，所以

\[
\mathbb Q=\bigcup_{q\in\mathbb Q}\{q\}\in\mathcal B(\mathbb R).
\]

同理，任意可数子集都是 Borel 集。板书中特别提醒：“任一无理数集属于 $\mathcal B(\mathbb R)$”这个说法是错的。但是，某个区间中的无理数点集是 Borel 集。例如 $(a,b)\cap \mathbb Q^c = (a,b)\setminus \mathbb Q$.

因为 $(a,b)\in\mathcal B(\mathbb R)$，$\mathbb Q\in\mathcal B(\mathbb R)$，所以该集合也是 Borel 集。

### Thm 1.8 Borel σ-代数的一个生成方式

课堂中给出的定理是

\[
\mathcal B(\mathbb R)
= \sigma\left(\{(-\infty,x]\mid x\in\mathbb R\}\right).
\]

这说明，虽然 Borel σ-代数可以由所有区间生成，但实际上只用半无限区间 $(-\infty,x]$也可以生成整个 $\mathcal B(\mathbb R)$。

**【推导中断】** 原笔记写了“可证明”，但没有展开证明。这里需要补一个标准证明思路：先证明每个 $(-\infty,x]$ 是 Borel 集，因此右边包含于 $\mathcal B(\mathbb R)$；再证明开区间 $(a,b)$ 可以由这些半无限区间通过补集和可列并交构造出来，例如 $(a,b] = (-\infty,b]\cap(-\infty,a]^c$,进一步用可列并得到开区间，从而生成所有开集，再生成 Borel σ-代数。

### Def 1.9 随机变量

设 $(\Omega,\mathcal F,\mathbb P)$是概率空间。映射 $X:\Omega\to\mathbb R$

若满足对任意 $x\in\mathbb R$，都有 $X^{-1}((-\infty,x])\in\mathcal F$,则称 $X$ 为随机变量。等价地， $\{X\le x\} = \{\omega\in\Omega:X(\omega)\le x\} \in\mathcal F$.

这句话的意思是：对每个阈值 $x$，事件“随机变量 $X$ 的取值不超过 $x$”必须是一个可测事件。这样才能定义分布函数 $F_X(x)=\mathbb P(X\le x)$.

数学上，随机变量不是“随机变化的数”，而是一个从样本空间到实数轴的 **可测映射**。金融上，股票收益、资产价格、期权收益、终端财富都要先满足这个可测性条件，才能谈它们的分布、期望、条件期望和风险度量。

### Def 1.10 随机变量生成的 σ-代数

设 $X$ 是定义在概率空间 $(\Omega,\mathcal F,\mathbb P)$ 上的随机变量。称

\[
\sigma(X)
= \sigma\left(\{X^{-1}((-\infty,x])\mid x\in\mathbb R\}\right)
\]

为由随机变量 $X$ 生成的 σ-代数。其中

\[
X^{-1}((-\infty,x])
= \{\omega\in\Omega:X(\omega)\le x\}.
\]

由它们生成的 σ-代数 $\sigma(X)$ 表示“只观察 $X$ 时能够知道的全部事件”。显然有 $\sigma(X)\subseteq \mathcal F$.

这是因为 $X$ 是随机变量，所以所有 $\{X\le x\}$ 都已经属于 $\mathcal F$，而 $\mathcal F$ 本身是 σ-代数，因此它也包含由这些集合生成的最小 σ-代数。

### Def 1.11 两个随机变量生成的 σ-代数

设 $X,Y$ 是两个随机变量。课堂中定义

\[
\sigma(X,Y)
= \sigma\left(
\{X^{-1}((-\infty,x]),Y^{-1}((-\infty,y])\mid x,y\in\mathbb R\}
\right).
\]

**【根据前后文补充】** 如果把 $(X,Y)$ 看成二维随机向量，则也可写为

\[
\sigma(X,Y)=\sigma\left((X,Y)^{-1}(C)\mid C\in\mathcal B(\mathbb R^2)\right).
\]

金融上，$\sigma(X,Y)$ 表示同时观察到 $X$ 和 $Y$ 后拥有的信息。例如同时观察股票价格和利率，就比只观察股票价格拥有更细的信息结构。

### Def 1.12 完备概率空间

设 $(\Omega,\mathcal F,\mathbb P)$是概率空间。称其为 **完备的**，如果任意零测集的任意子集仍属于 $\mathcal F$。也就是说，若 $A\in\mathcal F$ 且 $\mathbb P(A)=0$,则对任意 $B\subseteq A$，都有 $B\in\mathcal F$.

完备性处理的是概率为 $0$ 的异常集合。随机分析中经常讨论“几乎处处”或“几乎必然”成立的性质，完备性保证零概率集合内部的子集也不会造成可测性问题。

### Def 1.13 σ-代数流与通常条件

设 $\{\mathcal F_t,t\ge 0\}$是 $\mathcal F$ 的一族子 σ-代数。如果它满足以下条件，则称其为一个满足通常条件的 **σ-代数流**，也称 **filtration**。

首先是单调性。若 $s\le t$，则 $\mathcal F_s\subseteq \mathcal F_t$.

这表示信息随时间增加。时间越晚，知道的信息不能比过去更少。

其次是完备性。课堂板书写作“$\mathcal F_0$ 包含 $\mathcal F$ 中所有 $\mathbb P$-零集”。也就是说，所有零概率异常事件从一开始就被纳入信息系统。

再次是右连续性。

**【条件缺失】** 原笔记在“右连续性”后只写了“要抄”，没有抄出公式。标准通常条件中的右连续性是

\[
\mathcal F_t=\bigcap_{s>t}\mathcal F_s,
\qquad t\ge 0.
\]

这里需要回看老师是否采用这一标准定义。右连续性在后面讨论停时、可选停止、鞅正则化时会很重要。

### Def 1.14 带滤的概率空间

设 $(\Omega,\mathcal F,\mathbb P)$是概率空间，且 $\{\mathcal F_t,t\ge 0\}$是满足通常条件的 σ-代数流，则称 $(\Omega,\mathcal F,\{\mathcal F_t\}_{t\ge 0},\mathbb P)$为一个 **带滤的概率空间**，也称 **filtered probability space**。

数学上，带滤的概率空间是连续时间随机分析的基本舞台。金融上，$\mathcal F_t$ 表示时刻 $t$ 市场参与者已经掌握的全部信息，包括历史价格、历史利率、历史噪声等。后面的 martingale、stochastic integral、risk-neutral pricing 都必须相对于某个 filtration 来定义。

### Def 1.15 随机过程

设 $T\subseteq\mathbb R$。若对任意 $t\in T$，$X_t$ 都是概率空间 $(\Omega,\mathcal F,\mathbb P)$ 上的随机变量，则称 $\{X_t,t\in T\}$为一个随机过程。

如果 $T$ 是一个区间，则称它为 **连续时间随机过程**。如果 $T$ 至多可数，则称它为 **离散时间随机过程**。

随机过程可以看成一个二元映射 $X:\Omega\times T\to\mathbb R$.

固定 $t\in T$ 时， $X_t(\omega)$是关于 $\omega$ 的随机变量。固定 $\omega_0\in\Omega$ 时， $t\mapsto X_t(\omega_0)$是关于时间 $t$ 的函数，称为一条样本路径。

### Rmk 1.16 随机变量视角与路径视角

课堂中特别强调了随机过程的两个观察角度。固定时间 $t$ 时， $X_t:\Omega\to\mathbb R$是一个随机变量。固定样本点 $\omega_0$ 时， $X_t(\omega_0):T\to\mathbb R$是一条关于时间的函数，也就是路径。

这两个视角必须同时掌握。概率论更常从固定 $t$ 的随机变量视角出发，而随机分析和金融数学经常需要研究整条路径，例如连续性、跳跃、变差、二次变差等。

### Def 1.17 路径

对随机过程 $\{X_t,t\in T\}$,

固定 $\omega_0\in\Omega$ 后得到的函数 $t\mapsto X_t(\omega_0)$称为该随机过程在样本点 $\omega_0$ 下的一条路径。

课堂中画了路径示意，并区分了连续时间下的不同路径类型，例如连续路径和带跳路径。

**【原笔记留白】** 这里没有给出严格的“连续路径”“带跳路径”定义。后面如果进入 Brownian motion，需要重点补上：Brownian motion 要求样本路径几乎处处连续；而 Poisson process 或跳过程则允许路径出现跳跃。这是后面区分 Itô calculus 与 jump process 的基础。

### Def 1.18 适应过程

设 $(\Omega,\mathcal F,\mathbb P)$ 是概率空间，$\{X_t,t\ge 0\}$ 是随机过程，$\{\mathcal F_t,t\ge 0\}$ 是其上的 σ-代数流。若对任意 $t\ge 0$，随机变量 $X_t$ 关于 $\mathcal F_t$ 可测，则称 $\{X_t,t\ge 0\}$是关于 $\{\mathcal F_t,t\ge 0\}$的 **适应过程**，也称 **adapted process**。也就是说，对任意 $x\in\mathbb R$，有 $\{X_t\le x\}\in\mathcal F_t$.

适应性表达的是：在时刻 $t$，$X_t$ 的值不能依赖未来信息。金融上，这一点对应交易策略的非预见性。一个交易策略在 $t$ 时刻只能使用 $\mathcal F_t$ 中的信息，不能提前知道未来价格。后面定义自融资策略、Itô integral 和无套利定价时，适应性会反复出现。

**【推导中断】** 原笔记最后一行停在“i.e. $\forall x\in\cdots$”附近，公式没有抄完整。这里按标准定义补全为 $\{X_t\le x\}\in\mathcal F_t$。

## Part B. 复习视角

Lecture 1 的主线是从 **事件的可测性** 过渡到 **随机对象的信息结构**。前半部分复习概率空间 $(\Omega,\mathcal F,\mathbb P)$，重点不是重新学概率公理，而是重新理解 $\mathcal F$ 的作用：$\mathcal F$ 决定哪些集合是事件，哪些事件能被赋予概率。紧接着，老师引入 Borel σ-代数 $\mathcal B(\mathbb R)$，目的是为随机变量的定义准备目标空间上的可测结构。最后，随机变量、随机变量生成的 σ-代数、filtration、随机过程和适应过程连在一起，形成连续时间随机分析的语言框架。

本讲最核心的关键词是 **σ-代数**、**Borel σ-代数**、**measurable random variable**、**generated σ-algebra**、**filtration**、**filtered probability space**、**stochastic process** 和 **adapted process**。其中 Def 1.9 的随机变量定义非常基础，因为后面所有 $X_t$、$S_t$、$W_t$ 都必须先是随机变量。Def 1.10 的 $\sigma(X)$ 是理解信息的第一步，因为它表示“由 $X$ 产生的信息”。Def 1.13 的 filtration 是把信息放进时间轴，Def 1.18 的 adapted process 则规定随机过程不能提前使用未来信息。

本讲的公式链可以整理成这样：先有概率空间 $(\Omega,\mathcal F,\mathbb P)$,

然后实值随机变量是可测映射

\[
X:\Omega\to\mathbb R,
\qquad X^{-1}((-\infty,x])\in\mathcal F.
\]

由随机变量产生信息

\[
\sigma(X)=\sigma\left(\{X^{-1}((-\infty,x])\mid x\in\mathbb R\}\right).
\]

把信息放进时间轴，得到 filtration $\mathcal F_s\subseteq\mathcal F_t, \qquad s\le t$.

随机过程是时间参数化的一族随机变量 $\{X_t,t\in T\}$.

若每个 $X_t$ 都只使用当前信息 $\mathcal F_t$，则 $X_t\text{ is }\mathcal F_t\text{-measurable}$,

于是 $X$ 是适应过程。

这一讲和后面内容的关系非常直接。Lecture 2 会继续讨论随机过程的更强可测性，例如 **measurable process** 和 **progressively measurable process**。Lecture 3 会进入 **conditional expectation**，而条件期望必须相对于某个子 σ-代数定义。Lecture 4 的 **martingale** 需要同时使用 filtration、adaptedness 和 conditional expectation。也就是说，Lecture 1 不是普通预备知识，而是在搭建 martingale theory 的语法系统。

本讲明显需要补的地方有三处。第一处是 Ex 1.4 后面的有限样本空间 σ-代数计数问题，原笔记只写了问题，没有写答案。第二处是 Def 1.13 中通常条件的右连续性，原笔记明确写了“要抄”，这里属于高优先级缺口，因为右连续性后面会影响停时和鞅的技术条件。第三处是 Def 1.17 路径部分，连续路径和带跳路径只画了示意，没有给严格定义。这个缺口在进入 Brownian motion 时会变得重要，因为 Brownian motion 的连续路径性质是 Itô calculus 的基础。

---

# Lecture 2. 随机过程的可测性、循序可测、生成滤流与一致可积

## Part A. 课堂内容还原

### Rmk 2.1 随机变量可测性的复习

Lecture 2 一开始复习随机变量的可测性。设 $X:\Omega\to\mathbb R$.

若对任意 $x\in\mathbb R$，有 $X^{-1}((-\infty,x])\in\mathcal F$,则 $X$ 是随机变量。课堂中把这个条件和分布函数联系起来，因为 $\{\omega:X(\omega)\le x\}$必须是随机事件，$\mathbb P(X\le x)$ 才有意义。

课堂还补充了一个更一般的等价形式：

\[
X\text{ 是随机变量}
\Longleftrightarrow \forall A\in\mathcal B(\mathbb R),\ X^{-1}(A)\in\mathcal F.
\]

这句话非常重要。它说明随机变量的可测性不只是对半无限区间成立，而是对所有 Borel 集成立。由于 Lecture 1 中 Thm 1.8 已经说明 $\mathcal B(\mathbb R)$ 可以由 $(-\infty,x]$ 生成，所以只检查 $(-\infty,x]$ 足够。

### Rmk 2.2 随机过程的两种视角

课堂再次强调随机过程 $X=\{X_t,t\in T\}$

可以看成映射 $X:T\times\Omega\to\mathbb R$.

固定 $t$ 时，$X_t$ 是随机变量。固定 $\omega_0$ 时，$X_t(\omega_0)$ 是关于 $t$ 的函数。

若 $T$ 是离散点集，得到离散时间随机过程；若 $T$ 是区间，得到连续时间随机过程。课堂中特别提到“Borel 集是不是区间？”这一问题。答案是：**区间是 Borel 集，但 Borel 集远不止区间**。Borel σ-代数是由区间生成出来的 σ-代数，因此包含可列并、可列交、补集等操作生成的复杂集合。

### Def 2.3 可测随机过程

设 $(\Omega,\mathcal F,\mathbb P)$ 是概率空间，$X=\{X_t,t\in T\}$ 是随机过程，并把它看成映射 $X:T\times\Omega\to\mathbb R$.

若对任意 $A\in\mathcal B(\mathbb R)$，都有 $X^{-1}(A)\in\mathcal B(T)\otimes\mathcal F$,则称 $X$ 是 **可测随机过程**。

这里 $\mathcal B(T)\otimes\mathcal F$ 是定义在乘积空间 $T\times\Omega$ 上的 σ-代数。这个定义比“每个固定 $t$ 时 $X_t$ 是随机变量”更强，因为它要求 $(t,\omega)$ 作为整体变量时也是可测的。

**【根据前后文补充】** 如果只知道每个 $X_t$ 都是随机变量，不能自动推出 $X:T\times\Omega\to\mathbb R$ 对乘积 σ-代数可测。Lecture 2 在这里补上随机过程作为二元映射时的可测性。

### Def 2.4 循序可测随机过程

设 $X=\{X_t,t\ge0\}$ 是随机过程。记 $X:[0,+\infty)\times\Omega\to\mathbb R$.

若对任意 $T>0$，限制映射 $X|_{[0,T]\times\Omega}:[0,T]\times\Omega\to\mathbb R$满足

\[
X^{-1}(A)\in\mathcal B([0,T])\otimes\mathcal F_T,
\qquad A\in\mathcal B(\mathbb R),
\]

则称 $X$ 是 **循序可测的随机过程**，也称 **progressively measurable process**。

循序可测性比普通可测性更贴近金融中的时间信息结构。它不仅要求 $(t,\omega)$ 可测，而且要求在任意有限时间窗口 $[0,T]$ 上，过程只使用 $\mathcal F_T$ 中的信息。

**【板书照片补充】** 第 10 页下方的板书照片显示，老师在证明或解释时强调了对任意 $T>0$ 都要检查 $[0,T]\times\Omega$ 上的可测性。原笔记文字在这里比较断裂，建议回看 13:31 后后的板书推进。

### Def 2.5 适应过程

设 $\{\mathcal F_t,t\ge0\}$ 是 σ-代数流，$X=\{X_t,t\ge0\}$ 是随机过程。若对任意 $t\ge0$，都有 $X_t\text{ is }\mathcal F_t\text{-measurable}$,则称 $X$ 是关于 $\{\mathcal F_t\}$ 的 **适应过程**。

课堂中特别标注“14:00 重听”。这说明 Def 2.5 附近很可能是一个听课断点。适应性是后面 martingale 和 trading strategy 的基础，建议优先补这段回放。

### Thm 2.6 由随机过程生成的 σ-代数流

设 $X=\{X_t,t\ge0\}$是一个随机过程。定义 $\mathcal F_t^X = \sigma\bigl( X_s:s\le t \bigr), \qquad t\ge0$.则 $\mathcal S^X=\{\mathcal F_t^X,t\ge0\}$是一个 σ-代数流，并且 $X$ 关于 $\mathcal S^X$ 是适应过程。

证明思路是直接的。若 $s\le t$，那么 $\{X_u:u\le s\}\subseteq \{X_u:u\le t\}$,因此 $\mathcal F_s^X\subseteq\mathcal F_t^X$.

这说明 $\{\mathcal F_t^X\}$ 满足 filtration 的单调性。另一方面，因为 $X_t$ 本身被包含在 $\{X_s:s\le t\}$ 中，所以 $X_t$ 关于 $\mathcal F_t^X$ 可测，故 $X$ 关于其自然滤流是适应的。

金融上，$\mathcal F_t^X$ 就是“到时刻 $t$ 为止由过程 $X$ 的历史产生的信息”。例如 $S_t$ 是股票价格过程时，$\mathcal F_t^S$ 表示只由股票历史价格产生的信息流。

### Def 2.7 $L^p$ 空间

课堂接着进入几个常用空间。对 $p\ge1$，定义

\[
L^p(\Omega)=\left\{X:\Omega\to\mathbb R\mid X\text{ 是随机变量且 }\mathbb E|X|^p<+\infty\right\}.
\]

当 $p\ge1$ 时，范数定义为 $\|X\|_p=\bigl(\mathbb E|X|^p\bigr)^{1/p}$.

课堂中指出 $(L^p,\|\cdot\|_p)$是一个 **Banach 空间**，即完备赋范线性空间。

### Def 2.8 $L^p$ 过程与 $L^p$-有界过程

若 $X=\{X_t,t\in T\}$ 是随机过程，并且对每个 $t\in T$，都有 $\mathbb E|X_t|^p<+\infty$,则称 $X$ 是一个 **$L^p$ 过程**。

如果进一步有 $\sup_{t\in T}\mathbb E|X_t|^p<+\infty$,则称 $X$ 是一个 **$L^p$-有界过程**。

特别地，当 $p=2$ 时，课堂写到平方可积过程空间，记作类似 $M_T^2$ 的符号，并定义范数

\[
\|X\|_{M_T^2}
= \left(\sup_{t\in T}\mathbb E|X_t|^2\right)^{1/2}
= \sup_{t\in T}\left(\mathbb E|X_t|^2\right)^{1/2}.
\]

**【符号需确认】** 原笔记中的空间符号写得像 $M_T^2$ 或 $\mathcal M_T^2$。这里按随机分析常用写法整理为 $M_T^2$。需要回看老师是否采用固定符号。

### Def 2.9 一致可积随机变量族或过程

先回顾单个随机变量的可积性。随机变量 $X$ 可积是指 $\mathbb E|X|<+\infty$.等价地，尾部积分满足

\[
\lim_{k\to\infty}\int_{\{|X|>k\}} |X|\,d\mathbb P=0.
\]

设 $X=\{X_t,t\in T\}$ 是随机过程。如果

\[
\lim_{k\to\infty}\sup_{t\in T}\int_{\{|X_t|>k\}} |X_t|\,d\mathbb P=0,
\]

则称 $\{X_t,t\in T\}$ 是 **一致可积的**，也称 **uniformly integrable**。

一致可积比逐点可积更强。它要求所有 $X_t$ 的大尾部同时可控，不允许某些时刻出现很大的尾部质量。

### Prop 2.10 一致可积的判定定理

课堂给出一致可积的一个判定条件。若随机过程 $\{X_t,t\in T\}$ 满足：存在一个函数 $g:[0,+\infty)\to\mathbb R$

使得 $g$ 单调递增、非负，并且 $\lim_{x\to\infty}\frac{g(x)}{x}=+\infty$,

同时 $\sup_{t\in T}\mathbb E\,g(|X_t|)<+\infty$,则 $\{X_t,t\in T\}$ 一致可积。

一个重要推论是：若对某个 $p>1$，有 $\sup_{t\in T}\mathbb E|X_t|^p<+\infty$,则 $\{X_t,t\in T\}$ 一致可积。此时可以取 $g(x)=x^p$.

因为 $\frac{g(x)}{x}=x^{p-1}\to+\infty$.

### Proof 2.11 一致可积判定定理的证明主线

课堂从 $\sup_{t\in T}\mathbb E[g(|X_t|)]<+\infty$

出发，记 $M=\sup_{t\in T}\mathbb E[g(|X_t|)]<+\infty$.

由于 $\lim_{x\to\infty}\frac{g(x)}{x}=+\infty$,对任意 $\varepsilon>0$，可以取 $N$ 足够大，使得当 $x\ge N$ 时， $\frac{g(x)}{x}>\frac{M}{\varepsilon}$.

于是，在集合 $\{|X_t|\ge N\}$ 上，有 $|X_t|\le \frac{\varepsilon}{M}g(|X_t|)$.因此

\[
\int_{\{|X_t|\ge N\}} |X_t|\,d\mathbb P
\le \frac{\varepsilon}{M}\int_\Omega g(|X_t|)\,d\mathbb P
\le \varepsilon.
\]

对 $t\in T$ 取上确界，就得到

\[
\sup_{t\in T}\int_{\{|X_t|\ge N\}} |X_t|\,d\mathbb P\le \varepsilon.
\]

这正是一致可积的定义。

### Prop 2.12 一致可积与 $L^1$ 收敛

课堂最后写到一个重要定理。设 $\{X_n,n\ge0\}$ 是随机序列，则 $X_n\to X\text{ in }L^1$

当且仅当 $X_n\to X\text{ in probability}$并且 $\{X_n,n\ge0\}$ 一致可积。

其中依概率收敛是

\[
X_n\xrightarrow{P} X
\quad\Longleftrightarrow\quad
\forall\varepsilon>0,
\lim_{n\to\infty}\mathbb P(|X_n-X|\ge\varepsilon)=0.
\]

$L^1$ 收敛是 $\mathbb E|X_n-X|\to0$.

这个定理说明，一致可积是把“概率意义上的收敛”升级为“期望意义上的收敛”的关键条件。

**【证明留白】** 原笔记写了“证明要看书”，没有展开。建议回看教材中该定理的证明，因为它会和后面鞅收敛、停时定理中的一致可积条件产生联系。

## Part B. 复习视角

Lecture 2 的主线是把 Lecture 1 中“每个 $X_t$ 都是随机变量”的概念升级为对整个随机过程的可测性控制。老师先复习 Def 1.9 的随机变量可测性，然后把随机过程看成 $T\times\Omega\to\mathbb R$ 的二元映射，由此引出 Def 2.3 的 **可测随机过程** 和 Def 2.4 的 **循序可测随机过程**。紧接着，老师回到 Def 2.5 的 **适应过程**，并用 Thm 2.6 说明任何随机过程都可以生成自己的自然滤流 $\mathcal F_t^X=\sigma(X_s:s\le t)$。后半讲转向 $L^p$ 空间和一致可积，为 Lecture 3 的条件期望和 Lecture 4 的鞅做准备。

这一讲最容易混淆的是 **可测过程、循序可测过程、适应过程** 三者。可测过程关心 $(t,\omega)$ 整体是否对 $\mathcal B(T)\otimes\mathcal F$ 可测。循序可测过程要求在每个 $[0,T]$ 上对 $\mathcal B([0,T])\otimes\mathcal F_T$ 可测。适应过程只要求每个时刻 $X_t$ 关于当前信息 $\mathcal F_t$ 可测。三者强弱不同，作用也不同。金融上，适应性表达“不用未来信息”；循序可测性通常是定义连续时间积分时需要的更强技术条件。

本讲的公式链是：

\[
X\text{ random variable}
\Longleftrightarrow X^{-1}(A)\in\mathcal F,\quad A\in\mathcal B(\mathbb R),
\]

然后随机过程作为二元映射满足 $X^{-1}(A)\in\mathcal B(T)\otimes\mathcal F$,

循序可测要求对每个 $T>0$， $X^{-1}(A)\in\mathcal B([0,T])\otimes\mathcal F_T$,

自然滤流是 $\mathcal F_t^X=\sigma(X_s:s\le t)$,

一致可积是

\[
\lim_{k\to\infty}\sup_{t\in T}\int_{\{|X_t|>k\}}|X_t|\,d\mathbb P=0.
\]

本讲需要重点补的空白是第 11 页 Def 2.5 附近标注的 “14:00 重听”，那里很可能讲了 **adaptedness** 和 **progressive measurability** 的关系。第 12 页关于 $M_T^2$ 的符号也需要确认。第 14 页的一致可积与 $L^1$ 收敛定理只写了结论，证明留给教材，因此考前至少要能复述定理用途：**一致可积控制尾部，是从依概率收敛走向 $L^1$ 收敛的补充条件**。

---

# Lecture 3. 一致可积补充、条件期望及其性质

## Part A. 课堂内容还原

### Rmk 3.1 从 Lecture 2 到条件期望的过渡

Lecture 3 开头先复习 Lecture 2 的核心内容：随机变量的可测性、Borel σ-代数、随机过程的可测性、循序可测、适应过程，以及一致可积。板书中再次写出

\[
X:\Omega\to\mathbb R,
\qquad
X^{-1}((-\infty,x])\in\mathcal F,
\]

以及

\[
X:[0,T]\times\Omega\to\mathbb R,
\qquad
X^{-1}(A)\in\mathcal B([0,T])\otimes\mathcal F_T.
\]

这说明老师在进入条件期望前，先确保“随机变量相对于 σ-代数可测”这个语言已经建立起来。条件期望本质上就是“给定较少信息时，随机变量的最佳可测替代物”。

### Prop 3.2 一致可积判定定理的复习

若随机过程 $\{X_t,t\in T\}$ 满足存在函数 $g:[0,+\infty)\to\mathbb R$

使得 $g$ 单调递增、非负，且 $\lim_{x\to\infty}\frac{g(x)}{x}=+\infty$,并且 $\sup_{t\in T}\mathbb E[g(|X_t|)]<+\infty$,则 $\{X_t,t\in T\}$ 一致可积。特别地，若存在 $p>1$ 使得 $\sup_{t\in T}\mathbb E|X_t|^p<+\infty$,则 $\{X_t,t\in T\}$ 一致可积。

### Proof 3.3 一致可积判定定理的证明

证明中记 $M=\sup_{t\in T}\mathbb E[g(|X_t|)]<+\infty$.

由于 $\lim_{x\to\infty}\frac{g(x)}{x}=+\infty$,对任意 $\varepsilon>0$，存在 $N>0$，使得当 $x\ge N$ 时， $\frac{g(x)}{x}>\frac{M}{\varepsilon}$.

于是当 $|X_t(\omega)|\ge N$ 时，有

\[
|X_t(\omega)|\le \frac{\varepsilon}{M}g(|X_t(\omega)|).
\]

因此

\[
\int_{\{|X_t|\ge N\}} |X_t|\,d\mathbb P
\le \int_{\{|X_t|\ge N\}} \frac{\varepsilon}{M}g(|X_t|)\,d\mathbb P
\le \frac{\varepsilon}{M}\mathbb E[g(|X_t|)]
\le \varepsilon.
\]

取 $t\in T$ 上确界后，得到一致可积定义中的尾部控制。

### Rmk 3.4 条件期望的直观入口

课堂接着从“两个随机变量”的情形进入条件期望。设 $X,Y$ 是离散随机变量，板书写到类似

\[
\mathbb E[X\mid Y=j]
= \sum_i x_i\frac{p_{ij}}{p_j},
\]

以及

\[
\mathbb E[Y\mid X=i]
= \sum_j y_j\frac{p_{ij}}{p_i}.
\]

这里 $p_{ij}=\mathbb P(X=x_i,Y=y_j)$，$p_j=\mathbb P(Y=y_j)$，$p_i=\mathbb P(X=x_i)$。离散条件期望的结果是一个数，因为条件事件 $\{Y=j\}$ 已经固定。

若 $X,Y$ 有联合密度，则课堂写到类似

\[
\mathbb E[X\mid Y=y]
= \int_{\mathbb R}x f_{X\mid Y}(x\mid y)\,dx,
\]

以及

\[
\mathbb E[Y\mid X=x]
= \int_{\mathbb R}y f_{Y\mid X}(y\mid x)\,dy.
\]

然后板书提出全期望公式：$\mathbb E\bigl[\mathbb E(Y\mid X)\bigr]=\mathbb EY$.

**【符号修正】** 原笔记中这一行写得比较像“$\mathbb E[\mathbb E[Y\mid X]]=\mathbb EY$ ?”，问号说明当时可能还在连接离散直觉和一般定义。标准结论是成立的，只要 $Y\in L^1$。

### Def 3.5 条件期望

设 $(\Omega,\mathcal F,\mathbb P)$是概率空间，$\mathcal G$ 是 $\mathcal F$ 的子 σ-代数，$X$ 是 $(\Omega,\mathcal F,\mathbb P)$ 上的随机变量，并且

\[
X\in L^1(\Omega),
\qquad
\mathbb E|X|<+\infty.
\]

定义 $X$ 关于 $\mathcal G$ 的条件期望，记作 $\mathbb E[X\mid \mathcal G]$.

它是一个随机变量，常记作 $Y=\mathbb E[X\mid\mathcal G]$,并且满足两个条件。首先，$Y$ 关于 $\mathcal G$ 可测。其次，对任意 $A\in\mathcal G$，有

\[
\int_A X\,d\mathbb P
= \int_A Y\,d\mathbb P.
\]

这两个条件共同刻画了条件期望。第一条说明 $Y$ 只能使用 $\mathcal G$ 中的信息。第二条说明在所有 $\mathcal G$-可观测事件 $A$ 上，$Y$ 与原随机变量 $X$ 的积分一致。

数学上，**条件期望是用较少信息 $\mathcal G$ 对 $X$ 做出的可测投影**。金融上，如果 $\mathcal G=\mathcal F_t$，那么 $\mathbb E[X\mid\mathcal F_t]$ 表示在时刻 $t$ 信息下对未来随机收益 $X$ 的估计。

### Prop 3.6 条件期望的几乎处处唯一性

若 $X,Y$ 是两个 $\mathcal G$-可测随机变量，并且对任意 $A\in\mathcal G$，都有

\[
\int_A X\,d\mathbb P
= \int_A Y\,d\mathbb P,
\]

则 $X=Y\quad a.s$.

证明思路是考察集合 $\{X>Y\}$ 和 $\{Y>X\}$。因为 $X,Y$ 都关于 $\mathcal G$ 可测，所以这些集合属于 $\mathcal G$。在这些集合上积分相等，推出差的正部和负部积分为零，因此 $X=Y$ 几乎处处成立。

这解释了为什么条件期望不是逐点唯一，而是 **a.s. 唯一**。

### Prop 3.7 条件期望的基本性质

课堂列出了条件期望的一组性质。若 $X\in L^1$，则如果 $X$ 关于 $\mathcal G$ 可测，有 $\mathbb E[X\mid\mathcal G]=X$.

若 $c$ 是常数，则 $\mathbb E[c\mid\mathcal G]=c$.

全期望公式为 $\mathbb E\left[\mathbb E[X\mid\mathcal G]\right]=\mathbb E[X]$.

若 $X=Y$ a.s.，则 $\mathbb E[X\mid\mathcal G] = \mathbb E[Y\mid\mathcal G] \quad a.s$.

若 $a,b\in\mathbb R$，则

\[
\mathbb E[aX+bY\mid\mathcal G]
=a\mathbb E[X\mid\mathcal G]+b\mathbb E[Y\mid\mathcal G].
\]

若 $X\le Y$ a.s.，则 $\mathbb E[X\mid\mathcal G] \le \mathbb E[Y\mid\mathcal G] \quad a.s$.

若 $X$ 与 $\mathcal G$ 独立，则 $\mathbb E[X\mid\mathcal G]=\mathbb E[X]$.

课堂还写到一个函数型性质，形式类似

\[
\mathbb E[\varphi(X,Y)\mid\mathcal G]
= \left.\mathbb E[\varphi(x,Y)\mid\mathcal G]\right|_{x=X},
\]

其中通常需要 $X$ 关于 $\mathcal G$ 可测，并且 $Y$ 与 $\mathcal G$ 或与 $X$ 的关系满足相应条件。

**【条件缺失】** 原笔记没有写完整该函数型性质的条件。这里不能直接当作无条件公式使用。考试若遇到类似题，必须先确认哪些随机变量 $\mathcal G$-可测，哪些随机变量独立。

### Rmk 3.8 条件期望的塔式性质和不可交换性

课堂照片中强调“配关系才能交换顺序”。如果 $\mathcal G_1\subseteq\mathcal G_2\subseteq\mathcal F$，则塔式性质成立：

\[
\mathbb E\left[\mathbb E[X\mid\mathcal G_2]\mid\mathcal G_1\right]
= \mathbb E[X\mid\mathcal G_1].
\]

同时

\[
\mathbb E\left[\mathbb E[X\mid\mathcal G_1]\mid\mathcal G_2\right]
= \mathbb E[X\mid\mathcal G_1],
\]

因为 $\mathbb E[X\mid\mathcal G_1]$ 已经是 $\mathcal G_1$-可测，而 $\mathcal G_1\subseteq\mathcal G_2$ 时它也 $\mathcal G_2$-可测。

如果 $\mathcal G_1$ 和 $\mathcal G_2$ 没有包含关系，则一般不能交换条件期望的顺序，也不能直接断言

\[
\mathbb E\left[\mathbb E[X\mid\mathcal G_1]\mid\mathcal G_2\right]
= \mathbb E\left[\mathbb E[X\mid\mathcal G_2]\mid\mathcal G_1\right].
\]

**【板书无法识别】** 第 21 页的白板照片包含若干条件期望交换顺序的反例或性质，但照片角度和反光导致部分内容无法准确识别。需要补一张更清晰板书或回看这一段。

### Prop 3.9 条件期望下的收敛性质

课堂照片中写到类似结论：若 $X_n\to X\quad a.s$.并且存在 $Y\in L^1(\Omega)$，使得 $|X_n|\le Y$,则 $\mathbb E[X_n\mid\mathcal G]\to \mathbb E[X\mid\mathcal G] \quad a.s$.

**【根据前后文补充】** 这是条件期望版本的 dominated convergence theorem。严格证明通常依赖条件期望的性质和普通支配收敛定理。

### Formula 3.10 全期望公式

由条件期望定义，取 $A=\Omega\in\mathcal G$，有

\[
\int_\Omega X\,d\mathbb P
= \int_\Omega \mathbb E[X\mid\mathcal G] \ d\mathbb P.
\]

因此 $\mathbb E[X] = \mathbb E\left[\mathbb E[X\mid\mathcal G]\right]$.

这个公式在金融中非常常用。定价中经常先在未来某个信息层下取条件期望，再对当前信息取条件期望，塔式性质保证这种逐层估计是兼容的。

## Part B. 复习视角

Lecture 3 的主线是从 **一致可积** 过渡到 **条件期望**。一致可积解决的是“能不能把收敛和期望联系起来”的问题；条件期望解决的是“在给定信息 $\mathcal G$ 时如何重新表达一个随机变量”的问题。老师先补完 Lecture 2 中一致可积判定定理的证明，再用离散和连续条件期望引入直觉，最后给出一般概率空间中 $\mathbb E[X\mid\mathcal G]$ 的定义。

本讲最核心的对象是 Def 3.5。它的两条条件都要背熟：**$\mathbb E[X\mid\mathcal G]$ 必须 $\mathcal G$-可测，并且在任意 $A\in\mathcal G$ 上与 $X$ 的积分相同**。第一条对应“只能使用给定信息”；第二条对应“在给定信息可区分的事件上，平均效果不变”。这两条一起决定条件期望，而不是某个单独公式决定条件期望。

Lecture 3 和 Lecture 4 的关系非常紧。鞅的定义会写成 $\mathbb E[X_t\mid\mathcal F_s]=X_s, \qquad s\le t$.

这里直接使用了 Def 3.5 的条件期望和 Def 1.13 的 filtration。若没有理解 $\mathcal F_s$ 是较少信息、$\mathbb E[X_t\mid\mathcal F_s]$ 是在较少信息下对未来 $X_t$ 的估计，就很难真正理解 martingale 是“公平游戏”。

本讲需要重点补的地方是第 21 页白板照片中的条件期望交换顺序与收敛性质。尤其“配关系才能交换顺序”这句话很重要，因为塔式性质必须有子 σ-代数包含关系。若 $\mathcal G_1$ 和 $\mathcal G_2$ 没有包含关系，不能随便交换条件期望顺序。这个点在证明鞅性质、停时定理、风险中性定价中的迭代条件期望时都会出现。

---

# Lecture 4. 鞅、随机游走、Brownian motion 与鞅判别

## Part A. 课堂内容还原

### Rmk 4.1 本讲主题预告

Lecture 4 开始时，板书列出几个典型随机过程：**Brownian motion**、**Poisson process**、**martingale** 和 **Markov process**。其中 Brownian motion 和 Poisson process 是连续时间中最基本的噪声模型；martingale 是公平游戏和无套利定价的数学核心；Markov process 强调未来只依赖当前状态而不依赖完整历史。

本讲主要进入 **martingale** 和 **Brownian motion**。

### Def 4.2 鞅、上鞅和下鞅

设 $X=\{X_t,t\in T\}$ 是随机过程，$\{\mathcal F_t,t\in T\}$ 是 σ-代数流。若满足以下条件，则称 $X$ 是关于 $\{\mathcal F_t\}$ 的 **鞅**，即 **martingale**。

首先，对任意 $t\in T$，有 $\mathbb E|X_t|<+\infty$.

其次，$X$ 是适应过程，即对任意 $t\in T$，$X_t$ 关于 $\mathcal F_t$ 可测。

最后，对任意 $s\le t$，有 $\mathbb E[X_t\mid\mathcal F_s]=X_s$.

如果把等号改成 $\mathbb E[X_t\mid\mathcal F_s]\le X_s$,则称 $X$ 为 **上鞅**，即 supermartingale。它表示条件意义下未来期望不超过当前值，可以理解为“趋势不升”。

如果改成 $\mathbb E[X_t\mid\mathcal F_s]\ge X_s$,则称 $X$ 为 **下鞅**，即 submartingale。它表示条件意义下未来期望不低于当前值，可以理解为“趋势不降”。

金融上，鞅的核心意义是 **在当前信息下，未来的条件期望等于当前值**。在风险中性测度下，贴现资产价格过程常被要求是鞅，这正是无套利定价的数学表达。

### Def 4.3 离散时间与连续时间

课堂区分了 **离散时间** 和 **连续时间**。若时间指标集 $T$ 是可数集，例如 $T=\{0,1,2,\dots\}$,则是离散时间过程。若时间指标集是区间，例如 $T=[0,+\infty)$,则是连续时间过程。

### Def 4.4 自然滤流

设 $X=\{X_t,t\in T\}$ 是随机过程。自然滤流定义为 $\mathcal F_t^X=\sigma(X_s:s\le t)$.

由此 $X$ 自动关于 $\{\mathcal F_t^X\}$ 适应。

课堂红字特别提醒：不要写成 $\sigma(X_t)$,

因为 $\sigma(X_t)$ 只包含时刻 $t$ 的信息，而自然滤流应包含从初始时刻到 $t$ 为止的全部历史信息。正确写法必须是 $\sigma(X_s:s\le t)$.

### Ex 4.5 随机游走

设 $X_0=a, \qquad X_n=X_{n-1}+\xi_n, \qquad n\ge1$,

其中 $\xi_n$ 取值为 $1$ 或 $-1$，并且 $\mathbb P(\xi_n=1)=p, \qquad \mathbb P(\xi_n=-1)=q, \qquad p+q=1$.

令自然滤流为 $\mathcal F_n=\sigma(X_m:m\le n)$.

若 $p=q=\frac12$，则 $\{X_n,n=0,1,2,\dots\}$ 是鞅。若 $p>q$，则它是下鞅。若 $p<q$，则它是上鞅。

证明中先检查可积性：

\[
\mathbb E|X_n|
=\mathbb E|a+\xi_1+\cdots+\xi_n|
\le |a|+\mathbb E|\xi_1|+\cdots+\mathbb E|\xi_n|
=|a|+n<+\infty.
\]

适应性由自然滤流定义直接得到。对 $m<n$，有

\[
\mathbb E[X_n\mid\mathcal F_m]
= \mathbb E[X_m+\xi_{m+1}+\cdots+\xi_n\mid\mathcal F_m].
\]

由于 $X_m$ 关于 $\mathcal F_m$ 可测，且后续增量与 $\mathcal F_m$ 独立，有

\[
\mathbb E[X_n\mid\mathcal F_m]
= X_m + \sum_{j=m+1}^n \mathbb E\xi_j.
\]

而 $\mathbb E\xi_j=p-q$.所以 $\mathbb E[X_n\mid\mathcal F_m] = X_m+(n-m)(p-q)$.

当 $p=q$ 时等于 $X_m$，得到鞅。当 $p>q$ 时大于 $X_m$，得到下鞅。当 $p<q$ 时小于 $X_m$，得到上鞅。

### Ex 4.6 Brownian motion 的若干鞅

课堂写到：设 $\{W_t,t\ge0\}$ 是标准 Brownian motion，令 $\mathcal F_t=\sigma(W_s:s\le t)$.则以下过程是鞅：$W_t$, $W_t^2-t$,以及对任意 $\alpha\in\mathbb R$，

\[
\exp\left(\alpha W_t-\frac{\alpha^2}{2}t\right).
\]

**【原笔记标注：期末】** 第 24 页红字把这些例子框出并写了“期末”。这说明它们很可能是考试重点，至少要能证明 $W_t$ 是鞅，并理解另外两个是 Brownian motion 的典型指数鞅和平方鞅。

### Def 4.7 Brownian motion

随机过程 $\{W_t,t\ge0\}$ 称为标准 **Brownian motion**，如果满足以下性质。

首先， $W_0=0$.

其次，对任意 $t>0$， $W_t\sim N(0,t)$.

第三，具有独立增量。若 $0\le t_0<t_1<\cdots<t_n$,则 $W_{t_1}-W_{t_0},\ W_{t_2}-W_{t_1},\ \dots,\ W_{t_n}-W_{t_{n-1}}$

相互独立。

第四，具有平稳增量：$W_{t+s}-W_t\sim N(0,s)$.最后，每条路径连续，通常表述为 $W_t(\omega)\text{ is continuous in }t\quad a.s$.

Brownian motion 在数学上是连续时间随机噪声模型。它的样本路径连续但处处高度不规则，这正是 Itô integral 和 Itô formula 要被引入的原因。金融上，它常用来刻画连续时间资产价格模型中的随机冲击。

### Proof 4.8 Brownian motion 是鞅

首先证明可积性。因为 $W_t\sim N(0,t)$，有

\[
\mathbb E|W_t|
=\int_{\mathbb R}|x|\frac1{\sqrt{2\pi t}}e^{-x^2/(2t)}\,dx
=\sqrt{\frac{2t}{\pi}}<+\infty.
\]

其次，$W_t$ 关于自然滤流 $\mathcal F_t=\sigma(W_s:s\le t)$ 适应。

最后，当 $s<t$ 时， $W_t=W_s+(W_t-W_s)$.

于是

\[
\mathbb E[W_t\mid\mathcal F_s]
= \mathbb E[W_s+(W_t-W_s)\mid\mathcal F_s].
\]

由于 $W_s$ 关于 $\mathcal F_s$ 可测，且 $W_t-W_s$ 与 $\mathcal F_s$ 独立，并且 $W_t-W_s\sim N(0,t-s)$,所以 $\mathbb E[W_t\mid\mathcal F_s] =W_s+\mathbb E[W_t-W_s] =W_s$.因此 $\{W_t,t\ge0\}$ 是鞅。

### Thm 4.9 鞅的期望保持不变

若 $\{X_t,\mathcal F_t,t\in T\}$ 是鞅，则对任意 $s\le t$，有 $\mathbb E[X_t]=\mathbb E[X_s]$.

证明使用全期望公式：

\[
\mathbb E[X_t]
= \mathbb E\left[\mathbb E[X_t\mid\mathcal F_s]\right]
= \mathbb E[X_s].
\]

这说明鞅在无条件期望层面保持不变。更强的是，它在任意过去信息 $\mathcal F_s$ 下的条件期望也保持为当前值。

### Ex 4.10 下鞅在期望不变时退化为鞅

课堂写到：若 $\{X_t,\mathcal F_t,t\ge0\}$ 是下鞅，并且 $\mathbb E[X_t]=\mathbb E[X_0]$对所有 $t\ge0$ 成立，则 $\{X_t,t\ge0\}$ 是鞅。

证明思路是：下鞅给出 $\mathbb E[X_t\mid\mathcal F_s]\ge X_s$.

两边取期望得到 $\mathbb E[X_t]\ge\mathbb E[X_s]$.

但条件中期望恒定，因此差的期望为零。非负随机变量 $\mathbb E[X_t\mid\mathcal F_s]-X_s$的期望为零，所以它几乎处处为零，从而得到鞅等式。

### Thm 4.11 离散时间鞅的单步判别

设 $X=\{X_n,\mathcal F_n,n\ge0\}$是离散时间随机过程。则 $X$ 是鞅，当且仅当它满足可积性、适应性，并且对任意 $n\ge0$，有 $\mathbb E[X_{n+1}\mid\mathcal F_n]=X_n$.

证明中用到塔式性质。如果 $m>n$，则

\[
\mathbb E[X_m\mid\mathcal F_n]
= \mathbb E\left[\mathbb E[X_m\mid\mathcal F_{m-1}]\mid\mathcal F_n\right].
\]

由单步条件， $\mathbb E[X_m\mid\mathcal F_{m-1}]=X_{m-1}$.

于是反复迭代，得到 $\mathbb E[X_m\mid\mathcal F_n]=X_n$.

这说明离散时间中，只要验证一步条件，就能推出任意多步的鞅条件。

## Part B. 复习视角

Lecture 4 是前面三讲的第一次真正合流。Lecture 1 的 filtration、Lecture 2 的适应性、Lecture 3 的条件期望，在 Def 4.2 的 martingale 定义中全部出现。鞅不是单纯的“期望不变”，而是 **在任意过去信息下，未来条件期望等于当前值**。这就是为什么 martingale 是公平游戏和无套利定价的数学核心。

本讲的主线可以概括为：先给出鞅定义，再用随机游走说明离散时间公平游戏，然后进入 Brownian motion，并证明 Brownian motion 本身是鞅。最后给出鞅的期望保持性质和离散时间单步判别法。

本讲公式链非常清楚：鞅定义是 $\mathbb E[X_t\mid\mathcal F_s]=X_s, \qquad s\le t$.

随机游走满足 $\mathbb E[X_n\mid\mathcal F_m]=X_m+(n-m)(p-q)$.

Brownian motion 满足 $W_t=W_s+(W_t-W_s)$,

且 $W_t-W_s$ 与 $\mathcal F_s$ 独立、均值为零，因此 $\mathbb E[W_t\mid\mathcal F_s]=W_s$.

离散时间鞅的单步判别是 $\mathbb E[X_{n+1}\mid\mathcal F_n]=X_n$.

这讲最可能考的是 Brownian motion 的定义、证明 $W_t$ 是鞅、随机游走在 $p=q$、$p>q$、$p<q$ 下分别是什么鞅，以及离散时间单步判别。第 24 页被红字框出的 $W_t^2-t$ 和指数鞅也标了“期末”，建议单独补证明。证明 $W_t^2-t$ 是鞅需要用 $\mathbb E[(W_t-W_s)^2]=t-s$,

证明指数鞅需要用正态分布的 moment generating function。

本讲有两个明显补点。第一是 Def 4.2 的上鞅和下鞅中文方向要固定：**supermartingale 是上鞅，对应条件期望不超过当前值；submartingale 是下鞅，对应条件期望不低于当前值**。第二是 Ex 4.6 的三个 Brownian 鞅中，后两个没有展开证明，但被标为期末，需要优先补。

---

# Lecture 5. 条件期望生成鞅、条件 Jensen、不等式与停时

## Part A. 课堂内容还原

### Thm 5.1 条件期望生成鞅

设 $X$ 是随机变量，满足 $\mathbb E|X|<+\infty$.

设 $\{\mathcal F_t,t\in T\}$ 是一族子 σ-代数，形成一个 filtration。定义 $X_t=\mathbb E[X\mid\mathcal F_t], \qquad t\in T$.则 $\{X_t,\mathcal F_t,t\in T\}$是一个鞅，并且是 **一致可积的**。

证明分成三步。首先证明可积性。由条件 Jensen 不等式或三角不等式，有 $|\mathbb E[X\mid\mathcal F_t]| \le \mathbb E[|X|\mid\mathcal F_t]$.

于是

\[
\mathbb E|X_t|
= \mathbb E|\mathbb E[X\mid\mathcal F_t]|
\le \mathbb E\left[\mathbb E[|X|\mid\mathcal F_t]\right]
= \mathbb E|X|<+\infty.
\]

其次，$X_t=\mathbb E[X\mid\mathcal F_t]$ 按定义关于 $\mathcal F_t$ 可测，因此适应性成立。

最后，对 $s\le t$，由塔式性质，

\[
\mathbb E[X_t\mid\mathcal F_s]
= \mathbb E[\mathbb E[X\mid\mathcal F_t]\mid\mathcal F_s]
= \mathbb E[X\mid\mathcal F_s]
=X_s.
\]

因此 $\{X_t\}$ 是鞅。

### Rmk 5.2 条件 Jensen 不等式

课堂补充了 **条件 Jensen 不等式**。若 $f$ 是凸函数，且相应期望存在，则

\[
f\left(\mathbb E[X\mid\mathcal G]\right)
\le \mathbb E[f(X)\mid\mathcal G].
\]

特别地，取 $f(x)=|x|$，可以得到 $|\mathbb E[X\mid\mathcal G]| \le \mathbb E[|X|\mid\mathcal G]$.

这正是 Thm 5.1 中证明 $X_t$ 可积时使用的关键不等式。

### Proof 5.3 条件期望生成鞅的一致可积性

还需要证明 $\{X_t,t\in T\}$ 一致可积，即

\[
\lim_{k\to\infty}\sup_{t\in T}\int_{\{|X_t|\ge k\}}|X_t|\,d\mathbb P=0.
\]

课堂从事件 $\{|X_t|\ge k\}\in\mathcal F_t$

出发，因为 $X_t$ 关于 $\mathcal F_t$ 可测，所以指示函数 $\mathbf 1_{\{|X_t|\ge k\}}$

也关于 $\mathcal F_t$ 可测。于是

\[
\int_{\{|X_t|\ge k\}}|X_t|\,d\mathbb P
= \int_{\{|X_t|\ge k\}}|\mathbb E[X\mid\mathcal F_t]|\,d\mathbb P.
\]

由条件 Jensen， $|\mathbb E[X\mid\mathcal F_t]| \le \mathbb E[|X|\mid\mathcal F_t]$.所以

\[
\int_{\{|X_t|\ge k\}}|X_t|\,d\mathbb P
\le \int_{\{|X_t|\ge k\}}\mathbb E[|X|\mid\mathcal F_t]d\mathbb P.
\]

由于 $\{|X_t|\ge k\}\in\mathcal F_t$，根据条件期望定义，

\[
\int_{\{|X_t|\ge k\}}\mathbb E[|X|\mid\mathcal F_t]d\mathbb P
= \int_{\{|X_t|\ge k\}} |X|d\mathbb P.
\]

接着对任意 $J\in\mathbb N^+$，分解

\[
\{|X_t|\ge k\}
= \left(\{|X_t|\ge k\}\cap\{|X|\le J\}\right)
\cup
\left(\{|X_t|\ge k\}\cap\{|X|>J\}\right).
\]

于是

\[
\int_{\{|X_t|\ge k\}} |X|d\mathbb P
\le J\mathbb P(|X_t|\ge k)+\int_{\{|X|>J\}}|X|d\mathbb P.
\]

由 Markov 不等式，且 $\sup_t\mathbb E|X_t|\le \mathbb E|X|=:M$，有

\[
\mathbb P(|X_t|\ge k)
\le \frac{\mathbb E|X_t|}{k}
\le \frac{M}{k}.
\]

因此

\[
\sup_{t\in T}\int_{\{|X_t|\ge k\}} |X_t|d\mathbb P
\le \frac{JM}{k}+\int_{\{|X|>J\}}|X|d\mathbb P.
\]

给定 $\varepsilon>0$，先取 $J$ 足够大，使得

\[
\int_{\{|X|>J\}}|X|d\mathbb P<\frac\varepsilon2,
\]

再取 $k$ 足够大，使得 $\frac{JM}{k}<\frac\varepsilon2$.

于是得到一致可积性。

### Prop 5.4 鞅的一些后续性质预告

课堂列出鞅的若干后续性质，包括 **停时定理**、**convergence theorem**、**inequalities** 和 **分解定理**。

**【原笔记留白】** 这里只是列出主题，没有展开。后续 lecture 很可能会继续讲 Doob optional stopping theorem、Doob martingale convergence theorem、Doob inequalities 和 Doob decomposition。需要在后续整理中接上。

### Def 5.5 停时

设 $(\Omega,\mathcal F,\mathbb P,\{\mathcal F_t,t\in T\})$是 filtered probability space。映射 $\tau:\Omega\to T\cup\{+\infty\}$称为关于 $\{\mathcal F_t\}$ 的 **停时**，如果对任意 $t\in T$，有

\[
\tau^{-1}((-\infty,t])
= \{\omega:\tau(\omega)\le t\}
\in\mathcal F_t.
\]

停时的含义是：在时刻 $t$，我们只用当前信息就能判断“是否已经停止”。它不要求在时刻 $t$ 知道未来什么时候停止，只要求知道停止是否已经发生。

金融上，停时对应“基于当前和过去信息决定的交易或行权时间”。例如美式期权的行权时间必须是停时，因为投资者不能根据未来价格决定现在是否行权。

### Ex 5.6 常数时间是停时

设 $a\ge0$，若 $\{\mathcal F_t,t\ge0\}$ 是 filtration，则常数映射 $\tau(\omega)=a$是停时。

证明是直接的。对任意 $t\ge0$，有

\[
\{\tau\le t\}
= \begin{cases}
\varnothing, & t<a,\\
\Omega, & t\ge a.
\end{cases}
\]

因为 $\varnothing,\Omega\in\mathcal F_t$，所以 $\tau$ 是停时。

### Ex 5.7 离散确定时刻是停时

对离散时间 filtration $\{\mathcal F_n,n\ge0\}$，任意固定 $m\in\mathbb N$ 都是停时，即 $\tau(\omega)=m$.

这和 Ex 5.6 是同一个思想在离散时间中的版本。

### Ex 5.8 连续适应过程的首次 hitting time

设 $\{X_t,t\ge0\}$ 是连续时间随机过程，$\{\mathcal F_t,t\ge0\}$ 是一个 filtration，且 $X$ 关于 $\{\mathcal F_t\}$ 适应。假设 $X_t(\omega)$ 关于 $t$ 连续。对常数 $a$，定义 $\tau^a=\inf\{t\ge0:X_t\ge a\}$.

称 $\tau^a$ 为首次达到水平 $a$ 的时间。课堂要求证明：$\tau^a\text{ 是停时}$.

证明关键是对任意 $t\ge0$，要证明 $\{\tau^a\le t\}\in\mathcal F_t$.

由于路径连续，事件“在 $[0,t]$ 之前某一时刻达到 $a$”等价于 $\sup_{0\le s\le t}X_s\ge a$.

又因为连续函数在有理点上的取值可以逼近整个区间上的上确界，所以

\[
\{\tau^a\le t\}
= \left\{\sup_{s\in[0,t]\cap\mathbb Q}X_s\ge a\right\}.
\]

这个事件可以写成可列并交形式，例如

\[
\{\tau^a\le t\}
= \bigcap_{m=1}^{\infty}\bigcup_{s\in[0,t]\cap\mathbb Q}\{X_s>a-1/m\}.
\]

对每个有理 $s\le t$，由于 $X_s$ 关于 $\mathcal F_s$ 可测，且 $\mathcal F_s\subseteq\mathcal F_t$，所以 $\{X_s>a-1/m\}\in\mathcal F_t$.

可列并和可列交仍属于 $\mathcal F_t$，因此 $\{\tau^a\le t\}\in\mathcal F_t$。故 $\tau^a$ 是停时。

**【根据前后文补充】** 原笔记中该证明写得比较简略，核心思想是把连续时间的“存在某个 $s\le t$”转化为有理时间点上的可列操作。这里补全了标准证明。

### Thm 5.9 停止过程与停时定理的开端

课堂最后进入停止过程。设 $\{X_n,\mathcal F_n,n\ge0\}$是一个离散时间鞅，$\tau$ 是关于 $\{\mathcal F_n\}$ 的停时。定义停止过程 $X_n^\tau=X_{n\wedge\tau}$.

课堂板书写到：$\{X_n^\tau,\mathcal F_n,n\ge0\}$

也是鞅。

这就是停时定理的基本形式之一：**把鞅在一个停时处停止，得到的停止过程仍然是鞅**。

**【证明中断】** 第 32 页只有定理形式和白板照片，没有完整证明。标准证明需要用到事件 $\{\tau\le n\}\in\mathcal F_n$、分解

\[
X_{(n+1)\wedge\tau}
= X_{n\wedge\tau}+\mathbf 1_{\{\tau>n\}}(X_{n+1}-X_n),
\]

再利用 $\{\tau>n\}\in\mathcal F_n$ 和鞅差分条件 $\mathbb E[X_{n+1}-X_n\mid\mathcal F_n]=0$.因此 $\mathbb E[X_{(n+1)\wedge\tau}\mid\mathcal F_n] =X_{n\wedge\tau}$.

这部分需要后续重点补，因为它是 optional stopping theorem 的入口。

## Part B. 复习视角

Lecture 5 的主线是从 **条件期望** 进一步发展到 **鞅构造与停时**。Thm 5.1 说明，只要给定一个终端可积随机变量 $X$，令 $X_t=\mathbb E[X\mid\mathcal F_t]$,

就自动得到一个鞅。这是 martingale theory 中非常核心的构造：随着信息增加，对终端变量的条件期望不断更新，但这种更新过程本身是公平的。

本讲第二个重点是 **条件 Jensen 不等式**。它不仅用于证明可积性，也解释了为什么条件期望不会放大凸风险度量。例如绝对值函数是凸函数，所以 $|\mathbb E[X\mid\mathcal G]| \le \mathbb E[|X|\mid\mathcal G]$.

这说明“先在较少信息下取平均”会降低凸意义下的波动或风险。

第三个重点是 **停时**。Def 5.5 的停时定义不是说 $\tau$ 是普通随机变量，而是要求 $\{\tau\le t\}\in\mathcal F_t$.

这表达的是“是否已经停止”必须能由当前信息判断。首次 hitting time 是停时，因为连续路径允许我们用有理时间点逼近整个区间上的达标事件。这个证明同时用到了适应性、filtration 的单调性、路径连续性和 Borel/σ-代数的可列封闭性。

Lecture 5 与后续金融定价关系很大。停时是美式期权、最优停止、barrier option、止损策略等问题的数学语言。停止过程仍为鞅是 optional stopping theorem 的基础，而 optional stopping theorem 是很多无套利定价和公平游戏结果的核心。

本讲需要优先补的地方有两处。第一处是 Prop 5.4 中列出的鞅性质只是目录，后续需要补完整定理。第二处是 Thm 5.9 的停止过程证明中断，必须回看或补教材证明。这一处非常重要，因为它是从“固定时刻的鞅性质”过渡到“随机时刻的鞅性质”的关键。

---

# Lec 1–5 空白与中断诊断报告

Lecture 1 的主要缺口是通常条件中的 **右连续性** 没有抄完整。这个缺口重要程度高，因为右连续性会影响停时和鞅的技术条件。有限样本空间上 σ-代数数量的问题也留白，但对金融随机分析主线的重要性中等，除非老师把它作为测度论小题考。

Lecture 2 的主要缺口是 **14:00 适应过程附近需要重听**。这里处在可测过程、循序可测和适应过程之间，是后面定义鞅与 stochastic integral 的基础。若这段没补清，后面容易把 “measurable”、“progressively measurable”、“adapted” 混成一类。

Lecture 3 的主要缺口是第 21 页的白板照片，涉及条件期望交换顺序和收敛性质。这个缺口重要程度高，因为条件期望的塔式性质是鞅证明的核心工具。尤其要补清：什么时候可以交换顺序，什么时候不能交换。

Lecture 4 的主要缺口是 **Brownian motion 的平方鞅和指数鞅证明**。原笔记写出结论并标注“期末”，但没有展开证明。建议单独补成两个证明模板：证明 $W_t^2-t$ 是鞅，以及证明 $\exp(\alpha W_t-\alpha^2t/2)$ 是鞅。

Lecture 5 的主要缺口是 **停止过程仍为鞅的证明**。这一点是 optional stopping theorem 的入口，必须优先补。若后续课程继续讲停时定理、美式期权或最优停止，这一处会成为承上启下的关键位置。

---

# Lec 1-5 考前压缩版公式链

概率空间与可测性：

\[
(\Omega,\mathcal F,\mathbb P),
\qquad
X:\Omega\to\mathbb R,
\qquad
X^{-1}((-\infty,x])\in\mathcal F.
\]

Borel σ-代数：

\[
\mathcal B(\mathbb R)
= \sigma\{(-\infty,x]:x\in\mathbb R\}.
\]

随机变量生成的信息：

\[
\sigma(X)=\sigma\{X^{-1}((-\infty,x]):x\in\mathbb R\}.
\]

Filtration：$\mathcal F_s\subseteq\mathcal F_t, \qquad s\le t$.

自然滤流：$\mathcal F_t^X=\sigma(X_s:s\le t)$.

适应过程：$X_t\text{ is }\mathcal F_t\text{-measurable}$.

条件期望：$Y=\mathbb E[X\mid\mathcal G]$满足

\[
Y\text{ is }\mathcal G\text{-measurable},
\qquad
\int_A Y\,d\mathbb P=\int_A X\,d\mathbb P,
\quad A\in\mathcal G.
\]

塔式性质：

\[
\mathcal G_1\subseteq\mathcal G_2
\Longrightarrow
\mathbb E[\mathbb E[X\mid\mathcal G_2]\mid\mathcal G_1]
= \mathbb E[X\mid\mathcal G_1].
\]

鞅：$\mathbb E[X_t\mid\mathcal F_s]=X_s, \qquad s\le t$.

Brownian motion：$W_0=0, \qquad W_t\sim N(0,t), \qquad W_{t+s}-W_t\sim N(0,s)$,

且具有独立增量和连续路径。

Brownian 鞅：

\[
W_t,
\qquad
W_t^2-t,
\qquad
\exp\left(\alpha W_t-\frac{\alpha^2}{2}t\right).
\]

条件期望生成鞅：

\[
X_t=\mathbb E[X\mid\mathcal F_t]
\Longrightarrow
\{X_t,\mathcal F_t\}\text{ is a martingale}.
\]

条件 Jensen：$f(\mathbb E[X\mid\mathcal G]) \le \mathbb E[f(X)\mid\mathcal G]$.

停时：

\[
\tau\text{ is a stopping time}
\Longleftrightarrow \{\tau\le t\}\in\mathcal F_t.
\]

停止过程：$X_n^\tau=X_{n\wedge\tau}$.





# Lecture 6. 停时、鞅变换、停时定理与 Doob--Meyer 分解的引入

## Part A. 课堂内容还原

### Rmk 6.1 Pre-lecture：鞅是什么

本讲一开始复习 **martingale** 的三个组成条件。设 $(\Omega,\mathcal F,\mathbb P,\{\mathcal F_t,t\in T\})$ 是带滤概率空间。一个过程 $X=\{X_t,t\in T\}$ 是鞅，直观上需要满足三层条件。第一是 **可积性**，也就是每个时刻的随机变量都有一阶矩：

\[
\mathbb E|X_t|<+\infty.
\]

第二是 **适应性**，也就是每个 $X_t$ 只能依赖当前时刻的信息 $\mathcal F_t$. 第三是 **无趋势性**。离散时间下写为

\[
\mathbb E[X_{n+1}\mid \mathcal F_n]=X_n.
\]

连续或一般指标集下，若 $s<t$, 则写为

\[
\mathbb E[X_t\mid \mathcal F_s]=X_s.
\]

这三个条件分别对应“值可积分”、“过程不预知未来”、“在当前信息下未来的最佳预测就是当前值”。金融上，鞅的无趋势性是无套利定价和风险中性测度的核心语言：在适当测度下，贴现资产价格应该没有可预测漂移。

---

### Rmk 6.2 为什么需要一致可积

课堂中特别强调：仅仅知道每个 $X_t$ 都是可积的并不够，因为这只是“逐点可积”。我们还需要某种统一控制所有时刻尾部质量的条件，这就是 **一致可积**。

课堂例子可以整理为：令

\[
X_t= \begin{cases}
t^2, & \text{with probability }1/t^2,\\
0, & \text{with probability }1-1/t^2.
\end{cases}
\]

则对每个固定的 $t$, 都有

\[
\mathbb E|X_t|=1<+\infty.
\]

所以每个单点都可积。但是对任意大的 $K$, 总能取足够大的 $t$ 使得 $t^2>K$. 此时

\[
\mathbb E\left[|X_t|\mathbf 1_{\{|X_t|>K\}}\right]=1.
\]

因此

\[
\sup_t \mathbb E\left[|X_t|\mathbf 1_{\{|X_t|>K\}}\right]
\]

不会随着 $K\to\infty$ 而趋于 $0$. 所以这族随机变量不是一致可积的。这个例子说明：**单个随机变量可积，只控制一个时刻；一致可积控制的是整个过程在所有时刻的尾部质量**。

---

### Def 6.3 一致可积

设 $\{X_t,t\in T\}$ 是一族可积随机变量。如果

\[
\lim_{K\to\infty}\sup_{t\in T} \mathbb E\left[|X_t|\mathbf 1_{\{|X_t|>K\}}\right]=0,
\]

则称 $\{X_t,t\in T\}$ 是一致可积的。

一致可积的数学作用是防止“概率很小但数值极大”的尾部质量在不同时间点逃逸。金融上，它经常用于保证极限和期望可以交换，尤其是 optional stopping、martingale convergence 和风险中性定价中的极限过程。

---

### Def 6.4 停时

设 $(\Omega,\mathcal F,\mathbb P,\{\mathcal F_t,t\in T\})$ 是带滤概率空间。映射

\[
\tau:\Omega\to T\cup\{+\infty\}
\]

称为关于 $\{\mathcal F_t\}$ 的 **停时**，如果对任意 $t\in T$, 都有

\[
\{\omega:\tau(\omega)\le t\}\in\mathcal F_t.
\]

这一定义的意思是：到时刻 $t$ 为止，我们已经能够判断停时是否发生。停时不是任意随机时间，而是不能依赖未来信息的随机时间。

课堂例子是 hitting time。若

\[
\tau=\inf\{n:X_n\ge 10,\ n\ge 0\},
\]

则 $\tau$ 表示过程第一次达到或超过阈值 $10$ 的时间。在时刻 $t$ 我们可以通过观察 $X_0,\dots,X_t$ 判断 $\tau\le t$ 是否发生，所以这是典型停时。

---

### Rmk 6.5 随机变量与停时的关系

课堂中提醒：停时本身也是一种随机变量。普通随机变量通常写成 $X:\Omega\to\mathbb R$, 并要求对任意 Borel 集 $B\in\mathcal B(\mathbb R)$, 都有 $\{\omega:X(\omega)\in B\}\in\mathcal F$. 停时则是取值在时间集合 $T\cup\{+\infty\}$ 上的随机变量，并且额外满足与 filtration 相容的条件 $\{\tau\le t\}\in\mathcal F_t$. 因此，**停时比普通随机变量多了一层信息约束**。

---

### Def 6.6 停过程

设 $X=\{X_t,t\in T\}$ 是关于 $\{\mathcal F_t,t\in T\}$ 适应的随机过程， $\tau$ 是一个停时。定义 $X^\tau=\{X_t^\tau,t\in T\}$ 为停过程，其中

\[
X_t^\tau:=X_{t\wedge\tau}.
\]

这里 $t\wedge\tau=\min\{t,\tau\}$. 也就是说，在达到 $\tau$ 之前，过程继续按原来的 $X_t$ 运行；一旦达到 $\tau$, 过程就冻结在 $X_\tau$. 金融上，停过程对应“到某个触发时间为止的交易/价格/财富过程”。例如止损策略、触发障碍的期权、首次违约时间后的现金流冻结，都是停过程思想的应用。

---

### Def 6.7 鞅差序列

设 $\{Y_n,\mathcal F_n,n\ge 0\}$ 是可积适应过程。如果对任意 $n\ge 0$ 都有

\[
\mathbb E[Y_{n+1}\mid\mathcal F_n]=0,
\]

则称 $\{Y_n,\mathcal F_n,n\ge 0\}$ 为一个 **鞅差序列**。

鞅差序列表示“下一期增量在当前信息下均值为零”。它是离散鞅的增量形式，也是很多统计估计和随机近似算法的误差结构。

---

### Thm 6.8 鞅的差是鞅差序列

若 $\{X_n,\mathcal F_n,n\ge 0\}$ 是鞅，令 $Y_0=X_0$, 并对 $n\ge 1$ 定义 $Y_n=X_n-X_{n-1}$. 则 $\{Y_n,\mathcal F_n,n\ge 0\}$ 是鞅差序列。

**Proof.** 对任意 $n\ge 0$, 有

\[
\mathbb E[Y_{n+1}\mid\mathcal F_n] = \mathbb E[X_{n+1}-X_n\mid\mathcal F_n].
\]

由于 $X_n$ 是 $\mathcal F_n$ 可测的，因此

\[
\mathbb E[X_n\mid\mathcal F_n]=X_n.
\]

又因为 $X$ 是鞅，所以

\[
\mathbb E[X_{n+1}\mid\mathcal F_n]=X_n.
\]

于是

\[
\mathbb E[Y_{n+1}\mid\mathcal F_n] = X_n-X_n=0.
\]

这说明 $Y$ 是鞅差序列。

---

### Def 6.9 可料过程

设 $\{V_n,\mathcal F_n,n\ge 0\}$ 是可积过程。如果对任意 $n\ge 0$, 都有 $V_{n+1}\ \text{is}\ \mathcal F_n\text{-measurable}$, 则称 $V$ 为 **可料过程**，也称 **predictable process**。

课堂笔记中写作

\[
\mathbb E[V_{n+1}\mid\mathcal F_n]=V_{n+1},
\]

这与 $V_{n+1}$ 关于 $\mathcal F_n$ 可测等价。

数学上，可料过程是“提前一个时刻可知”的过程。金融上，它正是交易策略的基本形式：在 $(n-1,n]$ 这个时间段持有多少资产，必须由 $n-1$ 时刻之前的信息决定，不能等到 $n$ 时刻价格变化后再决定。

---

### Def 6.10 鞅变换

设

\[
X=\{X_n,\mathcal F_n,n\ge 0\}
\]

是鞅，

\[
V=\{V_n,\mathcal F_n,n\ge 0\}
\]

是可料过程。定义

\[
Z_n = V_0X_0+\sum_{j=1}^{n}V_j(X_j-X_{j-1}).
\]

称 $Z=\{Z_n,n\ge 0\}$ 为 $X$ 关于 $V$ 的 **鞅变换**。

金融解释非常直接： $X_j-X_{j-1}$ 是资产价格或收益的增量， $V_j$ 是在该增量发生之前已经确定的持仓数量，因此

\[
\sum_{j=1}^{n}V_j(X_j-X_{j-1})
\]

就是策略累计收益。鞅变换定理说明：如果价格过程是鞅，且交易策略不预知未来，那么交易收益仍然不能产生可预测趋势。

---

### Thm 6.11 有界可料过程的鞅变换仍为鞅

设

\[
X=\{X_n,\mathcal F_n,n\ge 0\}
\]

是鞅，

\[
V=\{V_n,\mathcal F_n,n\ge 0\}
\]

是有界可料过程，即存在 $M>0$ 使得对任意 $n\ge 0$, 都有 $|V_n|\le M$. 令

\[
Z_n = V_0X_0+\sum_{j=1}^{n}V_j(X_j-X_{j-1}).
\]

则

\[
Z=\{Z_n,\mathcal F_n,n\ge 0\}
\]

仍为鞅。

**Proof.** 先证可积性。由三角不等式和 $|V_j|\le M$ 可得

\[
\mathbb E|Z_n| \le M\mathbb E|X_0| + M\sum_{j=1}^{n} \mathbb E\left(|X_j|+|X_{j-1}|\right).
\]

因为 $X$ 是鞅，所以每个 $X_j$ 都可积，于是

\[
\mathbb E|Z_n|<+\infty.
\]

再证适应性。对 $j\le n$, 有 $V_j$ 在 $\mathcal F_{j-1}$ 中可测，从而也在 $\mathcal F_j \subseteq \mathcal F_n$ 中可测；而 $X_j-X_{j-1}$ 关于 $\mathcal F_j$ 可测。因此每一项都关于 $\mathcal F_n$ 可测，所以 $Z_n$ 关于 $\mathcal F_n$ 可测。

最后证鞅性质。注意

\[
Z_{n+1}-Z_n = V_{n+1}(X_{n+1}-X_n).
\]

于是

\[
\mathbb E[Z_{n+1}-Z_n\mid\mathcal F_n] = \mathbb E[V_{n+1}(X_{n+1}-X_n)\mid\mathcal F_n].
\]

因为 $V_{n+1}$ 是 $\mathcal F_n$ 可测的，可以从条件期望中提出：

\[
\mathbb E[Z_{n+1}-Z_n\mid\mathcal F_n] = V_{n+1}\mathbb E[X_{n+1}-X_n\mid\mathcal F_n].
\]

由鞅性质，

\[
\mathbb E[X_{n+1}-X_n\mid\mathcal F_n]=0.
\]

所以

\[
\mathbb E[Z_{n+1}-Z_n\mid\mathcal F_n]=0.
\]

这等价于

\[
\mathbb E[Z_{n+1}\mid\mathcal F_n]=Z_n.
\]

因此 $Z$ 是鞅。

---

### Thm 6.12 停时定理：停下来的鞅仍为鞅

设

\[
X=\{X_n,\mathcal F_n,n\ge 0\}
\]

是离散时间鞅， $\tau$ 是关于 $\{\mathcal F_n,n\ge 0\}$ 的停时。定义停过程 $X_n^\tau=X_{n\wedge\tau}$. 则

\[
\{X_n^\tau,\mathcal F_n,n\ge 0\}
\]

仍为鞅。

**Proof.** 课堂证明的核心是把停过程写成一个鞅变换。定义

\[
V_j=\mathbf 1_{\{\tau\ge j\}}, \qquad j\ge 1,
\]

并取 $V_0=1$. 直观上， $V_j$ 表示第 $j$ 个增量 $X_j-X_{j-1}$ 是否被保留。如果 $\tau\ge j$, 说明停时尚未在 $j-1$ 之前发生，所以第 $j$ 个增量保留；如果 $\tau<j$, 说明已经停止，该增量剔除。

由于 $\tau$ 是停时，

\[
\{\tau\le j-1\}\in\mathcal F_{j-1}.
\]

因此

\[
\{\tau\ge j\} = \{\tau\le j-1\}^c \in\mathcal F_{j-1}.
\]

这说明 $V_j$ 是 $\mathcal F_{j-1}$ 可测的，所以 $V$ 是可料过程。并且 $|V_j|\le 1$, 所以它是有界可料过程。

构造鞅变换

\[
Z_n = X_0+\sum_{j=1}^{n}\mathbf 1_{\{\tau\ge j\}}(X_j-X_{j-1}).
\]

由 Thm 6.11， $Z$ 是鞅。现在验证 $Z_n=X_{n\wedge\tau}$. 若 $0\le \tau\le n$ ,

则

\[
Z_n = X_0+(X_1-X_0)+\cdots+(X_\tau-X_{\tau-1}) = X_\tau = X_{n\wedge\tau}.
\]

若 $n<\tau$, 则

\[
Z_n = X_0+(X_1-X_0)+\cdots+(X_n-X_{n-1}) = X_n = X_{n\wedge\tau}.
\]

因此 $X_n^\tau=Z_n$. 由于 $Z$ 是鞅，所以停过程 $X^\tau$ 也是鞅。

---

### Thm 6.13 Doob--Meyer 分解定理的离散时间版本

设 $\{X_n,\mathcal F_n,n\ge 0\}$ 是一个下鞅。则 $X_n$ 可以唯一分解为 $X_n=M_n+A_n$, 其中 $\{M_n,\mathcal F_n,n\ge 0\}$ 是鞅， $\{A_n,\mathcal F_n,n\ge 0\}$ 是零初值的可料增过程，即 $A_0=0$, $A_{n+1}\ge A_n$,

且 $A_{n+1}$ 关于 $\mathcal F_n$ 可测。

课堂旁注说：“把下鞅中的递增漂移项剥离以后，可以得到一个鞅。”这正是 Doob--Meyer 分解的核心思想。下鞅允许正漂移：

\[
\mathbb E[X_{n+1}\mid\mathcal F_n]\ge X_n.
\]

分解中的 $A_n$ 捕捉这部分可预测的递增漂移，而 $M_n$ 留下真正无趋势的鞅部分。

【推导中断】本讲末尾只开始写构造，完整证明在 Lecture 7 的板书中继续展开。因此这里先保留定理形式，证明放在 Lecture 7 的 Proof 7.1 中整理。

---

## Part B. 复习视角

Lecture 6 的主线是从 **鞅的定义** 走向 **鞅的操作规则**。前面几讲已经有了 filtration、adaptedness、conditional expectation 和 martingale 的定义；本讲开始回答一个更实用的问题：如果我们对鞅做“停止”“加权累积”“分解漂移”，这些操作会不会保留鞅结构？

本讲最核心的概念是 **stopping time**、**stopped process**、**martingale difference sequence**、**predictable process**、**martingale transform** 和 **Doob--Meyer decomposition**。其中 Def 6.9 的 predictable process 是金融意义最强的对象，因为它对应交易策略的非预见性。Thm 6.11 说明“非预见性交易不能把鞅价格变成有趋势的收益过程”。Thm 6.12 则说明“按停时停止鞅，仍不会制造趋势”。

本讲的公式链可以压缩为：

\[
\tau\text{ is a stopping time} \quad\Longleftrightarrow\quad \{\tau\le n\}\in\mathcal F_n.
\] $X_n^\tau=X_{n\wedge\tau}$. \[
Z_n=V_0X_0+\sum_{j=1}^{n}V_j(X_j-X_{j-1}).
\]

\[
V_j=\mathbf 1_{\{\tau\ge j\}} \quad\Longrightarrow\quad Z_n=X_{n\wedge\tau}.
\]

所以停时定理本质上是鞅变换定理的一个应用。

最容易混淆的是 **adapted** 和 **predictable**。适应过程要求 $X_n\in\mathcal F_n$, 而可料过程要求 $V_{n+1}\in\mathcal F_n$. 也就是说，adapted 是“现在可知现在”，predictable 是“上一刻已经知道下一步要用的东西”。交易策略必须是 predictable，而资产价格通常只要求 adapted。

本讲缺口主要在两个地方。第一，Def 6.9 原笔记中关于可料过程的符号略混乱，本文按标准离散时间定义补全。第二，Thm 6.13 的 Doob--Meyer 分解只在 Lec 6 中开头，完整证明接在 Lec 7 板书图片里，因此复习时应该把 Lec 6 和 Lec 7 连起来看。

---

# Lecture 7. Doob--Meyer 分解证明、鞅收敛定理与大数定律补充

## Part A. 课堂内容还原

### Proof 7.1 Doob--Meyer 分解定理的证明

本讲开头继续证明 Thm 6.13。设 $\{X_n,\mathcal F_n,n\ge 0\}$ 是下鞅。定义 $B_0=0$, 并对 $n\ge 1$ 定义

\[
B_n= \mathbb E[X_n\mid\mathcal F_{n-1}]-X_{n-1}.
\]

由于 $X$ 是下鞅，

\[
\mathbb E[X_n\mid\mathcal F_{n-1}]\ge X_{n-1},
\]

所以 $B_n\ge 0$. 并且 $\mathbb E[X_n\mid\mathcal F_{n-1}]$ 关于 $\mathcal F_{n-1}$ 可测， $X_{n-1}$ 也关于 $\mathcal F_{n-1}$ 可测，因此 $B_n$ 关于 $\mathcal F_{n-1}$ 可测。

令

\[
A_n=\sum_{i=0}^{n}B_i.
\]

则 $A_0=0$, 且 $A_n-A_{n-1}=B_n\ge 0$ .

因此 $A$ 是零初值递增过程。又因为 $A_n$ 由 $B_0,\dots,B_n$ 组成，而 $B_n$ 在 $\mathcal F_{n-1}$ 中已经可测，所以 $A$ 是可料过程。

接着定义 $M_n=X_n-A_n$. 要证 $M$ 是鞅。首先， $M_n$ 关于 $\mathcal F_n$ 可测，因为 $X_n$ 和 $A_n$ 都关于 $\mathcal F_n$ 可测。其次，板书中先证明可积性。由于 $X_n$ 可积，而

\[
A_n=\sum_{i=1}^{n}B_i,
\]

只要证明每个 $B_i$ 可积即可。由定义，

\[
\mathbb E|B_i| = \mathbb E\left|\mathbb E[X_i\mid\mathcal F_{i-1}]-X_{i-1}\right| \le \mathbb E|X_i|+\mathbb E|X_{i-1}| <+\infty.
\]

所以 $A_n$ 和 $M_n$ 都可积。

最后证明鞅性质。对 $n\ge 0$, 有

\[
\mathbb E[M_{n+1}\mid\mathcal F_n] = \mathbb E[X_{n+1}-A_{n+1}\mid\mathcal F_n].
\]

因为 $A_{n+1}=A_n+B_{n+1}$, 所以

\[
\mathbb E[M_{n+1}\mid\mathcal F_n] = \mathbb E[X_{n+1}\mid\mathcal F_n]-A_n-B_{n+1}.
\]

根据

\[
B_{n+1} = \mathbb E[X_{n+1}\mid\mathcal F_n]-X_n,
\]

得到

\[
\mathbb E[M_{n+1}\mid\mathcal F_n] = X_n-A_n = M_n.
\]

因此 $M$ 是鞅。

唯一性证明如下。若还有另一组分解

\[
X_n=\widetilde M_n+\widetilde A_n,
\]

其中 $\widetilde M$ 是鞅， $\widetilde A$ 是零初值可料增过程，则

\[
M_n-\widetilde M_n = \widetilde A_n-A_n.
\]

对 $\mathcal F_{n-1}$ 取条件期望。左边由鞅性质给出

\[
\mathbb E[M_n-\widetilde M_n\mid\mathcal F_{n-1}] = M_{n-1}-\widetilde M_{n-1}.
\]

右边因为 $A_n,\widetilde A_n$ 都是可料的，所以 $\widetilde A_n-A_n$ 关于 $\mathcal F_{n-1}$ 可测，从而

\[
\mathbb E[\widetilde A_n-A_n\mid\mathcal F_{n-1}] = \widetilde A_n-A_n.
\]

于是

\[
\widetilde A_n-A_n = M_{n-1}-\widetilde M_{n-1} = \widetilde A_{n-1}-A_{n-1}.
\]

递推得到

\[
\widetilde A_n-A_n = \widetilde A_0-A_0 = 0.
\]

所以 $A_n=\widetilde A_n$. 进一步 $M_n=\widetilde M_n$. 因此分解唯一。

---

### Rmk 7.2 条件期望在 Doob--Meyer 分解中的作用

板书中在证明旁边重新写了条件期望的定义。若 $X\in L^1(\Omega)$ 且 $\mathcal G\subseteq\mathcal F$ 是子 σ-代数，则 $\mathbb E[X\mid\mathcal G]$ 是一个 $\mathcal G$ 可测随机变量，并满足对任意 $A\in\mathcal G$, 都有

\[
\int_A \mathbb E[X\mid\mathcal G]\,d\mathbb P = \int_A X\,d\mathbb P.
\]

在 $L^2$ 情形下， $\mathbb E[X\mid\mathcal G]$ 可以理解为 $X$ 在所有 $\mathcal G$ 可测平方可积随机变量构成的闭子空间上的正交投影。板书写到“已知当前信息对 $X$ 的最佳预测”，这句话非常重要：Doob--Meyer 分解中的

\[
B_n = \mathbb E[X_n\mid\mathcal F_{n-1}]-X_{n-1}
\]

正是在用“上一时刻信息下对下一时刻的最佳预测”提取下鞅中的可预测上升部分。

---

### Thm 7.3 L1 有界鞅的收敛定理

设 $\{X_n,\mathcal F_n,n\ge 0\}$ 是一个 $L^1$ 有界鞅，即

\[
\sup_{n\ge 0}\mathbb E|X_n|<+\infty.
\]

则存在 $X_\infty\in L^1(\Omega)$ 使得

\[
X_n\xrightarrow{a.s.}X_\infty.
\]

【根据前后文补充】更标准的结论是：如果 $X$ 是 $L^1$ 有界下鞅，则 $X_n$ 几乎处处收敛到某个有限随机变量 $X_\infty$. 若还要推出 $L^1$ 收敛，则通常需要一致可积。也就是说， $L^1\text{-bounded}$ 主要给出 a.s. 收敛，而 $uniformly\ integrable$ 进一步给出 $L^1$ 收敛和条件期望表示。

---

### Thm 7.4 一致可积鞅的收敛定理

设 $\{X_n,\mathcal F_n,n\ge 0\}$ 是一致可积鞅。则存在 $X_\infty\in L^1(\Omega)$ 使得

\[
X_n\xrightarrow{a.s.}X_\infty,
\]

并且

\[
X_n\xrightarrow{L^1}X_\infty.
\]

此外，对任意 $n\ge 0$, 都有

\[
X_n=\mathbb E[X_\infty\mid\mathcal F_n].
\]

这个定理把“一致可积”与“极限可交换”联系起来。金融中，如果一个贴现价格过程是 UI martingale，那么它不仅几乎处处有极限，而且当前价格可以表示为终端 payoff 的条件期望。这是风险中性定价公式背后的数学结构。

---

### Ex 7.5 非负独立乘积鞅的极限为零

课堂给出的例子可以整理如下。设 $\{Y_i\}_{i\ge 1}$ 独立同分布，且 $Y_i\ge 0$, \[
\mathbb E[Y_i]=1,
\]

并且

\[
\mathbb P(Y_i=1)<1.
\]

令

\[
\mathcal F_n=\sigma(Y_1,\dots,Y_n),
\]

并定义

\[
X_n=\prod_{i=1}^{n}Y_i.
\]

则 $X_n$ 是非负鞅。因为

\[
\mathbb E[X_{n+1}\mid\mathcal F_n] = \mathbb E\left[X_nY_{n+1}\mid\mathcal F_n\right].
\]

由于 $X_n$ 关于 $\mathcal F_n$ 可测，而 $Y_{n+1}$ 独立于 $\mathcal F_n$, 所以

\[
\mathbb E[X_{n+1}\mid\mathcal F_n] = X_n\mathbb E[Y_{n+1}] = X_n.
\]

因此 $X$ 是鞅。由于非负鞅是下鞅，且

\[
\mathbb E[X_n]=\mathbb E[X_0]=1,
\]

所以由鞅收敛定理，

\[
X_n\xrightarrow{a.s.}X_\infty.
\]

下面证明 $X_\infty=0$. 由 Jensen 不等式和平方根函数的严格凹性，

\[
a:=\mathbb E\sqrt{Y_1}<\sqrt{\mathbb E Y_1}=1,
\]

其中严格小于来自

\[
\mathbb P(Y_1=1)<1
\]

导致 $Y_1$ 不是常数 1。

定义

\[
Z_n=\prod_{i=1}^{n}\frac{\sqrt{Y_i}}{\mathbb E\sqrt{Y_i}} = \prod_{i=1}^{n}\frac{\sqrt{Y_i}}{a}.
\]

同样可验证 $Z_n$ 是非负鞅，因此 $Z_n$ 几乎处处收敛到某个有限随机变量 $Z_\infty$. 而

\[
\sqrt{X_n} = \prod_{i=1}^{n}\sqrt{Y_i} = Z_n a^n.
\]

由于 $a^n\to 0$ 且

\[
Z_n\to Z_\infty<+\infty \quad a.s.,
\]

所以

\[
\sqrt{X_n}\xrightarrow{a.s.}0.
\]

因此

\[
X_n\xrightarrow{a.s.}0.
\]

这说明 $X_\infty=0$. ---

### Thm 7.6 强大数定律：完整定理

【根据用户要求补充】设 $\{\xi_n,n\ge 1\}$ 独立同分布，且

\[
\mathbb E|\xi_1|<+\infty.
\]

记

\[
\mu=\mathbb E[\xi_1],
\]

\[
S_n=\sum_{i=1}^{n}\xi_i.
\]

则

\[
\frac{S_n}{n}\xrightarrow{a.s.}\mu.
\]

等价地，

\[
\frac{1}{n}\sum_{i=1}^{n}(\xi_i-\mu)\xrightarrow{a.s.}0.
\]

这是最标准的 Kolmogorov 强大数定律。它说明样本均值几乎必然收敛到总体均值。

---

### Proof 7.7 强大数定律的鞅证明思路：有限二阶矩版本

【根据用户要求补充】为了模仿本课已经学过的鞅工具，这里先给出一个有限二阶矩版本的证明思路。设 $\{\xi_n,n\ge 1\}$ 独立同分布，满足

\[
\mathbb E[\xi_1]=\mu,
\]

\[
\mathbb E[(\xi_1-\mu)^2]<+\infty.
\]

令 $D_n=\xi_n-\mu$, \[
\mathcal F_n=\sigma(\xi_1,\dots,\xi_n).
\]

则 $\{D_n,\mathcal F_n,n\ge 1\}$ 是鞅差序列，因为

\[
\mathbb E[D_{n+1}\mid\mathcal F_n] = \mathbb E[\xi_{n+1}-\mu\mid\mathcal F_n] = \mathbb E[\xi_{n+1}]-\mu = 0.
\]

定义

\[
M_n=\sum_{k=1}^{n}D_k.
\]

则 $M_n$ 是鞅。要证明

\[
\frac{M_n}{n}\to 0 \quad a.s.
\]

考虑加权鞅

\[
N_n=\sum_{k=1}^{n}\frac{D_k}{k}.
\]

由于

\[
\mathbb E\left[\left(\frac{D_k}{k}\right)^2\right] = \frac{\mathbb E[D_k^2]}{k^2},
\]

且

\[
\sum_{k=1}^{\infty}\frac{\mathbb E[D_k^2]}{k^2} = \mathbb E[D_1^2]\sum_{k=1}^{\infty}\frac{1}{k^2} <+\infty,
\]

所以 $N_n$ 是 $L^2$ 有界鞅，因而收敛 a.s.。由 Kronecker 引理，

\[
\frac{1}{n}\sum_{k=1}^{n}D_k = \frac{M_n}{n} \to 0 \quad a.s.
\]

于是

\[
\frac{S_n}{n}\to\mu \quad a.s.
\]

【条件说明】这不是最一般的 Kolmogorov 强大数定律证明，因为这里额外用了有限二阶矩条件。完整的

\[
\mathbb E|\xi_1|<+\infty
\]

版本通常需要截断、Borel--Cantelli 引理和更细的独立性论证。

---

### Proof 7.8 强大数定律的指数鞅证明思路：板书风格补充

【根据板书补充】板书第 23--25 页使用了 moment generating function 和指数型鞅的思路。该证明需要一个额外条件：存在 $\delta>0$ 使得对 $|t|<\delta$ 有

\[
\psi(t):=\mathbb E[e^{t\xi_1}]<+\infty.
\]

设

\[
\mu=\mathbb E[\xi_1],
\]

\[
S_n=\sum_{i=1}^{n}\xi_i.
\]

对固定 $t$ 定义

\[
L_n(t)=\frac{e^{tS_n}}{\psi(t)^n}.
\]

由于独立同分布，

\[
\mathbb E[e^{t\xi_{n+1}}\mid\mathcal F_n] = \psi(t),
\]

所以

\[
\mathbb E[L_{n+1}(t)\mid\mathcal F_n] = \frac{e^{tS_n}}{\psi(t)^{n+1}} \mathbb E[e^{t\xi_{n+1}}\mid\mathcal F_n] = L_n(t).
\]

因此 $L_n(t)$ 是非负鞅。由非负鞅收敛定理， $L_n(t)$ 几乎处处收敛到有限随机变量。

下面证明右尾。给定 $\varepsilon>0$, 定义

\[
g(t)=\frac{e^{t(\mu+\varepsilon)}}{\psi(t)}.
\]

因为 $g(0)=1$, 且 $g'(0) = \varepsilon>0$ ,

所以存在 $t_0>0$ 使得 $g(t_0)>1$. 若某些 $n$ 满足

\[
\frac{S_n}{n}\ge \mu+\varepsilon,
\]

则

\[
L_n(t_0) = \frac{e^{t_0S_n}}{\psi(t_0)^n} \ge \left(\frac{e^{t_0(\mu+\varepsilon)}}{\psi(t_0)}\right)^n = g(t_0)^n.
\]

由于 $g(t_0)^n\to+\infty$, 而 $L_n(t_0)$ 几乎处处收敛到有限值，所以事件

\[
\left\{\frac{S_n}{n}\ge \mu+\varepsilon \text{ infinitely often}\right\}
\]

概率为 $0$. 因此

\[
\limsup_{n\to\infty}\frac{S_n}{n}\le\mu \quad a.s.
\]

对左尾用 $-t$ 重复同样证明，可得

\[
\liminf_{n\to\infty}\frac{S_n}{n}\ge\mu \quad a.s.
\]

于是

\[
\frac{S_n}{n}\to\mu \quad a.s.
\]

---

### Thm 7.9 弱大数定律：切比雪夫不等式版本

【根据用户要求补充】设 $\{\xi_n,n\ge 1\}$ 独立同分布，且

\[
\mathbb E[\xi_1]=\mu,
\]

\[
\operatorname{Var}(\xi_1)=\sigma^2<+\infty.
\]

记

\[
S_n=\sum_{i=1}^{n}\xi_i.
\]

则

\[
\frac{S_n}{n}\xrightarrow{P}\mu.
\]

**Proof.** 因为独立同分布，

\[
\mathbb E\left[\frac{S_n}{n}\right]=\mu,
\]

并且

\[
\operatorname{Var}\left(\frac{S_n}{n}\right) = \frac{1}{n^2}\sum_{i=1}^{n}\operatorname{Var}(\xi_i) = \frac{\sigma^2}{n}.
\]

由切比雪夫不等式，对任意 $\varepsilon>0$, 有

\[
\mathbb P\left(\left|\frac{S_n}{n}-\mu\right|\ge\varepsilon\right) \le \frac{\operatorname{Var}(S_n/n)}{\varepsilon^2} = \frac{\sigma^2}{n\varepsilon^2} \to 0.
\]

这就是 $S_n/n$ 依概率收敛到 $\mu$. ---

### Thm 7.10 中心极限定理

【根据用户要求补充】设 $\{\xi_n,n\ge 1\}$ 独立同分布，满足

\[
\mathbb E[\xi_1]=\mu,
\]

\[
\operatorname{Var}(\xi_1)=\sigma^2\in(0,+\infty).
\]

则

\[
\frac{\sum_{i=1}^{n}\xi_i-n\mu}{\sigma\sqrt n} \xrightarrow{d} N(0,1).
\]

等价地，

\[
\frac{\sqrt n(\bar \xi_n-\mu)}{\sigma} \xrightarrow{d} N(0,1).
\]

---

### Proof 7.11 中心极限定理的特征函数证明

【根据用户要求补充】令

\[
Y_i=\frac{\xi_i-\mu}{\sigma}.
\]

则

\[
\mathbb E[Y_i]=0,
\]

\[
\mathbb E[Y_i^2]=1.
\]

记

\[
\varphi(t)=\mathbb E[e^{itY_1}]
\]

为 $Y_1$ 的特征函数。由于 $Y_1$ 有二阶矩，特征函数在 $0$ 附近有展开

\[
\varphi(t)=1-\frac{t^2}{2}+o(t^2), \qquad t\to 0.
\]

令

\[
T_n=\frac{1}{\sqrt n}\sum_{i=1}^{n}Y_i.
\]

由独立性，

\[
\varphi_{T_n}(t) = \mathbb E[e^{itT_n}] = \prod_{i=1}^{n} \mathbb E\left[e^{itY_i/\sqrt n}\right] = \left[\varphi\left(\frac{t}{\sqrt n}\right)\right]^n.
\]

利用展开式，

\[
\varphi\left(\frac{t}{\sqrt n}\right) = 1-\frac{t^2}{2n}+o\left(\frac{1}{n}\right).
\]

于是

\[
\left[\varphi\left(\frac{t}{\sqrt n}\right)\right]^n \to e^{-t^2/2}.
\]

而 $e^{-t^2/2}$ 正是标准正态分布 $N(0,1)$ 的特征函数。由 Lévy 连续性定理，

\[
T_n\xrightarrow{d}N(0,1).
\]

因此

\[
\frac{\sum_{i=1}^{n}\xi_i-n\mu}{\sigma\sqrt n} \xrightarrow{d} N(0,1).
\]

【补充说明】如果课程还没有正式讲 Lévy 连续性定理，可以把它先记作“特征函数收敛推出分布收敛”的标准工具。

---

## Part B. 复习视角

Lecture 7 的主线是：**用条件期望拆出可预测漂移，用鞅收敛定理控制长期极限，再把这些工具应用到经典极限定理**。Doob--Meyer 分解说明下鞅可以拆成“真正无趋势的鞅部分”和“可预测递增部分”；鞅收敛定理说明在合适有界性条件下，鞅不会无限振荡；大数定律和中心极限定理则说明随机平均的长期稳定性和波动规模。

本讲最重要的逻辑连接是：

\[
\text{submartingale} \quad\Longrightarrow\quad X_n=M_n+A_n.
\]

\[
\text{nonnegative martingale} \quad\Longrightarrow\quad \text{a.s. convergence}.
\]

\[
\text{martingale difference} \quad\Longrightarrow\quad \text{law of large numbers}.
\]

\[
\text{characteristic function expansion} \quad\Longrightarrow\quad \text{central limit theorem}.
\]

这里最容易混淆的是 **强大数定律、弱大数定律、中心极限定理** 的收敛模式。强大数定律是几乎处处收敛： $\bar \xi_n\to\mu \quad a.s$. 弱大数定律是依概率收敛：

\[
\bar \xi_n\to\mu \quad in\ probability.
\]

中心极限定理不是说 $\bar \xi_n$ 收敛到正态，而是说中心化并放大

\[
\sqrt n
\]

后的误差收敛到正态：

\[
\frac{\sqrt n(\bar \xi_n-\mu)}{\sigma} \xrightarrow{d} N(0,1).
\]

本讲明显的缺失区域是 Lec 7 的板书图片中有多处被老师身体遮挡，尤其是 Doob--Meyer 分解证明中的部分可积性估计和强大数定律指数鞅证明的最后几行。因此本文对这些部分作了 **【根据前后文补充】** 和 **【根据用户要求补充】**。复习时建议优先确认三点：Doob--Meyer 中

\[
B_n=\mathbb E[X_n\mid\mathcal F_{n-1}]-X_{n-1}
\]

为什么非负且可料；指数鞅 $L_n(t)=e^{tS_n}/\psi(t)^n$ 为什么是鞅；中心极限定理中

\[
\varphi(t/\sqrt n)^n\to e^{-t^2/2}
\]

为什么成立。

---

# Lecture 8. 鞅收敛定理：上穿不等式证明

## Part A. 课堂内容还原

### Thm 8.1 鞅收敛定理

设 $\{X_n,\mathcal F_n,n\ge 0\}$ 是 $L^1$ 有界鞅，即

\[
\sup_{n\ge 0}\mathbb E|X_n|<+\infty.
\]

则存在 $X_\infty\in L^1(\Omega)$ 使得

\[
X_n\xrightarrow{a.s.}X_\infty.
\]

课堂还写了连续时间版本： $\{X_t,t\ge 0\}$ 若是 $L^1$ 有界鞅，则存在 $X_\infty\in L^1(\Omega)$ 使得

\[
X_t\xrightarrow{a.s.}X_\infty, \qquad t\to\infty.
\]

【条件提醒】连续时间版本通常需要额外的正则性条件或先在有理时间上证明，再用路径正则性扩展。原笔记没有展开连续时间版本，本文后面主要整理离散时间证明。

---

### Def 8.2 上穿次数

设 $x=(x_0,x_1,\dots,x_n,\dots)$ 是一个广义实数列，即 $x_n\in\mathbb R\cup\{+\infty,-\infty\}$. 给定两个实数 $a<b$. 如果数列先从 $a$ 以下出发，之后到达 $b$ 以上，就称它完成一次对区间 $[a,b]$ 的 **上穿**。

记 $U_n^{[a,b]}(x)$ 为数列 $x$ 到时刻 $n$ 为止上穿区间 $[a,b]$ 的次数，并记

\[
U^{[a,b]}(x) = \lim_{n\to\infty}U_n^{[a,b]}(x)
\]

为总上穿次数。

上穿次数衡量的是数列在两个水平 $a$ 和 $b$ 之间反复振荡的次数。若一个数列不收敛，就一定存在某个有理区间 $[a,b]$ 被无限上穿。

---

### Rmk 8.3 上穿过程中的可料指标

课堂证明中构造了一个指标过程 $H_k(x)$ 来表示第 $k$ 步是否处在一次上穿操作中。直观地说，当数列低于 $a$ 时开始“买入”，当数列超过 $b$ 时完成一次上穿并“卖出”。因此 $H_k(x)$ 只依赖 $x_0,\dots,x_{k-1}$, 所以如果 $x_k=X_k(\omega)$ 来自适应过程 $X_k$, 那么 $H_k(X)$ 关于 $\mathcal F_{k-1}$ 可测，是一个可料过程。

这正好把上穿次数和 Lecture 6 的鞅变换联系起来：上穿策略本质上是一个可料交易策略。

---

### Cor 8.4 上穿不等式

设 $\{X_n,\mathcal F_n,n\ge 0\}$ 是下鞅。对任意 $a<b$ 和 $n\ge 1$ ,

有 Doob 上穿不等式：

\[
(b-a)\mathbb E\left[U_n^{[a,b]}(X)\right] \le \mathbb E\left[(X_n-a)^+\right].
\]

因此，如果

\[
\sup_{n\ge 0}\mathbb E|X_n|<+\infty,
\]

则

\[
\sup_{n\ge 0}\mathbb E\left[U_n^{[a,b]}(X)\right]<+\infty.
\]

课堂板书中出现的形式是先给路径不等式，再对它取期望。其核心思想是：每完成一次从 $a$ 到 $b$ 的上穿，至少获得 $b-a$ 的增量；而这个增量可以用一个可料策略作用在下鞅增量上来控制。

---

### Proof 8.5 上穿不等式证明思路

【根据前后文补充】构造可料过程

\[
H_k=\mathbf 1_{\{\text{第 }k\text{ 步处在一次上穿交易中}\}}.
\]

也就是说，当过程已经低于 $a$ 但尚未达到 $b$ 时， $H_k=1$. 当一次上穿完成后， $H_k$ 恢复为 $0$. 由于 $H_k$ 只依赖过去信息，所以 $H_k$ 是 $\mathcal F_{k-1}$ 可测的。

考虑鞅变换型和式

\[
\sum_{k=1}^{n}H_k(X_k-X_{k-1}).
\]

路径上，每完成一次上穿至少贡献 $b-a$. 所以有路径不等式

\[
(b-a)U_n^{[a,b]}(X) \le \sum_{k=1}^{n}H_k(X_k-X_{k-1}) + (X_n-a)^+.
\]

对两边取期望。由于 $X$ 是下鞅，

\[
\mathbb E[X_k-X_{k-1}\mid\mathcal F_{k-1}]\ge 0.
\]

又因为 $H_k\ge 0$ 且 $H_k$ 关于 $\mathcal F_{k-1}$ 可测，

\[
\mathbb E[H_k(X_k-X_{k-1})] = \mathbb E\left[ H_k\mathbb E[X_k-X_{k-1}\mid\mathcal F_{k-1}] \right] \ge 0.
\]

标准整理后得到

\[
(b-a)\mathbb E[U_n^{[a,b]}(X)] \le \mathbb E[(X_n-a)^+].
\]

若

\[
\sup_n\mathbb E|X_n|<+\infty,
\]

则

\[
\mathbb E[(X_n-a)^+] \le \mathbb E|X_n|+|a| \le \sup_n\mathbb E|X_n|+|a| <+\infty.
\]

于是 $\mathbb E[U_n^{[a,b]}(X)]$ 被统一控制。

【板书无法识别】原板书中关于 telescoping 的中间路径不等式有部分符号模糊。本文采用标准 Doob 上穿不等式的证明结构补全。

---

### Cor 8.6 有限上穿次数

由上穿不等式和单调收敛定理， $U_n^{[a,b]}(X)\uparrow U^{[a,b]}(X)$, 所以

\[
\mathbb E[U^{[a,b]}(X)] = \lim_{n\to\infty}\mathbb E[U_n^{[a,b]}(X)] \le \frac{\sup_n\mathbb E|X_n|+|a|}{b-a} <+\infty.
\]

因此

\[
U^{[a,b]}(X)<+\infty \quad a.s.
\]

也就是说，对于任意固定的有理区间 $[a,b]$, 过程几乎必然只会上穿有限次。

---

### Proof 8.7 用上穿不等式证明鞅收敛定理

设 $\{X_n,\mathcal F_n,n\ge 0\}$ 是 $L^1$ 有界鞅。由于鞅既是下鞅也是上鞅，所以可用上穿不等式。

对任意有理数 $a<b$, 由 Cor 8.6，

\[
\mathbb P\left(U^{[a,b]}(X)=+\infty\right)=0.
\]

考虑事件

\[
\left\{\liminf_{n\to\infty}X_n<a<b<\limsup_{n\to\infty}X_n\right\}.
\]

在这个事件上，路径会无限次从 $a$ 以下跑到 $b$ 以上，因此

\[
U^{[a,b]}(X)=+\infty.
\]

于是

\[
\mathbb P\left( \liminf_{n\to\infty}X_n<a<b<\limsup_{n\to\infty}X_n \right) \le \mathbb P\left(U^{[a,b]}(X)=+\infty\right) = 0.
\]

如果 $X_n$ 不收敛，则存在有理数 $a<b$ 使得

\[
\liminf_{n\to\infty}X_n<a<b<\limsup_{n\to\infty}X_n.
\]

由于有理区间可数，取可数并仍为零概率事件。因此 $X_n$ 几乎处处收敛到某个扩展实值随机变量 $X_\infty$. 最后证明 $X_\infty$ 有限且可积。由 Fatou 引理，

\[
\mathbb E|X_\infty| \le \liminf_{n\to\infty}\mathbb E|X_n| \le \sup_{n\ge 0}\mathbb E|X_n| <+\infty.
\]

因此 $X_\infty\in L^1(\Omega)$. 这就证明了鞅收敛定理。

---

## Part B. 复习视角

Lecture 8 的主线是证明 Lecture 7 中使用过的 **鞅收敛定理**。它的关键不是直接证明 $X_n$ 有极限，而是先证明它不能在两个水平 $a<b$ 之间无限振荡。上穿次数 $U^{[a,b]}(X)$ 把“是否收敛”转化成“是否无限次穿越某个区间”。这一步非常漂亮，因为它把极限问题变成了一个可用鞅变换控制的路径问题。

本讲关键词是 **upcrossing**、**upcrossing inequality**、**submartingale**、**Fatou lemma** 和 **martingale convergence theorem**。其中上穿不等式是整个证明的技术核心。它和 Lecture 6 的鞅变换相连：构造一个只依赖过去的交易策略 $H_k$ ，在低于 $a$ 时买入，在高于 $b$ 时卖出；下鞅性质保证这种策略的期望收益有方向性，从而控制上穿次数。

本讲的公式链可以压缩为：

\[
(b-a)\mathbb E[U_n^{[a,b]}(X)] \le \mathbb E[(X_n-a)^+].
\]

\[
\sup_n\mathbb E|X_n|<+\infty \quad\Longrightarrow\quad \mathbb E[U^{[a,b]}(X)]<+\infty.
\]

\[
\mathbb E[U^{[a,b]}(X)]<+\infty \quad\Longrightarrow\quad U^{[a,b]}(X)<+\infty\quad a.s.
\]

\[
\text{not convergent} \quad\Longrightarrow\quad \exists a<b\in\mathbb Q,\ U^{[a,b]}(X)=+\infty.
\]

因此

\[
X_n\xrightarrow{a.s.}X_\infty.
\]

最后用 Fatou 引理得到 $X_\infty\in L^1$. 本讲最容易混淆的地方是：上穿不等式证明的是 **有限上穿次数**，不是直接证明极限存在。极限存在还需要一个逻辑转换：如果一个实数列不收敛，那么必然存在一个有理区间被无限上穿。这个“有理区间可数化”的步骤非常重要，因为它把不可数的振荡情况压缩成可数个零概率事件的并。

【复习优先级】如果时间有限，Lecture 8 至少要掌握三句话：第一，**不收敛意味着某个区间被无限上穿**；第二，**上穿次数由上穿不等式控制**；第三，**L1 有界性通过 Fatou 引理保证极限可积**。

---

# Lec 6-8 空白与中断诊断报告

本次笔记的主要缺失集中在三个位置。第一，Lecture 6 中 **Doob--Meyer 分解定理**只在手写笔记中开头，完整证明依赖 Lecture 7 的板书图片，因此需要把 Lec 6 和 Lec 7 连读。第二，Lecture 7 的板书图片存在遮挡，尤其是 Doob--Meyer 分解可积性证明、非负乘积鞅例子和强大数定律指数鞅证明的部分中间式有遮挡，本文已按前后文补齐。第三，Lecture 8 的上穿不等式中 telescoping 的路径不等式部分板书较模糊，本文采用标准证明补全。

最需要回看的具体位置是：Lec 7 板书中

\[
A_n=\sum_{i=1}^{n}B_i, \qquad M_n=X_n-A_n
\]

之后证明 $M$ 是鞅的几行；Lec 7 中 $L_n(t)=e^{tS_n}/\psi(t)^n$ 为何是非负鞅以及如何推出 $S_n/n\to\mu$ 的几行；Lec 8 中定义上穿策略 $H_k$ 和推导上穿不等式的 telescoping 部分。

---

# Lec 6-8 考前压缩版公式链

停时：

\[
\tau\text{ is a stopping time} \quad\Longleftrightarrow\quad \{\tau\le n\}\in\mathcal F_n.
\]

停过程：

\[
X_n^\tau=X_{n\wedge\tau}.
\]

鞅差序列：

\[
Y_n=X_n-X_{n-1}, \qquad \mathbb E[Y_{n+1}\mid\mathcal F_n]=0.
\]

可料过程：

\[
V_{n+1}\in\mathcal F_n.
\]

鞅变换：

\[
Z_n=V_0X_0+\sum_{j=1}^{n}V_j(X_j-X_{j-1}).
\]

停时定理的关键构造：

\[
V_j=\mathbf 1_{\{\tau\ge j\}}, \qquad Z_n=X_{n\wedge\tau}.
\]

Doob--Meyer 分解：

\[
X_n=M_n+A_n.
\]

漂移项构造：

\[
B_n=\mathbb E[X_n\mid\mathcal F_{n-1}]-X_{n-1},
\]

\[
A_n=\sum_{i=1}^{n}B_i,
\]

\[
M_n=X_n-A_n.
\]

非负乘积鞅：

\[
X_n=\prod_{i=1}^{n}Y_i, \qquad \mathbb E[Y_i]=1.
\]

指数鞅：

\[
L_n(t)=\frac{e^{tS_n}}{\psi(t)^n}, \qquad \psi(t)=\mathbb E[e^{t\xi_1}].
\]

弱大数定律：

\[
\mathbb P\left(\left|\frac{S_n}{n}-\mu\right|\ge\varepsilon\right) \le \frac{\sigma^2}{n\varepsilon^2}.
\]

中心极限定理：

\[
\frac{\sum_{i=1}^{n}\xi_i-n\mu}{\sigma\sqrt n} \xrightarrow{d} N(0,1).
\]

特征函数证明核心：

\[
\left[\varphi\left(\frac{t}{\sqrt n}\right)\right]^n \to e^{-t^2/2}.
\]

上穿不等式：

\[
(b-a)\mathbb E[U_n^{[a,b]}(X)] \le \mathbb E[(X_n-a)^+].
\]

鞅收敛定理：

\[
\sup_n\mathbb E|X_n|<+\infty \quad\Longrightarrow\quad X_n\xrightarrow{a.s.}X_\infty\in L^1.
\]




# Lecture 9. Doob 不等式、函数有界变差、Riemann--Stieltjes 积分与 Itô 积分的动机

## Part A. 课堂内容还原

### Rmk 9.1 本讲从“不等式”开始：上穿不等式与 Doob 不等式

Lec 9 开头板书写了“不等式”，下面列出两类结果：**上穿不等式** 和 **Doob 不等式**。上穿不等式已经在 Lec 8 中用于证明鞅收敛定理，其核心形式是：若 \(X=\{X_n,\mathcal F_n,n\ge 0\}\) 是下鞅，则对 \(a<b\) 有

\[
(b-a)\mathbb E[U_n^{[a,b]}(X)]
\le \mathbb E[(X_n-a)^+].
\]

这里 \(U_n^{[a,b]}(X)\) 是到时刻 \(n\) 为止路径从 \(a\) 以下穿到 \(b\) 以上的次数。它的作用是控制路径振荡。若一个过程在两个水平之间无限来回穿越，就难以收敛；上穿不等式说明在 \(L^1\) 控制下，这种无限振荡几乎不会发生。

紧接着，老师转向 **Doob maximal inequality**。它控制的对象不是上穿次数，而是路径最大值，例如 $\sup_{n\ge 0}|X_n|$. 这两类不等式的共同作用是：**把路径层面的极值或振荡，用终端变量或整体 \(L^p\) 范数控制住**。这正是鞅理论强大的地方。

---

### Thm 9.2 Doob 的 \(L\log L\) 型极大不等式

板书给出一个 \(L\log L\) 型的 Doob 不等式。设 $X=\{X_n,n\ge 0\}$ 是下鞅或非负下鞅，并满足适当的可积性条件。记 $X^*=\sup_{n\ge 0}|X_n|$. 则有形如

\[
\mathbb E[X^*]
\le \frac{e}{e-1}
\left\{
1+\sup_{n\ge 0}\mathbb E\left[|X_n|\ln^+|X_n|\right]
\right\}.
\]

其中

\[
\ln^+|a|
= \begin{cases}
0, & |a|<1,\\
\ln|a|, & |a|\ge 1.
\end{cases}
\]

【条件缺失】板书中没有完整写出该不等式的精确定理条件，例如是否要求 \(X\) 非负、是否是有限时间 \(0\le n\le N\)、以及 \(X^*\) 是否取有限上确界。本文保留课堂给出的形式，并把它理解为 Doob 极大不等式族中的 \(L\log L\) 版本。

这个结果说明：如果不一定有 \(p>1\) 阶矩，但有稍强于 \(L^1\) 的 \(L\log L\) 控制，仍然可以控制路径最大值的期望。

---

### Thm 9.3 Doob 的 \(L^p\) 极大不等式

设 $p>1, \qquad \frac{1}{p}+\frac{1}{q}=1$. 若 \(X=\{X_n,n\ge 0\}\) 是合适的鞅或非负下鞅，则板书给出的形式是

\[
\left\|\sup_{n\ge 0}\bar X_n\right\|_p
\le q\|\bar X\|_p.
\]

这里的关键是右侧范数和左侧范数不是同一个对象。板书中特别提醒“两个是有区别的，两种范数”。

对过程 $\bar X=\{X_n,n\ge 0\}$, 过程的 \(L^p\) 有界范数是

\[
\|\bar X\|_p
= \sup_{n\ge 0}\|X_n\|_p
= \sup_{n\ge 0}\left(\mathbb E|X_n|^p\right)^{1/p}.
\]

而路径最大值的 \(L^p\) 范数是

\[
\left\|\sup_{n\ge 0}|X_n|\right\|_p
= \left(\mathbb E\left[
\left(\sup_{n\ge 0}|X_n|\right)^p
\right]
\right)^{1/p}.
\]

前者是先对每个时刻取 \(L^p\) 范数，再对时间取上确界；后者是先沿着每条路径取时间上最大值，再对这个随机变量取 \(L^p\) 范数。第二个通常更强，因为它要求整条路径的最大波动也在 \(L^p\) 中可控。

在有限终端时间 \(T\) 的常见形式中，如果 \(X\) 是非负下鞅，则

\[
\left\|\sup_{0\le t\le T}X_t\right\|_p
\le \frac{p}{p-1}\|X_T\|_p.
\]

对于一般鞅，常对 $|X_t|$ 使用该不等式，因为 \(|X_t|\) 是下鞅。

---

### Ex 9.4 Doob \(L^p\) 不等式的有限时间写法

板书中给出包络过程： $\bar X=\{X_t,0\le t\le T\}$. 若 \(\bar X\) 是非负下鞅，则

\[
\mathbb E\left[
\left(\sup_{0\le t\le T}\bar X_t\right)^p
\right]
\le \left(\frac{p}{p-1}\right)^p
\mathbb E\left[|\bar X_T|^p\right].
\]

等价地，

\[
\left\|
\sup_{0\le t\le T}\bar X_t
\right\|_p
\le \frac{p}{p-1}
\|\bar X_T\|_p.
\]

这个例子承接前面的两种范数区分：Doob 不等式把“路径最大值”的 \(L^p\) 范数控制在终端值或过程整体范数之下。它后面会频繁用于证明随机积分过程的估计、鞅收敛和局部化结果。

---

### Def 9.5 有界变差函数

下面进入经典分析准备。设 $f:[a,b]\to\mathbb R$ 是一个函数。任取区间分割 $T:\quad a=x_0<x_1<\cdots<x_n=b$. 定义 \(f\) 关于该分割的变差和为

\[
V_a^b(f,T)
= \sum_{i=1}^{n}|f(x_i)-f(x_{i-1})|.
\]

若

\[
V_a^b(f)
= \sup_T V_a^b(f,T)
= \sup_T\sum_{i=1}^{n}|f(x_i)-f(x_{i-1})|
<+\infty,
\]

则称 \(f\) 是 \([a,b]\) 上的 **有界变差函数**，也称 **bounded variation function**。

有界变差的本质是：函数在整个区间内的累计上下波动总量有限。它比连续性强得多。连续函数可以无限振荡，从而没有有限变差；而有界变差函数虽然可以有跳跃，但总跳跃和总振荡必须有限。

---

### Ex 9.6 有界变差函数一定有界：反例的用意

板书中给出一个函数例子：

\[
f(x)=
\begin{cases}
1/x, & 0<x\le 1,\\
1, & x=0.
\end{cases}
\]

【根据用户补充重点说明】这个例子的用意是说明：**有界变差函数一定是有界函数**，因此像上面这样在紧区间 \([0,1]\) 上无界的函数不可能是有界变差函数。

原因是，如果 \(f\) 在 \([a,b]\) 上有界变差，则对任意 \(x\in[a,b]\)，取分割只包含 \(a\) 和 \(x\)，可以得到 $|f(x)-f(a)| \le V_a^b(f)$. 于是 $|f(x)| \le |f(a)|+V_a^b(f)$. 右侧是有限常数，所以 \(f\) 必有界。这个例子提醒我们：在讨论 Riemann--Stieltjes 积分时，不能只说函数“有定义”就够了；作为积分器或被积函数，它还需要足够强的路径正则性。

---

### Ex 9.7 单调函数是有界变差函数

若 $f$ 在 $[a,b]$ 上单调递增，则 \(f\) 是有界变差函数。对任意分割 $T:\quad a=x_0<x_1<\cdots<x_n=b$, 由于 \(f\) 单调递增， $f(x_i)-f(x_{i-1})\ge 0$. 所以

\[
\sum_{i=1}^{n}|f(x_i)-f(x_{i-1})|
= \sum_{i=1}^{n}\left(f(x_i)-f(x_{i-1})\right).
\]

右侧望远镜求和，得到

\[
\sum_{i=1}^{n}\left(f(x_i)-f(x_{i-1})\right)
= f(b)-f(a).
\]

因此 $V_a^b(f) = f(b)-f(a) <+\infty$. 单调递减情形类似，变差为 $f(a)-f(b)$. ---

### Ex 9.8 Lipschitz 函数是有界变差函数

【根据用户补充：这里修改了条件，是为了说明 Lipschitz 函数一定是有界变差函数。】

若 \(f\) 在 \([a,b]\) 上满足 Lipschitz 条件，即存在常数 $L>0$ 使得对任意 $x_1,x_2\in[a,b]$, 都有 $|f(x_2)-f(x_1)| \le L|x_2-x_1|$, 则 \(f\) 是有界变差函数。

对任意分割 $T:\quad a=x_0<x_1<\cdots<x_n=b$, 有

\[
\sum_{i=1}^{n}|f(x_i)-f(x_{i-1})|
\le \sum_{i=1}^{n}L|x_i-x_{i-1}|.
\]

由于分割点递增， $\sum_{i=1}^{n}|x_i-x_{i-1}| = b-a$. 因此 $V_a^b(f,T) \le L(b-a)$. 对所有分割取上确界，得到 $V_a^b(f) \le L(b-a) <+\infty$. 所以 \(f\) 有界变差。

---

### Ex 9.9 分段单调函数是有界变差函数

若 \(f\) 在 \([a,b]\) 上是分段单调函数，也就是说存在有限分割 $a=c_0<c_1<\cdots<c_m=b$ 使得 \(f\) 在每个小区间 $[c_{j-1},c_j]$ 上单调，则 \(f\) 在 \([a,b]\) 上有界变差。

原因是每一段上的变差有限，而有限多个有限数相加仍有限：

\[
V_a^b(f)
\le \sum_{j=1}^{m}V_{c_{j-1}}^{c_j}(f)
<+\infty.
\]

---

### Ex 9.10 导数有界推出有界变差

若 \(f\) 在 \([a,b]\) 上可微，并且存在 $L>0$ 使得 $|f'(x)|\le L, \qquad x\in[a,b]$, 则 \(f\) 是 Lipschitz 函数。由中值定理，对任意 $x_1,x_2\in[a,b]$, 存在 \(\xi\) 介于两者之间，使得 $|f(x_2)-f(x_1)| = |f'(\xi)||x_2-x_1| \le L|x_2-x_1|$. 于是由 Ex 9.8，\(f\) 是有界变差函数。

板书中特别提醒：**连续函数不一定是有界变差函数**。连续性只说明没有跳跃，不说明总振荡有限。某些高度振荡的连续函数可以在紧区间上有无限变差。

---

### Prop 9.11 有界变差函数的代数性质

若 $f,g$ 都是 \([a,b]\) 上的有界变差函数，则以下函数仍是有界变差函数： $f(x)\pm g(x)$,  $c_1f(x)+c_2g(x)$,  $f(x)g(x)$. 如果还存在常数 $\alpha>0$ 使得 $|g(x)|\ge \alpha, \qquad x\in[a,b]$, 则 $\frac{f(x)}{g(x)}$ 也是有界变差函数。

这里乘积成立的原因是，有界变差函数必有界。若 $|f|\le M_f,\qquad |g|\le M_g$, 则对任意分割有

\[
|f(x_i)g(x_i)-f(x_{i-1})g(x_{i-1})|
\le M_f|g(x_i)-g(x_{i-1})|
+
M_g|f(x_i)-f(x_{i-1})|.
\]

求和后得到有限上界。

商的情形来自 $\frac{f}{g}=f\cdot \frac{1}{g}$, 而 $|g|\ge\alpha$ 保证 $1/g$ 不会爆掉，并且 \(1/g\) 也保持有界变差。

---

### Prop 9.12 由可积函数积分得到的函数有界变差

若 $\varphi$ 在 $[a,b]$ 上可积，并且 $\int_a^b|\varphi(t)|\,dt<+\infty$, 定义 $f(t)=\int_a^t\varphi(s)\,ds$, 则 $f$ 在 $[a,b]$ 上有界变差。

因为对任意分割 $a=x_0<x_1<\cdots<x_n=b$, 有

\[
|f(x_i)-f(x_{i-1})|
= \left|
\int_{x_{i-1}}^{x_i}\varphi(s)\,ds
\right|
\le \int_{x_{i-1}}^{x_i}|\varphi(s)|\,ds.
\]

求和得到

\[
\sum_{i=1}^{n}|f(x_i)-f(x_{i-1})|
\le \int_a^b|\varphi(s)|\,ds
<+\infty.
\]

因此 $f$ 有界变差。

---

### Prop 9.13 有界变差的局部性质与变差函数

若 $f$ 在 $[a,b]$ 上有界变差，则对任意 $a<c<b$, 函数 $f$ 在 $[a,c]$ 和 $[c,b]$ 上也有界变差。

进一步，定义变差函数 $g(t)=V_a^t(f), \qquad a\le t\le b$. 则 $g$ 是单调递增函数。若 \(f\) 还具有连续性，则 \(g\) 通常也具有相应的连续性性质。

【板书无法识别】右侧板书关于 \(g(t)=V_a^t(f)\) 后续性质有遮挡，疑似在说明“若 \(f\) 连续且有界变差，则变差函数 \(g\) 也是连续的有界变差函数”。这一点需要回看原视频确认老师是否要求证明。

---

### Def 9.14 Riemann--Stieltjes 积分

设 $f,g:[a,b]\to\mathbb R$. 给定分割 $T:\quad a=x_0<x_1<\cdots<x_n=b$, 并在每个小区间 $[x_{i-1},x_i]$ 中取点 $\xi_i\in[x_{i-1},x_i]$. 考虑和式

\[
\sum_{i=1}^{n}f(\xi_i)\left(g(x_i)-g(x_{i-1})\right).
\]

记分割网格大小为 $\lambda(T)=\max_{1\le i\le n}(x_i-x_{i-1})$. 如果当 $\lambda(T)\to 0$ 时，上述和式的极限存在，并且与分割和取点方式无关，则称 $f$ 关于 $g$ 在 \([a,b]\) 上的 Riemann--Stieltjes 积分存在，记为 $\int_a^b f(x)\,dg(x)$. Riemann 积分是特殊情形。当 $g(x)=x$ 时， $dg(x)=dx$, 于是 $\int_a^b f(x)\,dg(x) = \int_a^b f(x)\,dx$. ---

### Rmk 9.15 Riemann--Stieltjes 积分与普通 Riemann 积分的关系

若 $g$ 在 $[a,b]$ 上处处可微，并且 \(g'\) 的正则性足够好，则 $\int_a^b f(x)\,dg(x)$ 可以化成普通 Riemann 积分：

\[
\int_a^b f(x)\,dg(x)
= \int_a^b f(x)g'(x)\,dx.
\]

这说明 Stieltjes 积分把“积分变量”从 $x$ 推广成了一个函数 $g(x)$. 当 $g$ 是累积分布函数或有跳跃的函数时，\(\int f\,dg\) 会自动把 \(g\) 的变化，包括跳跃，计入积分。

---

### Prop 9.16 Riemann--Stieltjes 积分的线性性质

若 $\int_a^b f_1(x)\,dg(x)$ 和 $\int_a^b f_2(x)\,dg(x)$ 都存在，则对任意常数 $c_1,c_2$, 积分

\[
\int_a^b \left(c_1f_1(x)+c_2f_2(x)\right)\,dg(x)
\]

存在，并且

\[
\int_a^b \left(c_1f_1+c_2f_2\right)\,dg
= c_1\int_a^b f_1\,dg
+
c_2\int_a^b f_2\,dg.
\]

若 $\int_a^b f(x)\,dg_1(x)$ 和 $\int_a^b f(x)\,dg_2(x)$ 都存在，则 $\int_a^b f(x)\,d(c_1g_1+c_2g_2)(x)$ 存在，并且

\[
\int_a^b f\,d(c_1g_1+c_2g_2)
= c_1\int_a^b f\,dg_1
+
c_2\int_a^b f\,dg_2.
\]

这说明 Riemann--Stieltjes 积分对被积函数和积分器都有线性结构，但存在性本身并不自动保证，需要额外条件。

---

### Ex 9.17 Riemann--Stieltjes 积分不一定存在：共同跳跃例子

板书给出例子。定义在 $[-1,1]$ 上的函数

\[
f(x)=
\begin{cases}
0, & -1\le x\le 0,\\
1, & 0<x\le 1,
\end{cases}
\]

以及

\[
g(x)=
\begin{cases}
0, & -1\le x<0,\\
1, & 0\le x\le 1.
\end{cases}
\]

这两个函数都是阶跃函数，因此都是有界变差函数。但是 $\int_{-1}^{1}f(x)\,dg(x)$ 不一定存在。

原因在于 \(g\) 在 \(0\) 处有跳跃，而 \(f\) 也在 \(0\) 附近发生跳跃。对于包含 \(0\) 的小区间，\(g\) 的增量为 $g(x_i)-g(x_{i-1})=1$. 但如果取样点 $\xi_i=0$, 则 $f(\xi_i)=0$. 如果取样点 $\xi_i>0$, 则 $f(\xi_i)=1$. 因此同一个分割下，不同取样点可能给出不同极限。积分值无法唯一确定，所以 Riemann--Stieltjes 积分不存在。

【根据用户补充重点说明】这个例子的用意是说明：**Riemann--Stieltjes 积分的存在性不是自动的，即使 \(f\) 和 \(g\) 都是有界变差函数，也可能因为共同跳跃导致积分不存在。** 这为后面引入 Itô 积分埋下伏笔：面对 Brownian motion 这样的路径，经典 Stieltjes 积分条件更不够用。

---

### Thm 9.18 Jordan 分解：有界变差函数等价于两个单调函数之差

板书右侧给出定理：函数 $f$ 在 $[a,b]$ 上有界变差，当且仅当 \(f\) 可以表示为两个单调函数之差。

更具体地说，若 $f$ 有界变差，则存在两个单调递增函数 $h_1,h_2$ 使得 $f(x)=h_1(x)-h_2(x), \qquad x\in[a,b]$. 标准构造是令 $v(x)=V_a^x(f)$, 然后定义 $h_1(x)=\frac{v(x)+f(x)}{2}$,  $h_2(x)=\frac{v(x)-f(x)}{2}$. 

可以证明 \(h_1,h_2\) 都是单调递增函数，并且 $h_1(x)-h_2(x)=f(x)$. 反过来，如果 $f=h_1-h_2$ 且 \(h_1,h_2\) 单调递增，则 $V_a^b(f) \le V_a^b(h_1)+V_a^b(h_2) = h_1(b)-h_1(a)+h_2(b)-h_2(a) <+\infty$. 所以 \(f\) 有界变差。

---

### Rmk 9.19 为什么这里要讲 Riemann 与 Stieltjes 积分

【根据用户补充重点说明】这一段经典分析不是偏题，而是为了引入 Brownian motion 的积分。

我们最终想定义类似 $\int_0^T H_s(\omega)\,dW_s(\omega)$ 这样的对象。若把 \(\omega\) 固定，\(s\mapsto W_s(\omega)\) 是一条 Brownian path。自然想法是把它看成 Riemann--Stieltjes 积分： $\int_0^T H_s(\omega)\,dW_s(\omega)$. 但是 Brownian path 几乎处处连续、处处不可微，而且不是有界变差函数。因此经典 Riemann--Stieltjes 积分无法直接适用。Itô 积分的引入，正是为了解决“积分器是 Brownian motion”时经典积分理论失效的问题。

---

### Rmk 9.20 随机过程、随机变量与适应性的提醒

板书和用户补充中特别强调：随机过程关于 σ-代数流应写成 **适应过程**，不要把随机过程和随机变量混淆。

一个随机变量是单个映射 $X:\Omega\to\mathbb R$. 一个随机过程是一族随机变量 $H=\{H_t,0\le t\le T\}$. 如果它关于 Brownian filtration $\mathcal F_t=\sigma(W_s,s\le t)$ 适应，则意思是对每个 $t$, 都有 $H_t\ \text{is}\ \mathcal F_t\text{-measurable}$. 这表示 \(H_t\) 只能依赖到 \(t\) 为止的 Brownian 历史，不能使用未来的 \(W_{t+h}\)。在 Itô 积分中，这一点非常关键，因为被积过程 \(H_t\) 必须是非预见的。如果允许 \(H_t\) 预知未来，随机积分就会失去鞅性质，也会破坏金融上的无套利解释。

---

## Part B. 复习视角

Lecture 9 的主线可以概括为两段。第一段是从 **Doob 不等式** 继续巩固鞅路径控制工具；第二段突然转向 **有界变差函数和 Riemann--Stieltjes 积分**，看似换了主题，其实是在为 Itô 积分铺路。

本讲最关键的转折点是：如果我们想定义 $\int_0^T H_s\,dW_s$, 按照经典积分直觉，会先想到 Riemann--Stieltjes 积分。但经典 Stieltjes 积分通常依赖积分器 \(g\) 的有界变差性质；而 Brownian motion 的路径虽然连续，却几乎处处不是有界变差函数。因此必须建立新的积分理论，也就是 Lecture 10 开始构造的 Itô integral。

本讲最容易考的内容有两类。第一类是 **Doob 不等式的范数区别**：要分清 $\left\|\sup_n |X_n|\right\|_p$ 和 $\sup_n\|X_n\|_p$. 第二类是 **有界变差函数的判定和性质**，比如单调函数、Lipschitz 函数、导数有界函数、分段单调函数为什么是有界变差函数。第三类是 **Riemann--Stieltjes 积分不存在的例子**，要能说出“共同跳跃导致取样点影响极限”这个核心机制。

本讲需要回看或确认的地方主要有两处。第一，\(L\log L\) 型 Doob 不等式的完整条件没有在板书中写清，复习时如果老师要求严格陈述，需要补教材。第二，Prop 9.13 中变差函数 \(g(t)=V_a^t(f)\) 的后续性质右侧板书不够清楚，需要回看是否讲了连续性或 Jordan 分解的细节。

---

# Lecture 10. Itô 积分的构造：简单过程、均值为零、Itô 等距与平方可积鞅

## Part A. 课堂内容还原

本讲继续 Lec 9 末尾的 Stieltjes 积分动机。设 $W=\{W_t,t\ge 0\}$ 是标准 Brownian motion。我们想定义 $\int_0^T H_t\,dW_t$. 但是对几乎每条 Brownian path， $t\mapsto W_t(\omega)$ 在 $[0,T]$ 上连续、处处不可微，并且不是有界变差函数。因此经典 Riemann--Stieltjes 或 Lebesgue--Stieltjes 路径积分不能直接定义这个积分。Itô 积分的策略是：**先定义简单过程的积分，再用 \(L^2\) 极限推广到一般平方可积适应过程**。

---

### Def 10.1 Itô 积分的被积过程空间 \(L_T^2\)

设 $\mathcal F_t=\sigma(W_s,s\le t), \qquad 0\le t\le T$. 若过程 $H=\{H_t,0\le t\le T\}$ 满足以下条件，则称 \(H\) 属于 Itô 积分的平方可积过程空间，记作 $H\in L_T^2$. 首先，\(H\) 关于 Brownian filtration 适应，即对任意 $0\le t\le T$, 都有 $H_t\ \text{is}\ \mathcal F_t\text{-measurable}$. 其次，\(H\) 满足平方可积范数控制：

\[
\mathbb E\left[\int_0^T H_s^2\,ds\right]<+\infty.
\]

这里的第一条是信息条件，保证 \(H_t\) 不预知未来；第二条是大小条件，保证积分在 \(L^2\) 中有意义。

【根据用户补充提醒】这里不能写成“随机过程关于 σ-代数是随机变量”。准确说法是：**随机过程 \(H=\{H_t\}\) 关于 σ-代数流 \(\{\mathcal F_t\}\) 适应**，也就是每个 \(H_t\) 是对应 \(\mathcal F_t\)-可测的随机变量。

---

### Def 10.2 简单过程

先从简单过程开始。若 $H\in L_T^2$, 并且存在分割 $0=t_0<t_1<\cdots<t_n=T$ 以及随机变量 $H(t_{k-1}), \qquad k=1,\dots,n$, 使得对 $t_{k-1}<t\le t_k$, 有 $H(t)=H(t_{k-1})$, 并且 $H(t_{k-1})$ 关于 $\mathcal F_{t_{k-1}}$ 可测，则称 \(H\) 是简单过程。

这完全类比实变函数中的简单函数，但多了一个非常重要的信息约束：每段上的常数不是普通常数，而是随机变量，并且必须在该段开始时刻已经可知。这个“左端点可测”就是 Itô 积分的非预见性。

---

### Def 10.3 简单过程的 Itô 积分

若 $H$ 是如 Def 10.2 的简单过程，则定义

\[
\int_0^T H_s\,dW_s
= \sum_{k=1}^{n}
H(t_{k-1})
\left(W_{t_k}-W_{t_{k-1}}\right).
\]

这个定义非常关键。它使用左端点 $H(t_{k-1})$ 乘以未来 Brownian 增量 $W_{t_k}-W_{t_{k-1}}$. 因为 $H(t_{k-1})$ 在 $\mathcal F_{t_{k-1}}$ 中已经可知，而 Brownian 增量独立于过去且均值为零，所以后面能得到积分期望为零和鞅性质。

---

### Prop 10.4 简单过程 Itô 积分的均值为零

若 $H$ 是简单过程，则 $\mathbb E\left[\int_0^T H_s\,dW_s\right]=0$. **Proof.** 根据定义，

\[
\mathbb E\left[\int_0^T H_s\,dW_s\right]
= \mathbb E\left[
\sum_{k=1}^{n}
H(t_{k-1})
\left(W_{t_k}-W_{t_{k-1}}\right)
\right].
\]

交换有限求和与期望，

\[
= \sum_{k=1}^{n}
\mathbb E\left[
H(t_{k-1})
\left(W_{t_k}-W_{t_{k-1}}\right)
\right].
\]

对 $\mathcal F_{t_{k-1}}$ 取条件期望：

\[
\mathbb E\left[
H(t_{k-1})
\left(W_{t_k}-W_{t_{k-1}}\right)
\right]
= \mathbb E\left[
\mathbb E\left[
H(t_{k-1})
\left(W_{t_k}-W_{t_{k-1}}\right)
\mid
\mathcal F_{t_{k-1}}
\right]
\right].
\]

由于 $H(t_{k-1})$ 是 $\mathcal F_{t_{k-1}}$ 可测的，可以提出：

\[
= \mathbb E\left[
H(t_{k-1})
\mathbb E\left[
W_{t_k}-W_{t_{k-1}}
\mid
\mathcal F_{t_{k-1}}
\right]
\right].
\]

Brownian motion 的独立增量和零均值给出

\[
\mathbb E\left[
W_{t_k}-W_{t_{k-1}}
\mid
\mathcal F_{t_{k-1}}
\right]=0.
\]

因此每一项都是零，所以 $\mathbb E\left[\int_0^T H_s\,dW_s\right]=0$. ---

### Thm 10.5 Itô 等距：简单过程情形

若 $H$ 是简单过程，则 $\int_0^T H_s\,dW_s\in L^2(\Omega)$, 并且满足 **Itô isometry**

\[
\mathbb E\left[
\left(\int_0^T H_s\,dW_s
\right)^2
\right]
= \mathbb E\left[
\int_0^T H_s^2\,ds
\right].
\]

**Proof.** 由定义，

\[
\int_0^T H_s\,dW_s
= \sum_{k=1}^{n}
H(t_{k-1})
\left(W_{t_k}-W_{t_{k-1}}\right).
\]

平方后分成对角项和交叉项：

\[
\mathbb E\left[
\left(\sum_{k=1}^{n}
H(t_{k-1})
\Delta W_k
\right)^2
\right]
= I+II,
\]

其中 $\Delta W_k=W_{t_k}-W_{t_{k-1}}$, \[
I=
\sum_{k=1}^{n}
\mathbb E\left[
H(t_{k-1})^2(\Delta W_k)^2
\right],
\]

\[
II=
2\sum_{1\le i<j\le n}
\mathbb E\left[
H(t_{i-1})\Delta W_i
H(t_{j-1})\Delta W_j
\right].
\]

先看交叉项。对 $\mathcal F_{t_{j-1}}$ 取条件期望。由于 \(i<j\)，前面的因子 $H(t_{i-1})\Delta W_iH(t_{j-1})$ 关于 $\mathcal F_{t_{j-1}}$ 可测，而

\[
\mathbb E[\Delta W_j\mid\mathcal F_{t_{j-1}}]=0,
\]

所以每个交叉项为零。因此 $II=0$. 再看对角项。由于 $H(t_{k-1})$ 关于 $\mathcal F_{t_{k-1}}$ 可测，而 $\Delta W_k$ 独立于 $\mathcal F_{t_{k-1}}$, 并且 $\mathbb E[(\Delta W_k)^2] = t_k-t_{k-1}$, 所以

\[
\mathbb E\left[
H(t_{k-1})^2(\Delta W_k)^2
\right]
= \mathbb E\left[
H(t_{k-1})^2(t_k-t_{k-1})
\right].
\]

于是

\[
I=
\sum_{k=1}^{n}
\mathbb E\left[
H(t_{k-1})^2(t_k-t_{k-1})
\right].
\]

因为 \(H\) 在每个区间 $(t_{k-1},t_k]$ 上等于 $H(t_{k-1})$, 所以

\[
\sum_{k=1}^{n}
H(t_{k-1})^2(t_k-t_{k-1})
= \int_0^T H_s^2\,ds.
\]

取期望得到

\[
\mathbb E\left[
\left(\int_0^T H_s\,dW_s
\right)^2
\right]
= \mathbb E\left[
\int_0^T H_s^2\,ds
\right].
\]

这就是 Itô 等距。

---

### Thm 10.6 简单过程积分过程是平方可积鞅

设 $H$ 是简单过程。定义 $I_t=\int_0^t H_s\,dW_s, \qquad 0\le t\le T$. 则 $\{I_t,\mathcal F_t,0\le t\le T\}$ 是平方可积鞅。

**Proof.** 首先，由 Prop 10.4， $\mathbb E[I_t]=0$. 由 Thm 10.5，

\[
\mathbb E[I_t^2]
= \mathbb E\left[\int_0^t H_s^2\,ds\right]
<+\infty.
\]

所以 $I_t\in L^2(\Omega)$. 由 Cauchy--Schwarz 不等式，

\[
\mathbb E|I_t|
= \mathbb E[|I_t|\cdot 1]
\le \left(\mathbb E[I_t^2]\right)^{1/2}
\left(\mathbb E[1^2]\right)^{1/2}
<+\infty.
\]

因此 \(I_t\) 可积。

其次，\(I_t\) 关于 $\mathcal F_t$ 可测，因为它由 \(t\) 之前的 \(H\) 和 \(W\) 增量构成。因此 \(I\) 是适应过程。

最后证明鞅性质。取 $0\le s<t\le T$. 写成

\[
I_t
= \int_0^t H_r\,dW_r
= \int_0^s H_r\,dW_r
+
\int_s^t H_r\,dW_r.
\]

也就是 $I_t=I_s+\int_s^t H_r\,dW_r$. 对 $\mathcal F_s$ 取条件期望：

\[
\mathbb E[I_t\mid\mathcal F_s]
= I_s
+
\mathbb E\left[
\int_s^t H_r\,dW_r
\mid
\mathcal F_s
\right].
\]

由于 \(\int_s^t H_r\,dW_r\) 是由 \(s\) 之后的 Brownian 增量构成，并且每段的系数在对应左端点已经可知，利用 Brownian 独立增量和零均值可得

\[
\mathbb E\left[
\int_s^t H_r\,dW_r
\mid
\mathcal F_s
\right]=0.
\]

因此 $\mathbb E[I_t\mid\mathcal F_s]=I_s$. 所以 \(I\) 是鞅。

---

### Def 10.7 \(L_T^2\) 上的范数

在被积过程空间上定义范数

\[
\|H\|_{L_T^2}
= \left(\mathbb E\left[
\int_0^T H_s^2\,ds
\right]
\right)^{1/2}.
\]

在该范数下， $L_T^2$ 是一个 Banach 空间，即完备赋范空间。

这个范数不是单个随机变量的 \(L^2(\Omega)\) 范数，而是先沿时间积分，再对概率取期望。它正好与 Itô 等距对应：

\[
\left\|
\int_0^T H_s\,dW_s
\right\|_{L^2(\Omega)}
= \|H\|_{L_T^2}.
\]

---

### Thm 10.8 简单过程在 \(L_T^2\) 中稠密

简单过程在 $L_T^2$ 中稠密。也就是说，对任意 $H\in L_T^2$, 存在一列简单过程 $H^{(n)}$ 使得

\[
\mathbb E\left[
\int_0^T
\left|H_s^{(n)}-H_s\right|^2\,ds
\right]
\to 0.
\]

也可以写成 $\|H^{(n)}-H\|_{L_T^2}\to 0$. 这一步类似实变函数中“简单函数在 \(L^p\) 空间中稠密”。它的作用是：先把 Itô 积分定义在简单过程上，再用简单过程逼近一般平方可积适应过程。

---

### Def 10.9 一般 \(L_T^2\) 过程的 Itô 积分

设 $H\in L_T^2$. 由 Thm 10.8，取简单过程列 $H^{(n)}$ 使得 $\|H^{(n)}-H\|_{L_T^2}\to 0$. 对每个简单过程， $\int_0^T H_s^{(n)}\,dW_s$ 已经定义。由 Itô 等距，

\[
\mathbb E\left[
\left(\int_0^T H_s^{(n)}\,dW_s - \int_0^T H_s^{(m)}\,dW_s
\right)^2
\right] = \mathbb E\left[
\int_0^T
\left(H_s^{(n)}-H_s^{(m)}\right)^2\,ds
\right].
\]

因为 $H^{(n)}$ 在 $L_T^2$ 中收敛，所以右侧趋于 $0$. 

因此 
\[
\left\{ \int_0^T H_s^{(n)}\,dW_s \right\}
\]
是 $L^2(\Omega)$ 中的 Cauchy 列。由于 $L^2(\Omega)$ 完备，存在随机变量 $Y\in L^2(\Omega)$ 使得



\[
\int_0^T H_s^{(n)}\,dW_s
\to Y
\quad\text{in }L^2(\Omega).
\]

定义 $\int_0^T H_s\,dW_s = Y$. 这就是一般平方可积适应过程的 Itô 积分。

【推导中断】PDF 第 32 页停在“存在随机变量 \(Y\in L^2\)”附近，后续“定义积分为极限”没有完整写完。这里按标准构造补全。

---

## Part B. 复习视角

Lecture 10 的主线非常清楚：**由于 Brownian motion 的路径不是有界变差函数，经典 Stieltjes 积分失效，所以要从概率空间和 \(L^2\) 极限角度重新定义积分。**

Itô 积分不是逐条路径先定义的 Riemann--Stieltjes 积分。它的构造路线是：

\[
\text{simple adapted process}
\quad\Longrightarrow\quad \int H\,dW\text{ by finite sums}
\quad\Longrightarrow\quad \text{Itô isometry}
\quad\Longrightarrow\quad L^2\text{ extension}.
\]

最核心的公式是简单过程积分定义：

\[
\int_0^T H_s\,dW_s
= \sum_{k=1}^{n}
H(t_{k-1})(W_{t_k}-W_{t_{k-1}}).
\]

这里必须使用左端点，因为左端点可测性保证被积过程不预知未来。紧接着，Itô 等距是整个构造的核心：

\[
\mathbb E\left[
\left(\int_0^T H_s\,dW_s
\right)^2
\right]
= \mathbb E\left[
\int_0^T H_s^2\,ds
\right].
\]

这个等距说明 Itô 积分是从 \(L_T^2\) 到 \(L^2(\Omega)\) 的连续线性映射，所以可以由简单过程稠密性推广到一般 \(H\in L_T^2\)。

本讲最容易混淆的是 **Itô 积分不是普通路径积分**。虽然写成 $\int_0^T H_s(\omega)\,dW_s(\omega)$, 但定义不是固定 \(\omega\) 后逐路径做 Stieltjes 积分，而是通过平方均值极限定义的随机变量。Brownian path 的非有界变差性正是迫使我们这样做的原因。

考试可能会问三个层次。第一个层次是定义：什么是 \(L_T^2\)？什么是简单过程？简单过程的 Itô 积分怎么定义？第二个层次是性质证明：为什么积分期望为零？为什么满足 Itô 等距？为什么积分过程是鞅？第三个层次是构造逻辑：为什么可以从简单过程推广到一般 \(L_T^2\) 过程？答案要引用 **简单过程稠密性** 和 **Itô 等距**。

---

# Lec 9-10 空白与中断诊断报告

本次文件中 Lec 9 是按时间顺序截取的黑板板书，其中第 1--2 页重复，整理时已合并。第 3、5、6 页关于 Doob 不等式和两种范数有重复内容，本文合并为 Thm 9.2、Thm 9.3 和 Rmk 9.4。

Lec 9 的主要不清楚位置有三处。第一，\(L\log L\) 型 Doob 不等式的完整适用条件没有完全出现在板书中，本文用 **【条件缺失】** 标记。第二，变差函数 \(g(t)=V_a^t(f)\) 后面的连续性性质右侧板书不清，本文用 **【板书无法识别】** 标记。第三，Riemann--Stieltjes 积分性质中关于分段区间存在性的右侧板书较模糊，本文只保留了确定的线性性质和共同跳跃反例。

Lec 10 的主要中断在第 32 页：从简单过程推广到一般 \(H\in L_T^2\) 时，原笔记停在“存在随机变量 \(Y\in L^2\)”附近，没有完整写出“定义 \(\int H\,dW\) 为该 \(L^2\) 极限”。本文已按标准 Itô 积分构造补全，并标记 **【推导中断】**。

最需要优先回看的位置是 Lec 9 的 Doob \(L\log L\) 不等式条件、Lec 9 中 Jordan 分解附近的板书右侧，以及 Lec 10 最后一页中从 Cauchy 列到一般 Itô 积分定义的收尾。

---

# Lec 9-10 考前压缩版公式链

Doob \(L^p\) 极大不等式：

\[
\left\|\sup_{0\le t\le T}X_t\right\|_p
\le \frac{p}{p-1}\|X_T\|_p.
\]

过程范数与路径最大范数：

\[
\|\bar X\|_p
= \sup_n(\mathbb E|X_n|^p)^{1/p},
\]

\[
\left\|\sup_n|X_n|\right\|_p
= \left(\mathbb E[(\sup_n|X_n|)^p]
\right)^{1/p}.
\]

有界变差：

\[
V_a^b(f)
= \sup_T\sum_{i=1}^{n}|f(x_i)-f(x_{i-1})|.
\]

Lipschitz 推出有界变差： $|f(x)-f(y)|\le L|x-y| \quad\Longrightarrow\quad V_a^b(f)\le L(b-a)$. Riemann--Stieltjes 积分：

\[
\int_a^b f(x)\,dg(x)
= \lim_{\lambda(T)\to0}
\sum_{i=1}^{n}
f(\xi_i)(g(x_i)-g(x_{i-1})).
\]

若 \(g\) 可微：

\[
\int_a^b f(x)\,dg(x)
= \int_a^b f(x)g'(x)\,dx.
\]

Jordan 分解： $f\in BV[a,b] \quad\Longleftrightarrow\quad f=h_1-h_2$, 其中 \(h_1,h_2\) 单调递增。

Brownian path 的困难： $W_t(\omega)\text{ continuous but not of bounded variation}$. Itô 被积过程空间：

\[
H\in L_T^2
\quad\Longleftrightarrow\quad H_t\in\mathcal F_t,\quad
\mathbb E\left[\int_0^T H_s^2\,ds\right]<+\infty.
\]

简单过程积分：

\[
\int_0^T H_s\,dW_s
= \sum_{k=1}^{n}
H(t_{k-1})(W_{t_k}-W_{t_{k-1}}).
\]

均值为零： $\mathbb E\left[\int_0^T H_s\,dW_s\right]=0$. Itô 等距：

\[
\mathbb E\left[
\left(\int_0^T H_s\,dW_s
\right)^2
\right]
= \mathbb E\left[
\int_0^T H_s^2\,ds
\right].
\]

积分过程是鞅：

\[
I_t=\int_0^t H_s\,dW_s,
\qquad
\mathbb E[I_t\mid\mathcal F_s]=I_s.
\]

一般 \(L_T^2\) 过程的定义：

\[
H^{(n)}\to H\text{ in }L_T^2
\quad\Longrightarrow\quad \int_0^T H_s^{(n)}\,dW_s
\to
\int_0^T H_s\,dW_s
\text{ in }L^2(\Omega).
\]
