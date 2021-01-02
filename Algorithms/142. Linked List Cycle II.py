# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return None
        fast = head.next.next
        slow = head.next
        while fast and slow and fast!=slow:
            if fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
        if (fast is None) or (slow is None):
            return None
        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next
        return fast
        