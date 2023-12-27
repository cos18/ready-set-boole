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

    def is_minimal_form(self) -> bool:
        return self.value.isupper() or self.value == '!'

    def negative_normalize(self) -> None:
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

    def is_cnf_form(self, already_conjunctive: bool) -> bool:
        if self.is_minimal_form():
            return True
        if already_conjunctive and self.value == '&':
            return False
        if self.left.is_minimal_form() and self.right.is_minimal_form():
            return True
        if self.value != '&':
            already_conjunctive = True
        return self.left.is_cnf_form(
            already_conjunctive) and self.right.is_cnf_form(
                already_conjunctive)

    def apply_cnf_distributivity(self) -> None:
        if self.is_minimal_form():
            return
        if self.value == '|':
            target: BoolASTNode = None
            opposite: BoolASTNode = None
            if self.right.value == '&':
                target = self.right
                opposite = self.left
            elif self.left.value == '&':
                target = self.left
                opposite = self.right
            if target:
                self.left = BoolASTNode('|', target.left, opposite)
                self.right = BoolASTNode('|', target.right, opposite)
                self.value = '&'
        self.left.apply_cnf_distributivity()
        self.right.apply_cnf_distributivity()

    def find_not_or_set(self):
        result: [BoolASTNode] = []
        result += (self.left.find_not_or_set()
                   if self.left.value == '|' else [self.left])
        result += (self.right.find_not_or_set()
                   if self.right.value == '|' else [self.right])
        return result

    def change_or_logical(self) -> None:
        if self.value == '&':
            self.sort_or_logical()
        elif self.value == '|':
            logical_list: [BoolASTNode] = self.find_not_or_set()
            self.left = logical_list[0]
            self.right = logical_list[1]
            if len(logical_list) > 2:
                target = self
                for idx in range(2, len(logical_list)):
                    target.right = BoolASTNode('|', logical_list[idx - 1],
                                               logical_list[idx])
                    target = target.right

    def sort_or_logical(self) -> None:
        if self.is_minimal_form():
            return
        if self.value == '|':
            self.change_or_logical()
        self.left.change_or_logical()
        self.right.change_or_logical()

    def find_not_conjunctive_set(self):
        result: [BoolASTNode] = []
        result += (self.left.find_not_conjunctive_set()
                   if self.left.value == '&' else [self.left])
        result += (self.right.find_not_conjunctive_set()
                   if self.right.value == '&' else [self.right])
        return result

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

    def conjunctive_normalize(self) -> None:
        self.negative_normalize()
        while not self.root.is_cnf_form(False):
            self.root.apply_cnf_distributivity()
        self.root.sort_or_logical()
        if self.root.value != '&':
            return
        logical_list = self.root.find_not_conjunctive_set()
        new_root = BoolASTNode('&', logical_list[0], logical_list[1])
        if len(logical_list) > 2:
            target = new_root
            for idx in range(2, len(logical_list)):
                target.right = BoolASTNode('&', logical_list[idx - 1],
                                           logical_list[idx])
                target = target.right
        self.root = new_root

    def sat(self):
        bool_var_list = list(self.bool_var)
        for bool_state in range(2**len(bool_var_list)):
            binary_format = '{:0' + str(len(bool_var_list)) + 'b}'
            binary_format = binary_format.format(bool_state)
            bool_dict: Dict[str, bool] = {}
            for idx in range(len(bool_var_list)):
                bool_dict[bool_var_list[idx]] = (binary_format[idx] == '1')
            if self.root.cal_bool(bool_dict):
                return True
        return False

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
