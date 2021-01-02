# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddH = ListNode(-1)
        odd = oddH
        even = ListNode(-1)
        evenH = even
        while head:
            odd.next = head
            head = head.next
            odd = odd.next
            odd.next = None
            if head:
                even.next = head
                head = head.next
                even = even.next
                even.next = None
        odd.next = evenH.next
        return oddH.next