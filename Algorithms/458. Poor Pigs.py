class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        r = minutesToTest//minutesToDie
        ans = math.log(buckets,r+1)
        if pow(r+1,int(ans))==buckets:
            ans = int(ans)
        else:
            ans = int(ans)+1
        return ans