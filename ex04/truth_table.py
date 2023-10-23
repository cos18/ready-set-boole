from __future__ import annotations  # typing class itself
from beartype import beartype
from beartype.typing import Dict, Set


@beartype
class BoolASTNode:

    def __init__(self,
                 value: str,
                 left: BoolASTNode = None,
                 right: BoolASTNode = None) -> None:
        if value.isupper():
            if left or right:
                raise ValueError('Wrong formular character')
        else:
            if value not in '!&|^>=':
                raise ValueError('Wrong formular character')
            if value == '!':
                if (not left) or right:
                    raise ValueError('Wrong formular character')
            elif (not left) or (not right):
                raise ValueError('Wrong formular character')
        self.value = value
        self.left = left
        self.right = right

    def cal_bool(self, bool_dict: Dict[str, bool]) -> bool:
        if self.value.isupper():
            if self.value not in bool_dict.keys():
                raise ValueError('Wrong formular character')
            return bool_dict[self.value]
        match self.value:
            case '!':
                return not self.left.cal_bool()
            case '&':
                return self.left.cal_bool() and self.right.cal_bool()
            case '|':
                return self.left.cal_bool() or self.right.cal_bool()
            case '^':
                return self.left.cal_bool() ^ self.right.cal_bool()
            case '>':
                return (not self.left.cal_bool()) or self.right.cal_bool()
            case '=':
                return not (self.left.cal_bool() ^ self.right.cal_bool())
            case _:
                raise ValueError('Wrong formular character')


@beartype
class BoolAST:

    def __init__(self, formula: str):
        stack: [BoolASTNode] = []
        self.bool_var: Set[str] = set()
        for f in formula:
            if f.isupper():
                stack.append(BoolASTNode(f))
                self.bool_var.add(f)
                continue
            if len(stack) < 2:
                raise ValueError('Wrong formular character')
            right = stack.pop()
            left = stack.pop()
            stack.append(BoolASTNode(f, left, right))
        if len(stack) != 1 or len(self.bool_var) == 0:
            raise ValueError('Wrong formular character')
        self.root = stack[0]

    def print_truth_table(self):
        bool_var_list = sorted(list(self.bool_var))
        for bool_var in bool_var_list:
            print(f'| {bool_var} ', end='')
        print('| = |\n|', end='')
        for _ in range(len(bool_var_list) + 1):
            print('---|', end='')
        print()
        for bool_state in range(2**len(bool_var_list)):
            pass
            # | A | B | C | = |


@beartype
def print_truth_table(formula: str) -> None:
    ast = BoolAST(formula)
    ast.print_truth_table()


def main():
    print_truth_table('AB&C|')


if __name__ == "__main__":
    main()
