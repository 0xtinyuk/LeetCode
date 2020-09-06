# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (head is None) or (head.next is None):
            return head
        head = ListNode(0,head)
        pre = head
        now = head.next
        while (not (now is None)) and (not(now.next is None)):
            nt = now.next
            pre.next = nt
            now.next = nt.next
            nt.next=now
            pre=now
            now=now.next
        return head.next