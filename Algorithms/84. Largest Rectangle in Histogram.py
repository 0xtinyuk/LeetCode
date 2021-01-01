class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(-1,0)]
        ans = 0
        for i in range(len(heights)):
            if len(stack)==1 or stack[-1][1]<=heights[i]:
                stack.append((i,heights[i]))
            else:
                while len(stack)>1 and stack[-1][1]>heights[i]:
                    ans = max(ans,(i-stack[-2][0]-1)*stack[-1][1])
                    stack.pop()
                stack.append((i,heights[i]))
        while len(stack)>1:
            ans = max(ans,(len(heights)-stack[-2][0]-1)*stack[-1][1])
            stack.pop()
        return ans