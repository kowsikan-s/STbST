# Sub-Tree balanced Splay Tree

## What is this project?

This project is a **Python program** that demonstrates a special kind of data structure called a **Splay Tree**.  
Think of it like a smart filing cabinet:

- When you look for a file, the cabinet rearranges itself so that file is right on top next time.
- Over time, the most frequently used files stay easy to reach.
- To keep the cabinet tidy, the program also balances the left and right sections so they don’t get too lopsided.

In short: it’s a tree that **learns from your usage patterns** and keeps itself organized.

---

## Why does it matter?

Even if you’re not a programmer, here’s why this idea is cool:

- **Fast access to recent items**: The tree automatically moves recently used items to the top.
- **Self‑organizing**: You don’t have to manually sort or rearrange things.
- **Balanced subtrees**: The left and right sides stay neat, so searches don’t slow down.

This combination makes it efficient for scenarios where some items are accessed much more often than others.

---

## Features

- Insert new numbers into the tree.
- Search for a number (it moves to the top if found).
- Delete a number.
- Print the tree contents in sorted order.
- Built‑in tests to check that everything works correctly.

---

## How to run

1. Make sure you have **Python 3.8+** installed.
2. Save the code into a file called `splay_tree.py`.
3. Open a terminal (Command Prompt, PowerShell, or macOS/Linux shell).
4. Run:

   ```bash
   python stbst_height_rotation.py


## Complexity comparision
| Operation  | Standard Splay Tree                  | Hybrid (with balancing) | Balancing Step Alone   |
|------------|--------------------------------------|-------------------------|------------------------|
| Insert     | Amortized O(log n), worst O(n)       | Worst O(n)              | O(n^2) worst           |
| Search     | Amortized O(log n), worst O(n)       | Worst O(n)              | O(n^2) worst           |
| Delete     | Amortized O(log n), worst O(n)       | Worst O(n)              | O(n^2) worst           |
| Traversal  | O(n)                                 | O(n)                    | N/A                    |
| Space      | O(n)                                 | O(n)                    | O(n)                   |
