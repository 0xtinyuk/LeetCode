class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        even_1 = nums[0]
        even_0 = 0
        odd_0 = nums[1]
        odd_1 = nums[0]
        for i in range(2,len(nums)):
            if i%2==0:
                even_0 += nums[i]
                even_1 += nums[i]
                if odd_0>even_0:
                    even_0=odd_0
                if odd_1>even_1:
                    even_1=odd_1
            else:
                odd_0 += nums[i]
                odd_1 += nums[i]
                if odd_0<even_0:
                    odd_0=even_0
                if odd_1<even_1:
                    odd_1=even_1
        if (len(nums)-1)%2==0:
            ans = max(even_0,max(odd_1,odd_0))
        else:
            ans = max(odd_0,max(even_0,even_1))
        return ans