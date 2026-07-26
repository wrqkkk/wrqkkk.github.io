# Interactive Room MVP — Technical Archive

> **Mandatory pre-flight for future work:** Read this document before modifying the interactive room, its Hugo shortcode, the navigation menu, or the GitHub Pages deployment workflow.

This document records the product intent, final MVP architecture, implementation details, deployment workflow, debugging history, validation procedure, and lessons learned while building the first version of **Rockkie's Room** for `wrqkkk.github.io`.

## 1. Project objective

The interactive room adds a personal, life-oriented layer to the website. It is not intended to be another technical dashboard. The room acts as a visual index of meaningful objects and stories.

The MVP includes:

- a Stephen Curry jersey for an article about an idol and personal influence;
- a basketball for an article about passion;
- a dumbbell for fitness and training;
- a foam roller for an injury and recovery story;
- a CD player for music;
- a bookshelf reserved for a future PDF library and reading-tracking system;
- a simple room containing a desk, bed, window, chair, and bookshelf;
- hover or keyboard-focus tooltips;
- click or tap navigation to story placeholders;
- light and dark theme support;
- responsive behavior without JavaScript.

The public route is:

```text
https://wrqkkk.github.io/room/
```

## 2. MVP scope

### Included

- Hugo content page and global navigation entry.
- CSS-drawn room and objects.
- Six interactive hotspots.
- In-page story placeholders.
- Dark-mode color variables.
- A rotating CD animation and twinkling night-window stars.
- Keyboard-focus styles and ARIA labels.
- Reduced-motion handling.
- GitHub Pages deployment through the existing Hugo workflow.

### Deliberately deferred

- Pixel-art image assets.
- A character walking around the room.
- JavaScript modal dialogs.
- Separate published essays for every object.
- Zotero synchronization.
- PDF hosting and public/private access control.
- Reading-time logging, progress tracking, streaks, and statistics.
- A GitHub README preview linking into the room.

The MVP validates the interaction model before investing in detailed illustration or a full reading system.

## 3. Final repository structure

The successful implementation uses the following files:

```text
wrqkkk.github.io/
├── content/
│   └── room.md
├── layouts/
│   └── shortcodes/
│       └── room.html
├── assets/
│   └── room/
│       └── room-source.html
├── docs/
│   └── Interactive-Room-MVP-Technical-Archive-072726.md
├── hugo.toml
└── .github/
    └── workflows/
        └── hugo.yml
```

### Responsibility of each file

| File | Responsibility |
|---|---|
| `content/room.md` | Defines the Hugo page metadata and invokes the room shortcode. |
| `layouts/shortcodes/room.html` | Loads the room source and emits it as trusted HTML. |
| `assets/room/room-source.html` | Stores the complete room CSS and HTML source. |
| `hugo.toml` | Adds the global `Room` navigation entry. |
| `.github/workflows/hugo.yml` | Builds the entire Hugo site and deploys it to GitHub Pages. |

## 4. Current rendering pipeline

The current page flow is:

```text
content/room.md
    ↓
{{< room >}}
    ↓
layouts/shortcodes/room.html
    ↓
readFile "assets/room/room-source.html"
    ↓
split the preserved original front matter at "+++"
    ↓
output the HTML/CSS body through safeHTML
    ↓
PaperMod page template
    ↓
public/room/index.html
```

### `content/room.md`

The content file must remain small:

```toml
+++
title = "Rockkie's Room"
date = "2026-07-27T00:00:00+08:00"
draft = false
description = "A small interactive room built from the things that matter to me."
ShowToc = false
hidemeta = true
ShowReadingTime = false
ShowBreadCrumbs = false
+++

{{< room >}}
```

Do not place the full room HTML back into this Markdown file. Large indented HTML blocks separated by blank lines can be reinterpreted by Goldmark as Markdown code blocks.

### `layouts/shortcodes/room.html`

The final shortcode is:

```go-html-template
{{- $source := readFile "assets/room/room-source.html" -}}
{{- $parts := split $source "+++" -}}
{{- if ge (len $parts) 3 -}}
  {{- index $parts 2 | safeHTML -}}
{{- else -}}
  {{- errorf "The interactive room source is missing its expected TOML front matter boundary." -}}
{{- end -}}
```

The error guard is important. A malformed or cleaned-up source file should fail the build clearly rather than silently rendering an empty page.

### Why the source file still contains front matter

`assets/room/room-source.html` currently reuses the exact blob from the original 748-line `content/room.md`. That blob contains both TOML front matter and the complete `<style>` plus room HTML.

Reusing the original blob avoided reconstructing hundreds of lines manually during debugging. The shortcode therefore splits the source on `+++` and emits only the third segment.

This is a stable MVP arrangement, but it is transitional. A future cleanup may:

1. remove the preserved front matter from `room-source.html`;
2. leave only `<style>...</style>` and the room HTML;
3. simplify the shortcode to:

```go-html-template
{{- readFile "assets/room/room-source.html" | safeHTML -}}
```

Do that cleanup only in a separately validated change.

## 5. Navigation integration

The global menu entry in `hugo.toml` is:

```toml
[[menu.main]]
  name = "Room"
  url = "/room/"
  weight = 17
```

Its intended position is:

```text
Posts → Updates → Room → Search → CV → Tags → Categories
```

The menu is global. `Posts`, `Search`, `Updates`, and normal content pages should all use the same PaperMod header.

When one or two routes appear to omit a newly added menu item while other routes show it, first test browser caching before creating a custom header override:

- hard refresh the affected route;
- open the exact route in a private/incognito window;
- clear site data for `wrqkkk.github.io`;
- verify that the route does not have a custom template;
- verify that the site was rebuilt after the configuration change.

Do not override PaperMod's header merely to solve a stale browser cache.

## 6. Room composition

The room is a responsive `16 / 9` scene rendered with HTML elements and CSS.

### Static room elements

- `.window`
- `.city`
- `.star`
- `.bed`
- `.desk`
- `.chair`

The floor and wall are layered CSS gradients on `.room-scene`.

### Interactive objects

Each interactive object is an anchor element with class `.room-object`.

| Object | Main class | Current target | Story meaning |
|---|---|---|---|
| Curry jersey | `.jersey` | `#idol` | Idol and personal influence |
| Bookshelf | `.bookshelf` | `#library` | Papers, PDFs, books, and notes |
| Basketball | `.basketball` | `#basketball` | Passion for basketball |
| Dumbbell | `.dumbbell` | `#fitness` | Fitness and strength training |
| Foam roller | `.roller` | `#injury` | Injury, rehabilitation, and recovery |
| CD player | `.cd-player` | `#music` | Music and personal memories |

Example interaction structure:

```html
<a
  class="room-object basketball"
  href="#basketball"
  aria-label="Open the story about basketball"
>
  <span class="room-tooltip">
    <strong>Basketball</strong>
    <small>More than a sport</small>
  </span>
</a>
```

When a real article is created, replace the fragment link with a stable Hugo route, for example:

```html
href="/posts/my-basketball-story/"
```

Do not remove the `aria-label` when changing the destination.

## 7. Tooltip and interaction behavior

Desktop interaction uses both hover and keyboard focus:

```css
.room-object:hover,
.room-object:focus-visible {
  transform: translateY(-3px) scale(1.045);
}

.room-object:hover .room-tooltip,
.room-object:focus-visible .room-tooltip {
  opacity: 1;
  transform: translate(-50%, 0);
}
```

The tooltip itself has `pointer-events: none`, so it does not block clicks on the underlying object.

On narrow screens, tooltips are hidden because hover is unreliable:

```css
@media (max-width: 720px) {
  .room-tooltip {
    display: none;
  }
}
```

The object anchors remain tappable.

## 8. Theme support

The room uses CSS custom properties under `.room-page`:

```css
.room-page {
  --room-wall: #f4efe7;
  --room-floor: #cda77a;
  --room-line: #3b342f;
  --room-accent: #6f42c1;
  --room-green: #40c463;
  --room-blue: #1d428a;
  --room-gold: #fdb927;
}
```

Dark mode overrides them through PaperMod's theme attribute:

```css
[data-theme="dark"] .room-page {
  --room-wall: #22283b;
  --room-floor: #46382f;
  --room-line: #e3e8f1;
  --room-accent: #bb9af7;
  --room-green: #73daca;
  --room-blue: #7aa2f7;
  --room-gold: #e0af68;
}
```

New objects should use these variables rather than introducing unrelated colors unless a real-world object requires a recognizable color.

## 9. Animation and accessibility

### Current animations

- The CD uses `room-spin`.
- Stars use `room-twinkle` in dark mode.
- Objects use short hover/focus transitions.

### Reduced motion

The source includes:

```css
@media (prefers-reduced-motion: reduce) {
  .room-page *,
  .room-page *::before,
  .room-page *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    scroll-behavior: auto !important;
    transition-duration: 0.01ms !important;
  }
}
```

Keep this block when adding future animation.

### Accessibility requirements for future objects

Every clickable object should have:

- an `<a>` element rather than a click-only `<div>`;
- a real `href`;
- an `aria-label` that explains the destination;
- visible focus behavior through `:focus-visible`;
- a sufficiently large click/tap area;
- reduced-motion compatibility.

## 10. Story placeholders

The MVP uses in-page cards so that interaction can be tested before essays are written.

Current sections:

- `#idol`
- `#basketball`
- `#fitness`
- `#injury`
- `#music`
- `#library`

The targeted card receives an accent border through `:target`.

As real articles are published, an object may link directly to its article while the placeholder card is either:

- removed;
- converted into a short introduction card;
- retained as a small index of related articles.

## 11. Future reading shelf

The bookshelf is a reserved entry point for a future reading system.

The intended long-term responsibility split is:

```text
Zotero
  ├── bibliographic metadata
  ├── PDFs
  ├── collections
  └── annotations

Reading log
  ├── reading sessions
  ├── minutes read
  ├── progress
  ├── last-read date
  └── status

Hugo website
  ├── public reading shelf
  ├── selected notes
  ├── progress visualizations
  └── motivation-oriented statistics
```

Do not turn the website into a second manually maintained Zotero database. The likely future workflow is:

1. create a dedicated public Zotero collection;
2. export or fetch selected metadata;
3. generate a JSON or Hugo data file;
4. keep private PDFs private unless redistribution is permitted;
5. display reading notes, status, and links rather than blindly publishing attachments;
6. store reading-session data separately from bibliographic metadata.

Potential public states:

```text
Unread
Reading
Finished
Paused
```

Potential metrics:

- weekly reading minutes;
- monthly completed papers;
- active reading streak;
- current-paper progress;
- number of Paper Cards produced;
- most recently resumed material;
- materials paused for the longest time.

This system was intentionally not implemented in the MVP.

## 12. Hugo and GitHub Pages deployment

The repository uses PaperMod and Hugo Extended.

The workflow in `.github/workflows/hugo.yml`:

1. checks out the repository with submodules;
2. installs Hugo Extended `0.164.0`;
3. runs:

```bash
hugo --minify
```

4. uploads the complete `public/` directory as a Pages artifact;
5. deploys it through `actions/deploy-pages`.

A change to `main` should trigger a full site build. The build is not intentionally incremental.

### Recommended local validation

Before future room changes are pushed, clone the repository and run:

```bash
git clone --recurse-submodules https://github.com/wrqkkk/wrqkkk.github.io.git
cd wrqkkk.github.io
hugo server -D
```

Then test:

```text
http://localhost:1313/room/
http://localhost:1313/posts/
http://localhost:1313/search/
```

For a production-style build:

```bash
hugo --minify
```

Inspect the generated page:

```text
public/room/index.html
```

## 13. Validation checklist

Run this checklist after every room-related change.

### Page rendering

- [ ] `/room/` loads without visible HTML source.
- [ ] No `<pre><code>` block contains room markup.
- [ ] The wall, floor, window, bed, desk, chair, and bookshelf render.
- [ ] The Curry jersey shows `CURRY` and `30`.
- [ ] The basketball, dumbbell, foam roller, and CD player render.

### Interaction

- [ ] Every object is clickable.
- [ ] Desktop hover displays the intended tooltip.
- [ ] Keyboard Tab focus displays the intended tooltip and focus state.
- [ ] Mobile tap activates the intended destination.
- [ ] The CD animation runs unless reduced motion is enabled.

### Theme and layout

- [ ] Light mode is readable.
- [ ] Dark mode is readable.
- [ ] The room remains inside its frame at desktop width.
- [ ] The page remains usable below 720 px.
- [ ] No tooltip is clipped in a critical way.

### Navigation

- [ ] `Room` appears on the home page.
- [ ] `Room` appears on `/posts/`.
- [ ] `Room` appears on `/updates/`.
- [ ] `Room` appears on `/search/`.
- [ ] `Room` appears on a normal article page.

### Build and deployment

- [ ] `hugo --minify` succeeds.
- [ ] No shortcode recursion occurs.
- [ ] No `readFile` target is missing.
- [ ] The GitHub Pages deployment completes.
- [ ] Hard refresh and incognito checks show the new version.

## 14. Safe modification workflow

Use this sequence for future changes.

1. Read this document.
2. Fetch the current versions of:
   - `content/room.md`;
   - `layouts/shortcodes/room.html`;
   - `assets/room/room-source.html`;
   - `hugo.toml`;
   - `.github/workflows/hugo.yml`.
3. Confirm the current `main` head before writing.
4. Make changes on a temporary branch when more than one file or more than a trivial edit is involved.
5. Run a local Hugo build, or at minimum use a PR build before updating `main`.
6. Verify both the source files and the generated page.
7. Use one coherent commit per completed change.
8. Re-read the commit diff after writing.
9. Test all major routes, not only `/room/`.
10. Only then report success.

## 15. Commit history relevant to the MVP

Key commits during this work included:

```text
dab4e5dd235b2699150b62f0e6bd538dc2f6b026
主页：新增互动房间 MVP
```

This introduced the first 748-line room directly in `content/room.md`.

Several intermediate debug commits used:

```text
主页：互动房间MVP显示异常debug
```

The successful architecture was finalized at:

```text
46c6de7e1550e77a6465cbcac9b9e40e3ab1de3e
主页：互动房间MVP显示异常debug
```

That commit attached the original room blob as `assets/room/room-source.html`, retained the small content page, and made the shortcode read the independent source file.

## 16. Future improvement roadmap

### Version 0.2 — visual asset replacement

- Replace CSS-drawn objects with custom pixel-art PNG layers.
- Keep the existing anchors and tooltip semantics.
- Use percentage positioning so hotspots remain responsive.
- Preserve CSS-drawn shapes as a fallback until the new scene is validated.

### Version 0.3 — richer room interaction

- Add small, restrained object animations.
- Consider object-specific focus outlines rather than rectangular hotspots.
- Add real articles for at least two objects before expanding the number of objects.
- Add a room preview to the GitHub profile README that links to `/room/`.

### Version 1.0 — reading shelf

- Create a dedicated `/library/` route.
- Connect a selected Zotero collection.
- Add reading status and progress.
- Add a separate low-friction reading-session log.
- Build motivating statistics without exposing private PDFs or notes.

## 17. Mistakes, debugging history, and lessons learned

This section is intentionally placed last so that future work can learn from the failed process rather than only from the final code.

### Mistake 1: placing a large HTML application directly inside Markdown

The initial room placed roughly 748 lines of CSS and HTML directly in `content/room.md`.

Goldmark accepted the beginning of a raw HTML block, but a blank line ended that block. Subsequent lines had four-space indentation, so Markdown interpreted them as an indented code block. The browser therefore displayed room source such as:

```html
<div class="bed" aria-hidden="true"></div>
```

instead of rendering it.

**Lesson:** Complex HTML components belong in shortcodes, partials, or templates. Markdown content should invoke them, not contain them.

### Mistake 2: confusing response truncation with missing file-read capability

A large `fetch_file` or `fetch_blob` response was truncated by the tool response budget. This was incorrectly described as the absence of an API for reading the full file.

The correct solution was to use `start_line` and `end_line` to read the file in multiple ranges.

**Lesson:** Distinguish an API capability limit from a single-response display limit. Check the tool schema before asking the user to upload a file unnecessarily.

### Mistake 3: creating a shortcode that referenced a file that did not yet exist

An intermediate shortcode read:

```go-html-template
readFile "assets/room/room-source.html"
```

before `assets/room/room-source.html` had been attached to the repository.

This created a broken intermediate commit.

**Lesson:** For a multi-file dependency, use an atomic Git tree/commit or a temporary branch. Do not update the consumer before its dependency exists.

### Mistake 4: creating a self-referential shortcode chain

After `content/room.md` had been reduced to:

```go-html-template
{{< room >}}
```

the shortcode was incorrectly changed to read `content/room.md` itself.

That produced this faulty dependency:

```text
room.md → room shortcode → room.md → room shortcode
```

The original room source was no longer available through that path.

**Lesson:** Draw the dependency graph before changing a template architecture. A content page must never be used as the independent source of the shortcode that it invokes.

### Mistake 5: reporting completion before re-reading every changed file

At multiple points, success was reported after a write without verifying all of:

- the new source file existed;
- the shortcode pointed to the correct file;
- the navigation entry was present;
- the commit contained exactly the intended paths;
- the deployed page rendered correctly.

**Lesson:** A write response is not proof of a successful feature. Re-fetch the files, inspect the commit, and validate the rendered result before reporting completion.

### Mistake 6: producing multiple debug commits despite an intended single commit

Sequential Contents API writes created multiple commits with the same debug message. The intended operation should have been atomic.

**Lesson:** When a change spans multiple dependent files, prefer one of these methods:

1. create blobs → create one tree → create one commit → fast-forward the branch;
2. use a temporary branch and squash before merge;
3. perform local changes and push one tested commit.

### Mistake 7: attributing route-specific navigation differences too quickly

When `Room` appeared on some pages but not on `Posts` and `Search`, caching was proposed before fully checking templates and the build process.

Caching turned out to be the practical cause, but the correct diagnostic order is:

1. inspect global menu configuration;
2. inspect route-specific layouts;
3. inspect the build workflow;
4. confirm the deployed revision;
5. test hard refresh and incognito mode.

**Lesson:** A correct final guess does not excuse an incomplete diagnostic process.

### Mistake 8: allowing status updates to become more confident than the evidence

Some status messages stated that navigation or page behavior had been completed before the repository and rendered page had both been verified.

**Lesson:** Report evidence, not intention. Use wording such as “the file write succeeded; rendered deployment is not yet verified” until the public page has been checked.

### Mistake 9: not using a local Hugo build before modifying `main`

The Goldmark code-block issue and the missing `readFile` dependency would have been caught immediately by a local `hugo server` or PR build.

**Lesson:** A Hugo component change should be treated as code, not as a simple Markdown edit. Build it before deployment.

## 18. Rules for the next implementation session

Before making any further room change, the assistant or developer must:

1. read this document;
2. inspect the five current source/configuration files listed in Section 14;
3. state the dependency graph of the proposed change;
4. avoid direct complex HTML in Markdown;
5. avoid self-referential shortcode reads;
6. create dependent files atomically;
7. validate with Hugo before updating `main` whenever possible;
8. re-read the final files and commit;
9. verify the public route and global navigation;
10. distinguish browser cache from repository or template defects.

The most important general lesson is:

> **Separate content, component source, template rendering, and deployment from the beginning. Then verify the complete dependency chain before claiming success.**
