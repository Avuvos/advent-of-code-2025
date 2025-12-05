from pathlib import Path


def solve_part1(data: str) -> int:
    input_data = data.split(',')

    result = 0
    for rng in input_data:
        left, right = rng.split('-')
        left = int(left)
        right = int(right)

        for x in range(left, right + 1):
            sx = str(x)
            lenx = len(sx)
            if lenx % 2 == 1:
                continue
            if sx[0: lenx//2] == sx[lenx // 2:]:
                result += x

    return result


def solve_part2(data: str) -> int:
    input_data = data.split(',')

    result = 0
    for rng in input_data:
        left, right = rng.split('-')
        left = int(left)
        right = int(right)

        for x in range(left, right + 1):
            sx = str(x)
            lenx = len(sx)
            for d in range(1, lenx // 2 + 1):
                if lenx % d == 0:
                    x0 = sx[0: d]
                    if all(x0 == sx[i: i + d] for i in range(0, lenx - d + 1, d)):
                        result += x
                        break

    return result


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
