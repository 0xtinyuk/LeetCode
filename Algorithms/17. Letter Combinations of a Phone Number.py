class Solution:
    dict = {"2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g","h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]}
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        if len(digits)==1:
            return Solution.dict[digits[0]]
        c = digits[0]
        ans = []
        left= self.letterCombinations(digits[1:])
        for i in Solution.dict[c]:
            for j in left:
                ans.append(i+j)
        return ans