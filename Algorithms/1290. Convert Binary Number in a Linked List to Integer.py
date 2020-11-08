# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if head is None:
            return 0
        cur = head
        length = 0
        while not (cur.next is None):
            length+=1
            cur=cur.next
        cur = head
        ans = 0
        while not (cur is None):
            ans += cur.val * (1<<length)
            cur=cur.next
            length-=1
        return ans
        