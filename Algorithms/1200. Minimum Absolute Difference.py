class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        d = 10000000
        last = -10000000
        for i in arr:
            if(abs(i-last) < d):
                d = abs(i-last)
            last = i
        ans = []
        last = arr[0]
        for i in range(1, len(arr)):
            if abs(arr[i]-last) == d:
                ans.append([last, arr[i]])
            last = arr[i]
        return ans
