class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=0:
            return 0
        mark=1<<70
        ln=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==ln:
                nums[i]=mark
            else:
                ln=nums[i]
        j=1
        for i in range(1,len(nums)):
            if nums[i]!=mark:
                nums[j]=nums[i]
                j+=1
        return j
        
                