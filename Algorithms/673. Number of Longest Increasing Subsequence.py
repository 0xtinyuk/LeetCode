class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return 0
        f = [1 for i in range(len(nums))]
        s = [1 for i in range(len(nums))]
        longest_length = 1
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    if f[j]+1>f[i]:
                        f[i]=f[j]+1
                        s[i]=s[j]
                    elif f[j]+1==f[i]:
                        s[i]+=s[j]
            if f[i]>longest_length:
                longest_length=f[i]
        
        ans = 0
        for i in range(len(nums)):
            if f[i]==longest_length:
                ans+=s[i]
        return ans