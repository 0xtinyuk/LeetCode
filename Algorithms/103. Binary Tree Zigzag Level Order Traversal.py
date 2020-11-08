# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.ans = []
        self.traverse(root,0)
        for i in range(1,len(self.ans),2):
            self.ans[i].reverse()
        return self.ans
    
    def traverse(self, root:TreeNode, depth:int):
        if root is None:
            return
        self.traverse(root.left,depth+1)
        while len(self.ans)<=depth:
            self.ans.append([])
        self.ans[depth].append(root.val)
        self.traverse(root.right,depth+1)
        return    