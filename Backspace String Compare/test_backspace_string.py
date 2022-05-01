import pytest
from backspace_string import Solution


class TestBackspaceString:

    @pytest.fixture(scope='function')
    def solution_class(self):
        return Solution()

    @pytest.mark.parametrize(
        's,t,answer', [
            ("ab##", "c#d#", True),
            ("a#c", "b", False),
            ("#ac#", "a", True)
        ]
    )
    def test_backspace_string(self, s, t, answer, solution_class):
        assert solution_class.backspaceCompare(s, t) == answer
