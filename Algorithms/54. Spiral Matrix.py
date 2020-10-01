class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        upper=0
        lower=len(matrix)
        if(lower<=0):
            return []
        left=0
        right=len(matrix[0])
        if(right<=0):
            return []
        ans=[]
        while (upper<lower) and (left<right):
            for i in range(left,right):
                ans.append(matrix[upper][i])
            upper+=1
            for i in range(upper,lower):
                ans.append(matrix[i][right-1])
            right-=1
            if upper>=lower or left>=right:
                break
            for i in range(right-1,left-1,-1):
                ans.append(matrix[lower-1][i])
            lower-=1
            for i in range(lower-1,upper-1,-1):
                ans.append(matrix[i][left])
            left+=1
        return ans
              