from beartype import beartype
from beartype.typing import Set, List


@beartype
def powerset(s: Set[int]) -> List[Set[int]]:
    s = sorted(list(s))

    @beartype
    def create_powerset(idx: int, prev: Set[int]) -> List[Set[int]]:
        now = set(prev)
        if idx == len(s):
            return [now]
        result: List[Set[int]] = create_powerset(idx + 1, now)
        now.add(s[idx])
        result += create_powerset(idx + 1, now)
        return result

    return create_powerset(0, set())


def main():
    print(powerset({1, 2, 3}))


if __name__ == "__main__":
    main()
