# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = ListNode(l1.val+l2.val)
        r = sum
        while True:
            if sum.val>=10:
                sum.val -= 10
                sum.next = ListNode(1)
                if l1.next!=None or l2.next!=None:
                    if l1.next!=None:
                        sum.next.val+=l1.next.val
                        l1 = l1.next
                    if l2.next!=None:
                        sum.next.val+=l2.next.val
                        l2 = l2.next
                sum = sum.next
            else:
                if l1.next!=None or l2.next!=None:
                    sum.next = ListNode(0)
                    if l1.next!=None:
                        sum.next.val+=l1.next.val
                        l1 = l1.next
                    if l2.next!=None:
                        sum.next.val+=l2.next.val
                        l2 = l2.next
                    sum = sum.next
            if l1.next==None and l2.next==None:
                break
        if sum.val>=10:
            sum.val -= 10
            sum.next = ListNode(1)
        return r
        