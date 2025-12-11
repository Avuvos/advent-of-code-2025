from collections import defaultdict
from functools import cache
from pathlib import Path



def build_graph(data: str) -> dict:
    graph = defaultdict(list)
    for line in data.splitlines():
        node, neighbors = line.split(": ")
        graph[node] = neighbors.split()
    return graph


def solve_part1(data: str) -> int:
    graph = build_graph(data)

    @cache
    def dfs(node: str) -> int:
        if node == "out":
            return 1
        paths = 0
        for neighbor in graph[node]:
            paths += dfs(neighbor)
        return paths

    return dfs("you")

def solve_part2(data: str) -> int:
    graph = build_graph(data)
    
    @cache
    def dfs(node: str, fft: bool, dac: bool) -> int:
        if node == "out":
            return 1 if (fft and dac) else 0
        paths = 0
        for neighbor in graph[node]:
            paths += dfs(neighbor, fft or neighbor == "fft", dac or neighbor == "dac")
        return paths

    return dfs("svr", False, False)


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
