class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return len(nums)
        last = nums[0]
        counter = 1
        j=0
        for i in range(1,len(nums)):
            if nums[i]==last:
                if counter == 2:
                    continue
                counter +=1
            else:
                last = nums[i]
                counter = 1
            j+=1
            nums[j]=nums[i]
        return j+1