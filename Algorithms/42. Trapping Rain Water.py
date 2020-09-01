class Solution:
    def trap(self, height: List[int]) -> int:

        stack = []
        sx = []
        ans = 0
        for i in range(len(height)):
            if len(stack) == 0 or stack[len(stack)-1] > height[i]:
                stack.append(height[i])
                sx.append(i)
                continue
            if stack[len(stack)-1] == height[i]:
                sx[len(stack)-1] = i
                continue
            lh = 0
            while stack[len(stack)-1] < height[i]:
                h = stack.pop()
                x = sx.pop()
                ans += (h-lh)*(i-x-1)
                lh = h
                if len(stack) == 0:
                    break
            if len(stack) != 0:
                ans += (height[i]-lh)*(i-sx[len(stack)-1]-1)
                if stack[len(stack)-1] == height[i]:
                    sx[len(stack)-1] = i
            stack.append(height[i])
            sx.append(i)
        return ans
