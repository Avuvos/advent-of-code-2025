from pathlib import Path

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def solve_part1(data: str) -> int:
    grid = data.splitlines()

    result = 0
    n, m = len(grid), len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] != "@":
                continue
            count = 0
            for dx, dy in DIRECTIONS:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "@":
                    count += 1
            if count < 4:
                result += 1
    return result


def solve_part2(data: str) -> int:
    grid = data.splitlines()
    grid = [[c for c in row] for row in grid]
    result = 0
    n, m = len(grid), len(grid[0])
    while True:
        removed = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != "@":
                    continue
                count = 0
                for dx, dy in DIRECTIONS:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "@":
                        count += 1
                if count < 4:
                    removed += 1
                    result += 1
                    grid[i][j] = '.'
        if removed == 0:
            break
    return result


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
