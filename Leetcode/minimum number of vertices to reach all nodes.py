class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return []
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)

        res = []
        visited = set()
        c = 0
        while c < n:
            for i in graph[c]:
                if i not in visited:
                    visited.add(i)

            c += 1

        for i in range(n):
            if i not in visited:
                res.append(i)


        return res
