"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = defaultdict(list)
        for employee in employees:
            _id, imp, sub = employee.id, employee.importance, employee.subordinates
            graph[_id].append(imp)
            graph[_id] += sub
        
        queue = deque([id])
        _sum = 0
        while queue:
            node = queue.popleft()
            _sum += graph[node][0]

            for n in graph[node][1:]:
                queue.append(n)



        return _sum
