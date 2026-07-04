# Hugo 静态图片与首页头像工作流迁移记录（070426）

## 一、问题背景
在原始 Hugo + PaperMod 博客结构中，图片管理同时存在三套体系：

一类是 `assets/imgs` + Hugo Resources 管线；
一类是 VS Code 自动粘贴到 `content/posts` 的本地文件；
还有一类是手动维护的 Markdown 相对路径（如 ../../assets/imgs/...）。

这导致两个核心问题：

首先，Markdown 预览与 Hugo 渲染路径不一致。编辑器生成的相对路径在本地可见，但在 GitHub Pages 上会失效或变形。

其次，旧的 assets 工作流依赖 `resources.Get`，对非资源管线路径不稳定，而新的粘贴路径又不断产生混乱的 ../../assets 结构。

## 二、此次结构性改动

### 1. 统一图片存储策略
本次将图片系统统一迁移为：

- 首页头像：`static/images/avatar.jpg`
- 文章图片：`static/imgs/*`

对应网页路径变为：

- `/images/avatar.jpg`
- `/imgs/xxx.png`

从而完全绕开 Hugo assets 管线的不确定性。

---

### 2. VS Code 自动粘贴路径修正
修改 `.vscode/settings.json`：

将原来的 assets 路径：
```
${workspaceRoot}/assets/imgs/${fileName}
```

统一改为：
```
${workspaceRoot}/static/imgs/${documentBaseName}-${fileName}
```

作用：
粘贴图片时直接进入 Hugo 可发布目录 static/imgs。

---

### 3. Hugo 图片渲染层升级
修改 `layouts/_default/_markup/render-image.html`：

新增逻辑：

- 识别 `../../static/`、`/static/`、`static/`
- 自动转换为 `/imgs/...` 或 `/xxx` 公开路径
- 同时保留旧 assets/imgs 兼容逻辑

这样保证三种输入都可用：

```
/imgs/a.png
static/imgs/a.png
../../static/imgs/a.png
```

均能正确渲染为网站可访问资源。

---

### 4. 头像系统修复
hugo.toml profileMode 已启用，并统一为：

```
imageUrl = "/images/avatar.jpg"
```

头像不再依赖 assets pipeline，避免构建失败或路径污染。

---

## 三、最终稳定工作流（当前版本）

### 写作流程
1. 截图或复制图片
2. 粘贴到 Markdown
3. 自动进入 static/imgs
4. Markdown 中引用 /imgs/xxx.png
5. Hugo server 自动可见

---

### 路径规范

| 类型 | 路径 | 输出 |
|------|------|------|
| 头像 | static/images/avatar.jpg | /images/avatar.jpg |
| 文章图 | static/imgs/xxx.png | /imgs/xxx.png |

---

## 四、关键修复点总结

本次修复本质上解决的是三层路径冲突问题：

1. 编辑器路径（../../static）
2. Hugo 构建路径（/imgs）
3. 资源管线路径（assets/imgs）

通过 render-image hook + static 统一入口，实现三者收敛。

---

## 五、建议（未来优化方向）

后续可进一步升级为 Page Bundle 模式（content/posts/post1/index.md + images），实现文章级封装，但当前 static 方案已足够稳定。
