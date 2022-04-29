import pytest
from ransom_note import Solution


class TestRomanToInt:

    @pytest.fixture(scope='function')
    def solution_class(self):
        solution = Solution()
        return solution

    @pytest.mark.parametrize('ransomNote,magazine,answer', [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
    ])
    def test_roman_to_int(self, solution_class, ransomNote, magazine, answer):
        assert solution_class.canConstruct(ransomNote, magazine) == answer
