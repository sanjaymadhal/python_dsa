# 📊 01 — Complexity Analysis

> Before writing a single line of DSA code, you need to speak the language of **efficiency**.
> Complexity analysis is how we measure *how fast* an algorithm runs and *how much memory* it uses — independent of hardware.

---

## 🧭 Why This Comes First

Every DSA problem has multiple solutions. Complexity analysis is the tool that tells you:
- Is this solution *good enough*?
- Will it break when input size grows from 100 → 1,000,000?
- Which of two working solutions is *actually better*?

Without this, you're coding blind.

---

## ⏱️ Time Complexity vs 🧠 Space Complexity

| | What it measures | Unit |
|---|---|---|
| **Time Complexity** | How runtime grows as input size `n` grows | Operations |
| **Space Complexity** | How memory usage grows as input size `n` grows | Memory units |

Both are expressed using **Big-O Notation**.

---

## 📐 Big-O Notation

Big-O describes the **upper bound** (worst case) of growth. We drop constants and lower-order terms because we care about the *shape* of growth, not the exact number.

```
f(n) = 3n² + 5n + 100  →  O(n²)
```

Why? Because as `n → ∞`, the `n²` term dominates completely.

---

## 🎯 The 7 Complexities You Must Know

Listed from best to worst:

### 1. O(1) — Constant
Runtime doesn't change no matter how large the input is.
```python
def get_first(arr):
    return arr[0]  # Always 1 operation
```

### 2. O(log n) — Logarithmic
Each step cuts the problem in half. Very efficient.
```python
# Binary search — halves the search space each step
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1
```

### 3. O(n) — Linear
One pass through all elements. Grows proportionally with input.
```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:        # n iterations
        if num > max_val:
            max_val = num
    return max_val
```

### 4. O(n log n) — Linearithmic
Typical of efficient sorting algorithms. Slightly worse than linear, much better than quadratic.
```python
# Merge Sort is O(n log n)
# n elements × log n levels of recursion
sorted_arr = sorted(arr)  # Python's Timsort is O(n log n)
```

### 5. O(n²) — Quadratic
Nested loops over the same data. Gets slow fast.
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):          # n iterations
        for j in range(n - 1):  # n iterations each
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
```

### 6. O(2ⁿ) — Exponential
Doubles with each new element. Only okay for tiny inputs.
```python
# Naive fibonacci — recalculates the same subproblems
def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)  # 2 calls per call → 2ⁿ
```

### 7. O(n!) — Factorial
Every permutation. Unusable beyond n ≈ 12.
```python
# Generating all permutations
from itertools import permutations
list(permutations([1, 2, 3, 4]))  # 4! = 24 results
```

---

## ⚡ The Big-O Cheat Sheet

```
Fastest                                           Slowest
  O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ) < O(n!)
```

| Complexity | n = 10 | n = 100 | n = 1,000 | n = 1,000,000 |
|---|---|---|---|---|
| O(1) | 1 | 1 | 1 | 1 |
| O(log n) | 3 | 7 | 10 | 20 |
| O(n) | 10 | 100 | 1,000 | 1,000,000 |
| O(n log n) | 33 | 664 | 9,966 | ~20M |
| O(n²) | 100 | 10,000 | 1,000,000 | 10¹² 💀 |
| O(2ⁿ) | 1,024 | 10³⁰ 💀 | — | — |

---

## 📏 Rules for Calculating Big-O

### Rule 1 — Drop Constants
```python
# O(2n) → O(n)
for i in range(n):   # n operations
    print(i)
for i in range(n):   # n more operations
    print(i)
# Total: 2n → just O(n)
```

### Rule 2 — Drop Non-Dominant Terms
```python
# O(n² + n) → O(n²)
for i in range(n):        # n
    for j in range(n):    # n²
        print(i, j)
for i in range(n):        # n (irrelevant)
    print(i)
```

### Rule 3 — Different Inputs, Different Variables
```python
# NOT O(n²) — it's O(a × b)
def multiply_lists(a, b):
    for i in a:        # len(a) iterations
        for j in b:    # len(b) iterations each
            print(i, j)
```

### Rule 4 — Loops = Multiply, Sequence = Add
```python
# Sequence (add): O(n) + O(n) = O(n)
for i in range(n): pass
for j in range(n): pass

# Nested (multiply): O(n) × O(n) = O(n²)
for i in range(n):
    for j in range(n): pass
```

---

## 🧠 Space Complexity Basics

Space complexity counts the **extra memory** your algorithm allocates, not the input itself.

```python
# O(1) space — only a few variables
def sum_list(arr):
    total = 0         # 1 variable
    for num in arr:
        total += num
    return total

# O(n) space — creates a new list
def double_list(arr):
    result = []       # grows with n
    for num in arr:
        result.append(num * 2)
    return result

# O(n) space — call stack grows n levels deep
def factorial(n):
    if n == 1: return 1
    return n * factorial(n - 1)  # n frames on call stack
```

---

## 🧪 Best, Average & Worst Case

Big-O is usually about **worst case**, but all three matter:

| | Definition | Example (Linear Search) |
|---|---|---|
| **Best** Ω (Omega) | Most favourable input | Target is at index 0 → O(1) |
| **Average** Θ (Theta) | Typical/expected input | Target is in middle → O(n/2) = O(n) |
| **Worst** O (Big-O) | Least favourable input | Target not in list → O(n) |

In practice, when someone says "time complexity is O(n)", they mean worst case.

---

## 🔎 Quick-Identify Patterns

| Code Pattern | Complexity |
|---|---|
| Single loop over n | O(n) |
| Loop inside a loop over n | O(n²) |
| Halving the input each step | O(log n) |
| Recursion that branches 2x | O(2ⁿ) |
| Sorting | O(n log n) |
| Hash table lookup | O(1) average |
| Accessing array by index | O(1) |

---

## 📝 My Notes & Observations

> *Fill this in as you learn — your own words matter most for revision.*

- [ ] Understood Big-O notation
- [ ] Can identify complexity by reading code
- [ ] Know the 7 complexities and their shapes
- [ ] Understand space vs time tradeoffs

---

## 🔗 What's Next

With complexity analysis under your belt, you're ready to analyse every data structure and algorithm you learn.

➡️ Next: [`02_arrays_and_strings`](../02_arrays_and_strings/README.md)

---

*Part of [python_dsa](../README.md) — started June 2026*