class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = ""
        if 2 in A:
            temp = A[:]
            temp.remove(2)
            if (2 in temp) or (3 in temp) or (0 in temp) or (1 in temp):
                ans = "2"
                for i in range(3,-1,-1):
                    if i in temp:
                        temp.remove(i)
                        ans=ans+str(i)+":"
                        break
                if (1 in temp) or (2 in temp) or (0 in temp) or (3 in temp)or (4 in temp)or (5in temp):
                    for i in range(5,-1,-1):
                        if i in temp:
                            temp.remove(i)
                            ans=ans+str(i)
                            break
                    if len(ans)<4:
                        return ""
                    for i in temp:
                        ans=ans+str(i)
                    return ans
                else:
                    ans = ""
    
        for i in range(1,-1,-1):
            if i in A:
                A.remove(i)
                ans=ans+str(i)
                break
        if len(ans)<1:
            return ""
        for i in range(9,-1,-1):
            if i in A:
                A.remove(i)
                ans=ans+str(i)+":"
                break
        if len(ans)<3:
            return ""
        for i in range(5,-1,-1):
            if i in A:
                A.remove(i)
                ans=ans+str(i)
                break
        if len(ans)<4:
            return ""
        for i in A:
            ans=ans+str(i)
        return ans
        