class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        memory = [False for i in range(26)]
        letters = 0
        for i in range(len(s)):
            x = ord(s[i])-ord('a')
            if not memory[x]:
                memory[x] = True
                letters += 1
        ans = 0
        for i in range(1,letters+1):
            memory = [0 for i in range(26)]
            current = 0
            currentValid = 0
            l = r = 0
            while (r<len(s)):
                if current <= i:
                    x = ord(s[r])-ord('a')
                    if memory[x]==0:
                        current +=1
                    memory[x]+=1
                    if memory[x]==k:
                        currentValid +=1
                    r+=1
                else:
                    x = ord(s[l])-ord('a')
                    if memory[x]==k:
                        currentValid-=1
                    memory[x]-=1
                    if memory[x]==0:
                        current-=1
                    l+=1
                if current==currentValid:
                    ans = max(ans,r-l)
        return ans