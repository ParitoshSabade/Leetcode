class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def backtrack(i,currstr):
            if len(currstr) == len(digits):
                res.append(currstr)
                return

            for c in phone_map[digits[i]]:
                backtrack(i+1,currstr+c)
        if digits:
            backtrack(0,"")
        return res
        