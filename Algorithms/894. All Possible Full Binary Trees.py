# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    ans = {0: [], 1: {TreeNode(0)}}

    def allPossibleFBT(self, N: int) -> []:
        if N in self.ans:
            return self.ans[N]
        cnt = []
        for i in range(N):
            if i % 2 == 1:
                j = N - 1 - i
                for x in self.allPossibleFBT(i):
                    for y in self.allPossibleFBT(j):
                        tem = TreeNode(0)
                        tem.left = x
                        tem.right = y
                        cnt.append(tem)
        self.ans[N] = cnt
        return cnt