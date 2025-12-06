from pathlib import Path


def solve_part1(data: str) -> int:
    banks = data.splitlines()

    result = 0
    for bank in banks:
        max_digit = "0"
        best_pair_value = 0
        for c in bank:
            if int(max_digit + c) > best_pair_value:
                best_pair_value = int(max_digit + c)
            max_digit = max(max_digit, c)
        result += best_pair_value

    return result


def solve_part2(data: str) -> int:
    banks = data.splitlines()

    result = 0
    LEN = 12
    for bank in banks:
        max_digits = [c for c in bank[0:LEN]]
        best = int("".join(max_digits))
        for cur_digit in bank[LEN:]:
            next_max_digits = max_digits
            for i in range(LEN):
                cur_max_digits = max_digits[0: i] + max_digits[i + 1:] + [cur_digit]
                cur_val = int("".join(cur_max_digits))
                if cur_val > best:
                    best = cur_val
                    next_max_digits = cur_max_digits
            max_digits = next_max_digits
        result += best

    return result


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(f"Part 1: {solve_part1(input_data)}")
    print(f"Part 2: {solve_part2(input_data)}")
