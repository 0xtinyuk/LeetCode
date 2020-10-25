class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens = sorted(tokens)
        ans = 0
        score = 0
        l = 0
        r = len(tokens)-1
        while l<=r:
            while l<=r and P>=tokens[l]:
                score+=1
                P-=tokens[l]
                l+=1
            if score>ans:
                ans=score
            if l>=r:
                break
            while l<r and P<tokens[l] and score>0:
                P+=tokens[r]
                score-=1
                r-=1
            if score==0 and P<tokens[l]:
                break
        return ans