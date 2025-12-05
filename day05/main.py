from pathlib import Path


def solve_part1(data: str) -> int:
    top, bottom = data.split("\n\n")
    ranges = [tuple(map(int, l.split('-'))) for l in top.splitlines()]
    ingredients = [int(l) for l in bottom.splitlines()]

    result = 0
    for ing in ingredients:
        for l, r in ranges:
            if l <= ing <= r:
                result += 1
                break

    return result


def solve_part2(data: str) -> int:
    top, _ = data.split("\n\n")
    ranges = sorted([tuple(map(int, l.split('-'))) for l in top.splitlines()])
    merged = []
    for l, r in ranges:
        # No intervals or disjoint
        if not merged or merged[-1][1] < l:
            merged.append([l, r])
            continue
        # Contained or overlaps
        merged[-1][1] = max(merged[-1][1], r)

    result = sum(r - l + 1 for l, r in merged)
    return result


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
