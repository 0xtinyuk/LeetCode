class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        seen = set()
        ans = 1
        temp = 1
        while(temp<K):
            temp=temp*10+1
            ans+=1
        if temp==K:
            return ans
        r=temp%K
        while (not(r in seen)):
            seen.add(r)
            r=(r*10+1)%K
            ans +=1
            if r==0:
                return ans
        return -1