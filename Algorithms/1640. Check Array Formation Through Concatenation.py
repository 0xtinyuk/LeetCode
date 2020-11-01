class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mark = {}
        for i in range(len(pieces)):
            mark[pieces[i][0]]=i
        i=0
        while i<len(arr):
            index=mark.get(arr[i])
            if index is None:
                return False
            for j in range(len(pieces[index])):
                if i+j>=len(arr):
                    return False
                if arr[i+j]!=pieces[index][j]:
                    return False
            i=i+len(pieces[index])
        return True