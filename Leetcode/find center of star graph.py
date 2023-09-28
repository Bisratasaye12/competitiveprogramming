class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        for i in graph:
            if len(graph[i]) == len(graph) - 1:
                return i
 
