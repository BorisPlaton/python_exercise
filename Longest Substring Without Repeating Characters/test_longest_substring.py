import pytest
from longest_substring import Solution


@pytest.fixture(scope='function')
def solution_class():
    s = Solution()
    return s


@pytest.mark.parametrize(
    's,answer', [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("aab", 2),
        ("a", 1),
        ("dvdf", 3),
        ("ddddddddvdv", 2)
    ]
)
def test_longest_substring(solution_class, s, answer):
    assert solution_class.lengthOfLongestSubstring(s) == answer
