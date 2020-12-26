class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        sx = 0
        sy = 0
        m = len(matrix)
        if m==0:
            return []
        n = len(matrix[0])
        if n==0:
            return []
        ans = []
        reverse = False
        while sx<m and sy<n:
            x=sx
            y=sy
            temp = []
            while x>=0 and y<n:
                temp.append(matrix[x][y])
                x-=1
                y+=1
            if reverse:
                temp.reverse()
            reverse = not reverse
            ans = ans + temp
            if (sx==m-1):
                sy+=1
            else:
                sx+=1
        return ans