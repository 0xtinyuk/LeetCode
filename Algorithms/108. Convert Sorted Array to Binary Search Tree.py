# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        self.nums = nums
        return self.work(0,len(nums)-1)

    def work(self,l,r) -> TreeNode:
        if l>r:
            return None
        mid = (r+l)//2
        root = TreeNode(self.nums[mid])
        root.left = self.work(l,mid-1)
        root.right = self.work(mid+1,r)
        return root