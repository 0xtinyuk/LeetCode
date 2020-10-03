class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[i for i in range(1,n+1)]
        return self.getPartialPermutation(nums,n,k)
    
    def getPartialPermutation(self, nums:List[int], n: int, k: int) -> str:
        if n==1:
            return str(nums[0])
        next_amount = 1
        for i in range(2,n):
            next_amount*=i
        current_index = (k-1)//next_amount
        current = str(nums[current_index])
        nums.pop(current_index)
        k-=current_index*next_amount
        return current+self.getPartialPermutation(nums,n-1,k)
        