# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def work(root:TreeNode):
            if root is None:
                return (None,0)
            ls = work(root.left)
            rs = work(root.right)
            if ls[1]==rs[1]:
                return (root,ls[1]+1)
            if ls[1]>rs[1]:
                return (ls[0],ls[1]+1)
            return (rs[0],rs[1]+1)
        return work(root)[0] 