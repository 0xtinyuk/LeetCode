class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(len(nums)-1,i+2,-1):
                if j<len(nums)-1 and nums[j]==nums[j+1]:
                    continue
                k=i+1
                l=j-1
                while(k<l):
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    # print(i,k,l,j)
                    if sum==target:
                        candidate = [nums[i],nums[k],nums[l],nums[j]]
                        if not (candidate in ans):
                            ans.append(candidate)
                        k+=1
                        l-=1
                        # while k<l and nums[k]==nums[k-1]:
                        #     k+=1
                        # while k<l and nums[l]==nums[l+1]:
                        #     l-=1
                    elif sum<target:
                        k+=1
                    else:
                        l-=1
        return ans