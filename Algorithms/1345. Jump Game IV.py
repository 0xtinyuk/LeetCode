class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n==1:
            return 0
        if n==2:
            return 1
        dict = {}
        for i in range(n):
            if arr[i] in dict:
                dict[arr[i]].append(i)
            else:
                dict[arr[i]] = [i]
        mark = {0}
        q = [(0,0)]
        l = 0
        while l<len(q):
            if arr[q[l][0]] in dict:
                for v in dict[arr[q[l][0]]]:
                    if not (v in mark):
                        mark.add(v)
                        if v==n-1:
                            return q[l][1]+1
                        q.append((v,q[l][1]+1))
                dict[arr[q[l][0]]].clear()
            for v in range(q[l][0]-1,q[l][0]+2,2):
                if v>=0 and v<n and (not (v in mark)):
                    mark.add(v)
                    if v==n-1:
                        return q[l][1]+1
                    q.append((v,q[l][1]+1))
            l+=1
        return -1