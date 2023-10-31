from beartype import beartype

HILBERT_N = 16


@beartype
def map(x: int, y: int) -> float:
    max_int = 2**HILBERT_N - 1
    if x < 0 or y < 0 or x > max_int or y > max_int:
        raise ValueError(
            f"parameter isn't {HILBERT_N}bit unsigned integer range")
    s = 2**(HILBERT_N - 1)
    d = 0
    while s > 0:
        rx = int(bool(x & s))
        ry = int(bool(y & s))
        d += s * s * ((3 * rx) ^ ry)
        if ry == 0:
            if rx == 1:
                x = (s - 1) - x
                y = (s - 1) - y
            x, y = y, x
        s //= 2

    return d / (2**(HILBERT_N * 2))


def main():
    max_int = 2**HILBERT_N - 1

    print(map(2, 2))
    print(map(0, 0))
    print(map(0, max_int))
    print(map(max_int, max_int))
    print(map(max_int, 0))


if __name__ == "__main__":
    main()
