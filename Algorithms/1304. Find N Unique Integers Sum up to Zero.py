class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2==1:
            ans = [0]
            n-=1
        else:
            ans = []
        for i in range(n//2):
            ans.append(i+1)
            ans.append(-(i+1))
        return ans