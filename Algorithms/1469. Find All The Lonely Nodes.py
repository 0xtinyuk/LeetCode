# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        ans = self.getLonelyNodes(root.left) + self.getLonelyNodes(root.right)
        if root.left is None:
            if root.right:
                ans.append(root.right.val)
        if root.right is None:
            if root.left:
                ans.append(root.left.val)
        return ans