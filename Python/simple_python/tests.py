import pytest

from src import remove_null, reverse_substrings, find_missing_number


class TestSrc:
    @pytest.mark.parametrize(
        "input_string,expected",
        [
            ("2076,3B,19C,138D,NULL,NULL", "2076,3B,19C,138D"),
            ("2076,NULL,3B,19C,138D,NULL,NULL", "2076,3B,19C,138D"),
            ("2076,,NULL,3B,19C,138D,NULL,NULL", "2076,,3B,19C,138D"),
            ("2076,ANULL,3B,19C,138D,NULL,NULL", "2076,ANULL,3B,19C,138D"),
            ("2076,NULLs,3B,19C,138D,NULL,NULL", "2076,NULLs,3B,19C,138D"),
            ("", ""),
        ],
    )
    def test_remove_null(self, input_string, expected):
        assert remove_null(input_string) == expected

    @pytest.mark.parametrize(
        "input_string,expected",
        [
            ("hello,FROM, THE,other,side", "side,other, THE,FROM,hello"),
            (
                "Are you crazy?! Of course not,Can I trust you?,Yes,Darling",
                "Darling,Yes,Can I trust you?,Are you crazy?! Of course not",
            ),
            ("", ""),
        ],
    )
    def test_reverse_substring(self, input_string, expected):
        assert reverse_substrings(input_string) == expected

    @pytest.mark.parametrize("input_list,expected", [([1, 2, 3], 4), ([1, 4, 3], 2)])
    def test_find_missing_number(self, input_list, expected):
        assert find_missing_number(input_list) == expected
