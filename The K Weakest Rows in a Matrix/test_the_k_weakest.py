import pytest
from the_k_weakest import Solution


class TestKWeakest:

    @pytest.fixture(scope='function')
    def solution_class(self):
        solution = Solution()
        return solution

    @pytest.mark.parametrize('mat,k,answer', [
        ([[1, 1, 0, 0, 0],
          [1, 1, 1, 1, 0],
          [1, 0, 0, 0, 0],
          [1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1]], 3, [2, 0, 3]),
        ([[1, 1, 0],
          [1, 0, 0],
          [1, 0, 0],
          [1, 1, 1],
          [1, 1, 0],
          [0, 0, 0]], 4, [5, 1, 2, 0])
    ])
    def test_k_weakest(self, solution_class, mat, k, answer):
        assert solution_class.kWeakestRows(mat, k) == answer
