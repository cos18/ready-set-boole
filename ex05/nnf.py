from beartype import beartype
from NNFBoolAST import BoolAST


@beartype
def negation_normal_form(formula: str) -> str:
    ast = BoolAST(formula)
    ast.negative_normalize()
    return str(ast)


def main():
    print(negation_normal_form('AB&!'))


if __name__ == "__main__":
    main()
