# https://leetcode.com/problems/remove-nth-node-from-end-of-list
# Oleg Belov

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        start = end = head
        
        i = 0
        while i != n:
            end = end.next
            i += 1
            
        if end == None:
            return head.next

        while end.next:
            start = start.next
            end = end.next
        else:
            start.next = start.next.next

        return head