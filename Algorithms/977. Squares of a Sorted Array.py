class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = len(nums)
        for i in range(len(nums)):
            if nums[i]>=0:
                start = i
                break 
        if start == len(nums):
            return [nums[i]*nums[i] for i in range(len(nums)-1,-1,-1)]
        if start == 0:
            return [nums[i]*nums[i] for i in range(len(nums))]
        ans = []
        i=start-1
        j=start
        while i>=0 or j<len(nums):
            if i>=0 and j<len(nums):
                if abs(nums[i])<abs(nums[j]):
                    ans.append(nums[i]*nums[i])
                    i-=1
                else:
                    ans.append(nums[j]*nums[j])
                    j+=1
                continue
            if i>=0:
                ans.append(nums[i]*nums[i])
                i-=1
                continue
            if j<len(nums):
                ans.append(nums[j]*nums[j])
                j+=1
                continue
        return ans