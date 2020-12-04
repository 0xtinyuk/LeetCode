class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ops = []
        for i,x in enumerate(buildings):
            ops.append([x[0],-x[2],i])
            ops.append([x[1],x[2],i])
        ops = sorted(ops,key=lambda x: (x[0],x[1]))
        h=[]
        heapify(h)
        current = set()
        ans = []
        
        for op in ops:
            if op[1]<0:
                current.add(op[2])
                if len(h)==0 or op[1]<h[0][0]:
                    ans.append([op[0],-op[1]])
                heappush(h,(op[1],op[2]))
            else:
                current.remove(op[2])
                if h[0][1]==op[2]:
                    while h and (h[0][1] not in current):
                        heappop(h)
                if len(h)==0 or h[0][0]!=-ans[-1][1]:
                    if len(h)==0:
                        ans.append([op[0],0])
                    else:
                        ans.append([op[0],-h[0][0]])
        return ans