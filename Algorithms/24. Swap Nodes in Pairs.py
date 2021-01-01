# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        head = ListNode(-1,head)
        cur = head
        while cur and cur.next:
            p1 = cur.next
            p2 = p1.next
            if p2 is None:
                break
            p1.next = p2.next
            p2.next = p1
            cur. next = p2
            cur = p1
        return head.next