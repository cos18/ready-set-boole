from beartype import beartype
from BoolAST import BoolAST


@beartype
def print_truth_table(formula: str) -> None:
    ast = BoolAST(formula)
    ast.print_truth_table()


def main():
    print_truth_table('AB&C|')


if __name__ == "__main__":
    main()
