class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [nums[0]]
        ans = []
        for i in range(1,k):
            while (len(q)>0 and q[-1]<nums[i]):
                q.pop()
            q.append(nums[i])
        ans.append(q[0])
        for i in range(k,len(nums)):
            x = nums[i-k]
            if q[0]==x:
                q.pop(0)
            while (len(q)>0 and q[-1]<nums[i]):
                q.pop()
            q.append(nums[i])
            ans.append(q[0])
        return ans