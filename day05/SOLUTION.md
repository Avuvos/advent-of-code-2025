# Day 05

## Part 1

Brute force: for each ingredient, scan all intervals to check if any contains it.

### Time Complexity

**O(n × m)** where n = number of ingredients, m = number of intervals.

*Could be optimized to O((n + m) × log m)* by sorting intervals and binary searching for the smallest left value ≤ ingredient.

## Part 2

Classic interval merging problem.

Sort intervals by left value, then merge by considering:
- **No overlap** — add a new interval
- **Contained or overlaps** — extend the right bound of the last interval

Sum up the lengths of all merged intervals.

### Time Complexity

**O(m log m)** for sorting, then O(m) for merging.
