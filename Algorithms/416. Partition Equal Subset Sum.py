class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2==1:
            return False
        v = s//2
        f = [False for i in range(v+1)]
        f[0]=True
        for i in range(len(nums)):
            for j in range(v-nums[i],-1,-1):
                if f[j]:
                    f[j+nums[i]]=True
            if f[v]:
                return True
        if f[v]:
            return True
        return False
