# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ans = ListNode(-1)
        new = ans
        head = ListNode(-1,head)
        current = head.next
        pre = head
        while not (current is None):
            if current.val<x:
                new.next = current
                new = current
                pre.next = current.next
                current = current.next
            else:
                pre = current
                current = current.next
        new.next = head.next
        return ans.next
