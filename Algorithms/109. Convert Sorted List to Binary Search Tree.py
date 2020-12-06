# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        l = 0
        cur = head
        while cur:
            l+=1
            cur = cur.next
        def work(l,r):
            if l>r:
                return None
            nonlocal head
            mid = (l+r)//2
            ls = work(l,mid-1)
            node = TreeNode(head.val,ls)
            head = head.next
            node.right = work(mid+1,r)
            return node
        return work(1,l)
