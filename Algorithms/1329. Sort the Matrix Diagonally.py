class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        def sortOneDiagonal(x,y):
            sx = x
            sy = y
            cur = [mat[x][y]]
            while x+1<m and y+1<n:
                x+=1
                y+=1
                cur.append(mat[x][y])
            cur = sorted(cur)
            l = 0
            x = sx
            y = sy
            while l<len(cur):
                mat[x][y]=cur[l]
                l+=1
                x+=1
                y+=1
        for i in range(m-1):
            sortOneDiagonal(i,0)
        for i in range(1,n-1):
            sortOneDiagonal(0,i)
        return mat