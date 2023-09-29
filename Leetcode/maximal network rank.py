class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)

        lst = list(range(n))
        comb = list(combinations(lst,2))
        res = []
        for i,j in comb:
            if j in graph[i]:
                res.append(len(graph[i]) + len(graph[j]) - 1)
            else:
                res.append(len(graph[i]) + len(graph[j]))

        
        return max(res)
