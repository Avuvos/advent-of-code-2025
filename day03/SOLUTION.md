# Day 03

## Part 1

For each bank, find the largest 2-digit number we can form by picking two digits in order.

Track the `max_digit` seen so far. For each new digit, try forming a pair with `max_digit` and update the best if it's larger.

### Time Complexity

**O(n × m)** where n = number of banks, m = length of each bank.

## Part 2

Generalize to 12 digits instead of 2.

Start with the first 12 digits. For each new digit, try replacing each position in our current best to see if we get a larger number. Greedy approach—always keep the best combination.

### Time Complexity

**O(n × m × k)** where k = 12. For each digit in each bank, we try k possible replacements.
