class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles>=numExchange:
            t = numBottles//numExchange
            numBottles = numBottles%numExchange
            ans += t
            numBottles += t
        return ans