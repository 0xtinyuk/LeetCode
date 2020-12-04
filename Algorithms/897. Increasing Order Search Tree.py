# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans = TreeNode(-1)
        self.cur = self.ans
        self.work(root)
        return self.ans.right
    
    def work(self,root:TreeNode):
        if root is None:
            return
        self.work(root.left)
        self.cur.right = root
        root.left = None
        self.cur = self.cur.right
        self.work(root.right)
        return