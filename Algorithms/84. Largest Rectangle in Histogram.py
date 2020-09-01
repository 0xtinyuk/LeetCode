class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        loc = []
        for i in range(len(heights)):
            ans = max(ans, heights[i])
            # if (len(stack) != 0) and stack[len(stack)-1] > heights[i]:
            #mh = stack[len(stack)-1]
            #x = loc[len(stack)-1]
            # for j in range(len(stack)-2, -1, -1):
            #    ans = max(ans, mh*(x-loc[j]))
            #    mh = stack[j]
            #ans = max(ans, mh*(x+1))
            while (len(stack) != 0) and stack[len(stack)-1] > heights[i]:
                mh = stack.pop()
                loc.pop()
                if (len(stack) == 0):
                    x = 0
                else:
                    x = loc[len(stack)-1]+1
                ans = max(ans, (i-x)*mh)
            stack.append(heights[i])
            loc.append(i)
        if (len(stack) != 0):
            mh = stack[len(stack)-1]
            x = loc[len(stack)-1]
            for j in range(len(stack)-2, -1, -1):
                ans = max(ans, mh*(x-loc[j]))
                mh = stack[j]
            ans = max(ans, mh*(x+1))
        return ans
