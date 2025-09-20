# 1. Product of Array Except Self – Python Implementation

## Overview

This Python script implements a solution to the **“Product of Array Except Self”** problem.  

**Problem statement:**  
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` **except `nums[i]`.**

Example:
nums = [1, 2, 3, 4]
output = [24, 12, 8, 6]

## Code Explanation

The implementation uses **nested loops**:

1. **Outer loop** iterates through each index `index1` of `nums`.  
2. **Inner loop** iterates through all elements `n` of `nums` to calculate the product of all elements **except the one at the current outer index**.  
3. A variable `prev` is used to store the running product in the inner loop.  
4. The product for each index is stored in the `answers` list.

### Example Walkthrough

For `nums2 = [4, 3, 2, 1, 2]`:

- For `index 0`, exclude `4`: multiply `[3, 2, 1, 2]` → `12`  
- For `index 1`, exclude `3`: multiply `[4, 2, 1, 2]` → `16`  
- For `index 2`, exclude `2`: multiply `[4, 3, 1, 2]` → `24`  
- For `index 3`, exclude `1`: multiply `[4, 3, 2, 2]` → `48`  
- For `index 4`, exclude `2`: multiply `[4, 3, 2, 1]` → `24`

Final output:
[12, 16, 24, 48, 24]
---

## Why It’s Not Optimized

- This implementation uses **nested loops**, resulting in **O(n²) time complexity**.  
- For small arrays, this works fine, but for large inputs (like arrays with 10⁵ elements, which LeetCode tested it failed), it **exceeds the time limit**.  
- The standard optimized solution uses **prefix and suffix products**, which achieves **O(n) time complexity** without division.

---
### Optimization Considered

This problem can be optimized from **O(n²)** to **O(n)** time complexity by using **prefix and suffix products**:

* Instead of multiplying all elements except the current one in a nested loop, we can:
  1. Compute a **prefix product** for each index `i` (product of all elements before `i`).
  2. Compute a **suffix product** for each index `i` (product of all elements after `i`).
  3. Multiply `prefix[i] * suffix[i]` to get the final product except self.

* This approach avoids nested loops and works for large arrays efficiently.
* **Space complexity:** O(1) extra (excluding the output array), since we can reuse the output array to store prefix products and combine with suffix products.

**Time Complexity:** O(n)  
**Space Complexity:** O(1) extra


---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Outer loop over `nums` | O(n) |
| Inner loop over `nums` | O(n) |
| **Total** | O(n²) |

- **Space complexity:** O(n) (for the `answers` array)  


# 2. Find Max Value of Equation – Python Implementation

## Overview
This Python script implements a solution to the **“Max Value of Equation”** problem.

**Problem statement:**  
Given a list of points `[[xi, yi]]` sorted by `xi` and an integer `k`, find the maximum value of:

yi + yj + |xi - xj|


for all `i < j` such that `|xi - xj| <= k`.

---

## Implementation
- Uses **nested loops** with `enumerate` to preserve the original style.  
- For each point `i`, iterates over subsequent points `j` (`i < j`).  
- Calculates `diffy = yi + yj + (xj - xi)` if the points satisfy the constraint.  
- Tracks the **maximum value** in `max_val`.

---

## Time and Space Complexity
- **Time Complexity:** O(n²) — loops through all valid pairs of points.  
- **Space Complexity:** O(1) — only a few variables are used; no extra arrays needed.

---
### Optimization Considered

The problem can be optimized to **O(n) time complexity** using a **monotonic deque** (or a priority queue), leveraging the fact that:

yi + yj + |xi - xj| = (yi - xi) + (yj + xj)



* Instead of checking all pairs, you maintain a **deque of candidate points** that could produce the maximum value.
* Remove points from the deque if their `xi` is more than `k` away from the current `xj`.
* Always keep the **largest `(yi - xi)`** available for the current `j`.

This reduces the inner loop from iterating over all `j` to only considering valid candidates in the deque → **O(n) time**.

---

## Usage

```python
points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
sol = Solution()
sol.findMaxValueOfEquation(points, k)

