from beartype import beartype
from BoolAST import BoolAST


@beartype
def sat(formula: str) -> bool:
    ast = BoolAST(formula)
    return ast.sat()
