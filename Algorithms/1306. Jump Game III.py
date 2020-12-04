from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start]==0:
            return True
        q = deque()
        mark = [False for i in range(len(arr))]
        mark[start] = True
        q.append(start)
        while(len(q)>0):
            current = q.popleft()
            if current-arr[current]>=0 and (not mark[current-arr[current]]):
                mark[current-arr[current]]=True
                q.append(current-arr[current])
                if arr[current-arr[current]] == 0:
                    return True
            if current+arr[current]<len(arr) and (not mark[current+arr[current]]):
                mark[current+arr[current]]=True
                q.append(current+arr[current])
                if arr[current+arr[current]] == 0:
                    return True
        return False