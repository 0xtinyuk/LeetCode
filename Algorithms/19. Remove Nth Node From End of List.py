# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        last = head
        for i in range(n):
            last=last.next
        if last is None:
            return head.next
        first = head
        while not (last.next is None):
            first = first.next
            last = last.next
        first.next = first.next.next
        return head
        
        