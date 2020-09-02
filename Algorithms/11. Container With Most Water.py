class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        ans = 0
        while (l<r):
            width=r-l
            if height[l]<height[r]:
                s=width*height[l]
                if s>ans:
                    ans=s
                l+=1
            else:
                s=width*height[r]
                if s>ans:
                    ans=s
                r-=1
        return ans
        