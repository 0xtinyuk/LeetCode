# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        head = ListNode(-1,head)
        pre = head
        cur = head.next
        if cur is None:
            return None
        for _ in range(m-1):
            cur=cur.next
            pre=pre.next
        pre_reverse = pre
        first_reverse = cur
        pre = pre.next
        cur = cur.next
        if not (cur is None):
            post = cur.next
        for _ in range(n-m):
            cur.next = pre
            pre = cur
            cur = post
            if not (post is None):
                post = post.next
        pre_reverse.next = pre
        first_reverse.next = cur
        return head.next

            