class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Longest sub-array with atlmost 2 Type of Fruits
        hashmap = {}
        ans = l = 0
        for r, t in enumerate(fruits):
            hashmap[t] = 1 + hashmap.get(t, 0)
            while len(hashmap.keys()) == 3:
                hashmap[fruits[l]] -= 1
                if hashmap[fruits[l]] == 0:
                    del hashmap[fruits[l]]
                l += 1
            ans = max(ans, r - l + 1)
        return ans