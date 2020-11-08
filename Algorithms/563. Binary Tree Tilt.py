# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def work(root:TreeNode) -> (int,int):
            if root is None:
                return (0,0)
            (lsum,ltilt) = work(root.left)
            (rsum,rtilt) = work(root.right)
            s = lsum+rsum+root.val
            tilt = abs(rsum-lsum)
            return (s,ltilt+rtilt+tilt)
        return work(root)[1]