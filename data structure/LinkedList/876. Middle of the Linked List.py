# https://leetcode.com/problems/middle-of-the-linked-list/
# Oleg Belov

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = end = head
        while end and end.next:
            start = start.next
            end = end.next.next
        return start