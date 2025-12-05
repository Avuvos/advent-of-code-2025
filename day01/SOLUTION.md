# Day 01

## Part 1

Start at `position = 50`.

For each operation, add or subtract the count based on direction (`R` or `L`), using `% 100` to wrap around.

Count how many times we land exactly on position `0`.

### Time Complexity

**O(n)** where n = number of lines given, each line is processed in O(1) time.

## Part 2

Same idea, but now we need to count every time we *cross* zero, not just land on it.

Before applying the modulo, check if the position went out of bounds (≤0 or ≥100).

For large counts, we may cross zero multiple times in a single operation—track this by dividing the count by 100.

### Time Complexity

**O(n)** — same as part 1.
