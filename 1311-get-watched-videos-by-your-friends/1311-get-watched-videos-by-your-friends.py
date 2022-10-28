class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(watchedVideos)
        q = deque([id])
        
        freq = {}
        visited = set()
        visited.add(id)
        current_level = 0
        while q:
            k = len(q)
            for _ in range(k):
                node = q.popleft()
                for nei in friends[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            current_level += 1
            if current_level == level:
                break
        
        while q:
            node = q.popleft()
            for vid in watchedVideos[node]:
                freq[vid] = 1 + freq.get(vid, 0)
        
        temp = []
        for v,f in freq.items():
            temp.append([f, v])
        
        temp.sort()
        ans = []
        for _,v in temp:
            ans.append(v)
        
        return ans
        
        
        
                    
                
                
            