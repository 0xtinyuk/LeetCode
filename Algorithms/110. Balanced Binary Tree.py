# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def work(root:TreeNode):
            if root is None:
                return (0,True)
            ls = work(root.left)
            rs = work(root.right)
            depth = max(ls[0],rs[0])+1
            balanced = ls[1] and rs[1] and (abs(ls[0]-rs[0])<=1)
            return (depth,balanced)
        return work(root)[1]