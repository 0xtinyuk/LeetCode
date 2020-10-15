class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        if matrix[0][0]>target:
            return False
        m=len(matrix)
        n=len(matrix[0])
        if matrix[m-1][n-1]<target:
            return False
        l=0
        r=m-1
        while l<r:
            if r-1==l:
                if matrix[r][0]==target:
                    return True
                if matrix[r][0]<target:
                    l=r
                break
            mid = (l+r)//2
            if matrix[mid][0]==target:
                return True
            if matrix[mid][0]>target:
                r=mid-1
            else:
                l=mid
        row = l
        if matrix[row][0]==target:
            return True
        l=0
        r=n-1
        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid]==target:
                return True
            if matrix[row][mid]<target:
                l = mid + 1
            else:
                r = mid - 1
        return False
