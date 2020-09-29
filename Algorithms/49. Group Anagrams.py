class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans={}
        for s in strs:
            count=[0 for i in range(26)]
            for char in s:
                count[ord(char)-97]+=1
            key=""
            for i in range(26):
                key=key+str(count[i])+"!"
            if ans.get(key) is None:
                ans[key]=[s]
            else:
                ans[key].append(s)
        return ans.values()
        