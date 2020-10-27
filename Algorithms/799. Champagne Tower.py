class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cur = [poured]
        for i in range(query_row):
            post = [0 for j in range(i+2)]
            for j in range(i+1):
                if cur[j]>1:
                    post[j]+=(cur[j]-1)/2
                    post[j+1]+=(cur[j]-1)/2
            cur = post
        if cur[query_glass]>1:
            ans = 1
        else:
            ans = cur[query_glass]
        return ans