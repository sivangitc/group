from typing import List, Dict, Callable
from typing import TypeVar


T = TypeVar('T')
S = TypeVar('S')


def group(f: Callable[[S], T], group_items: List[S]) -> Dict[T, List[S]]:
    """Groups group_items by f(item) in a dictionary
    :param f: function with return value
    :group_items: list of items to be grouped
    Returns dictionary where each key is a value of f and is mapped to a list of
    items from group_items whose f result is that value
    """
    vals = {f(item) for item in group_items}
    return {val: [item for item in group_items if f(item) == val] for val in vals}


def mod_3(num: int) -> int:
    return num % 3


print(group(mod_3, [1, 3, 4, 5, 7, 9]))
