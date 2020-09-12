class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums)<=0:
            return []
        start = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1]>nums[i]:
                start = i
                break
        if start == -1:
            nums.sort()
            return
        candidate_value = nums[start+1]
        candidate_index=start+1
        for i in range(start+1,len(nums)):
            if nums[i]<=nums[start]:
                break
            if nums[i]<candidate_value:
                candidate_value=nums[i]
                candidate_index=i
        # temp = nums[start]
        # nums[start]=candidate_value
        # nums[candidate_index]=temp
        nums[start],nums[candidate_index]=nums[candidate_index],nums[start]
        for i in range(start+1,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        """
        Do not return anything, modify nums in-place instead.
        """