class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length=len(words[0])
        dict={}
        ind=0
        for word in words:
            if word in dict:
                (index,times)=dict[word]
                dict[word]=(index,times+1)
            else:
                dict[word]=(ind,1)
                ind+=1
        f=[-1 for i in range(len(s))]
        for i in range(len(s)-word_length+1):
            temp=s[i:i+word_length]
            if temp in dict:
                f[i]=dict[temp][0]
        total_length=word_length*len(words)
        ans = []
        for i in range(len(s)-total_length+1):
            if f[i]!=-1:
                mark=[0 for t in range(len(dict))]
                for (index,t) in dict.values():
                    mark[index]=t
                mark[f[i]]-=1
                not_found=False
                for j in range(i+word_length,i+total_length,word_length):
                    if f[j]==-1:
                        not_found=True
                        break
                    else:
                        mark[f[j]]-=1
                if not_found:
                    continue
                for t in range(len(dict)):
                    if mark[t]!=0:
                        not_found=True
                        break
                if not not_found:
                    ans.append(i)
        return ans