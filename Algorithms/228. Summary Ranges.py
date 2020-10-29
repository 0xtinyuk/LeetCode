class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        start = nums[0]
        end = nums[0]
        ans = []
        for x in nums[1:]:
            if x==end+1:
                end = x
            else:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(str(start)+"->"+str(end))
                start = x
                end = x
        if start == end:
                ans.append(str(start))
        else:
            ans.append(str(start)+"->"+str(end))
        return ans 