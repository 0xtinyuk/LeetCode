class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        n=len(nums)
        pre = [nums[0]]
        for i in range(1,n):
            pre.append(min(pre[i-1],nums[i]))
        stack = [nums[n-1]]
        for i in range(n-2,0,-1):
            if nums[i]>pre[i-1]:
                while len(stack)>0 and stack[-1]<=pre[i-1]:
                    stack.pop()
                if len(stack)>0 and stack[-1]<nums[i]:
                    return True
                stack.append(nums[i])
        return False