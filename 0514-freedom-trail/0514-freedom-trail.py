class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n, Q, visited = len(ring), deque(), set()
        Q.append([0,0,0]) #[node, rotations, current_index]
        
        while Q:
            i, rotations, current = Q.popleft()
            # If we have seen the current state already previously, we just avoid reworking on it.
            if (i, current) in visited:
                continue
            
            visited.add((i,current))
            # IF the current alligned character is equal to key we increment current index until duplicate adjacent characters are there
            # Think of any key where adjacent characters are equal like "aaaaabbbcde", so if we are already alligned at "a", we don't need to rotate 
            while current < len(key) and key[current] == ring[i]:
                current += 1
            # BREAK - CONDITION
            # The the key is always present i.e an answer always exists
            # if we have found all the characters of key and the current index becomes equal to length of key
            if current == len(key):
                # We also need to "press the centre" after the character is alligned, so there would always be clicks equal to length of key 
                clicks = len(key)
                return rotations + clicks
            # Appending next adjacent rotations based on index i.e. if index is 0 then the next level in BFS would be index 1 and last-index
            # for last index the next level in BFS would be previous index and the 0th index
            # else if the current index is somewhere in between we would check the left and right index
            if i == 0:
                Q.append([i+1, rotations + 1, current])
                Q.append([n-1, rotations + 1, current])
            elif i == n-1:
                Q.append([i-1, rotations + 1, current])
                Q.append([0, rotations + 1, current])
            else:
                Q.append([i+1, rotations + 1, current])
                Q.append([i-1, rotations + 1, current])
                
                