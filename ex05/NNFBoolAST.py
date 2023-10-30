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

    def __str__(self):
        result: str = ''
        result += (str(self.left) if self.left else '')
        result += (str(self.right) if self.right else '')
        return result + self.value

    def negative_normalize(self):
        if self.value == '>':
            self.value = '|'
            self.left = BoolASTNode('!', self.left)
        elif self.value == '=':
            new_left = BoolASTNode('&', self.left, self.right)
            new_right = BoolASTNode('&', BoolASTNode('!', self.left),
                                    BoolASTNode('!', self.right))
            self.value = '|'
            self.left = new_left
            self.right = new_right
        elif self.value == '^':
            new_left = BoolASTNode('&', BoolASTNode('!', self.left),
                                   self.right)
            new_right = BoolASTNode('&', self.left,
                                    BoolASTNode('!', self.right))
            self.value = '|'
            self.left = new_left
            self.right = new_right
        elif self.value == '!' and not self.left.value.isupper():
            self.left.negative_normalize()
            new_left = BoolASTNode('!', self.left.left)
            new_right = BoolASTNode('!', self.left.right)
            self.value = '&' if self.left.value == '|' else '|'
            self.left = new_left
            self.right = new_right
        if self.left:
            while self.left.value == '!' and self.left.left.value == '!':
                self.left = self.left.left.left
            self.left.negative_normalize()
        if self.right:
            while self.right.value == '!' and self.right.left.value == '!':
                self.right = self.right.left.left
            self.right.negative_normalize()

    def cal_bool(self, bool_dict: Dict[str, bool]) -> bool:
        if self.value.isupper():
            if self.value not in bool_dict.keys():
                raise ValueError('Wrong formular character')
            return bool_dict[self.value]
        match self.value:
            case '!':
                return not self.left.cal_bool(bool_dict)
            case '&':
                return (self.left.cal_bool(bool_dict)
                        and self.right.cal_bool(bool_dict))
            case '|':
                return (self.left.cal_bool(bool_dict)
                        or self.right.cal_bool(bool_dict))
            case '^':
                return (self.left.cal_bool(bool_dict)
                        ^ self.right.cal_bool(bool_dict))
            case '>':
                return ((not self.left.cal_bool(bool_dict))
                        or self.right.cal_bool(bool_dict))
            case '=':
                return not (self.left.cal_bool(bool_dict)
                            ^ self.right.cal_bool(bool_dict))
            case _:
                raise ValueError('Wrong formular character')


@beartype
class BoolAST:

    def __init__(self, formula: str) -> None:
        stack: [BoolASTNode] = []
        self.bool_var: Set[str] = set()
        for f in formula:
            if f.isupper():
                stack.append(BoolASTNode(f))
                self.bool_var.add(f)
                continue
            if f == '!':
                if not len(stack):
                    raise ValueError('Wrong formular character')
                root = stack.pop()
                stack.append(BoolASTNode(f, root))
                continue
            if len(stack) < 2:
                raise ValueError('Wrong formular character')
            right = stack.pop()
            left = stack.pop()
            stack.append(BoolASTNode(f, left, right))
        if len(stack) != 1 or len(self.bool_var) == 0:
            raise ValueError('Wrong formular character')
        self.root = stack[0]

    def __str__(self) -> str:
        return str(self.root)

    def negative_normalize(self) -> None:
        while self.root.value == '!' and self.root.left.value == '!':
            self.root = self.root.left.left
        self.root.negative_normalize()

    def print_truth_table(self) -> None:
        bool_var_list = sorted(list(self.bool_var))
        for bool_var in bool_var_list:
            print(f'| {bool_var} ', end='')
        print('| = |\n|', end='')
        for _ in range(len(bool_var_list) + 1):
            print('---|', end='')
        print()
        for bool_state in range(2**len(bool_var_list)):
            binary_format = '{:0' + str(len(bool_var_list)) + 'b}'
            binary_format = binary_format.format(bool_state)
            for binary_char in binary_format:
                print(f'| {binary_char} ', end='')
            bool_dict: Dict[str, bool] = {}
            for idx in range(len(bool_var_list)):
                bool_dict[bool_var_list[idx]] = (binary_format[idx] == '1')
            print(f'| {1 if self.root.cal_bool(bool_dict) else 0} |')
