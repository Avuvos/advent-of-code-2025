# Day 08

Union-Find (DSU) problem, essentially running Kruskal's MST algorithm on junction boxes in 3D space.

## Part 1

Sort all pairwise edges by squared Euclidean distance. Process the 1000 shortest pairs using DSU—some may already be connected (no-op). Multiply the 3 largest component sizes.

### Time Complexity

`O(n² log n)` for sorting edges. Union-Find operations are pretty much `O(1)`.

## Part 2

Classic MST via Kruskal's algorithm: process edges in order until all nodes form a single component (`num_components == 1`). Track component count as a variable, decrementing on each successful union for `O(1)` checks. Return the product of X-coordinates of the final connecting edge.

### Time Complexity

`O(n² log n)` for sorting. Loop terminates early once connected.

