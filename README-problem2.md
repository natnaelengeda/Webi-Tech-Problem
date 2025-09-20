# Find Max Value of Equation – Python Implementation

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
