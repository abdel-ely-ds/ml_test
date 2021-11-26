import pytest

from src import div, raise_something, add, random_gen, get_info, CacheDecorator
from typing import Generator


@pytest.fixture
def cache_decorator():
    return CacheDecorator()


@pytest.fixture
def func():
    def multiply(x: int, y: int) -> int:
        return x * y

    return multiply


class TestSrc:
    def test_generator(self):
        g = random_gen()
        assert isinstance(g, Generator)
        a = next(g)
        while a != 15:
            assert 10 <= a <= 20
            a = next(g)
        with pytest.raises(StopIteration):
            next(g)

    def test_to_str(self):
        assert add(5, 30) == "35"
        assert get_info({"info": [1, 2, 3]}) == "[1, 2, 3]"
        assert get_info({"info": None}) == "None"
        assert get_info({"info": 1.5}) == "1.5"

    def test_ignore_exception(self):
        assert div(10, 2) == 5
        assert div(10, 0) is None
        assert raise_something(TypeError) is None
        with pytest.raises(NotImplementedError):
            raise_something(NotImplementedError)

    def test_cache_decorator_class_cached_correctly(self, cache_decorator):
        @cache_decorator
        def func(x: int) -> int:
            return x + 1
        _ = func(1)
        assert 1 in cache_decorator.cache

    def test_cache_decorator_class_bug_detector(self, cache_decorator):
        args = [(1, 2), (1, 3)]

        @cache_decorator
        def func(x: int, y: int) -> int:
            return x + y

        assert func(*args[0]) != func(*args[1])

    def test_cache_decorator_class_memory_error(self, cache_decorator):
        pass



