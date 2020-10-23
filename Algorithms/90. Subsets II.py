class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        return self.search(nums)
    
    def search(self,nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        i = 0
        while i+1<len(nums) and nums[i]==nums[i+1]:
            i+=1
        tmp = self.search(nums[i+1:])
        ans = copy.copy(tmp)
        for j in range(0,i+1):
            for l in tmp:
                ans.append(nums[:j+1]+l)
        return ans
        