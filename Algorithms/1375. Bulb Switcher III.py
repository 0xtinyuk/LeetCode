class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        maxSoFar = 0
        ans = 0
        for i in range(len(light)):
            if light[i]>maxSoFar:
                maxSoFar = light[i]
            if i+1==maxSoFar:
                ans +=1
        return ans