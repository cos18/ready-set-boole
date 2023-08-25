from beartype import beartype


@beartype
def adder(a: int, b: int) -> int:
    pass


def main():
    print(adder(1, 2))


if __name__ == "__main__":
    main()
