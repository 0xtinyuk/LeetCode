# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root == None:
            return 0
        l = self.traversal(root)
        if len(l) <= 1:
            return 0
        l.sort()
        ans = abs(l[0]-l[1])
        for i in range(1, len(l)-1):
            ans = min(ans, abs(l[i]-l[i+1]))
        return ans

    def traversal(self, node: TreeNode) -> []:
        result = [node.val]
        if node.left == None and node.right == None:
            return result
        if node.left != None:
            result.extend(self.traversal(node.left))
        if node.right != None:
            result.extend(self.traversal(node.right))
        return result
