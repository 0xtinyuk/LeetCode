class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums)<=0:
            return False
        largest = self.searchLast(nums,0,len(nums)-1)
        if nums[0]<=target:
            r=largest
            l=0
        else:
            l=largest+1
            r=len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return True
            if nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False

    def searchLast(self,nums: List[int],l:int,r:int)-> int:
        if l>=r:
            return l
        if r-1==l:
            if nums[r]<nums[0]:
                return l
            else:
                return r
        mid = (l+r)//2
        if nums[mid]<nums[0]:
            return self.searchLast(nums,l,mid-1)
        elif nums[mid]>nums[0]:
            return self.searchLast(nums,mid,r)
        result_left = self.searchLast(nums,l,mid-1)
        result_right = self.searchLast(nums,mid,r)
        if nums[result_left]>nums[result_right]:
            return result_left
        return result_right 
