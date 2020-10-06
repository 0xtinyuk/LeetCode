class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i=0
        j=0
        tmp_len = len(words[0])
        ans = []
        while j+1<len(words):
            j+=1
            if tmp_len+len(words[j])+1>maxWidth:
                if j-i==1:
                    ans.append(words[i]+(" ")*(maxWidth-tmp_len))
                else:
                    remaining = maxWidth-tmp_len
                    r=remaining%(j-i-1)
                    d=remaining//(j-i-1)
                    tmp=""
                    for k in range(i,j-1):
                        tmp+=words[k]+" "
                        tmp+=" "*d
                        if(k-i+1<=r):
                            tmp+=" "
                    tmp+=words[j-1]
                    ans.append(tmp)
                tmp_len=len(words[j])
                i=j
            else:
                tmp_len+=len(words[j])+1
        tmp = ""
        for k in range(i,j):
            tmp+=words[k]+" "
        tmp+=words[j]
        tmp+=" "*(maxWidth-len(tmp))
        ans.append(tmp)
        return ans
        