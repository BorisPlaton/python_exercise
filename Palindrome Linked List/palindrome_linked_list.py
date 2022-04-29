from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []

        while head:
            l.append(head.val)
            head = head.next

        middle_i, middle = len(l) % 2, len(l) // 2
        l = l[:middle] + l[middle + 1:] if middle_i else l

        for index in range(middle):
            if l[index] != l[-1 - index]:
                return False

        return True
