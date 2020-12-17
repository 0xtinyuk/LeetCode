# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    current = []
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None:
            return []
        sum = sum - root.val
        self.current.append(root.val)
        if (sum==0) and (root.left is None) and (root.right is None):
            ans = [copy.deepcopy(self.current)]
            self.current.pop()
            return ans
        ans = self.pathSum(root.left,sum) + self.pathSum(root.right,sum)
        self.current.pop()
        return ans