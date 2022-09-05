class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(i):
            if i in visited:
                return False
            
            visited.add(i)
            if len(visited) == len(rooms):
                return True
            for nei in rooms[i]:
                if dfs(nei):
                    return True
            return False
        
        return dfs(0)