import heapq
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.heap = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self._find_min_in_tree(root)

        [heapq.heappop(self.heap) for _ in range(k - 1)]

        return self.heap[0]

    def _find_min_in_tree(self, node):

        heapq.heappush(self.heap, node.val)

        if node.left:
            self._find_min_in_tree(node.left)

        if node.right:
            self._find_min_in_tree(node.right)
