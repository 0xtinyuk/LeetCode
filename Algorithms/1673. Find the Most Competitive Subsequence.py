class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            atLeast = k-n+i+1
            while len(ans)>=atLeast and len(ans)>0 and ans[-1]>nums[i]:
                ans.pop()
            ans.append(nums[i])
        return ans[:k]