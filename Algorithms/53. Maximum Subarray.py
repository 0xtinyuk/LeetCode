class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return 0
        ans = nums[0]
        tmp = nums[0]
        for i in range(1,len(nums)):
            tmp+=nums[i]
            if nums[i]>tmp:
                tmp=nums[i]
            if tmp>ans:
                ans=tmp
        return ans    