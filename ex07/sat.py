from beartype import beartype
from BoolAST import BoolAST


@beartype
def sat(formula: str) -> bool:
    ast = BoolAST(formula)
    return ast.sat()


def main():
    print(sat('AB&C&D&'))


if __name__ == "__main__":
    main()
