class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        if len(nums)==1:
            if nums[0]==target:
                return [0,0]
            return [-1,-1]
        self.nums=nums
        self.t=target
        ans_l =  self.find(True)
        if ans_l>=len(self.nums)  or nums[ans_l]!=self.t:
            return [-1,-1]
        ans_r = self.find(False)
        return [ans_l,ans_r-1]
    
    def find(self,find_left_side:bool)->int:
        l=0
        r=len(self.nums)
        while l<r:
            mid=(l+r)//2
            if self.nums[mid]>self.t or (find_left_side and (self.nums[mid]==self.t)):
                r=mid
            else:
                l=mid+1
        return l