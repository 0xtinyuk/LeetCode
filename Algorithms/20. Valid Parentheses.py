class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            else:
                if len(stack)<1:
                    return False
                t = stack.pop()
                if abs(ord(c)-ord(t))>2:
                    return False
        if len(stack)>0:
            return False
        return True