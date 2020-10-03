class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if len(nums)<2:
            return 0
        nums.sort()
        ans=0
        i=0
        j=0
        while j<len(nums):
            if nums[j]-nums[i]==k:
                if (k==0) and (i==j):
                    j+=1
                else:
                    ans+=1
                    # print(nums[j],nums[i])
                    i=self.increase(nums,i)
                    j=self.increase(nums,j)
            elif nums[j]-nums[i]<k:
                j=self.increase(nums,j)
            else:
                i=self.increase(nums,i)
        return ans
    
    def increase(self, nums: List[int], x: int) -> int:
        x+=1
        while((x<len(nums)) and (nums[x]==nums[x-1])):
            x+=1
        return x
        
            
           