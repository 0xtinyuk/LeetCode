# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        ans = ListNode(-1,head)
        cur = head
        head = head.next
        cur.next = None
        while not(head is None):
            candidate = head
            head = head.next
            pre = ans
            cur = ans.next
            while (not (cur is None)) and (cur.val<candidate.val):
                pre=pre.next
                cur=cur.next
            pre.next = candidate
            candidate.next = cur
        return ans.next
        