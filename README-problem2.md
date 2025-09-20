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

## Usage

```python
points = [[1,3],[2,0],[5,10],[6,-10]]
k = 1
sol = Solution()
sol.findMaxValueOfEquation(points, k)
