class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        s = 0
        ans = 0
        for i in arr:
            if s + i <= 5000:
                s = s+i
                ans = ans + 1
            else:
                break
        return ans
