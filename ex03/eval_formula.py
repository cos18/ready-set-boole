from beartype import beartype


@beartype
def eval_formula(formula: str) -> bool:
    pass


def main():
    print(eval_formula('10&'))  # False
    print(eval_formula('10|'))  # True
    print(eval_formula('11>'))  # True
    print(eval_formula('10='))  # False
    print(eval_formula('1011||='))  # True


if __name__ == "__main__":
    main()
