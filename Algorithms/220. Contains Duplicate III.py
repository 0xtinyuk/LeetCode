class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if (t<0)or(k<=0):
            return False
        map = {}
        for i,v in enumerate(nums):
            x = v//(t+1)
            if x in map:
                return True
            if ((x-1) in map)and(abs(map[x-1]-v)<=t):
                return True
            if ((x+1) in map)and(abs(map[x+1]-v)<=t):
                return True
            map[x]=nums[i]
            if i-k>=0:
                map.pop(nums[i-k]//(t+1))
        return False
        

            