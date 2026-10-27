+++
date = '2026-05-06T13:00:00+09:00'
draft = false
title = 'graphical models——new perspective on linear regression'
isCJKLanguage = true
math = true
+++


# 概率图模型学习小记：从线性回归到贝叶斯图结构

当我们看到线性回归，脑子里首先出现的是：

$$
Y_i=\alpha+\beta x_i+\epsilon_i
$$

然后就是损失函数、OLS、残差、标准误、置信区间和 $p$-value。但在概率图模型的表达里，线性回归突然变成了一个由节点和箭头组成的生成系统。这个转变让我意识到，**线性回归不只是“拟合一条线”，它其实是在描述数据如何由一组未知量和随机机制生成出来**。

---

## 1. 核心模型框架：从公式到生成结构

### 1.1 普通线性回归的熟悉写法

最常见的线性回归写法是：

$$
Y_i=\alpha+\beta x_i+\epsilon_i,\qquad \epsilon_i\sim N(0,\sigma^2)
$$

这里的 $\alpha$ 是 **intercept**，也就是截距；$\beta$ 是 **slope**，也就是斜率；$\epsilon_i$ 是误差项，表示观测值没有被线性结构解释的剩余波动。

如果换成概率语言，同一个模型可以写成：

$$
Y_i\mid \alpha,\beta,\sigma^2 \sim N(\alpha+\beta x_i,\sigma^2)
$$

这一步看似只是换了一种写法，但它改变了理解方向。第一种写法更像是在说“观测值等于一条线加一个误差”。第二种写法更像是在说“给定参数以后，观测值是从一个条件正态分布中生成出来的”。

### 1.2 线性模型的两层结构

把上面的式子进一步拆开，可以得到：

$$
\mu_i=\alpha+\beta x_i
$$

$$
Y_i\mid \mu_i,\sigma^2\sim N(\mu_i,\sigma^2)
$$

这两行分别对应两个层次。

**第一层是系统结构**。$\mu_i$ 是模型给出的条件均值，它由截距、斜率和协变量 $x_i$ 决定。

**第二层是随机观测结构**。真实观测值 $Y_i$ 不一定等于 $\mu_i$，而是在 $\mu_i$ 附近发生随机波动。

这和时间序列里

$$
Y_t=\mu_t+X_t
$$

的思想有相通之处。$\mu_t$ 表示确定性趋势，$X_t$ 表示随机波动。在线性回归的概率图结构里，$\mu_i$ 表示系统规律，$Y_i$ 表示在这个规律周围生成出来的观测值。

**线性回归不只是一条线，而是一种数据生成假设**。

---

## 2. 概率图结构：节点、箭头与条件依赖

### 2.1 图里的节点代表什么？

在线性回归的 Bayesian graphical model 中，常见节点包括：

$$
\alpha,\quad \beta,\quad \tau,\quad \mu_i,\quad Y_i
$$

其中 $\tau$ 是 **precision**，即精度。它和方差的关系是：

$$
\tau=\frac{1}{\sigma^2}
$$

所以 $\tau$ 越大，表示 $\sigma^2$ 越小，观测值围绕均值 $\mu_i$ 越集中；$\tau$ 越小，表示误差方差越大，观测点越分散。

### 2.2 箭头表达条件依赖

在图结构中，$\alpha_0$ 和 $\beta$ 指向 $\mu_i$，因为：

$$
\mu_i=\alpha_0+\beta(x_i-\bar{x})
$$

其中，$\alpha_0$ 是中心化后的截距，当 $x_i=\bar x$，可以得到均值 $\mu_i=\alpha_0$，相较 $\alpha$ 具有实际意义。

这说明 $\mu_i$ 由中心化后的截距、斜率和中心化后的协变量决定。

紧接着，$\mu_i$ 和 $\tau$ 指向 $Y_i$，因为：

$$
Y_i\mid \mu_i,\tau\sim N(\mu_i,\tau^{-1})
$$

这说明观测值 $Y_i$ 的条件分布由条件均值 $\mu_i$ 和误差精度 $\tau$ 决定。

因此，图中的箭头不是装饰，而是在表达 **conditional dependence**。谁指向谁，谁就参与决定谁的条件分布。

### 2.3 联合分布的因子分解

图结构背后真正对应的是一个联合概率分布。线性回归可以写成：

$$
p(\alpha,\beta,\tau,Y_1,\ldots,Y_n)
=
p(\alpha)p(\beta)p(\tau)\prod_{i=1}^n p(Y_i\mid \alpha,\beta,\tau)
$$

这个式子非常关键。它说明复杂的联合分布可以拆成若干个局部条件分布。概率图模型做的事情，就是把这种拆分方式用图画出来。

**概率图模型的核心在于是用图表达联合分布如何因子分解。**

---

## 3. Plate notation：重复观测如何被表达？

在图模型中，$\mu_i$ 和 $Y_i$ 通常会被放在一个框里，框上写着 $i=1,\ldots,n$。这个框叫 **plate notation**。

它的含义是：框里的结构会对每一个观测重复一次。

也就是说，每个样本都有自己的：

$$
\mu_i,\quad Y_i
$$

但所有样本共享同一组全局参数：

$$
\alpha,\quad \beta,\quad \tau
$$

因此，给定共同参数以后，不同观测之间是条件独立的：

$$
Y_i\perp Y_j\mid \alpha,\beta,\tau,\qquad i\neq j
$$

这句话的意思是，第 $i$ 个观测和第 $j$ 个观测的共同性主要来自它们共享同一组参数。一旦这些参数被给定，两个观测之间就没有额外的直接依赖。

这让我第一次比较清楚地看到，**独立性不是一句孤立的假设，而是由图结构编码出来的条件关系**。

---

## 4. 参数作为随机变量：最关键的理解转变

### 4.1 频率学派的参数观

在频率学派中，$\alpha,\beta,\sigma^2$ 通常被看成未知但固定的常数。它们在真实世界中有一个确定值，只是我们不知道，所以需要用样本去估计。

因此，频率学派通常报告：

$$
\hat{\beta},\quad SE(\hat{\beta}),\quad CI,\quad p\text{-value}
$$

这里的重点是估计一个固定参数，并研究估计量在重复抽样下的性质。

### 4.2 贝叶斯的参数观

贝叶斯观点更直接地承认研究者的知识状态：既然我们不知道 $\alpha,\beta,\tau$，那么我们对它们的认识就是不确定的；既然不确定，就可以用概率分布表达。

因此可以写：

$$
\alpha\sim N(0,10^6)
$$

$$
\beta\sim N(0,10^6)
$$

$$
\tau\sim Gamma(0.001,0.001)
$$

这里的重点不是说真实世界里的斜率每天随机变化，而是说：**在看到数据之前，研究者对斜率的认识是不确定的，这种不确定性可以用先验分布表示**。

这种不确定性叫 **epistemic uncertainty**，即认识论不确定性。它来自知识不足，而不是来自现实对象本身的随机跳动。

### 4.3 两类不确定性

贝叶斯线性回归中至少有两类不确定性。

**第一类是观测层面的随机性**，也就是 $Y_i$ 围绕 $\mu_i$ 波动。这对应误差项 $\epsilon_i$，属于数据生成过程中的随机波动。

**第二类是参数层面的不确定性**，也就是我们不知道 $\alpha,\beta,\tau$ 的真实值。这对应先验分布和后验分布，属于认识论层面的不确定性。

把这两层都放进模型以后，推断才变得完整。

---

## 5. 先验、似然、后验：贝叶斯学习机制

贝叶斯推断的核心公式是：

$$
p(\theta\mid Y)=\frac{p(Y\mid \theta)p(\theta)}{p(Y)}
$$

其中 $\theta$ 可以代表 $\alpha,\beta,\tau$。这个式子常常被写成：

$$
\textbf{posterior}\propto \textbf{likelihood}\times \textbf{prior}
$$

也就是：

$$
\textbf{后验认识}\propto \textbf{数据证据}\times \textbf{先验认识}
$$

这里的 **prior** 表示看数据之前对参数的认识；**likelihood** 表示给定参数时观察到当前数据的可能性；**posterior** 表示看完数据以后更新得到的认识。

这一步把“学习”这件事数学化了。数据不是直接给出真理，而是在模型结构和先验认识的基础上更新我们对未知量的判断。

所以，贝叶斯模型并不是主观乱猜。相反，它要求我们把先验假设明确写出来，并允许我们进一步做 sensitivity analysis，检查不同先验对结果的影响。

---

## 6. Centering：从 OLS 几何到贝叶斯后验几何

在 linear regression 的图模型代码里，均值常常写成：

$$
\mu_i=\alpha_0+\beta(x_i-\bar{x})
$$

而不是：

$$
\mu_i=\alpha+\beta x_i
$$

这里的 $x_i-\bar{x}$ 是 **centering**，也就是中心化。

### 6.1 频率学派中的作用

在 OLS 的几何视角里，中心化可以让常数项和协变量方向更接近正交。对于设计矩阵来说，它会减少截距和斜率之间的耦合，使 $X^TX$ 的结构更容易处理。

也就是说，中心化有助于实现参数解耦。

### 6.2 贝叶斯计算中的作用

在贝叶斯模型中，中心化还有另一个意义：它可以降低 $\alpha$ 和 $\beta$ 在后验分布中的相关性。

如果不中心化，斜率稍微变大时，截距可能需要相应变小，才能让拟合线仍然穿过数据云的中心。这会导致后验分布呈现狭长的相关结构，MCMC 采样时移动比较慢，混合也会变差。

中心化以后，$\alpha$ 的解释变成“当 $x$ 处于平均水平时 $Y$ 的均值”。这通常更自然，也能改善后验几何形状。

所以，**中心化在频率学派里改善信息矩阵，在贝叶斯里改善后验几何结构**。

---

## 7. 从投影视角到概率视角：同一个线性模型的两张地图

在 OLS 的几何视角里，我们把观测向量 $Y$ 投影到由特征基底张成的子空间中。拟合值 $\hat{Y}$ 是投影，残差 $e=Y-\hat{Y}$ 垂直于模型子空间。

这个视角强调：

$$
Y\longrightarrow \hat{Y}
$$

也就是从观测数据出发，寻找最优拟合。

而概率图模型强调：

$$
\alpha,\beta,\tau\longrightarrow \mu_i\longrightarrow Y_i
$$

也就是从参数和随机机制出发，描述观测数据如何生成。

这两个视角并不冲突。它们只是看同一个线性模型的两个侧面。

**OLS 的几何视角回答的是：为什么这个估计量是最优投影。**

**概率图模型回答的是：数据如何由参数、均值结构和随机误差共同生成。**

于是，线性回归有了两张地图。一张是几何地图，关键词是 **projection, basis, orthogonality, residual**。另一张是概率地图，关键词是 **prior, likelihood, posterior, conditional independence**。

---

## 8. BUGS/JAGS/NIMBLE 为什么能自动计算？

概率图模型不只是帮助理解，它也直接服务于计算。

贝叶斯模型真正想得到的是：

$$
p(\alpha,\beta,\tau\mid Y)
$$

根据贝叶斯公式，它正比于：

$$
p(\alpha)p(\beta)p(\tau)\prod_{i=1}^n p(Y_i\mid \alpha,\beta,\tau)
$$

当模型很简单时，后验分布可能有解析形式。但当模型加入随机效应、空间效应、缺失机制、多结局结构以后，解析求解会变得非常困难。

MCMC 的作用就是从后验分布中抽样。BUGS、JAGS、NIMBLE 这类系统之所以能工作，是因为概率图模型把联合分布拆成了局部条件分布。系统可以根据图结构找到每个节点的局部依赖关系，然后逐步更新未知量。

比如更新 $\beta$ 时，系统主要需要知道 $\beta$ 的先验，以及所有通过 $\mu_i$ 与 $\beta$ 相连的观测值 $Y_i$。这就是图结构带来的模块化计算。

所以，**概率图模型把统计模型变成了计算机可以操作的对象**。

---

## 9. 扩展一：从线性回归到层级模型

把参数看成随机变量的思想，在层级模型中会变得更有力量。

假设我们研究不同地区 PM2.5 对某个健康结局的影响。每个地区都可以有自己的斜率：

$$
\beta_j
$$

其中 $j$ 表示地区。

如果每个地区单独估计，就是 **no pooling**。这种方法允许地区差异，但小样本地区会很不稳定。

如果所有地区共用一个斜率，就是 **complete pooling**。这种方法很稳定，但会抹掉真实的地区异质性。

贝叶斯层级模型可以写成：

$$
\beta_j\sim N(\beta_0,\sigma_\beta^2)
$$

这表示每个地区有自己的效应，但这些效应来自一个共同的总体分布。这就是 **partial pooling**。

partial pooling 的好处是：数据多的地区更多依赖自身信息，数据少的地区会向总体平均效应适度收缩。它既保留异质性，又避免小样本估计过度波动。

这对环境流行病学很重要，因为现实数据中不同地区、不同暴露水平、不同 cluster 的样本量往往并不均衡。

---

## 10. 扩展二：迁移到 PM2.5 与健康结局研究

如果研究 PM2.5 与疾病发生，可以写一个 Bayesian logistic regression：

$$
Y_i\sim Bernoulli(p_i)
$$

$$
\log\frac{p_i}{1-p_i}
=
\alpha+\beta PM_{2.5,i}+\gamma^\top Z_i
$$

其中 $Y_i$ 表示是否患病，$Z_i$ 表示年龄、性别、教育、城乡、收入等协变量。

频率学派通常报告：

$$
\hat{\beta},\quad SE,\quad CI,\quad p\text{-value}
$$

贝叶斯模型则给出：

$$
p(\beta\mid Y,PM_{2.5},Z)
$$

于是我们可以直接问：

$$
P(\beta>0\mid data)
$$

如果使用 odds ratio：

$$
OR=\exp(\beta)
$$

也可以问：

$$
P(OR>1\mid data)
$$

这比单纯判断 $p<0.05$ 更贴近公共卫生问题。因为我们真正关心的是：在当前数据和模型假设下，PM2.5 使疾病风险升高的后验概率有多大，效应大小大概落在哪里，不确定性有多宽。

更进一步，我们还可以问：

$$
P(OR>1.05\mid data)
$$

$$
P(OR>1.10\mid data)
$$

这类问题更接近实际决策，因为公共卫生中常常关心效应是否超过某个有意义的阈值。

---

## 11. 扩展三：迁移到空间模型、CAR、BYM 与 SCM

空间疾病模型也可以被看成概率图模型的扩展版本。

一个区域疾病模型可以写成：

$$
Y_i\sim Poisson(E_i\lambda_i)
$$

$$
\log\lambda_i=\alpha+\beta x_i+u_i+v_i
$$

这里 $E_i$ 是期望病例数，$\lambda_i$ 是相对风险，$x_i$ 是 PM2.5 或其他暴露，$u_i$ 是空间结构随机效应，$v_i$ 是非结构随机效应。

在图模型中，$\alpha,\beta,u_i,v_i$ 会指向 $\lambda_i$，$\lambda_i$ 和 $E_i$ 再指向 $Y_i$。这和线性回归的结构完全同源：

$$
\textbf{parameters and latent effects}
\longrightarrow
\textbf{mean or risk parameter}
\longrightarrow
\textbf{observed data}
$$

CAR 模型的关键在于，空间随机效应 $u_i$ 之间并不是彼此独立的。它通常通过邻接关系定义：

$$
u_i\mid u_{-i}\sim
N\left(
\frac{\sum_{j\sim i}u_j}{n_i},
\frac{1}{n_i\tau_u}
\right)
$$

这里 $j\sim i$ 表示地区 $j$ 是地区 $i$ 的邻居，$n_i$ 是地区 $i$ 的邻居数量。这个式子的意思是，一个地区的空间效应会受到邻近地区空间效应的影响。

所以，空间模型里的“借邻居信息”，在图结构里就是通过随机效应节点之间的依赖关系表达出来的。

这说明 linear regression 不是一个孤立例子，而是理解 CAR、BYM、SCM 的最小模板。

---

## 12. 扩展四：迁移到 CLARA 暴露画像和效应异质性

在 CLARA 暴露画像分析中，我们可能关心不同 exposure profile 下，PM2.5 对健康结局的效应是否不同。

频率学派可以写成交互项模型：

$$
Y_i=\alpha+\beta PM_i+\sum_k\delta_k I(cluster_i=k)
+\sum_k\eta_k PM_iI(cluster_i=k)+\epsilon_i
$$

其中 $\eta_k$ 表示不同 cluster 中 PM2.5 效应的差异。

贝叶斯层级模型可以更自然地写成：

$$
\beta_k\sim N(\beta_0,\sigma_\beta^2)
$$

$$
Y_i\sim N(\alpha_{cluster_i}+\beta_{cluster_i}PM_i,\sigma^2)
$$

这里每个 cluster 都有自己的暴露效应 $\beta_k$，但这些 $\beta_k$ 来自同一个总体分布。

这样做的好处是，某个 cluster 样本量少时，它的效应估计不会完全被小样本噪声支配，而会向总体效应适度收缩。与此同时，如果某个 cluster 的数据非常充分，它仍然可以表现出与总体不同的效应。

这就把 CLARA 从“先聚类、再分组回归”的流程，推进到一个更完整的层级推断框架。

**暴露画像不只是描述性标签，也可以成为效应异质性的层级来源。**

---

## 13. 和机器学习的连接：从 feature engineering 到 probabilistic programming

机器学习通常写成：

$$
\hat{y}=f_\theta(x)
$$

它关心的是如何通过参数 $\theta$ 把输入 $x$ 映射到预测值 $\hat{y}$。

概率图模型会进一步写成：

$$
Y\mid \theta,x\sim p(Y\mid f_\theta(x))
$$

也就是说，它不仅给出预测值，还给出预测值周围的不确定性。

贝叶斯模型再进一步，把 $\theta$ 也看成随机变量：

$$
\theta\sim p(\theta)
$$

$$
\theta\mid data\sim p(\theta\mid data)
$$

于是，模型不仅表达观测噪声，也表达参数不确定性。

这对医学和环境健康研究尤其重要。因为这些研究不只关心预测结果，还关心效应方向、效应大小、不确定性范围和科学解释。概率图模型给机器学习补上的，正是这种结构化的不确定性表达。

---

## 14. 小结：如何理解 graphical linear regression？

过去我们更多地把线性回归理解为一个估计公式：

$$
Y_i=\alpha+\beta x_i+\epsilon_i
$$

现在在贝叶斯视角下，我们可以思考这样一个概率生成系统：

$$
\alpha,\beta,\tau
\longrightarrow
\mu_i
\longrightarrow
Y_i
$$

其中，$\alpha,\beta,\tau$ 是未知参数，$\mu_i$ 是由线性结构决定的条件均值，$Y_i$ 是围绕 $\mu_i$ 生成的观测值。

所以，graphical models 里的 linear regression 不是普通回归的重复，而是一个入口。它展示了概率图模型的基本语法：

**节点表示变量，箭头表示条件依赖，plate 表示重复观测，先验表示参数不确定性，似然表示数据生成机制，后验表示数据对未知量的更新。**

---

## 15. 最终理解

如果说 OLS 的几何视角让我们看到线性回归的投影本质，那么 graphical model 的概率视角则揭示了线性回归的生成本质。

前者强调：

$$
\textbf{projection, basis, orthogonality, residual}
$$

后者强调：

$$
\textbf{prior, likelihood, posterior, conditional independence}
$$

这两个视角合在一起，让线性回归不再只是一个孤立公式，而是连接线性代数、概率论、统计推断和计算方法的一座桥。


这也解释了为什么继续学习 Bayesian network、NIMBLE、空间模型、层级模型和环境健康效应异质性时，linear regression 仍然是最重要的起点。复杂模型看起来形式不同，但底层逻辑是相同的：**把复杂系统拆成局部条件关系，再通过联合概率分布把这些局部关系重新连接起来。**
