class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.memory = {}
        return self.countString(n,0)
        
    def countString(self, n:int, start:int)-> int:
        if n==1:
            return 5-start
        if start == 4:
            return 1
        res = self.memory.get(str(n)+"->"+str(start))
        if res is None:
            res = 0
            for i in range(start,5):
                res += self.countString(n-1,i)
            self.memory[str(n)+"->"+str(start)]=res
        return res