from beartype import beartype
from BoolAST import BoolAST


@beartype
def conjunctive_normal_form(formula: str) -> str:
    ast = BoolAST(formula)
    ast.conjunctive_normalize()
    return str(ast)


def main():
    print(conjunctive_normal_form('AB&C&D&'))


if __name__ == "__main__":
    main()