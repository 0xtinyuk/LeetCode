# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        diff = 0
        curA=headA
        curB=headB
        while curA or curB:
            if curA and curB:
                curA=curA.next
                curB=curB.next
            else:
                if curA:
                    curA=curA.next
                    diff+=1
                else:
                    curB=curB.next
                    diff-=1
        curA=headA
        curB=headB
        if diff>0:
            while diff>0:
                curA=curA.next
                diff-=1
        if diff<0:
            while diff<0:
                curB=curB.next
                diff+=1
        while curA and curB:
            if curA==curB:
                return curA
            curA = curA.next
            curB = curB.next
        return None