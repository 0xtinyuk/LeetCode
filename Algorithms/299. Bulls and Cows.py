class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dep = [0 for i in range(10)]
        req = [0 for i in range(10)]
        a=0
        b=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                a+=1
            else:
                g=int(guess[i])
                if dep[g]>0:
                    dep[g]-=1
                    b+=1
                else:
                    req[g]+=1
                s=int(secret[i])
                if req[s]>0:
                    req[s]-=1
                    b+=1
                else:
                    dep[s]+=1
        return str(a)+"A"+str(b)+"B"