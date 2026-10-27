+++
date = '2026-10-27T20:38:00+08:00'
draft = false
title = 'longer-reading-and-writing'
isCJKLanguage = true
math = true
+++


#  Motivation


AI can give us a bunch of words and paragraphs, but to decide what are the core ideas beneath those bulletpoints and how to use them is still unavoidable.

I bought a decent plan of tokens, with usage pressure only comes before report deadlines coming.



# 10/27/2026

## On the Death of Amazon’s Writing Culture

> There is no way to write a six-page, narratively structured memo and not have clear thinking.

什么是亚马逊的写作文化？在senior team开会的时候，汇报者不被允许用ppt或者bulletpoint来呈现自己的汇报内容，因为Bezos认为虽然ppt对于制作者而言是更容易组织的（why？），但是对于recipients来说，比起一份well-written document，听取一场ppt演讲会让听众更加容易错过重要的ideas和信息。因此，在一场1小时会议中，演讲者会带上打印稿分发给大家，前半个小时所有人阅读这份memo，在打印稿上作标注；后半个小时等到大家都掌握了足够的信息后，会议才针对议题展开讨论。

> A senior engineer in my community told me that he has started tagging documents as “AI;DR.” AI; didn’t read. In his view, “If a model wrote it, a model can summarize it.” He had better things to do with his time.
>

idea是他虽然用AI来总结，“如果AI可以写出这些 '6-pagers'，那么它也可以阅读和总结它们。”但是他还是会给AI总结的文档打上 "AI;Didn't Read" 的字眼。所以说在脑子里对于文件有管理很重要。



> But the deeper cost is the trust between colleagues. A document used to be proof of thought. If you handed me six pages, I knew that you had spent significant time with the problem. Therefore, I knew that it would be worthwhile spending my time to understand your thoughts.

然而开弓没有回头箭，问题并不在于回到过去，在于怎样真正让批判性思考回到工作中来：

> These aren’t arguments for going back to a pre-AI era. That ship has sailed. AI is fundamentally changing the workplace, and for better or worse, you cannot simply prohibit its use. No company is going to ban it completely.



> The real question is how we can do it in a way that doesn’t abdicate critical thinking for critical decisions.

那么该怎么做呢？关于单向门和双向门。

一个决策能否被轻易地回滚，它的犯错成本是不是轻微的，这将决定一件事情能否高度自动化。

更深层次上的理解是，每一个自动化的决策背后都有过深思熟虑的设计。

> Bezos explained the rationale for this way of working in his 2016 annual shareholder letter. He drew a line between one-way doors, the decisions you can’t walk back easily, and two-way doors, the ones you can.
> 
> One-way doors deserve slow, deliberate, clear thought.
> 
> Two-way door decisions should be made fast, because for them, the cost of being wrong is small.
> 
> Most day-to-day engineering decisions are two-way doors. The teams above did what engineering needed to be done to earn the right to not have to write anything.
> 
> Therefore, I propose the following simple rule: Use AI liberally wherever you have engineered a two-way door. Let it write the code, bypass the code review, and ship it. You are allowed to trust the rollback you’ve built.
> 
> But keep the full ritual of a human writing and a human reading for every decision that is a one-way door. If you don’t know whether the decision in front of you is easily reversible or not, then think about it.





其中一个应对AI冲击的方案：

> Rather than banning the use of AI for the creation of documents, she wrote a policy for the engineering team to follow to ensure they communicated well and respected the people who read their documents. The rest of the company adopted it, and when a co-founder posted the policy on LinkedIn it went viral, which tells you how many companies have this problem.

> Here are the salient points:

> You must stand behind every sentence. “Oh, AI wrote that, ignore it” is never an acceptable answer to a reviewer’s question.

> Writing is thinking. A spec or a retrospective is proof that someone has thought about the problem. If you skip the writing then you lose that proof.

> Spend more time writing a document than your readers will spend reading it. One author; many readers. The time you take to ensure you will be understood will have a multiplying benefit..

> Longer is not better. If you have generated a long document from a short prompt, share the prompt instead.

> Quoting generated text is fine as long as you label it as such.




For Amazon, 作者认为可以执行的policy：

> If I were to write it, the policy would have at least three rules:

> Two-way doors can be AI. One-way doors require humans. If an issue can sort itself out or the stakes are low, let the machine do the writing, or don’t write anything at all. Otherwise, a human writes it, and a human reads it and gives feedback.

> You own every word. Generated or typed, if it is in your document, you are accountable for it. If you present a document where it’s clear that the AI did the thinking, the people in that room should feel free to tell your manager, and your manager will treat it as seriously as they treat any other failure to do the job. There must be consequences.

> Certain documents must always be human-written. Some documents only have value if a human has written them. The annual shareholder letters, planning documents (OP1 and OP2), PR-FAQs, any proposal for a new initiative, major rearchitectures, performance reviews, and promotion documents all belong on that list.


结尾，一个很有意思的视角：

![alt text](../../../static/imgs/longer-reading-and-writing-image.png)


