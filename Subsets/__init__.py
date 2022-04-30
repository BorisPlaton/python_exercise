import itertools
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = []
        for i in range(len(nums)+1):
            l += [list(combination) for combination in itertools.combinations(nums, i)]
        return l
