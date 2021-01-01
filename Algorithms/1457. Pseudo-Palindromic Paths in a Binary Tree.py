# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    f = [0 for i in range(10)]
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.f[root.val]+=1
        ans = 0
        if root.left or root.right:
            ans += self.pseudoPalindromicPaths(root.left) + self.pseudoPalindromicPaths(root.right)
        else:
            oddf = 0
            for x in self.f:
                if x%2==1:
                    oddf+=1
            if oddf<=1:
                ans = 1
            else:
                ans = 0
        self.f[root.val]-=1
        return ans