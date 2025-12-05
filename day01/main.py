from pathlib import Path


def solve_part1(data: str) -> int:
    input_data = data.splitlines()

    position = 50
    result_password = 0
    for operation in input_data:
        direction = operation[0]
        count = int(operation[1:])

        if direction == "R":
            position = (position + count) % 100
        elif direction == "L":
            position = (position - count) % 100
        else:
            raise ValueError("Unexpected direction")

        if position == 0:
            result_password += 1

    return result_password


def solve_part2(data: str) -> int:
    input_data = data.splitlines()

    position = 50
    result_password = 0
    for operation in input_data:
        direction = operation[0]
        count = int(operation[1:])
        times_of_rotation = count // 100

        if direction == "R":
            position = position + count
        elif direction == "L":
            position = position - count
        else:
            raise ValueError("Unexpected direction")

        if position >= 100 or position <= 0:
            result_password += max(1, times_of_rotation)
        position = position % 100

    return result_password


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
