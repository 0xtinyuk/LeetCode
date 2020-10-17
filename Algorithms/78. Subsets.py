class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        tmp = self.subsets(nums[1:])
        ans = []
        for l in tmp:
            ans.append([nums[0]]+l)
            ans.append(l)
        return ans