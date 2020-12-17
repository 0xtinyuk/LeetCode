class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        increase = True
        if arr[1]<=arr[0]:
            return False
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                if increase:
                    continue
                return False
            if arr[i]==arr[i-1]:
                return False
            if arr[i]<arr[i-1]:
                if increase:
                    increase = False
                    continue
        if increase:
            return False
        return True