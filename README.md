# 🔢 Next Sevenish Number

A minimal Python script that finds the **next integer greater than a given number** whose **digit sum is divisible by 7**.

---

## 📌 Problem Statement

Given an integer `n`, find the smallest integer greater than `n` such that:

```bash
sum_of_digits(x) % 7 == 0
```

---

## 🧠 Logic Overview

- Increment `n` by 1
- Compute the sum of its digits
- Repeat until the digit sum is divisible by 7

---

## 🧾 Example

| Input | Output | Reasoning                          |
|-------|--------|-------------------------------------|
| 26    | 32     | 2 + 6 = 8 → not valid → keep going |
| 999   | 1001   | 9 + 9 + 9 = 27 → not valid → keep going |

---

## 🧪 Function Reference

```python
def next_sevenish(n):
    def digit_sum(x):
        total = 0
        while x:
            total += x % 10
            x //= 10
        return total

    n += 1
    while digit_sum(n) % 7 != 0:
        n += 1

    return n
```

## 📁 Structure

.
├── main.py        # Core logic
└── README.md      # Documentation



## ✍️ Author

# **Crafted with clarity by Koorosh**


---

Let me know if you want to add a Persian version too — I can mirror it line by line.

