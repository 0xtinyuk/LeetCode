class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1)<len(num2):
            num1, num2 = num2, num1
        ans = [0 for i in range(len(num1)+len(num2)+1)]
        for i in range(len(num2)-1,-1,-1):
            temp = [0 for j in range(len(num1)+1)]
            cur = 0
            for j in range(len(num1)-1,-1,-1):
                temp[cur]=temp[cur]+(ord(num1[j])-ord('0'))*(ord(num2[i])-ord('0'))
                temp[cur+1]+=temp[cur]//10
                temp[cur]%=10
                cur+=1
            diff=len(num2)-1-i
            for j in range(len(num1)+1):
                ans[diff+j]+=temp[j]
                ans[diff+j+1]+=ans[diff+j]//10
                ans[diff+j]%=10
        while(ans and ans[-1]==0):
            ans.pop()
        if ans:
            res = ""
            ans.reverse()
            for x in ans:
                res=res+chr(ord('0')+x)
            return res
        else:
            return "0"