from beartype import beartype


@beartype
def multiplier(a: int, b: int) -> int:
    pass


def main():
    print(multiplier(3, 2))


if __name__ == "__main__":
    main()
