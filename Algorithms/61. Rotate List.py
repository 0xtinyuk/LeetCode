# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        current = head
        tail = head
        n = 0
        while not (current is None):
            n+=1
            tail = current
            current=current.next
        if n==0:
            return None
        k%=n
        if k==0:
            return head
        move = n-k-1
        current = head
        while(move>0):
            move-=1
            current=current.next
        new_tail = current
        tail.next = head
        head = new_tail.next
        new_tail.next = None
        return head