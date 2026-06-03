"""
Complexity Analysis — Beginner's Guide
========================================
Learn Big-O complexity with simple examples.

Run this file:  python examples.py
"""

def print_section(title):
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)


# ══════════════════════════════════════════════
# 1. O(1) — CONSTANT TIME
# ══════════════════════════════════════════════

def get_first_element(arr):
    """Always takes the same time, no matter list size."""
    return arr[0]


def is_even(n):
    """Always one operation: check n % 2."""
    return n % 2 == 0


def demo_o1():
    print_section("O(1) — Constant Time")
    print("  Time is ALWAYS the same, no matter the input size.\n")
    print("  Examples:")
    print(f"    get_first_element([10, 20, 30]) = {get_first_element([10, 20, 30])}")
    print(f"    is_even(42) = {is_even(42)}")
    print(f"    is_even(7) = {is_even(7)}")
    print("\n  ✓ These operations take the same time for any input size.")


# ══════════════════════════════════════════════
# 2. O(log n) — LOGARITHMIC TIME
# ══════════════════════════════════════════════

def binary_search(arr, target):
    """
    Find target by cutting search space in half each time.
    Example: Finding a page in a sorted book by opening to middle,
    then deciding which half to search next.
    """
    left, right = 0, len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, steps


def demo_olog_n():
    print_section("O(log n) — Logarithmic Time")
    print("  Double the size → only 1 more step needed.\n")
    
    print("  Searching in sorted lists:")
    print("    Size 10:")
    arr = list(range(10))
    _, steps = binary_search(arr, 9)
    print(f"      Steps to find last element: {steps}")
    
    print("    Size 100:")
    arr = list(range(100))
    _, steps = binary_search(arr, 99)
    print(f"      Steps to find last element: {steps}")
    
    print("    Size 1,000:")
    arr = list(range(1000))
    _, steps = binary_search(arr, 999)
    print(f"      Steps to find last element: {steps}")
    
    print("\n  ✓ Notice: 10x bigger list, but only ~3-4 more steps!")


# ══════════════════════════════════════════════
# 3. O(n) — LINEAR TIME
# ══════════════════════════════════════════════

def linear_search(arr, target):
    """Check each element one-by-one."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def sum_all(arr):
    """Must visit each element exactly once."""
    total = 0
    for num in arr:
        total += num
    return total


def demo_on():
    print_section("O(n) — Linear Time")
    print("  Double the size → double the time.\n")
    
    print("  Examples:")
    sample = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"    linear_search([3,1,4,1,5,9,2,6], 5) = {linear_search(sample, 5)}")
    print(f"    sum_all([3,1,4,1,5,9,2,6]) = {sum_all(sample)}")
    
    print("\n  With list of 1,000 items: ~1,000 operations")
    print("  With list of 2,000 items: ~2,000 operations")
    print("\n  ✓ Time grows proportionally with list size.")


# ══════════════════════════════════════════════
# 4. O(n log n) — LINEARITHMIC TIME
# ══════════════════════════════════════════════

def merge_sort(arr):
    """
    Sort by dividing in half, sorting each half, merging back.
    This is faster than checking every pair (O(n²)).
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """Merge two sorted lists."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def demo_on_log_n():
    print_section("O(n log n) — Linearithmic Time")
    print("  Faster than O(n²), but slower than O(n).\n")
    
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(f"  Example: Sorting {arr}")
    print(f"  Result:  {merge_sort(arr)}")
    
    print("\n  Why use this?")
    print("    - O(n²) checks every pair: too slow for big lists")
    print("    - O(n log n) divides and conquers: much better!")
    print("\n  ✓ Used in: merge sort, quick sort")


# ══════════════════════════════════════════════
# 5. O(n²) — QUADRATIC TIME
# ══════════════════════════════════════════════

def bubble_sort(arr):
    """
    Compare each pair of neighbors and swap if out of order.
    Two nested loops: O(n²) time.
    """
    arr = arr[:]  # copy to avoid modifying original
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def find_all_pairs(arr):
    """Find every pair of elements (nested loops)."""
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs


def demo_on_squared():
    print_section("O(n²) — Quadratic Time")
    print("  Double the size → 4× the time. Gets slow FAST.\n")
    
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"  Example: bubble_sort({arr})")
    print(f"  Result:  {bubble_sort(arr)}")
    
    print(f"\n  Another example:")
    print(f"  find_all_pairs([1, 2, 3]) = {find_all_pairs([1, 2, 3])}")
    
    print("\n  Why is this bad?")
    print("    - 100 items: 10,000 operations")
    print("    - 1,000 items: 1,000,000 operations")
    print("\n  ✓ Avoid nested loops when list can be large!")


# ══════════════════════════════════════════════
# QUICK COMPARISON
# ══════════════════════════════════════════════

def demo_comparison():
    print_section("Quick Comparison: All Complexities at n=10")
    print(f"  {'Complexity':<15} {'Operations':<15}")
    print("  " + "-" * 40)
    print(f"  {'O(1)':<15} {'1':<15}")
    print(f"  {'O(log n)':<15} {'~3':<15}")
    print(f"  {'O(n)':<15} {'10':<15}")
    print(f"  {'O(n log n)':<15} {'~33':<15}")
    print(f"  {'O(n²)':<15} {'100':<15}")
    print("\n  Notice: O(n²) is already 10x slower than O(n)!")
    print("  For n=1,000: O(n²) is 1,000,000 operations!")


# ══════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  Complexity Analysis for Beginners")
    print("=" * 50)
    
    demo_o1()
    demo_olog_n()
    demo_on()
    demo_on_log_n()
    demo_on_squared()
    demo_comparison()
    
    print("\n" + "=" * 50)
    print("  Key Takeaway:")
    print("  Always aim for O(n) or O(n log n).")
    print("  Avoid O(n²) for large inputs!")
    print("=" * 50 + "\n")