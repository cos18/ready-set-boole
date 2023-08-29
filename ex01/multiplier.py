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


@beartype
def multiplier(a: int, b: int) -> int:
    """
    Recode multiplication method by bit operatior.

    Parameter of functions is limited by **32bit unsigned integer**
    to secure O(1) time complexity.

    Return value can be over 32bit unsigned integer value.

    :param a: 32bit unsigned integer
    :param b: 32bit unsigned integer
    :return: multiplication result of params a and b
    """
    u32_max = 4294967295
    if a < 0 or b < 0 or a > u32_max or b > u32_max:
        raise ValueError("parameter isn't 32bit unsigned integer range")

    result = 0
    mask = 0
    for bits in range(32):
        if b == 0:
            break
        if b & 1:
            tmp = adder(result >> bits, a) << bits
            remain = result & mask
            result = tmp | remain
        b = b >> 1
        if mask:
            mask = (mask << 1) | mask
        else:
            mask = 1
    return result


def main():
    print(multiplier(3, 2))


if __name__ == "__main__":
    main()
