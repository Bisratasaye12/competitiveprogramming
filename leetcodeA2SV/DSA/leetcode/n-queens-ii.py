class Solution:
    def totalNQueens(self, n: int) -> int:
        

        cols = set()
        posDiag = set()
        negDiag = set()
        ans = set()

        def backtrack(r, candidate):
            if r == n:
                ans.add(tuple(candidate))
                return

            for c in range(n):
                if c in cols or r+c in posDiag or r-c in negDiag:
                    continue

                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                candidate.append((r,c))

                backtrack(r+1, candidate)

                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                candidate.pop()


        backtrack(0, [])
        return len(ans)

