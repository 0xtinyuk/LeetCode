# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    can1 = None
    can2 = None
    ln = TreeNode(float("-inf"))

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        if self.can1 != None:
            if (self.can2 is None):
                self.can2 = self.ln
            t = self.can1.val
            self.can1.val = self.can2.val
            self.can2.val = t
        return

    def inorder(self, node: TreeNode) -> None:
        if(self.can1 != None) and (self.can2 != None):
            return
        if node.left != None:
            self.inorder(node.left)
        if self.can1 is None:
            if node.val < self.ln.val:
                self.can1 = self.ln
            self.ln = node
        else:
            if (self.can2 is None) and (self.can1.val < node.val):
                self.can2 = self.ln
            self.ln = node
        if(self.can1 != None) and (self.can2 != None):
            return
        if node.right != None:
            self.inorder(node.right)
        return