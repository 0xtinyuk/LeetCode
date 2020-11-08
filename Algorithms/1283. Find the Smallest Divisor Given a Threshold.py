class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums = sorted(nums)
        l = 1
        r = nums[-1]
        while r-l>1:
            mid = (l+r)//2
            mid_value=self.calculate(nums,mid)
            if mid_value<=threshold:
                r = mid
            else:
                l = mid+1
        if r-l==1:
            if self.calculate(nums,l)<=threshold:
                return l
            return r
        return l
    
    def calculate(self,nums:List[int],divisor:int) -> int:
        res = 0
        for x in nums:
            if x%divisor==0:
                res+=x//divisor
            else:
                res+=(x//divisor)+1
        return res