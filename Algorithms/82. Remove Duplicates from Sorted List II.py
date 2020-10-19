# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head = ListNode(-1,head) 
        previous = head
        current = previous.next
        while not (current is None):
            post = current.next
            if (post is None) or (post.val!=current.val):
                previous=current
                current = post
                continue
            else:
                while (not (post is None)) and (post.val==current.val):
                    post=post.next
                previous.next=post
                current = post
        return head.next