class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        q, n, seen = deque(), len(s1), {s1}
        q.append((s1,0))
        
        while q:
            k = len(q)
            for _ in range(k):
                string, d = q.popleft()
                if string == s2: return d
                
                i = 0
                while string[i] == s2[i]: i += 1
                
                for j in range(i+1,n):
                    if string[i]==s2[j]!=s1[j]:
                        new = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
                        if new not in seen:
                            seen.add(new)
                            q.append((new, d+1))
                
                    