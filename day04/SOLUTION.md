# Day 04

## Part 1

Use a directions array to easily check all 8 neighbors:

```python
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
```

For each `@` cell, count how many neighbors are also `@`. If fewer than 4, count it.

### Time Complexity

**O(n × m)** where n, m = grid dimensions. Each cell checked in O(1) time.

## Part 2

Repeat part 1 in a loop: remove all `@` cells with fewer than 4 neighbors, then repeat until nothing changes.

### Time Complexity

**O(n × m × k)** where k = number of iterations until stable. Worst case k ≈ max(n, m) if cells peel away layer by layer.
