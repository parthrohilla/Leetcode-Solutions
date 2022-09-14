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
        adj = {}
        def dfs(i):
            imp = adj[i][0]
            for sub in adj[i][1]:
                imp += dfs(sub)
            return imp

        for emp in employees:
            adj[emp.id] = [emp.importance,emp.subordinates]
        
        return dfs(id) 