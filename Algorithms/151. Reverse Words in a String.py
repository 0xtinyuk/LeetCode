class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s)==0:
            return s
        l = 0
        r = len(s)-1
        while s[l]==" ":
            l+=1
        while s[r]==" ":
            r-=1
        s = s[l:r+1]
        l=0
        r = len(s)-1
        while l<r:
            i=l
            j=r
            while i<=r and s[i]!=" ":
                i+=1
            while l<=j and s[j]!=" ":
                j-=1
            if i<=j:
                ll = i-l
                rl = r-j
                if i==j:
                    s = s[:l]+s[j+1:r+1]+" "+s[l:i]+s[r+1:]
                else:
                    s = s[:l]+s[j+1:r+1]+" "+s[i+1:j]+" "+s[l:i]+s[r+1:]
                l=l+rl
                r=r-ll
                i = l
                j = r
                print(s)
                print(l,r,i,j)
                while i<=j and s[i]==" ":
                    i+=1
                while i<=j and s[j]==" ":
                    j-=1
                if i<=j:
                    s = s[:l]+" "+s[i:j+1]+" "+s[r+1:]
                    l=l+1
                    r=l+j-i
                    print(s[l],s[r])
                else:
                    s = s[:l]+" "+s[r+1:]
                    break
            else:
                break
        return s