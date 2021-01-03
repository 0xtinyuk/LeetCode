# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def work(root: TreeNode,maxV: int, minV: int) -> int:
            if root is None:
                return 0
            ans = max(abs(maxV-root.val),abs(minV-root.val))
            maxV = max(root.val,maxV)
            minV = min(root.val,minV)
            ans = max(ans,work(root.left,maxV,minV))
            ans = max(ans,work(root.right,maxV,minV))
            return ans
        if root:
            return work(root,root.val,root.val)
        return 0