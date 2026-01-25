+++
date = '2026-01-25T12:00:00+08:00' draft = false title = 'The art of 'at most''
+++

# The art of 'at most'

As we all know, to calculate 'exactly' is notoriously difficult. Why? For example, when we write an assignment on paper, a minimum word‑count line is often printed so that readers does not need to count every word to know whether the requirement is met; a single glance tells them whether the text reaches at least that line and gives an approximate conclusion that it passes.

This is the essence of an “at most / at least” condition: it is **visible**, **monotone**, and **easy to verify**. You only need to check whether something crosses a threshold.

By contrast, checking **exactly** how many words there are requires a precise count. Precision destroys the convenience of monotonicity. It turns a simple inequality into a sharp equality, and sharp equalities are always harder to work with.
