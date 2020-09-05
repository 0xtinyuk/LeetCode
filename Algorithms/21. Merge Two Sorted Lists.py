# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 is None) and (l2 is None):
            return None
        if (not (l1 is None)) and (not(l2 is None)):
            if l1.val<l2.val:
                head = l1
                l1=l1.next
            else:
                head = l2
                l2=l2.next
            current = head
            while (not(l1 is None)) and (not(l2 is None)):
                if l1.val<l2.val:
                    current.next = l1
                    l1=l1.next
                else:
                    current.next=l2
                    l2=l2.next
                current=current.next
            if l1 is None:
                current.next=l2
            else:
                current.next=l1
            return head
        else:
            if l1 is None:
                return l2
            else:
                return l1   