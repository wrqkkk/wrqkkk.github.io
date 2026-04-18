+++
date = '2026-04-18T16:40:00+08:00'
draft = false
title = 'prediction prevails'
isCJKLanguage = true
math = true
+++


# When Prediction Prevails

Lately I’ve been circling around a thought that feels increasingly hard to ignore: in much of modern technical practice, what really wins is not **causal understanding**, but **predictive performance**.

Systems become valuable long before they become intelligible. They work before we can cleanly explain why they work. They extract stable regularities from messy data, turn those regularities into useful outputs, and earn our trust through repeated success. But usefulness and understanding are not the same thing. A model can be effective without revealing the mechanism that makes it effective.

That is the sense in which I keep coming back to the phrase **prediction prevails**.

I do not mean it as a slogan, and I do not mean it as surrender. I mean it as a description of the order in which things seem to happen. In practice, **performance often arrives before theory**. We build systems that can do something remarkable, and only afterward do we begin the slower, more uncomfortable work of asking what exactly they have learned about the world.

This is part of why I keep returning to Pearl’s **ladder of causation**. The framework is appealing not just because it is elegant, but because it separates three things that are often blurred together: seeing, doing, and imagining alternatives. At the bottom is **association**. In the middle is **intervention**. At the top is the **counterfactual**.

And the more I think about it, the more I suspect that most of what we proudly call “causal” in real applications never fully escapes the first rung.

At the level of association, we are asking about $$P(Y \mid X)$$. When we observe $X$, what tends to happen to $Y$? This is the domain of pattern recognition. It is where modern machine learning is strongest. Classification, ranking, recommendation, risk scoring, diagnosis, forecasting—so much of our actual success lives here. We have become extraordinarily good at finding conditional structure in data and turning it into something operational.

That ability is powerful enough to create a dangerous illusion. Once a system performs well, it is tempting to feel that we have understood something deep. But often we have only learned that certain patterns travel together reliably. We may have compressed a complicated slice of reality into a useful predictive surface without uncovering the mechanism underneath.

Medicine makes this especially vivid. There are diseases for which mechanism is well understood, of course. But in a great deal of clinical practice, diagnosis is not derived from a fully transparent causal chain. It is produced by a highly trained pattern recognizer: the physician. Symptoms, lab values, histories, physical signs, imaging features—all of these are synthesized into a judgment that may be quite good, sometimes remarkably good, without being grounded in a complete mechanistic account. Medicine, in that sense, often lives in the space of sophisticated conditional inference. It can be deeply effective while remaining only partially explanatory.

Machine learning inherits this condition and industrializes it. What used to live inside expert intuition now becomes externalized into parameters, training objectives, and optimization dynamics. We no longer need the pattern recognizer to be human. But making the recognizer nonhuman does not automatically make it causal.

The real shift begins when we move from observation to **intervention**. This is where Pearl’s notation becomes more than notation. The difference between $P(Y \mid X=x)$ and $P(Y \mid do(X=x))$ looks small on the page, but it marks an enormous conceptual divide. The first asks what happens when $X=x$ is observed in the world as it naturally unfolds. The second asks what happens when we actively set $X$ to $x$, overriding the ordinary process by which $X$ comes to be.

This difference matters because observed variables are usually entangled with the rest of the system. They are influenced by upstream causes. They may themselves be consequences. Once we intervene, that changes. In Pearl’s graphical language, intervention severs the incoming arrows into $X$. The variable stops behaving like a child of the system and becomes, for the purposes of analysis, an externally imposed parent.

I still find that idea startlingly beautiful. It is such a clean mathematical move, and yet it captures something profound. A variable can change its role entirely depending on whether we are merely watching it or actively manipulating it. Under observation, it may be just another node in a tangled web of dependence. Under intervention, it becomes a point where we reach into the machinery and hold one gear fixed to see what the rest of the system does.

Take something as ordinary as food choice. In observational data, what a person eats may depend on weather, mood, money, habit, time pressure, culture, and countless other factors. Food choice is then a consequence, something downstream of many causes. But if an experiment requires a person to eat a specific meal, that variable is no longer downstream in the same way. It has been fixed from outside. It is no longer being explained by mood or weather within the model. It has become part of the explanation instead.

That is the moment when causal inference starts to feel different from sophisticated statistics. It is no longer just a better way to summarize correlations. It is an attempt to reason about how the world would respond if we altered it.

And then there is the third rung, the one that feels almost extravagant: the **counterfactual**.

This is the level that asks not merely what would happen if we intervened on a population, but what would have happened to this particular person, in this particular case, had one element of the past been different. If a person smoked and developed lung cancer, the counterfactual question is not just whether smoking raises cancer risk on average. It is whether this individual, having smoked and having developed cancer, would still have developed cancer had they not smoked.

What makes this so difficult is also what makes it fascinating. Counterfactual reasoning asks us to compare the actual world to a world that did not happen. The comparison is individualized, and one side of it is forever unobserved. We never get to see both outcomes for the same person under the same background conditions. So the counterfactual is never simply read off the data. It has to be built, justified, and defended through structure.

This is also why I instinctively think of counterfactuals as a kind of disciplined parallel-world reasoning. Not in the metaphysical sense. Not in the science-fiction sense. But in the sense that causality, at its highest level, asks us to say something credible about a nearby world that remained unrealized.

The trouble is that reality is hostile to this ambition.

Once causal ideas leave textbooks and enter actual research, everything gets messy. Variables are missing. Selection is imperfect. Confounding is partly hidden. Measurement is noisy. Ethics constrains experimentation. Longitudinal follow-up is expensive and fragile. Human behavior drifts. Environments change. Entirely reasonable causal questions become hard not because the definitions are unclear, but because the world refuses to provide the clean conditions those definitions would like.

That is why I keep feeling that much of real-world **causal inference** is unavoidably vague. Not useless. Not empty. Just fragile, conditional, and often more dependent on assumptions than people would like to admit. The theory can be sharp while the application remains blurry.

And this brings me back, again, to **prediction prevails**.

The phrase does not mean prediction is more noble than causality. It means prediction is often what succeeds first. In complex systems, capturing regularities is easier than recovering mechanism. Building a useful black box is easier than constructing a transparent world model. In many domains, from medicine to modern machine learning, we repeatedly see the same pattern: robust predictive success arrives before deep explanatory closure.

Large language models make this especially hard to ignore. They are a reminder that a system can become astonishingly competent before we possess a satisfying theory of its behavior. They do not settle the question of understanding. They sharpen it. They force us to confront the possibility that intelligence-like performance may emerge from procedures we only partially grasp, and that theory may spend years catching up to engineering.

I think that is part of why causality feels so compelling to me right now. It represents a refusal to stop at usefulness. It keeps asking a more difficult question. Not just: what patterns can we exploit? But: what would happen if we changed the world? And what, precisely, would have been different if the past had unfolded another way?

Those are slower questions. More expensive questions. In some settings, perhaps unreachable questions.

But they are also closer to what we usually mean by **understanding**.