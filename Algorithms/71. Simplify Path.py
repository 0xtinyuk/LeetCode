class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path=path.split("/")
        for x in path:
            if len(x)==0 or x==".":
                continue
            if x=="..":
                if len(stack)>0:
                    stack.pop(len(stack)-1)
            else:
                stack.append(x)
        if len(stack)==0:
            return "/"
        ans = ""
        for x in stack:
            ans+="/"+x
        return ans