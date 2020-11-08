# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = []
        s2 = []
        cur = l1
        while not (cur is None):
            s1.append(cur.val)
            cur = cur.next
        cur = l2
        while not (cur is None):
            s2.append(cur.val)
            cur = cur.next
        post = None
        accu = 0
        while len(s1)>0 or len(s2)>0:
            x = y = 0
            if len(s1)>0:
                x = s1.pop()
            if len(s2)>0:
                y = s2.pop()
            cur = ListNode((x+y+accu)%10,post)
            post = cur
            accu = (x+y+accu)//10
        if accu>0:
            return ListNode(accu,post)
        return post