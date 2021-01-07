class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        last = 0
        s = 0
        for x in arr:
            temp = x-last-1+s
            if temp>=k:
                return last+(k-s)
            s = temp
            last = x
        return last+(k-s)