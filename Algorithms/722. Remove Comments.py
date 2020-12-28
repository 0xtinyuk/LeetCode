class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        in_comment = False
        before_comment = ""
        l=0
        cl = source[0]
        while l<len(source):
            if in_comment:
                for i in range(len(cl)):
                    if cl[i]=='*' and i+1<len(cl) and cl[i+1]=='/':
                        cl = before_comment + cl[i+2:]
                        in_comment = False
                        print(cl)
                        break
                if in_comment:
                    l+=1
                    if l>=len(source):
                        break
                    cl=source[l]
            else:
                breaked = False
                for i in range(len(cl)):
                    if cl[i]=='/' and i+1<len(cl):
                        if cl[i+1]=='/':
                            if len(cl[:i])>0:
                                ans.append(cl[:i])
                            breaked = True
                            break
                        elif cl[i+1]=='*':
                            in_comment = True
                            before_comment = cl[:i]
                            cl = cl[i+2:]
                            breaked = True
                            break
                if not breaked:
                    if len(cl)>0:
                        ans.append(cl)
                if not in_comment:
                    l+=1
                    if l>=len(source):
                        break
                    cl = source[l]
        return ans  
        