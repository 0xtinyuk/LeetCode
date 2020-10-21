class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        m=len(matrix)
        if m<=0:
            return 0
        n=len(matrix[0])
        longest = [0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="1":
                    longest[j]+=1
                    length=longest[j]
                    ans = max(ans,longest[j])
                    for k in range(j-1,-1,-1):
                        if longest[k]==0:
                            break
                        length=min(length,longest[k])
                        ans=max(ans,length*(j-k+1))
                else:
                    longest[j]=0

        return ans
