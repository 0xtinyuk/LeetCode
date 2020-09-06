# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        li=[]
        for i in lists:
            current = i
            while not(current is None):
                li.append(current.val)
                current = current.next
        li.sort()
        head = current= ListNode(0)
        for v in li:
            current.next = ListNode(v)
            current=current.next
        return head.next
        
