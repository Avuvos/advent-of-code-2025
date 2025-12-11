# Day 11

Classic "count paths in acyclic graph" problem, easily solved with DFS and caching.

## Part 1

Given a directed acyclic graph (DAG), count the number of paths from node `"you"` to node `"out"`.

**Approach:** DFS with memoization. For each node, recursively count paths through all neighbors and cache results to avoid recomputation.

### Time Complexity

`O(V + E)` where V = vertices, E = edges. Each node is visited once due to caching.

## Part 2

Same problem, but only count paths that pass through both `"fft"` and `"dac"` nodes.

**Approach:** Extend the DFS state to track two boolean flags: whether we've visited `"fft"` and whether we've visited `"dac"`. Only count a path when it reaches `"out"` with both flags true.

### Time Complexity

`O(V + E)` — the state space is now `(node, fft_visited, dac_visited)`, giving 4x more states, but overall still `O(V + E)`.
