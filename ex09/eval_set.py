from beartype import beartype
from beartype.typing import List, Set
from SetAST import SetAST


@beartype
def eval_set(formula: str, sets: List[Set[int]]) -> Set[int]:
    ast = SetAST(formula)
    return ast.eval_set(sets)


def main():
    sets = [{0, 1, 2}, {0, 3, 4}]
    print(eval_set("AB&", sets))
    # {0}

    sets = [{0, 1, 2}, {3, 4, 5}]
    print(eval_set("AB|", sets))
    # {0, 1, 2, 3, 4, 5}

    sets = [{0, 1, 2}]
    print(eval_set("A!", sets))
    # {}


if __name__ == "__main__":
    main()
