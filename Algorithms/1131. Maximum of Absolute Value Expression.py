class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        def cal(s1:int,s2:int):
            maxV = -10**11
            minV = 10*11
            for i in range(len(arr1)):
                temp = s1*arr1[i]+s2*arr2[i] + i
                maxV = max(maxV,temp)
                minV = min(minV,temp)
            return maxV-minV
        ans = 0
        for i in [-1,1]:
            for j in [-1,1]:
                ans = max(ans,cal(i,j))
        return ans