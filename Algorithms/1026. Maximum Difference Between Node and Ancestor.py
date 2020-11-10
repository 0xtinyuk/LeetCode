# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def work(root:TreeNode)-> List[int]:
            if root is None:
                return None
            lr = work(root.left)
            rr = work(root.right)
            mini = root.val
            maxi = root.val
            ans = 0
            if lr:
                ans = max(ans,max(abs(root.val-lr[0]),abs(root.val-lr[1])))
                ans = max(ans,lr[2])
                mini = min(mini,lr[0])
                maxi = max(maxi,lr[1])
            if rr:
                ans = max(ans,max(abs(root.val-rr[0]),abs(root.val-rr[1])))
                ans = max(ans,rr[2])
                mini = min(mini,rr[0])
                maxi = max(maxi,rr[1])
            return [mini,maxi,ans]
        if root is None:
            return 0
        return work(root)[2]