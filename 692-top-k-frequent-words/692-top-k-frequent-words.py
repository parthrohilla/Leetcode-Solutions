class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_map = {}
        for word in words:
            word_map[word] = 1 + word_map.get(word, 0)
            
        bucket = [[] for _ in range(len(words)+1)]
        for key, value in word_map.items():
            bucket[value].append(key)
            
        res = []
        for i in range(len(bucket)-1, -1, -1):
            if len(bucket[i]) != 0:
                bucket[i].sort()
                for word in bucket[i]:
                    if len(res) == k:
                        break
                    else:
                        res.append(word)
                    
        return res
        