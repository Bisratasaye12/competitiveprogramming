class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        ans = []
        d = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7": "pqrs", "8":"tuv", "9":"wxyz"}
        def backtrack(i, path):
            if i == len(digits):
                ans.append("".join(path))
                return

            for char in d[digits[i]]:
                path.append(char)
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])

        return ans