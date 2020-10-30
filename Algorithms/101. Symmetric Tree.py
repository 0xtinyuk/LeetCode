# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.compare(root.left,root.right)

    def compare(self, x: TreeNode, y: TreeNode) -> bool:
        if (x is None) and (y is None):
            return True
        if (x is None) or (y is None):
            return False
        if x.val!=y.val:
            return False
        return self.compare(x.left,y.right) and self.compare(x.right,y.left) 