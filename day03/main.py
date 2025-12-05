from pathlib import Path


def solve_part1(data: str) -> int:
    input_data = data.splitlines()

    result = 0

    for bank in input_data:
        max_digit = "0"
        best = 0
        for i, c in enumerate(bank):
            if int(max_digit + c) > int(best):
                best = max_digit + c
            if int(c) > int(max_digit):
                max_digit = c
        result += int(best)

    return result


def solve_part2(data: str) -> int:
    input_data = data.splitlines()

    result = 0
    LEN = 12

    for bank in input_data:
        max_digits = [c for c in bank[0:LEN]]
        best = int("".join(max_digits))
        for cur_digit in bank[LEN:]:
            new_max_digits = max_digits
            for i in range(LEN):
                cur_max_digits = max_digits[0 : i] + max_digits[i + 1:] + [cur_digit]
                cur_val = int("".join(cur_max_digits))
                if cur_val > best:
                    best = cur_val
                    new_max_digits = cur_max_digits
            max_digits = new_max_digits
        result += best

    return result


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
