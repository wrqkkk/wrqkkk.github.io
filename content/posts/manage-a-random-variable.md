+++
date = '2026-07-11T23:59:00+08:00'
draft = false
title = 'Manage a long-term project like a random variable but do not expecting a uniform distribution'
isCJKLanguage = true
math = true
+++


Chatgpt 5.6 just released a few days ago and it has helped me probe much deeper into my initial idea. Thanks a lot. And it provided me with several high-quality references and conceptual tools that gave the idea a much more rigorous foundation, including principled methods for structuring the framework, as well as serious academic work that shares similar understanding and focus, and more importantly, that has been applied in various domains. 

It also helped connect these vague ideas and observations with concepts from statistics, mathematics and other fields I've encountered inm my previous studies and experience. Such connections made both the abstract framework and its detailed mechanisms richer, more precise and more strongly grounded in existing theory.

I really appreciate it.


I'll take its advice to name this project, in the first version, as

> 《Personal Adaptive Action System: An N-of-1 Framework for Latent-State-Aware, Stochastic, and Goal-Constrained Decision Making》





# PART I — Personal Adaptive Action System: Conceptual Model, Mathematical Specification, and Experimental Protocol


## 1.1 Problem Statement

长期复杂项目需要确定性产出，但个体的注意力、兴趣、认知能量和行动欲望存在波动。要求每天均匀推进多个项目可能产生过高的认知切换成本与，personally，某种逆反心理；而完全依赖状态和兴趣去实时给出一份更高效的安排——像一种目标不稳定的贪心算法，长期表现堪忧之外，还可能会带来错误的反馈，让我们的“精心安排”适得其反——例如因为时间紧张而飞速完成的经历给大脑正反馈和可以短时间内完成的暗示，长此以往就会把踩点赶工的行为模式固化；再例如天然喜欢节省能量的大脑会给出更加“偷懒”的倾向，形成即时满足的回路，一味的让步会让需要花费大量能量的任务的执行变得困难，进而影响这些任务指向的更加重要和远大的目标。

这些错误反馈可能导致重要项目出现长时间停滞，重启任务的门槛高、消耗大。为了减少执行上的熵增，我们通常会采用一些稳定行为的策略，例如通过养成习惯维持长期的产出，这对于一些只需要“肌肉记忆”的任务而言并不困难，例如每天刷牙以维护口腔健康。但对于高耗能的大项目来说，传统的连续打卡和固定日程进一步存在 Goodhart 定律风险，因为代理指标可能逐渐替代真正目标，最终导致执行重心发生偏移，反而妨害目标的实现。

因此，我们需要设计一种允许短期随机性、状态依赖性与兴趣节律存在，同时对长期产出、极端停滞和资源分配施加约束的动态行动系统。


## 1.2 Definition and Notation

### Projects and decision times

设项目集合为

\[
\mathcal I.
\]

其中，\(i \in \mathcal I\) 表示某一个具体项目。

使用 \(t\) 表示决策时刻。这里暂不强制规定 \(t\) 必须对应一天。它可以代表一天、一个工作 session，或者任何发生行动选择的决策节点。

---

### Execution dose

定义

\[
x_{i,t} \geq 0
\]

为在时刻 \(t\) 对项目 \(i\) 的执行剂量，记为 execution dose。

当

\[
x_{i,t}=0
\]

时，表示项目 \(i\) 在时刻 \(t\) 未被执行。

当

\[
x_{i,t}>0
\]

时，表示项目 \(i\) 在时刻 \(t\) 获得了一定程度的执行。

第一版中，\(x_{i,t}\) 可以暂时理解为有效投入时间。未来也可以将其扩展为结合时间、注意力投入和实际产出的综合执行强度。

---

### Effective activation

定义有效激活指标

\[
z_{i,t}
= \mathbf 1_\{\text{project } i \text{ is effectively activated at time } t\}.
\]

其中，

\[
z_{i,t}
= \begin{cases}
1, & \text{项目 } i \text{ 在时刻 } t \text{ 被有效激活},\\
0, & \text{否则}.
\end{cases}
\]

“有效激活”的具体测量标准将在后续 measurement protocol 中定义.

---

### Continuous inactivity gap

定义

\[
g_{i,t}
\]

为项目 \(i\) 在时刻 \(t\) 的连续未激活时间，即 continuous inactivity gap。

直观上，\(g_{i,t}\) 表示从项目 \(i\) 上一次有效激活开始，到当前时刻 \(t\) 已经过了多久。

未来可以进一步形式化定义为

\[
g_{i,t}
= t-\tau_i(t),
\]

其中

\[
\tau_i(t) = \max\{u\leq t:z_{i,u}=1\}
\]

表示项目 \(i\) 在时刻 \(t\) 之前最近一次有效激活发生的时刻。

---

### Execution continuity

定义

\[
\kappa_{i,t}\in[0,1]
\]

为项目 \(i\) 在时刻 \(t\) 的执行连续性指标，记为 execution continuity。

较大的 \(\kappa_{i,t}\) 表示项目仍然处于较高的行动与认知连续状态。

较小的 \(\kappa_{i,t}\) 表示项目正在逐渐脱离当前活跃的认知和行动空间。

第一版可以考虑以下候选形式：

\[
\kappa_{i,t} = e^{-\lambda_i g_{i,t}},
\]

其中

\[
\lambda_i>0
\]

表示项目 \(i\) 的连续性衰减率。

因此，

\[
g_{i,t}=0
\quad\Longrightarrow\quad
\kappa_{i,t}=1,
\]

并且随着连续未激活时间增加，

\[
g_{i,t}\uparrow
\quad\Longrightarrow\quad
\kappa_{i,t}\downarrow.
\]

指数衰减形式目前只是一个候选建模假设，不是已经验证的人类认知规律，待确认。

---

### Long-term importance

定义

\[
M_i
\]

为项目 \(i\) 的长期重要性。

\(M_i\) 描述项目对于长期目标、个人价值、研究发展、职业发展或其他远期结果的重要程度。

项目的重要性本身并不直接等于一次具体执行行为产生的收益。项目必须通过真实推进才能将长期重要性转化为实际价值。

（具体是什么形式还需要讨论，后期或许需要升级为  \(M_{i,t}\) ）

---

### Project progress

定义
\[
\Delta P_{i,t}(x) = P_{i,t+1}(x)-P_{i,t+1}(0).
\]

为在时刻 \(t\) 以执行剂量 \(x\) 推进项目 \(i\) 所产生的实际项目进展。

---

### Long-term benefit

因此，基于长期重要性和项目进展，长期重要性带来的收益可以通过

\[
M_i\Delta P_{i,t}(x)
\]

体现。

> 由于一个项目从 0% 到 10% 和从 90% 推进到 100% 的意义可能并不相同，对习惯的贡献可能也不甚相同。甚至，部分项目属于“无限游戏”，我们可能会使用日常执行的维护情况来作为项目完成情况的度量，例如将稳定在每周3次，每月12次为100%的标准，我们还会存在保持于某个恒定值 100% 但没有 Progress 的情况，因此后期或许需要引入其他函数形式来衡量收益，如：
> \[ V_i\left(M_i,\Delta P_{i,t}(x)\right) \]

---

### Avoided delay loss

定义

\[
D_{i,t}(x)
\]

为在时刻 \(t\) 以执行剂量 \(x\) 推进项目 \(i\) 所避免的延迟损失，记为 avoided delay loss。

该变量用于表达通常所说的“紧急性”。

与直接使用一个 urgency score 不同，\(D_{i,t}(x)\) 关注的是：

如果当前不执行该项目，相对于当前执行，将额外产生多大的未来损失。

因此，项目的长期重要性 \(M_i\) 与当前行动的延迟损失 \(D_{i,t}(x)\) 是两个不同概念。

（这里的损失要怎么衡量还是个问题，未来我们要看多个维度，比如延迟一小时/延迟一天/延迟三天/延迟一周等等带来的损失应该是不一样的，延迟也不一定之后会执行，所以除了延迟做以后，记忆衰退带来的效率降低，我们达到同样的工作量=效率乘以时间，会因为效率降低而增加时间成本，同时心理成本也会有，启动门槛变高。也有一个风险是未来我们预期的这个时间点我们并没有做，有更高的风险）



### Short-term state improvement

定义

\[
S_{i,t}(x)
\]

为执行项目 \(i\) 对当前或近期主观状态产生的净改善。

第一版中，\(S_{i,t}(x)\) 可以整体包含以下可能成分：

deadline 焦虑的缓解、执行本身带来的意义感、完成感、项目本身的内在愉悦，以及减少未完成任务带来的认知占用。

暂时不将这些变量进一步拆分，以避免 notation 过早膨胀。

---

### Future startup-cost reduction

定义

\[
R_{i,t}(x)
\]

为当前执行项目 \(i\) 对未来启动成本所带来的预期削减。

可以写为

\[
R_{i,t}(x) = \mathbb E
\left[
K_{i,t+1}\mid x_{i,t}=0
\right] - \mathbb E
\left[
K_{i,t+1}\mid x_{i,t}=x
\right].
\]

其中，\(K_{i,t+1}\) 表示未来再次启动项目 \(i\) 时的启动成本。

因此，即使一次执行行为没有产生很大的直接项目进展，它仍然可能通过保护项目连续性、保存上下文和降低未来重启成本产生长期价值。

---

### Time cost

定义

\[
T_{i,t}(x)
\]

为在时刻 \(t\) 以执行剂量 \(x\) 推进项目 \(i\) 所产生的时间成本。

---

### Attention demand

定义

\[
A_{i,t}(x)
\]

为在时刻 \(t\) 以执行剂量 \(x\) 推进项目 \(i\) 所需的注意力与认知控制需求。

这里的 \(A_{i,t}(x)\) 暂时作为操作性建模变量，而不直接将其解释为某种精确可测量的固定神经资源。

---

### Startup cost

定义

\[
K_{i,t}
\]

为在时刻 \(t\) 从未执行状态进入项目 \(i\) 的有效工作状态所需要付出的启动成本。

启动成本可能包括上下文重建、重新理解上一次进度、回忆相关材料、心理抗拒以及进入有效工作状态之前的时间损耗。

第一阶段可以保留两个原始测量维度。

定义

\[
L_{i,t}^{\mathrm{start}}
\]

为从决定开始项目，到真正进入有效工作状态之间的启动延迟。

进一步定义

\[
F_{i,t}^{\mathrm{start}}
\]

为主观启动阻力。

因此，在第一阶段，可以暂时将启动成本写成一个二维对象：

\[
K_{i,t} = \left(
L_{i,t}^{\mathrm{start}},
F_{i,t}^{\mathrm{start}}
\right).
\]

在获得足够数据之前，不预设两者必须线性组合成单一标量。

---

### Total benefit

定义

\[
B_{i,t}(x)
\]

为在时刻 \(t\) 以执行剂量 \(x\) 推进项目 \(i\) 所产生的总收益。

第一版可以写为

\[
B_{i,t}(x) = \beta_P M_i\Delta P_{i,t}(x) + \beta_D D_{i,t}(x) + \beta_S S_{i,t}(x) + \beta_R R_{i,t}(x),
\]

其中

\[
\beta_P,\beta_D,\beta_S,\beta_R\geq0
\]

表示不同收益维度的权重。

当前阶段先定义结构，不急于确定权重的具体取值。

---

### Total cost

定义

\[
C_{i,t}(x)
\]

为在时刻 \(t\) 以执行剂量 \(x\) 推进项目 \(i\) 所产生的总成本。

第一版可以写为

\[
C_{i,t}(x) = \gamma_T T_{i,t}(x) + \gamma_A A_{i,t}(x) + \gamma_K z_{i,t}K_{i,t}.
\]

其中

\[
\gamma_T,\gamma_A,\gamma_K\geq0
\]

表示不同成本维度的权重。

---

### Net benefit

定义

\[
N_{i,t}(x) = B_{i,t}(x)-C_{i,t}(x)
\]

为在时刻 \(t\) 以执行剂量 \(x\) 推进项目 \(i\) 所产生的净收益。

这是系统中最核心的评价对象之一。

完整展开后，

\[
N_{i,t}(x) = \beta_P M_i\Delta P_{i,t}(x) + \beta_D D_{i,t}(x) + \beta_S S_{i,t}(x) + \beta_R R_{i,t}(x) - \gamma_T T_{i,t}(x) - \gamma_A A_{i,t}(x) - \gamma_K z_{i,t}K_{i,t}.
\]

---

---

## 附录 现实问题对应理论模型：

此部分负责展开我们需要的notation和定义、性质是怎样来的。

### 1.连续未激活时间、最大中断、项目优先级和暂停状态变量


某些项目如果隔了一段时间未推进，重新的启动成本会上升。于是，定义项目 \(i\) 在时刻 \(t\) 的**连续未激活时间**为： \[ g_{i,t} = \text{截至时刻 } t,\text{ 项目 } i \text{ 连续未被激活的时间} \] 

进一步定义这个项目 \(i\) 允许的**最大中断**：

\[g_{i,t} \leq g_i^{max}\]​


然后可以提出一个**设计性质**：

设 \(p_i\) 表示项目 \(i\) 的优先级，\(p_0\) 表示需要受到该约束保护的最低优先级阈值。则对于任意满足 \[ p_i \geq p_0 \] 的项目 \(i\)，系统应保证： \[ g_{i,t} \leq g_i^{\max} \] 除非该项目处于显式暂停状态/优先级已经低于阈值。

更完整地，可以引入**暂停状态变量**：
\[ Z_{i,t}^{\text{pause}} \in \{0,1\} \]
其中：
\[ Z_{i,t}^{\text{pause}} = \begin{cases} 1, & \text{项目 } i \text{ 在时刻 } t \text{ 处于显式暂停状态}, \\ 0, & \text{否则}. \end{cases} \]

那么上述设计性质可以更严格地写为： \[ p_i \geq p_0 \quad\land\quad Z_{i,t}^{\text{pause}}=0 \quad\Longrightarrow\quad g_{i,t}\leq g_i^{\max} \]







## 1.3