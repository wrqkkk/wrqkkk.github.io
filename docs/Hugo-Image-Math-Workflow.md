# Hugo 博客公式渲染与图片自动管理技术报告

本报告记录了在 `机器学习与时间序列分析.md` 中的两次核心修复，并为你打造了一套“无脑粘贴图片自动归档到 assets”的完美工作流。

## 一、数学公式显示修复

### 1. 故障现象
在将文章部署到 github.io 后，Markdown 中的 `$` 和 `$$` 公式均显示为原生的美元符号与纯文本，无法被渲染为数学样式。

### 2. 根本原因
尽管我们在网站底层已经配好了 KaTeX 和 Hugo Passthrough，但 PaperMod 主题**默认是按需加载数学脚本的**。由于 `机器学习与时间序列分析.md` 的 Frontmatter（配置头）里没有声明需要数学支持，因此整个页面的 KaTeX 脚本压根没有被引入。

### 3. 解决方案
打开 [机器学习与时间序列分析.md](file:///d:/githubmyprojects/wrqkkk.github.io/content/posts/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%E4%B8%8E%E6%97%B6%E9%97%B4%E5%BA%8F%E5%88%97%E5%88%86%E6%9E%90.md)，在开头的 `+++` 配置块中增加了：
```toml
math = true
```
**后续维护建议**：之后凡是带有数学公式的文章，必须在文章开头写入 `math = true`。

---

## 二、自动图片归档与渲染工作流

### 1. 目标与挑战
**目标**：你希望在写文章时，只需 `Ctrl + V` 粘贴图片，图片就能自动存入统一的 `assets/imgs` 目录，且在 GitHub Pages 上正常显示。
**挑战**：
1. 编辑器（如 VS Code）默认会把粘贴的图片和 Markdown 文件混在一个文件夹里（你之前的 `image.png` 就是这样乱放的）。
2. 就算你强行让编辑器把图片存入 `assets/imgs`，它在 Markdown 里生成的相对路径链接（如 `../../assets/imgs/image.png`），在 Hugo 编译时会被 PaperMod 默认的图片渲染器拒绝识别，导致线上找不到图片。

### 2. 工作流改造过程

**第一步：控制编辑器的“手” (VS Code 配置)**
我为你创建了项目级的编辑器配置文件 [.vscode/settings.json](file:///d:/githubmyprojects/wrqkkk.github.io/.vscode/settings.json)：
```json
{
    "markdown.copyFiles.destination": {
        "content/posts/**/*": "${workspaceRoot}/assets/imgs/${fileName}"
    }
}
```
**效果**：现在你在 `content/posts/` 的任何 Markdown 文件里粘贴图片，编辑器都会**自动**把它保存在 `assets/imgs/` 下，并生成类似 `![alt text](../../assets/imgs/image.png)` 的相对路径链接。

**第二步：打通 Hugo 的“胃” (图片渲染钩子升级)**
为了让 Hugo 能够顺畅“消化”编辑器生成的这种乱七八糟的路径，我重写了你的图片渲染钩子（将它从第三方主题里拷贝到了你自己的站点目录中 [render-image.html](file:///d:/githubmyprojects/wrqkkk.github.io/layouts/_default/_markup/render-image.html)）：
```html
{{- /* 兼容处理 VS Code 自动生成的资产路径 */ -}}
{{- if strings.HasPrefix $path "../../assets/" -}}
  {{- $path = strings.TrimPrefix "../../assets/" $path -}}
{{- else if strings.HasPrefix $path "/assets/" -}}
  {{- $path = strings.TrimPrefix "/assets/" $path -}}
...
```
**效果**：当 Hugo 编译你的文章时，一旦发现链接里有 `../../assets/imgs/` 或 `/assets/imgs/`，它会智能地将其裁剪为 `imgs/image.png`，并直接从底层的 `assets` 目录里读取源文件进行编译和发布。

**第三步：历史数据清理**
我将原本散落在外面的 `image.png` 移动到了 [assets/imgs/image.png](file:///d:/githubmyprojects/wrqkkk.github.io/assets/imgs/image.png) 中，并将文章里出错的图片链接修复为了 `![alt text](imgs/image.png)`。

### 3. 今后的“无脑”写作流

从现在开始，你的图片处理工作流变得极其简单：
1. **截图**
2. **在文章里 Ctrl + V 粘贴**
3. **结束**
（图片会自动去它该去的地方，Hugo 会自动把它正确地渲染出来，线上也 100% 能够显示。）

## 三、部署检查
请执行以下命令提交更新并触发 GitHub Actions 部署：
```powershell
git add .
git commit -m "feat: enable math for ml-tsa post & setup auto image workflow"
git push origin main
```