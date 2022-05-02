from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_digits = int(''.join(self.get_list_of_digits(l1)))
        l2_digits = int(''.join(self.get_list_of_digits(l2)))

        return self.get_list_node(map(int, str(l1_digits + l2_digits)[::-1]))

    @staticmethod
    def get_list_of_digits(node):
        l = []
        while node:
            l.append(str(node.val))
            node = node.next
        return l[::-1]

    @staticmethod
    def get_list_node(mas):
        head_node = None
        previous_node = None
        for val in mas:

            new_node = ListNode(val)

            if not head_node:
                head_node = new_node
                previous_node = new_node
                continue

            previous_node.next = new_node
            previous_node = new_node

        return head_node
