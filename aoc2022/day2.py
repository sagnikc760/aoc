def score(left, right):
    return (1 + right - left) % 3 * 3 + right


def parse(lines):
    return (
        (ord(line[0]) - ord("A") + 1, ord(line[2]) - ord("X") + 1) for line in lines
    )


def main():
    with open("day2input.txt") as f:
        p = [i.strip() for i in f.readlines()]
    print(f"Part 1: {sum(score(left, right) for left, right in parse(p))}")

    ## part 2
    print(
        f"Part 2: {sum(score(left, 1 + (left + right) % 3) for left, right in parse(p))}"
    )


main()
