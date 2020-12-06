class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        last = -2
        ans = 0
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                ans += ((i-last)//2)-1
                last = i
        ans += (len(flowerbed)+1-last)//2-1
        return ans>=n