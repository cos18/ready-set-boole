from __future__ import annotations  # typing class itself
from beartype import beartype


@beartype
class BoolAST:

    def __init__(self,
                 value: bool | str,
                 left: BoolAST = None,
                 right: BoolAST = None) -> None:
        if type(value) is bool and (left or right):
            raise ValueError('Wrong formular character')
        if type(value) is str:
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

    def cal_bool(self) -> bool:
        match self.value:
            case True | False:
                return self.value
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
def eval_formula(formula: str) -> bool:
    stack: [BoolAST] = []
    for f in formula:
        if f in '01':
            stack.append(BoolAST(f == '1'))
            continue
        if len(stack) < 2:
            raise ValueError('Wrong formular character')
        right = stack.pop()
        left = stack.pop()
        stack.append(BoolAST(f, left, right))

    if len(stack) != 1:
        raise ValueError('Wrong formular character')
    return stack[0].cal_bool()


def main():
    print(eval_formula('10&'))  # False
    print(eval_formula('10|'))  # True
    print(eval_formula('11>'))  # True
    print(eval_formula('10='))  # False
    print(eval_formula('1011||='))  # True


if __name__ == "__main__":
    main()
