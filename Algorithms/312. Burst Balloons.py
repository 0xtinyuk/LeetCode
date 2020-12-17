class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        memory = [[0 for j in range(len(nums))] for i in range(len(nums))]
        def work(x,y):
            if memory[x][y]>0:
                return memory[x][y]
            for i in range(x+1,y):
                temp = nums[x]*nums[y]*nums[i] + work(x,i)+work(i,y)
                if temp>memory[x][y]:
                    memory[x][y]=temp
            return memory[x][y]
        return work(0,len(nums)-1)