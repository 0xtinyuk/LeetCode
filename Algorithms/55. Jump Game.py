class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if(len(nums)<=0):
            return True
        f=0
        for i in range(len(nums)):
            if i>f:
                return False
            f=max(f,nums[i]+i)
        return True