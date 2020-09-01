# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        self.getMaxPath(root)
        return self.ans

    def getMaxPath(self, node: TreeNode) -> int:
        lm = rm = 0
        now = node.val
        if node.left != None:
            lm = self.getMaxPath(node.left)
            if lm+node.val > now:
                now = lm+node.val
        if node.right != None:
            rm = self.getMaxPath(node.right)
            if rm+node.val > now:
                now = rm+node.val
        m = lm+rm+node.val
        if m>now:
            if m>self.ans:
                self.ans = m
        else:
            if now>self.ans:
                self.ans = now
        return now
