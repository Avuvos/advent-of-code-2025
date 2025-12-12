# Day 12

Polyomino packing problem: can given shapes fit into a rectangular grid without overlapping?

## Solution

Backtracking with bitmasks for fast collision detection.

### Preprocessing

- Generate all unique orientations per shape (up to 8: 4 rotations × 2 flips)
- Normalize each orientation by translating to origin, dedupe via set
- Precompute all valid placement positions as bitmasks

### Backtracking

1. Early exit if total shape area exceeds grid area
2. Sort pieces by fewest valid placements (most constrained first)
3. Try placing each piece, using `occupied & mask == 0` for O(1) collision check
4. Return immediately when a valid packing is found

### Time Complexity

Exponential worst case `O(p^n)`, but constraint ordering prunes heavily. Runs in ~42s for 1000 regions.
