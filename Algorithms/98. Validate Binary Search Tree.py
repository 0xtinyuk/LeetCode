# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root,None,None)

    def check(self, root : TreeNode, l: int, r: int) -> bool:
        if root is None:
            return True
        if (not l is None) and (root.val<=l):
            return False
        if (not r is None) and (root.val>=r):
            return False
        return self.check(root.left,l,root.val) and self.check(root.right,root.val,r)