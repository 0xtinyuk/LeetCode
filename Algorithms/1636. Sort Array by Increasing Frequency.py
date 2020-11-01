class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        f = [0 for i in range(201)]
        candidate = []
        for i in range(len(nums)):
            if f[nums[i]+100]==0:
                candidate.append(nums[i])
            f[nums[i]+100]+=1
        candidate = sorted(candidate, key=lambda x:(f[x+100],-x))
        ans = []
        for x in candidate:
            for j in range(f[x+100]):
                ans.append(x)
        return ans
        
        