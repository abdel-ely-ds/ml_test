from typing import List


def remove_null(cat_string: str, sep: str = ",", s_to_remove: str = "NULL") -> str:
    s_list = cat_string.split(sep)
    return sep.join([item for item in s_list if item != s_to_remove])


def reverse_substrings(cat_string: str, sep: str = ",") -> str:
    return sep.join(cat_string.split(sep)[::-1])


def find_missing_number(numbers: List[int]) -> int:
    n = len(numbers) + 1
    for i in range(1, n + 1):
        if i not in numbers:
            return i
