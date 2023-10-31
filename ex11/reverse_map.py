from beartype import beartype
from beartype.typing import List

HILBERT_N = 16


@beartype
def reverse_map(n: float) -> List[int]:
    if n < 0 or n > 1:
        raise ValueError(f"parameter isn't in the range of [0, 1]")
    if n == 1:
        return [2**HILBERT_N - 1, 0]
    n = int(n * (2**(HILBERT_N * 2)))
    s = 1
    x, y = 0, 0
    while s < 2**HILBERT_N:
        rx = 1 & (n // 2)
        ry = 1 & (n ^ rx)
        if ry == 0:
            if rx == 1:
                x = (s - 1) - x
                y = (s - 1) - y
            x, y = y, x
        x += s * rx
        y += s * ry
        n //= 4
        s *= 2
    return [x, y]


def main():
    print(reverse_map(1.862645149230957e-09))
    print(reverse_map(0.0))
    print(reverse_map(0.3333333332557231))
    print(reverse_map(0.6666666665114462))
    print(reverse_map(0.9999999997671694))

    print(reverse_map(1.0))


if __name__ == "__main__":
    main()
