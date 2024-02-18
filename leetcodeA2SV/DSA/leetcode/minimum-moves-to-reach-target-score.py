class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        nt = target
        ans = 0

        while maxDoubles and nt != 1:
            if nt != 1 and nt % 2:
                ans += 1
                
            nt //= 2
            ans += 1

            
            
            maxDoubles -= 1

        print(ans)
        return ans + nt - 1 if nt != 1 else ans

        