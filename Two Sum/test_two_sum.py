import pytest
from two_sum import Solution


class TestTwoSum:

    @pytest.fixture(scope='function')
    def solution_class(self):
        solution = Solution()
        return solution

    @pytest.mark.parametrize('nums,target,answer', [
        ([-3, 4, 3, 90], 0, [0, 2]),
        ([2, 7, 11, 15], 9, [0, 1])
    ])
    def test_k_weakest(self, solution_class, nums, target, answer):
        assert solution_class.twoSum(nums, target) == answer
