import pytest
from roman_to_integer import Solution


class TestRomanToInt:

    @pytest.fixture(scope='function')
    def solution_class(self):
        solution = Solution()
        return solution

    @pytest.mark.parametrize('s,integer', [
        ("LVIII", 58),
        ("III", 3),
        ("MCMXCIV", 1994),
    ])
    def test_roman_to_int(self, solution_class, s, integer):
        assert solution_class.romanToInt(s) == integer
