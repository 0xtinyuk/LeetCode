class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        post = [i+1 for i in range(n)]
        pre = [i-1 for i in range(n)]
        i=-1
        while i+1<n:
            i+=1
            cur=i
            while cur>=0 and asteroids[cur]>0:
                ne = post[cur]
                if ne>=n or asteroids[ne]>=0:
                    break
                if abs(asteroids[cur])==abs(asteroids[ne]):
                    asteroids[cur]=0
                    asteroids[ne]=0
                    tmp1=pre[cur]
                    tmp2=post[ne]
                    if tmp1>=0:
                        post[tmp1]=tmp2
                    if tmp2<n:
                        pre[tmp2]=tmp1
                    cur = tmp1
                    continue
                if abs(asteroids[cur])<abs(asteroids[ne]):
                    asteroids[cur]=asteroids[ne]
                asteroids[ne]=0
                post[cur]=post[ne]
                if post[ne]<n:
                    pre[post[ne]]=cur
                if asteroids[cur]<0:
                    cur=pre[cur]
            i=cur
        ans = []
        for x in asteroids:
            if x!=0:
                ans.append(x)
        return ans