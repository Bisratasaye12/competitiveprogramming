class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        n,m = len(isConnected), len(isConnected[0])
        for i in range(1,n+1):
            for j in range(1, m+1):
                if isConnected[i-1][j-1] == 1 and i!=j:
                    graph[i].append(j)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            if graph[node]:
                for i in graph[node]:
                    visited.add(node)
                    dfs(i)

        visited = set()
        count = 0
        for i in range(1, n+1):
            if i not in visited:
                dfs(i)
                count += 1

        
        return count
