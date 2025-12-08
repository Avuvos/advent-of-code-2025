from itertools import combinations
from math import prod
from pathlib import Path


class DSU:
    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.size = [1] * n
        self.n = n
        self.num_components = n

    def find(self, x: int) -> int:
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x: int, y: int) -> bool:
        """Union two elements by size. Returns True if they were in different components."""
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            if self.size[xr] > self.size[yr]:
                xr, yr = yr, xr
            self.p[xr] = yr
            self.size[yr] += self.size[xr]
            self.num_components -= 1
            return True
        return False


def dist(b1: list[int], b2: list[int]) -> int:
    return (b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 + (b1[2] - b2[2]) ** 2


def solve_part1(data: str) -> int:
    boxes = [list(map(int, box.split(","))) for box in data.splitlines()]
    n = len(boxes)
    ds = DSU(n)
    edges = sorted((dist(boxes[i], boxes[j]), i, j) for i, j in combinations(range(n), 2))

    for _, i, j in edges[:1000]:
        ds.union(i, j)

    roots = {ds.find(i) for i in range(n)}
    top_sizes = sorted([ds.size[r] for r in roots], reverse=True)[:3]
    return prod(top_sizes)


def solve_part2(data: str) -> int:
    boxes = [list(map(int, box.split(","))) for box in data.splitlines()]
    n = len(boxes)
    ds = DSU(n)
    edges = sorted((dist(boxes[i], boxes[j]), i, j) for i, j in combinations(range(n), 2))

    for _, i, j in edges:
        ds.union(i, j)
        if ds.num_components == 1:
            return boxes[i][0] * boxes[j][0]

    return 0


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
