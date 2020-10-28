# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if (head is None) or (head.next is None):
            return None
        s = head
        f = head
        while not ((f.next is None)):
            s=s.next
            f=f.next.next
            if f is None:
                return None
            if f is s:
                break
        if f.next is None:
            return None
        #The number of steps that s moved is the length of cycle
        #s moving (n-l) more steps can reach ans 
        #from head moving (n-l) steps is also ans
        f = head
        while not(s is f):
            s=s.next
            f=f.next
        return s