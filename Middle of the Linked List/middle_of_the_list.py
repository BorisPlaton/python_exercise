class Solution:
    def middleNode(self, head):
        count = 0
        itr = head
        while itr:
            count += 1
            itr = itr.next

        for i in range(count // 2):
            head = head.next
        return head
