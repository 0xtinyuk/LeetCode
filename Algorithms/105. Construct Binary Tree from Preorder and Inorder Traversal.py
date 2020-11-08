# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)<=0:
            return None
        cur = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])
        cur.left = self.buildTree(preorder[1:1+pos],inorder[:pos])
        cur.right = self.buildTree(preorder[1+pos:],inorder[pos+1:])
        return cur