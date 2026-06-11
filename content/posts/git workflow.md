+++
date = '2026-06-10T16:40:00+08:00'
draft = false
title = 'git workflow'
isCJKLanguage = true
math = true
+++

下面这份可以当成你的 **Git 操作速查工作流**。我按你实际最常遇到的情况写，默认你在 Windows PowerShell 里操作，仓库例子用你的 GitHub Pages 项目风格：`D:\githubmyprojects\wrqkkk.github.io`。真正用的时候把路径、仓库名、commit message 换成自己的。

---

# Step 0 Check

进入仓库目录后，先看三个东西：**当前在哪个仓库、远端连到哪里、现在有哪些改动**。

```powershell
cd D:\githubmyprojects\wrqkkk.github.io

git status
git branch -vv
git log --oneline -5
```

Hugo / GitHub Pages 项目，建议每次提交前额外检查一次：

```powershell
git status --ignored -s
```

我们希望看到 `public/` 是：

```powershell
!! public/
```

如果看到：

```powershell
?? public/
```

说明 `public/` 没有被 ignore，**这时候不要 `git add .`**，否则 Hugo build 产物会被提交进去，这里的产物比较大，无法git，会报错。

---

# Scenario 1：已有仓库，一直正常 add / commit / push

这是最常规流程。先进入仓库，查看状态。

```powershell
cd D:\githubmyprojects\wrqkkk.github.io

git status
git remote -v
git branch -vv
```

确认没问题后，先看自己改了什么。

```powershell
git diff
```

如果只想看文件列表，用：

```powershell
git diff --stat
```

然后加入暂存区。一般项目 `.gitignore` 配好以后，可以用：

```powershell
git add .
```

然后可以先看status，防止错误地上传大文件：

```powershell
git status --short
```

确认没有奇怪文件以后再 commit：

```powershell
git commit -m "Fix stochastic analysis math rendering"
```

提交后推送：

```powershell
git push
```

如果本地落后于远端，`git push` 可能会失败，提示你先 pull。这个时候不要慌，先用 rebase 拉远端更新：

```powershell
git pull --rebase
```

如果没有冲突，再推送：

```powershell
git push
```

如果有冲突，Git 会告诉你哪些文件冲突。你手动打开文件，解决 `<<<<<<<`、`=======`、`>>>>>>>` 这些冲突标记，然后：

```powershell
git add .
git rebase --continue
git push
```

如果 rebase 搞乱了，想退出这次 rebase：

```powershell
git rebase --abort
```

---

# Scenario 2：已有仓库，但本地没连接上，需要手动关联远端和使用者

这种情况通常表现为：本地文件夹里有项目，但 `git remote -v` 没有输出，或者远端地址错了，或者 push 时提示身份不对。

先进入项目目录：

```powershell
cd D:\githubmyprojects\wrqkkk.github.io
```

确认这个目录是不是 Git 仓库：

```powershell
git status
```

如果提示不是 Git 仓库，初始化：

```powershell
git init
```

然后设置 Git 使用者。这个是写进 commit 记录里的名字和邮箱，不等于登录 GitHub，但最好和 GitHub 邮箱一致。

全局设置：

```powershell
git config --global user.name "username"
git config --global user.email "github email"
```

只给当前仓库设置：

```powershell
git config user.name "username"
git config user.email "github email"
```

检查设置：

```powershell
git config --global --list
git config --list
```

接着关联远端。先看有没有已有 remote：

```powershell
git remote -v
```

如果没有 remote，用 SSH：

```powershell
git remote add origin git@github.com:wrqkkk/wrqkkk.github.io.git
```

或者用 HTTPS：

```powershell
git remote add origin https://github.com/wrqkkk/wrqkkk.github.io.git
```

如果 remote 已经存在但地址错了，用：

```powershell
git remote set-url origin git@github.com:wrqkkk/wrqkkk.github.io.git
```

检查：

```powershell
git remote -v
```

然后确认分支名字。现在 GitHub 默认通常是 `main`：

```powershell
git branch
```

如果你当前分支叫 `master`，想改成 `main`：

```powershell
git branch -M main
```

接着把本地分支和远端分支关联。若远端已经有内容，先 fetch：

```powershell
git fetch origin
```

如果远端已经有 `main`，并且你想把远端内容合进本地：

```powershell
git pull origin main --rebase
```

然后正常提交：

```powershell
git add .
git commit -m "Update notes"
git push -u origin main
```

这里的 `-u` 很重要，它会建立本地 `main` 和远端 `origin/main` 的追踪关系。之后你就可以直接：

```powershell
git push
```

如果 push 时提示权限问题，先测试 SSH：

```powershell
ssh -T git@github.com
```

如果你用 HTTPS，GitHub 现在通常需要 token，而不是普通密码。最简单是改用 SSH remote：

```powershell
git remote set-url origin git@github.com:wrqkkk/wrqkkk.github.io.git
```

---

# Scenario 3：一个全新仓库

全新仓库有两种做法。最稳的是先在 GitHub 网页上创建空仓库，不要勾选 README、`.gitignore`、license，然后本地初始化并推上去。

先进入你准备放项目的文件夹：

```powershell
cd D:\githubmyprojects
mkdir my-new-repo
cd my-new-repo
```

初始化 Git：

```powershell
git init
git branch -M main
```

设置使用者，如果你已经全局设置过，可以跳过：

```powershell
git config user.name "wrqkkk"
git config user.email "你的GitHub邮箱@example.com"
```

创建 `.gitignore`。如果是 Hugo / GitHub Pages 源码仓库，建议一开始就写好：

```powershell
@"
# Hugo generated files
public/
resources/_gen/
.hugo_build.lock

# OS / editor
.DS_Store
Thumbs.db
.vscode/
"@ | Set-Content .gitignore -Encoding UTF8
```

如果你很担心 Windows BOM 污染第一条 ignore 规则，可以用我们之前那个更稳的 PowerShell 写法：

```powershell
[System.IO.File]::WriteAllText(
  ".gitignore",
  "# Hugo generated files`npublic/`nresources/_gen/`n.hugo_build.lock`n`n# OS / editor`n.DS_Store`nThumbs.db`n.vscode/`n",
  (New-Object System.Text.UTF8Encoding $false)
)
```

创建 README：

```powershell
"# my-new-repo" | Set-Content README.md -Encoding UTF8
```

检查状态：

```powershell
git status --ignored -s
```

提交：

```powershell
git add .
git commit -m "Initial commit"
```

关联 GitHub 远端：

```powershell
git remote add origin git@github.com:wrqkkk/my-new-repo.git
```

第一次推送：

```powershell
git push -u origin main
```

如果你在 GitHub 创建仓库时勾选了 README，远端已经有一个 commit，本地第一次 push 可能失败。这时先拉远端：

```powershell
git pull origin main --rebase
git push -u origin main
```

---

# Scenario 4：push 不成功或 Actions / Pages 出问题，怎么排查

先不要乱 reset。第一步永远是看状态和远端。

```powershell
git status
git remote -v
git branch -vv
git log --oneline -5
```

如果是 push 失败，把终端报错原样读一下。Git 报错通常已经告诉你原因。下面是你最容易遇到的几类。

---

## 情况 A：本地落后远端，push 被拒绝

典型提示是 `non-fast-forward` 或 `fetch first`。意思是远端有你本地没有的 commit。

先拉取远端并 rebase：

```powershell
git pull --rebase
```

如果成功：

```powershell
git push
```

如果有冲突，解决冲突后：

```powershell
git add .
git rebase --continue
git push
```

想放弃这次 rebase：

```powershell
git rebase --abort
```

---

## 情况 B：commit message 写错了

如果还没 push：

```powershell
git commit --amend -m "新的 commit 名字"
git push
```

如果已经 push：

```powershell
git commit --amend -m "新的 commit 名字"
git push --force-with-lease
```

这里用 **`--force-with-lease`**，不要用裸 `--force`。它会先确认远端没有别人新推的东西，更安全。

---

## 情况 C：刚 commit 了不该 commit 的东西，但还没 push

如果想撤销最新 commit，但保留文件改动：

```powershell
git reset --mixed HEAD~1
```

然后重新检查：

```powershell
git status
```

如果是不小心把 `public/` staged 了，先从暂存区拿掉：

```powershell
git restore --staged public
```

如果是不小心把某个文件改坏了，想丢弃这个文件的本地修改：

```powershell
git restore "path/to/file.md"
```

如果想丢弃所有未提交修改，非常危险，确认后再用：

```powershell
git restore .
```

---

## 情况 D：已经 push 了错误 commit，想撤回

如果只是你自己的个人仓库，并且确定不会影响别人，可以回退到上一个 commit：

```powershell
git reset --hard HEAD~1
git push --force-with-lease
```

如果你不想改历史，想用一个新 commit 抵消上一个 commit，用：

```powershell
git revert HEAD
git push
```

两者区别很重要。`reset --hard` 是改历史，`revert` 是新增一个“反向提交”。个人笔记仓库用 `reset --hard + --force-with-lease` 可以，但多人协作项目更推荐 `revert`。

---

## 情况 E：上传了过大文件，push 被 GitHub 拒绝

GitHub 单文件超过限制时，push 会失败。你先找大文件：

```powershell
git rev-list --objects --all | sort
```

这个命令不太直观。PowerShell 下更实用的是先看当前目录大文件：

```powershell
Get-ChildItem -Recurse -File | Sort-Object Length -Descending | Select-Object -First 20 FullName,Length
```

如果大文件只是工作区里没 commit，先加入 `.gitignore`，例如 Hugo 项目：

```powershell
[System.IO.File]::WriteAllText(
  ".gitignore",
  "# Hugo generated files`npublic/`nresources/_gen/`n.hugo_build.lock`n",
  (New-Object System.Text.UTF8Encoding $false)
)
```

确认 ignore 生效：

```powershell
git check-ignore -v public/index.json
git status --ignored -s
```

你希望看到：

```powershell
!! public/
```

如果大文件已经 staged：

```powershell
git restore --staged public
```

如果大文件已经 commit 但还没 push：

```powershell
git reset --mixed HEAD~1
```

然后修 `.gitignore`，再重新 add / commit。

如果大文件已经进入更早的历史，普通删除不够，因为 GitHub 会检查整个历史。个人仓库可以用 `git filter-repo` 或 BFG 清历史。更现代的方式是安装 `git-filter-repo` 后：

```powershell
git filter-repo --path public/index.json --invert-paths
git push --force-with-lease
```

如果整个 `public/` 都进过历史：

```powershell
git filter-repo --path public/ --invert-paths
git push --force-with-lease
```

这个操作会重写历史，做之前先备份仓库文件夹。

---

## 情况 F：Hugo / GitHub Pages 的 `public/` 又被加进去了

这是你刚遇到过的典型坑。先看：

```powershell
git status --ignored -s
```

如果看到：

```powershell
?? public/
```

说明 `public/` 没被忽略。先修 `.gitignore`：

```powershell
[System.IO.File]::WriteAllText(
  ".gitignore",
  "# Hugo generated files`npublic/`nresources/_gen/`n.hugo_build.lock`n",
  (New-Object System.Text.UTF8Encoding $false)
)
```

验证：

```powershell
git check-ignore -v public/index.json
git status --ignored -s
```

正确状态是：

```powershell
!! public/
```

如果 `public/` 已经 staged：

```powershell
git restore --staged public
```

如果 `public/` 已经 commit 但没 push：

```powershell
git reset --mixed HEAD~1
```

然后重新：

```powershell
git add .gitignore
git add "content/posts/你真正改的文章.md"
git commit -m "Fix notes"
git push
```

以后每次 `git add .` 之前先跑：

```powershell
git status --ignored -s
```

只要 `public/` 是 `!! public/`，就可以放心。

---

## 情况 G：GitHub Actions 没显示、显示奇怪、或者时间像未来

先本地看最新 commit：

```powershell
git log --pretty=fuller -1
```

这里会显示 `AuthorDate` 和 `CommitDate`。如果你的电脑系统时间错了，commit 时间可能跑到未来，GitHub 页面和 Actions 排序可能会很怪。先修电脑系统时间，然后修最新 commit 的时间。

如果 commit 还没 push，直接 amend：

```powershell
git commit --amend --no-edit --reset-author
```

然后：

```powershell
git log --pretty=fuller -1
git push
```

如果已经 push，修完后需要：

```powershell
git commit --amend --no-edit --reset-author
git push --force-with-lease
```

如果你想手动指定当前时间，在 PowerShell 里可以这样：

```powershell
$now = Get-Date -Format "yyyy-MM-ddTHH:mm:ssK"
$env:GIT_AUTHOR_DATE = $now
$env:GIT_COMMITTER_DATE = $now
git commit --amend --no-edit --date="$now"
git push --force-with-lease
```

Actions 不显示时，还要确认 workflow 文件是否存在：

```powershell
dir .github\workflows
```

看最近一次 push 的 commit：

```powershell
git log --oneline -1
```

如果你要重新触发 GitHub Actions，最简单可以做一个空 commit：

```powershell
git commit --allow-empty -m "Trigger GitHub Actions"
git push
```

如果是 Actions 失败，去 GitHub 页面点 Actions 看失败日志。若要本地先跑 Hugo build：

```powershell
hugo
```

或者如果你项目用了 extended 版 Hugo，需要确认本地和 Actions 里的 Hugo 版本一致。

---

## 情况 H：push 提示认证失败

如果用 HTTPS，可能提示密码不对。GitHub 不接受账户密码 push，通常要 token。更推荐改 SSH：

```powershell
git remote set-url origin git@github.com:wrqkkk/wrqkkk.github.io.git
ssh -T git@github.com
git push
```

如果 SSH 还没配置，需要生成 key：

```powershell
ssh-keygen -t ed25519 -C "你的GitHub邮箱@example.com"
```

一路回车，然后查看公钥：

```powershell
cat ~/.ssh/id_ed25519.pub
```

复制输出内容，去 GitHub 的 SSH keys 里添加。

---

## 情况 I：分支名不对，比如本地是 master，远端是 main

查看分支：

```powershell
git branch -vv
```

改成本地 `main`：

```powershell
git branch -M main
```

推送并关联：

```powershell
git push -u origin main
```

如果远端默认分支还在 `master`，需要去 GitHub 仓库设置里改 default branch，或者继续使用远端实际分支名。

---

## 情况 J：想知道这次 commit 到底改了什么

看最近一次 commit 的文件统计：

```powershell
git show --stat --oneline HEAD
```

看具体 diff：

```powershell
git show HEAD
```

看 staged 了什么：

```powershell
git diff --cached --stat
git diff --cached
```

看工作区还没 staged 的改动：

```powershell
git diff
```

这几个命令特别适合防止你再次把 `public/`、大 JSON、build 产物、临时文件误提交。

---

# 你以后最稳的日常模板

对你的 GitHub Pages / Hugo 笔记仓库，我建议以后每次都这样走：

```powershell
cd D:\githubmyprojects\wrqkkk.github.io

git status --ignored -s
git check-ignore -v public/index.json

git diff --stat
git add .
git status --short
git diff --cached --stat

git commit -m "Update stochastic analysis notes"
git push
```

如果 `git status --short` 或 `git diff --cached --stat` 里出现了 `public/`，立刻停下：

```powershell
git restore --staged public
git status --ignored -s
```

确认 `public/` 是 `!! public/` 以后再继续。
