# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.work(root)[1]
        
    def work(self, root: TreeNode) -> (int,int):
        if root is None:
            return (0,0)
        la = self.work(root.left)
        ra = self.work(root.right)
        a0 = la[1] + ra[1]
        a1 = max(a0, la[0] + ra[0] + root.val)
        return (a0,a1)