from beartype import beartype


@beartype
def adder(a: int, b: int) -> int:
    """
    Recode addition method by bit operatior.

    Parameter of functions is limited by **32bit unsigned integer**
    to secure O(1) time complexity.

    Return value can be over 32bit unsigned integer value.

    :param a: 32bit unsigned integer
    :param b: 32bit unsigned integer
    :return: addition result of params a and b
    """
    u32_max = 4294967295  # https://doc.rust-lang.org/std/primitive.u32.html
    if a < 0 or b < 0 or a > u32_max or b > u32_max:
        raise ValueError("parameter isn't 32bit unsigned integer range")

    for _ in range(32):
        carry = a & b
        a = a ^ b
        if carry == 0:
            break
        b = carry << 1
    return a


def main():
    print(adder(1, 2))


if __name__ == "__main__":
    main()
