class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        asc = True
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                asc = False
                break
        if asc:
            return arr
        for i in range(len(arr)-2,-1,-1):
            if arr[i]>arr[i+1]:
                pos = i+1
                for j in range(i+2,len(arr)):
                    if arr[j]<arr[i] and arr[j]>arr[pos]:
                        pos = j
                temp = arr[i]
                arr[i]=arr[pos]
                arr[pos] = temp
                return arr
        return arr