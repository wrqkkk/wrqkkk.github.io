# Article Status Workflow

Article lifecycle is represented by the source folder. Do not duplicate the status in front matter.

## Folder structure

```text
content/posts/
├── updating/
├── paused/
└── finished/
```

- `updating`: actively written, reviewed, or expanded.
- `paused`: not actively maintained, but may be revisited.
- `finished`: complete within the current scope.

## Create a new article

```bash
hugo new content posts/updating/article-name.md
```

New articles are drafts by default.

## Change an article's status

Use `git mv` so Git can track the rename.

```bash
git mv "content/posts/updating/article-name.md" "content/posts/finished/article-name.md"
```

```bash
git mv "content/posts/updating/article-name.md" "content/posts/paused/article-name.md"
```

```bash
git mv "content/posts/updating/What-to-do-when-waiting-for-agents.md" "content/posts/paused/What-to-do-when-waiting-for-agents.md"
```

Public post URLs remain stable because Hugo permalinks ignore the lifecycle folder.

## Optional dashboard fields

Add these fields only when they are useful:

```toml
update_note = 'The main structure is stable; examples are still being added.'
next_step = 'Add the connection between projection and PCA reconstruction.'
```

Both fields are public because this repository and the Updates page are public.

## Images

Continue pasting images into `static/imgs/`. Images do not move when an article changes status. The Markdown image render hook accepts paths from nested article folders.

## Source of truth

- Status: lifecycle folder.
- Current public note: `update_note`.
- Next public action: `next_step`.
- Dashboard: generated automatically during the Hugo build.
