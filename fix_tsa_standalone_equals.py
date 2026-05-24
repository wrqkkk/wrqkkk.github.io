from pathlib import Path

# Run from the repository root: D:\githubmyprojects\wrqkkk.github.io
path = Path("content/posts/TSA_final_review.md")

if not path.exists():
    raise FileNotFoundError(
        "Cannot find content/posts/TSA_final_review.md. "
        "Please run this script from the repository root."
    )

text = path.read_text(encoding="utf-8")
lines = text.splitlines()

out = []
in_display_math = False
changed = 0
i = 0

OPENERS = {r"\[", "$$"}
CLOSERS = {r"\]", "$$"}

while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    if stripped in OPENERS and not in_display_math:
        in_display_math = True
        out.append(line)
        i += 1
        continue

    if stripped in CLOSERS and in_display_math:
        in_display_math = False
        out.append(line)
        i += 1
        continue

    # Only repair a line that is exactly "=" inside a display math block.
    # It is changed from:
    #   previous line
    #   =
    #   next line
    # to:
    #   previous line
    #   = next line
    # This avoids Markdown Setext-heading parsing while preserving readable math blocks.
    if in_display_math and stripped == "=":
        if i + 1 < len(lines):
            next_line = lines[i + 1]
            next_stripped = next_line.strip()

            if next_stripped and next_stripped not in CLOSERS:
                indent = line[: len(line) - len(line.lstrip())]
                out.append(indent + "= " + next_line.lstrip())
                changed += 1
                i += 2
                continue

        # Fallback: if no safe next line exists, keep "=" but mark it non-heading by adding a space after it.
        out.append(line.rstrip() + " ")
        changed += 1
        i += 1
        continue

    out.append(line)
    i += 1

new_text = "\n".join(out)
if text.endswith("\n"):
    new_text += "\n"

path.write_text(new_text, encoding="utf-8")
print(f"Updated {path}. Repaired {changed} standalone equals lines inside display math blocks.")
print("Next commands:")
print("  hugo --cleanDestinationDir")
print("  Get-ChildItem public/posts/tsa_final_review/index.html | Select-String -Pattern '<h1 id=\"mu_tey_t\"'")
print("  git diff -- content/posts/TSA_final_review.md")
