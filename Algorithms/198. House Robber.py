class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return 0
        ans1=0
        ans0=0
        for i in range(len(nums)):
            if i%2==0:
                ans0+=nums[i]
                if ans1>ans0:
                    ans0=ans1
            else:
                ans1+=nums[i]
                if ans0>ans1:
                    ans1=ans0
        if ans1>ans0:
            return ans1
        return ans0   