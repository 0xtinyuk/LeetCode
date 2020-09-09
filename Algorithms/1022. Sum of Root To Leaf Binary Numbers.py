# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.dfs(root,0)
        
    def dfs(self,root:TreeNode,temp:int)->int :
        temp = (temp<<1)+root.val
        ans = 0
        if(root.left is None) and (root.right is None):
            return temp
        if root.left:
            ans += self.dfs(root.left,temp)
        if root.right:
            ans += self.dfs(root.right,temp)
        return ans
            
        