class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1 or k==0:
            return
        n=len(nums)
        if k>n:
            k=k%n
        initial = 0
        counter = 0
        while counter<n:
            i=initial
            last = nums[initial]
            while True:
                if i+k<n-1:
                    i+=k
                else:
                    i=(i+k)-n
                new = nums[i]
                nums[i]=last
                last = new
                counter+=1
                if i==initial:
                    break
            initial+=1
        return