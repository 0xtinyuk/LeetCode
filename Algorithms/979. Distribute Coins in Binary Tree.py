# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> List[int]:
            res = [0,0]
            if root is None:
                return res
            lr = dfs(root.left)
            rr = dfs(root.right)
            res[0]+=lr[0]+rr[0]+abs(lr[1])+abs(rr[1])
            res[1]=lr[1]+rr[1]+root.val-1
            return res
        return dfs(root)[0]