# Hugo Article Status Refactor Record (072426)

## 1. Background

The original repository stored all Markdown posts directly under:

```text
content/posts/
```

As the number of articles increased, this flat structure created two related problems:

1. The author could not see which articles were actively maintained, temporarily paused, or complete without opening each file.
2. The public `Updates` page relied on a manually maintained table, which could drift away from the real state of the source files.

The goal of this refactor was to make article lifecycle visible in the local file tree while keeping the public site stable.

## 2. Final lifecycle structure

Article status is now represented by the source folder:

```text
content/posts/
├── updating/
├── paused/
└── finished/
```

The meanings are:

- `updating`: actively written, reviewed, reorganized, or expanded.
- `paused`: not actively maintained at the moment, but may be revisited.
- `finished`: complete within the current scope; only minor corrections or link maintenance are expected.

The folder is the single source of truth. A duplicate `status` front matter field should not be added.

During the initial migration, all 38 existing Markdown posts were moved into `content/posts/updating/` without changing their contents. GitHub recognized these operations as zero-content-change renames.

## 3. Changes implemented

### 3.1 Stable public post URLs

Moving a source file into a nested lifecycle folder would normally change its Hugo URL. A permalink rule was added to `hugo.toml`:

```toml
[permalinks]
  [permalinks.page]
    posts = '/posts/:slugorcontentbasename/'
```

Therefore, these source paths:

```text
content/posts/updating/article.md
content/posts/paused/article.md
content/posts/finished/article.md
```

all use the same public URL:

```text
/posts/article/
```

Lifecycle folder names do not appear in public post URLs.

### 3.2 Automatic Updates dashboard

The manually maintained status table in `content/updates.md` was replaced by:

```go-html-template
{{< article-status-table >}}
```

The shortcode is implemented at:

```text
layouts/shortcodes/article-status-table.html
```

It automatically groups public posts into:

- Updating
- Paused
- Finished

The dashboard reads:

- article title from `title`;
- lifecycle status from the source folder;
- category from `categories`;
- current note from `update_note`;
- next action from `next_step`.

Draft posts remain in their lifecycle folders but are excluded from the public dashboard by Hugo's normal draft filtering.

### 3.3 Optional author-facing fields

The default article archetype now includes:

```toml
update_note = ''
next_step = ''
```

These fields are optional. They are intended to make the public Updates dashboard useful as an author control panel.

Because the repository and website are public, these fields must not contain private information.

### 3.4 Nested image path compatibility

Article images remain centralized under:

```text
static/imgs/
```

Only Markdown files move between lifecycle folders. Image files do not move.

The render hook at:

```text
layouts/_default/_markup/render-image.html
```

was updated to accept any number of leading `../` segments. It therefore supports image references generated from both the former flat folder and the new nested folders, including:

```text
../../static/imgs/example.png
../../../static/imgs/example.png
/static/imgs/example.png
```

Legacy `assets/` resource references remain supported.

### 3.5 Reproducible Hugo builds

The GitHub Actions workflow now pins Hugo Extended to:

```text
0.164.0
```

Pull requests run the Hugo build but do not deploy. Pushes to `main` continue to build and deploy GitHub Pages.

This prevents an unreviewed Hugo upgrade from silently changing future builds.

## 4. Files added or modified

### Added

```text
content/posts/paused/.gitkeep
content/posts/finished/.gitkeep
layouts/shortcodes/article-status-table.html
docs/Article-Status-Workflow.md
docs/Hugo-Article-Status-Refactor-072426.md
```

### Modified

```text
.github/workflows/hugo.yml
archetypes/default.md
content/updates.md
hugo.toml
layouts/_default/_markup/render-image.html
```

### Moved

All existing files formerly matching:

```text
content/posts/*.md
```

were moved to:

```text
content/posts/updating/*.md
```

## 5. Validation completed

The refactor was implemented through pull request #1 and merged into `main`.

Validation results:

- all 38 post moves were recognized as renames with no content changes;
- Hugo Extended 0.164.0 completed the pull-request build successfully;
- the PR deployment job was skipped as intended;
- draft flags were preserved;
- the only source-path-dependent `relref` references were removed with the old manual Updates table;
- Markdown article images continue to use the centralized image workflow;
- the lifecycle folders are not exposed as public subsections.

Merged commit:

```text
4a485b0a6193978de1c3d9025eeb75b0571f817d
```

## 6. Local synchronization after the refactor

Open PowerShell in the repository:

```powershell
cd D:\githubmyprojects\wrqkkk.github.io
```

First inspect the working tree:

```powershell
git status -sb
```

### Clean working tree

When there are no local changes:

```powershell
git switch main
git pull --ff-only origin main
git submodule update --init --recursive
```

Then verify the new structure:

```powershell
Get-ChildItem content\posts
Get-ChildItem content\posts\updating
```

### Working tree with local changes

Save the local work before pulling:

```powershell
git add -A
git commit -m "Save local work before article lifecycle sync"
git pull --rebase origin main
```

If Git reports a conflict, do not force the pull or delete either version. Inspect the conflict first. To return safely to the pre-rebase state:

```powershell
git rebase --abort
```

The most likely conflict is an edited article whose remote path moved from `content/posts/` to `content/posts/updating/`.

## 7. Local verification

Start the local site:

```powershell
hugo server -D
```

Check:

1. `/posts/` still lists the articles.
2. `/updates/` shows the automatic Updating, Paused, and Finished dashboard.
3. Existing post URLs do not contain `/updating/`.
4. Existing article images render correctly.
5. A newly pasted image in an article under `content/posts/updating/` is saved to `static/imgs/` and renders locally.
6. Draft articles are visible only because `-D` was used; they remain excluded from production builds.

## 8. Daily author workflow

Create a new article:

```powershell
hugo new content posts/updating/article-name.md
```

Mark an article as finished:

```powershell
git mv "content/posts/updating/article-name.md" "content/posts/finished/article-name.md"
```

Pause an article:

```powershell
git mv "content/posts/updating/article-name.md" "content/posts/paused/article-name.md"
```

Resume a paused article:

```powershell
git mv "content/posts/paused/article-name.md" "content/posts/updating/article-name.md"
```

After moving a file, run the local Hugo server and verify the article before committing.

## 9. Current design boundary

This refactor intentionally does not add status badges to post cards or article headers. The current scope is:

- author-visible lifecycle folders;
- stable public URLs;
- safe image references;
- an automatic public Updates dashboard.

Status badges can be added later as a separate presentation-layer change after the folder workflow has been used and validated in normal writing.
