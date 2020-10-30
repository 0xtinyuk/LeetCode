class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        occupied = []
        for i in range(n):
            if seats[i]==1:
                occupied.append(i)
        ans = max(occupied[0],1)
        for i in range(1,len(occupied)):
            ans=max(ans,(occupied[i]-occupied[i-1])//2)
        if seats[n-1]==0:
            ans=max(ans,(n-1-occupied[len(occupied)-1]))
        return ans