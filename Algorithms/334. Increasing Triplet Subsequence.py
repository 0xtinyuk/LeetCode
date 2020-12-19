class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        t=[(1<<31),(1<<31)]
        for x in nums:
            if x<t[0]:
                t[0]=x
            if x>t[0] and x<t[1]:
                t[1]=x
            if x>t[1]:
                return True
        return False