from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self):
        self.nodes_list = []
        self.list = None

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        self._find_all_nodes(head)
        return self.list

    def _find_all_nodes(self, node):

        self.nodes_list.append(node.val)

        if node.next:
            return self._find_all_nodes(node.next)

        self._build_reversed_list(ListNode(self.nodes_list.pop()))

    def _build_reversed_list(self, node):

        if not self.list:
            self.list = node

        if self.nodes_list:
            next_node = ListNode(self.nodes_list.pop())
            node.next = next_node
            self._build_reversed_list(next_node)
