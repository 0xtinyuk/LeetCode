class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        u,b = 0,len(matrix)-1
        l,r = 0, len(matrix[0])-1
        ans = []
        while True:
            if u<=b:
                for j in range(l,r+1):
                    ans.append(matrix[u][j])
                u+=1
            else:
                break
            if l<=r:
                for i in range(u,b+1):
                    ans.append(matrix[i][r])
                r-=1
            else:
                break
            if u<=b:
                for j in range(r,l-1,-1):
                    ans.append(matrix[b][j])
                b-=1
            else:
                break
            if l<=r:
                for i in range(b,u-1,-1):
                    ans.append(matrix[i][l])
                l+=1
            else:
                break
        return ans
                