from typing import Generator, Callable
import math
from random import randint


def random_gen(
    start: int = 10, end: int = 20, target_number: int = 15
) -> Generator[int, int, None]:
    # to avoid not returning the target number
    sent = math.inf

    while sent != target_number:
        sent = randint(start, end)
        yield sent


def decorator_to_str(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> str:
        return str(func(*args, **kwargs))

    return wrapper


@decorator_to_str
def add(a, b):
    return a + b


@decorator_to_str
def get_info(d):
    return d["info"]


def ignore_exception(exception, default_value=None):
    def wrapper(func):
        def new_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                return default_value

        return new_func

    return wrapper


@ignore_exception(ZeroDivisionError)
def div(a, b):
    return a / b


@ignore_exception(TypeError)
def raise_something(exception):
    raise exception


# exercise 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""

    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap
