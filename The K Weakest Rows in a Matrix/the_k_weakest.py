from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        rows_list = []
        for index, row in enumerate(mat):
            rows_list.append((index, row.count(1)))

        return [i[0] for index, i in zip(range(k), sorted(rows_list, key=lambda x: (x[1], x[0])))]
