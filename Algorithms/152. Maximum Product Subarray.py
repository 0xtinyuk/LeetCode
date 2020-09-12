class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return 0
        p=nums[0]
        n=nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i]>0:
                nn=min(nums[i]*n,nums[i])
                np=max(nums[i],p*nums[i])
            elif nums[i]<0:
                nn=min(nums[i]*p,nums[i])
                np=max(nums[i]*n,nums[i])
            else:
                nn=0
                np=0
            n=nn
            p=np
            if p>ans:
                ans = p
        return ans
        