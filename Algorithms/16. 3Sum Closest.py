class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        v = 100000
        ans = 100000
        nums.sort()
        for i in range(len(nums)):
            # if nums[i]>target:
            #     break
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                # print(sum,nums[i],nums[j],nums[k])
                if abs(sum-target)<v:
                    v = abs(sum-target)
                    ans = sum
                if sum==target:
                    return ans
                elif sum<target:
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                else:
                    k-=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return ans    