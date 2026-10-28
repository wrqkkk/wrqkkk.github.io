+++
date = '2026-10-27T20:30:00+08:00'
draft = false
title = 'longer-reading-and-writing-ref'
isCJKLanguage = true
math = true
+++


# 10/27/2026

## [On the Death of Amazon’s Writing Culture](https://alifeengineered.substack.com/p/on-the-death-of-amazons-writing-culture)

# 10/28/2026

## [Working with academic communities to build scientific understanding](https://openai.com/index/building-scientific-understanding-with-academic-communities/)


Released by OPENAI, on October 26, 2026

### 指数时间假设不成立

计算机科学合作小组将研究并阐释一项有关指数时间假设（ETH）的成果。ETH 是一个长期未决的猜想，涉及布尔公式可满足性问题的计算复杂性，而这一问题与 P 与 NP 问题密切相关。学界普遍认为 ETH 成立。数百篇论文以此为前提，推导出了有条件的计算困难性结论，涉及图论、计算生物学、数据库、计算几何等众多领域。出人意料的是，我们的系统最近证明了 ETH 不成立，且这一结果随后在 Lean 中得到了验证。ETH 被推翻，使得这些计算任务究竟还能加快多少重新成为开放问题，也可能为寻找更好的算法指明方向。要找到这样的算法，并将理论进展转化为实际改进，还需要大量后续研究。

这项工作将由 Russell Impagliazzo（加利福尼亚大学圣迭戈分校）、Ramamohan Paturi（加利福尼亚大学圣迭戈分校）和 Ryan Williams（麻省理工学院）领导的小组负责验证并推动后续研究。三位都是算法设计和复杂性理论方面的专家。

Impagliazzo、Paturi 与 Francis Zane 是指数时间假设的最初提出者。过去 30 年来，他们围绕这一主题⁠撰写了多篇颇具影响力的⁠论文⁠ 。

Williams 曾推翻 ETH 的强化版本⁠ ，利用 ETH 推导困难性结论⁠ ，并建立了算法与下界之间的联系。

我们已同意该小组的请求：公开这些成果的所有原始数据，以便学术界独立验证；同时，OpenAI 承诺资助一场学术会议，探讨这项工作对整个领域的影响。该小组邀请学术界协助组织对这一 ETH 结论的公开审查，并讨论 AI 生成的突破在验证、获取成果的机会、学术贡献归属以及研究的未来等方面引发的更广泛问题。

我们的 AI 于 2026 年 10 月 16 日找到了以自然语言表述的 ETH 反证，随后我们于 2026 年 10 月 17 日在 Lean 中完成了这一结果的形式化，由此促成了本文所述的合作。为此，我们已在公开的 GitHub 代码仓库中发布了模型生成的AI 自然语言输出文稿⁠ 以及 Lean 证明⁠ 。

计算复杂性领域仍有许多开放问题和猜想，尽管科学家竭尽全力，迄今仍未能将其证明或推翻。我们希望，人类借助 AI 能够为这一领域带来新的认识，揭示高效计算的内在能力与局限。




















## [Why Clay Has an AI Writing Policy](https://www.clay.com/blog/ai-writing-policy)

Released by Clay, on Aug 19, 2026


### Intro
Earlier this year, I noticed an uptick in documents and presentations within our teams that were hard to read: many of them were longer than necessary, had sections that didn’t make complete sense, and incorporated many of the common tics of AI writing. Although these AI-generated documents may have saved their authors a bit of time, I observed that they were getting in the way of effective collaboration. After discussing with the other engineering leads at Clay, I wrote up this policy and rolled it out to the engineering team. Rather than ban the use of AI for writing entirely, we opted to focus more on **what good writing should be** and a little less on how it’s produced.


... ...


### Clay’s AI Writing Policy
For all Clay employees: whenever you use AI to write text seen by other people, please abide by this policy to ensure we’re communicating well and making the best use of everyone’s time.

Good writing is a tool to clearly communicate ideas from your brain into someone else’s.

As of 2026, AI models — despite their coding ability — are not yet at a point where their unedited output will achieve this goal; you as an author need to take the time to make sure that all of the ideas in the writing are the ideas that you personally intend to convey (including the structure and wording that determines which ideas are emphasized) and that the documents are a good use of your readers’ time.

It’s allowed to use AI tools while brainstorming or drafting your writing and certainly while proofreading, but make sure to consider the following principles while doing so:

You must stand behind every idea and every sentence in your docs. It is your responsibility to make sure that the entire document is representative of your own thoughts before you share it. If a reviewer asks, “What did you mean by this line?”, it’s not acceptable to reply with “Oh sorry, AI wrote that, just ignore it.” You will confuse your readers (and waste their time) if you present them things that are not genuinely representative of your thoughts. In some cases, readers will recognize and call out the incongruous parts; in others, they will be misled as to what your actual thoughts are.

Writing is thinking. Spending time on the writing process — on deciding what to emphasize and how to structure your ideas clearly — teaches you more about your topic. If you circumvent this process, you will probably walk away with a poorer understanding of the subject matter. In many cases, written artifacts like project specs, status updates, and retrospectives serve as a “proof of thought”. The artifact itself is not the only goal; instead, detailed thinking about the problem is the goal. Outsourcing the creation of these documents to AI (so that you can skip the thinking) risks circumventing this very purpose. Even if working with AI helps you think through a problem, you’ll understand it better if you thoroughly review the result yourself.

More time should be spent authoring a document than consuming it. If you generate a document from a short prompt then ask your readers to go through the longer output, you are disrespecting their time. They can always talk to ChatGPT themselves if they want to. Most docs are written by one person but are read by many people, so any extra time that readers need to spend to understand what you meant incurs a multiplicative cost on the team’s time. Conversely, if you spend extra time to make your document clear and concise before sending it, you are paying a one-time cost that every reader will benefit from.

Longer is not better. Pascal once wrote, “I have made this [letter] longer than usual because I have not had time to make it shorter.” AI makes it much easier to generate a long doc, and one of its strategies is to include many sentences that don’t say much at all and detract from the actual content. If you are producing a longer piece of writing from a shorter prompt, consider instead just sharing the prompt itself. If you use AI to edit without lengthening, vacuous sentences are less of a risk but your meaning may still get obscured.

There are no lossless transformations of natural-language text—every rewrite and rephrase changes the meaning of your writing, and if this is done by an entity that doesn’t have the most detailed mental representation of what you personally were trying to communicate, information will be lost. Readers will appreciate hearing your thoughts, even at the expense of supposed “polish”.
It’s also OK to quote AI generations verbatim that don’t meet the above standards if you mark them clearly as such. Sometimes it’s useful to say like “Claude offered this idea, do you think it’s worth looking more into?”, and this is allowed.

As AI tools improve over time at theory of mind and get better at writing, it may make sense to lean more heavily on them, but the principles in this policy will remain important.



## 