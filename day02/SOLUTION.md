# Day 02

## Part 1

For each range, loop over every number and convert it to a string.

A number is valid if its length is even and the first half equals the second half (e.g., `1212`, `5555`).

Sum up all valid numbers.

### Time Complexity

**O(n × m)** where n = total numbers across all ranges, m = max digits per number.

## Part 2

Generalize part 1: instead of just checking halves, check all possible repeating patterns.

Loop over all divisors `d` of the string length. If the first `d` characters repeat throughout the entire string, it's valid.

### Time Complexity

**O(n × m)** — same as part 1, checking divisors is O(m) per number.
