class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap=[]
        heapq.heapify(heap)
        for i in range(1,len(heights)):
            if heights[i]<=heights[i-1]:
                continue
            tmp = heights[i]-heights[i-1]
            if len(heap)>0 and bricks<tmp and heap[0]<tmp and ladders>0:
                ladders-=1
                continue
            while bricks<tmp and len(heap)>0 and ladders>0:
                bricks+=(-heapq.heappop(heap))
                ladders-=1
            if bricks<tmp and ladders>0:
                ladders-=1
                continue
            if bricks>=tmp:
                bricks-=tmp
                heapq.heappush(heap,-tmp)
            else:
                return i-1
        return len(heights)-1