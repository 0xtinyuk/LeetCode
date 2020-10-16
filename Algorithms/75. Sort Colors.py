class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0=0
        c1=0
        c2=0
        for i in nums:
            if i==0:
                c0+=1
            if i==1:
                c1+=1
            if i==2:
                c2+=1
        for i in range(len(nums)):
            if c0>0:
                c0-=1
                nums[i]=0
                continue
            if c1>0:
                c1-=1
                nums[i]=1
                continue
            if c2>0:
                c2-=1
                nums[i]=2
                continue
        return
        