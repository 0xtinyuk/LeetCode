# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        ans = None
        if l1.val<l2.val:
            ans = l1
            l1 = l1.next
        else:
            ans = l2
            l2 = l2.next
        head = ans
        while l1 and l2:
            if l1.val<l2.val:
                ans.next = l1
                l1 = l1.next
                ans = ans.next
            else:
                ans.next = l2
                l2 = l2.next
                ans = ans.next
        if l1:
            ans.next = l1
        if l2:
            ans.next = l2
        return head