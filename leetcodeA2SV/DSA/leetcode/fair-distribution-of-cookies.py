class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        mn = [float('inf')]


        def backtrack(cookie, dist):
            if cookie >= len(cookies):
                mn[0] = min(max(dist), mn[0])
                return 

            for child in range(k):
                if dist[child] + cookies[cookie] < mn[0]:
                    dist[child] += cookies[cookie]
                    backtrack(cookie + 1, dist)
                    dist[child] -= cookies[cookie]

        backtrack(0, [0]*k)

        return mn[0]

            