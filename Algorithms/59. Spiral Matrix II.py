class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if(n==0):
            return []
        matrix=[[0 for i in range(n)] for j in range(n)]
        upper=0
        lower=n
        left=0
        right=n
        ans=0
        while (upper<lower) and (left<right):
            for i in range(left,right):
                ans+=1
                matrix[upper][i]=ans
            upper+=1
            for i in range(upper,lower):
                ans+=1
                matrix[i][right-1]=ans
            right-=1
            if upper>=lower or left>=right:
                break
            for i in range(right-1,left-1,-1):
                ans+=1
                matrix[lower-1][i]=ans
            lower-=1
            for i in range(lower-1,upper-1,-1):
                ans+=1
                matrix[i][left]=ans
            left+=1
        return matrix
                 