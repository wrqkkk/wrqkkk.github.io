# Hugo + KaTeX 数学公式渲染排坑与最佳实践

本记录用于追溯在 Hugo (使用 PaperMod 主题) 博客中配置数学公式支持时遇到的多次渲染报错问题，并提供一劳永逸的最终解决方案和编写规范。

## 1. 曾经出现的故障症状

在引入数学公式支持的过程中，曾出现以下几种错误现象：

1. **公式被渲染成了乱码纯文本**：比如 `(P(Y \mid X))` 没有变成数学公式。
2. **公式强制换行并居中**：原本应该在句子中间显示的公式 `$$P(Y \mid X)$$` 打断了段落。
3. **出现重复字符与无样式的乱码**：原本应该渲染为 $X$ 和 $Y$ 的字母，变成了丑陋的 `XX`、`YY`，且 `P(Y | X)` 出现了两次（一次居中，一次像纯文本一样夹在句子里）。
4. **公式代码直接暴露**：页面上直接显示 `$$P(Y \mid X)$$` 文本本身，没有任何渲染效果。

---

## 2. 问题根因分析 (Root Causes)

导致上述现象的原因是多个配置层面的相互冲突：

### 2.1 Markdown 引擎 (Goldmark) 的转义冲突
Hugo 默认的 Markdown 引擎（Goldmark）会把 `_` 识别为斜体，把 `\` 识别为转义符。当我们在文章中写 LaTeX 公式时，这些符号会被 Goldmark 强行解析破坏，导致传给前端 KaTeX 的字符串已经是不完整的。
*(对应症状：渲染出乱码纯文本)*

### 2.2 KaTeX 前端脚本的 DOM 破坏
为了解决上述问题，曾尝试使用前端 JS (`renderMathInElement`) 强行正则扫描页面文本进行替换。但如果页面的 HTML 标签已经被 Goldmark 破坏，这个脚本就会解析错乱，导致它复制了文本节点却无法正确覆盖原节点。
*(对应症状：文本重复显示)*

### 2.3 严格校验 (Integrity) 导致的 CSS 加载失败
KaTeX 为了照顾盲人的屏幕阅读器，在渲染时会生成两套 DOM（一套隐藏的纯文本，一套可见的视觉排版）。它必须依赖 `katex.min.css` 来把那套纯文本隐藏掉。
由于之前引入 CDN 时带了极其严格的哈希校验码 (`integrity="sha384-..."`)，当浏览器安全策略拦截或 CDN 版本出现微小偏差时，**CSS 文件会被直接丢弃**。CSS 一丢，隐藏失效，两套 DOM 就会并排显示。
*(对应症状：原本的 $X$ 变成了并排的 `XX`)*

### 2.4 行内 (Inline) 与块级 (Block) 符号混用
在 LaTeX / KaTeX 标准中：
- `$$ ... $$` 是 **Display Math**，它会强制占据一整行并且居中。
- `$ ... $` 是 **Inline Math**，它可以自然地嵌在文本段落的句子里。
在段落内错误地使用了双美元符，就会导致排版错乱。
*(对应症状：公式强制换行并居中)*

---

## 3. 最终解决方案 (The Solution)

为了彻底解决上述问题，项目目前采用了 **“Hugo 原生透传 + 纯净 KaTeX 自动渲染”** 的闭环方案。

### 3.1 开启 Hugo 原生 Passthrough 扩展
在 `hugo.toml` 中，我们配置了 Goldmark 的 `passthrough` 扩展。这让 Hugo 在编译时主动识别出 `$` 和 `$$` 包裹的内容，并**原封不动地保留**，完全避免了 Markdown 转义破坏。
```toml
[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true
    [markup.goldmark.extensions]
      [markup.goldmark.extensions.passthrough]
        enable = true
        [markup.goldmark.extensions.passthrough.delimiters]
          block = [['\[', '\]'], ['$$', '$$']]
          inline = [['\(', '\)'], ['$', '$']]
```

### 3.2 注入安全、无阻碍的 KaTeX 渲染脚本
在 `layouts/partials/extend_head.html` 中，我们通过 PaperMod 提供的扩展入口，引入了 KaTeX。
**关键修复：**移除了所有 CDN 的 `integrity` 属性，确保 CSS 和 JS 能在所有环境下稳定加载。
```html
{{ if or .Params.math .Site.Params.math }}
<!-- 移除严格 integrity 以免 CDN 变动导致加载失败 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" crossorigin="anonymous"></script>
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false},
        {left: '\\(', right: '\\)', display: false},
        {left: '\\[', right: '\\]', display: true}
      ],
      throwOnError : false
    });
  });
</script>
{{ end }}
```

---

## 4. 之后编写公式的规范 (Best Practices)

以后在写包含数学公式的博客文章时，**必须严格遵守以下 3 条规范**，即可保证 100% 渲染成功：

### 规范 1：必须在文章头部开启 `math`
在文章的 Frontmatter（开头配置区）中，必须显式加上 `math = true`。如果没有这一行，为了网站性能，KaTeX 引擎是不会加载的，公式只会显示为纯文本。
```yaml
+++
title = '你的文章标题'
date = '2026-04-18T16:40:00+08:00'
math = true
+++
```

### 规范 2：严格区分单、双美元符号
- **行内公式（夹在文字中间）**：**必须**使用单美元符 `$ ... $`。
  - ❌ 错误写法：`当变量 $$X$$ 发生变化时...`
  - ✅ 正确写法：`当变量 $X$ 发生变化时...`
- **块级公式（单独占据一行）**：**必须**使用双美元符 `$$ ... $$`。
  - ✅ 正确写法：
    ```text
    根据贝叶斯定理：
    $$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$
    ```

### 规范 3：放弃伪 LaTeX 括号写法
千万不要再使用普通括号 `(P(Y \mid X))` 来代替数学公式包裹符。只要是数学符号或公式，哪怕只有一个字母 $X$，也要用 `$X$` 包裹。
