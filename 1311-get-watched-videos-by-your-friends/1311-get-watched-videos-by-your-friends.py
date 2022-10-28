class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n, q = len(watchedVideos), deque([id])
        freq, visited = {}, set([id])
        current_level = 0
        
        # BFS for reaching the "level" of required friends
        while q and current_level < level:
            k = len(q)
            for _ in range(k):
                node = q.popleft()
                for nei in friends[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            current_level += 1
        
        # Maintaining a map of videos watched by kth level friends and keeping their count
        while q:
            node = q.popleft()
            for vid in watchedVideos[node]:
                freq[vid] = 1 + freq.get(vid, 0)
        
        return sorted(freq.keys(), key = lambda x : (freq[x],x))
    
        
        
        
                    
                
                
            