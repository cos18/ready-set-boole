from beartype import beartype


@beartype
def gray_code(n: int) -> int:
    """
    Recode multiplication method by bit operatior.

    :param n: integer
    :return: gray code of params n
    """
    if n < 0:
        raise ValueError("parameter cannot be negative")
    return n ^ (n >> 1)


def main():
    print(gray_code(0))  # 0
    print(gray_code(1))  # 1
    print(gray_code(2))  # 3
    print(gray_code(3))  # 2
    print(gray_code(4))  # 6
    print(gray_code(5))  # 7
    print(gray_code(6))  # 5
    print(gray_code(7))  # 4
    print(gray_code(8))  # 12


if __name__ == "__main__":
    main()
