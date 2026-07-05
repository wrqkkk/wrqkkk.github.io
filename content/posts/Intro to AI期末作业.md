+++
date = '2026-07-04T00:20:00+08:00'
draft = false
title = 'Intro to AI期末作业'
isCJKLanguage = true
math = true
+++




# Ideas
## 维护工作/思考框架
我们应该维护自己的框架，也就是说，稳定工作、生活的流程，当我们需要看一篇论文的时候，也许方式是多样、多变的，但评价标准是具有某种粘性的，尤其是针对高难度、多阶段的复杂任务，这些任务或许AI能完成、能完成得不错（相对原来人工质量的60/80/100/200分），但不代表我们要完全让出“思考的权利”，放弃“思考的义务”，正相反，我们需要思考的事情更多了，除了原来需要完成的任务以外，我们还要思考，人类在其中扮演的角色是什么？还要思考：

## 一些需要思考的问题
- 60分的能力怎样提高到80分？
- 人类的80分工作和机器的100分工作，用哪一个？怎样衡量其中获得/损失的社会、经济效益？对于可以以较为完善的标准验收的工作，速度和质量还能成为唯一的标准吗？——毕竟有时，我们的senior之所以能成长成为如今有“创造力”、“组织力”、“判断力”的senior，是因为他们在junior时期不厌其烦地做着简单工作，并从中得到历练，在这些历练中，如同训练神经网络，或是强化学习一样，他们和环境交互，获得反馈，更新参数，更新“惩罚”机制，思考目标等等。这个过程是很重要的。
- 对于一些任务，我们是无法用一个很好的标准来AI的成果是多少分的，在此之前，人类明确地为他们的工作负责，每一个词都在人类大脑的“神经网络”中过了一遍；但现如今，当AI承担起越来越高比例的工作时，当文字都由概率模型吐出、而非经过大脑复杂计算，由大脑深处某个神秘神经元组织的时候，我们要以怎样的态度相信这些内容？我们要怎样审查它们？用什么标准审查它们？



## 维护用脑边界

在思考这些业界、学界还争论不休的宏大问题之前，我们有一件紧迫但隐形的事情要去做：维护自己的用脑边界。有研究表明，依赖大语言模型去做任务，即使是简单任务，也会损害大脑的认知/独立思考能力（这个表述目前不是特别精确），一些参考文献：

> - [Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task](https://www.semanticscholar.org/reader/b9fbc328dd40391321ddd80cc2bc911a80e574f7)
> - [Protecting Human Cognition in the Age of AI](https://www.semanticscholar.org/paper/Protecting-Human-Cognition-in-the-Age-of-AI-Singh-Taneja/2f147f41fb9cd03a8fa217c9ad6156a112890169)
> - [Intention Is All You Need](https://www.semanticscholar.org/paper/Intention-Is-All-You-Need-Sarkar/fa40b6c53f3dfccbaf16286e6156319dbcc3bde3)
> - [AI Tools in Society: Impacts on Cognitive Offloading and the Future of Critical Thinking](https://www.semanticscholar.org/paper/AI-Tools-in-Society%3A-Impacts-on-Cognitive-and-the-Gerlich/cce6e863d5408244284d97f5a13e8c9ab103ad01)
> - [The Impact of Generative AI on Critical Thinking: Self-Reported Reductions in Cognitive Effort and Confidence Effects From a Survey of Knowledge Workers](https://www.semanticscholar.org/paper/The-Impact-of-Generative-AI-on-Critical-Thinking%3A-a-Lee-Sarkar/93a07d548608d2368ae2e3287275e3caf42a562c)
> - [Cognitive ease at a cost: LLMs reduce mental effort but compromise depth in student scientific inquiry](https://www.semanticscholar.org/paper/Cognitive-ease-at-a-cost%3A-LLMs-reduce-mental-effort-Stadler-Bannert/ec4baa3477020f66f8ddd4d6899a2b384d612b17)
> - [The effects of over-reliance on AI dialogue systems on students’ cognitive abilities: a systematic review](https://www.semanticscholar.org/paper/The-effects-of-over-reliance-on-AI-dialogue-systems-Zhai-Wibowo/81e8666325b02b1287d4fdcf33232c74e7144f9a)
















## 机械化趋同： Mechanised Convergence: The Homogenising Effect of AI on Intention

这种 convergence 是可以 mathematically 被定义并证明的吗？
![alt text](<static/imgs/Intro to AI期末作业-image.png>)







## 如何让AI产出稳定的结果


一些过程


## Auto encoder、表征学习探索等等


## Neural Network和人类大脑的相似性，CNN的尝试，Transformer的尝试。











# 正文


## 目录

- 本文档的思路总结，大概是心路历程的一段前言
- 学术探索，关于Transformer
- Agent 探索，以及产出的笔记等等成果
- 关于AI时代的思考




## 前言

上大学之后会发现，原来世界上不止语数英物化生史地政这9个学科，每个领域用他们的语言在讲述着这个世界，人与人之间的联系，物与物之间的联系，很有意思的是，我对“语言”这一概念的内涵和外延的理解在不断变得丰富。


### 人与人之间的语言

关于其他外语：小学在外国语学校，先是浅尝了一点点法语——只是囫囵吞枣，姑且记得 bonjour 和一首小曲《Je m'appelle Hélène》，还有r读起来像嗓子里有东西要咯出来，至于语言的美，那是一点也没感受到的，再后来懵懵懂懂地在“韩流”席卷的时候喜欢了一段时间的kpop，又记了零星几个字眼的韩语；初中曹老师给我们分享她特别喜欢的德语词——zugluft，穿堂风，并告诉我们德语的语法特别复杂，阴性阳性难以分辨，这些时至今日我仍然记得——后来23年在家里实在无聊，想起哲学典籍多用德语撰写这一事，又心血来潮打卡了一个月的 duolingo 德语课程。好像就此结束了，其实在大学还有二外的学分，可以选很多外语课程，但架不住主业的工作量实在庞大，而英语的优势又难以放弃，难免兴致缺缺了。

陪伴我最久的还是英语。高中时，在Shel的点拨和指引下，我开始真正把英语当作一门语言来品味和欣赏，去学习另外一个文化表达情感，描绘世界的方式——这非常有意思！在品尝另一门语言韵味的同时，我也一遍遍在领悟中文的美。分享许渊冲先生的译作：


> “寻寻觅觅，冷冷清清，凄凄惨惨戚戚”
> 
> “I look for what I miss, I know not what it is”

我们在语文课堂上认识了这句诗，听了肖老师给我们放的古汉语版本的音频；又在英语课堂上认识了许渊冲，从英语的视角，品味这句在诗顿挫中传递出的情感与美。那一刻，时空好像真的可以折叠，原文、译文和我们，处在了宇宙中的同一个位置。


### 人与机器之间的语言

上了大学，我们开始学习“编程语言”，以前我从未思考过：
- “语言”这个概念的边界是什么
- 为什么“编程语言”可以被称之为语言
  
我读到了关于编程（Programing）的一个很有意思的定义，来自Blackwell：

> any activity exhibiting the property “that the user is not directly manipulating observable things, but specifying behaviour to occur at some future time” 
> （Blackwell, A. F. (2002). What is programming? In PPIG (Vol. 14, pp. 204–218).
>









