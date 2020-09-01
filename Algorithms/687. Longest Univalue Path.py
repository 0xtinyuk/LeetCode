# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l = self.longestPath(root)
        return l[0]

    def longestPath(self, node: TreeNode) -> [int, int]:
        if node.left == None and node.right == None:
            return [0, 0]
        dp = 0
        lp = 0
        if node.left != None:
            ll = self.longestPath(node.left)
            lp = max(lp, ll[0])
            if node.left.val == node.val:
                dp = max(dp, ll[1]+1)
                lp = max(lp, ll[1]+1)
        if node.right != None:
            rl = self.longestPath(node.right)
            lp = max(lp, rl[0])
            if node.right.val == node.val:
                dp = max(dp, rl[1]+1)
                lp = max(lp, rl[1]+1)
        if node.left != None and node.right != None:
            if node.left.val == node.val == node.right.val:
                lp = max(lp, ll[1]+rl[1]+2)
        return [lp, dp]
