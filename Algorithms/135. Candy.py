class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        e_in = [[] for i in range(n)]
        e_out = [[] for i in range(n)]
        for i in range(n):
            if i-1 >= 0 and ratings[i] > ratings[i-1]:
                e_in[i].append(i-1)
                e_out[i-1].append(i)
            if i+1 < n and ratings[i] > ratings[i+1]:
                e_in[i].append(i+1)
                e_out[i+1].append(i)
        candies=[-1 for i in range(n)]
        visited=set()
        cur=set()
        for i in range(n):
            if len(e_in[i])==0:
                candies[i]=1
                cur.add(i)
        while len(visited)<n:
            ne = set()
            for u in cur:
                visited.add(u)
                for v in e_out[u]:
                    e_in[v].remove(u)
                    candies[v]=max(candies[v],candies[u]+1)
                    if len(e_in[v])==0:
                        ne.add(v)
            cur = ne
        return sum(candies)
        
