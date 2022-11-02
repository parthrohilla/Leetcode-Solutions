class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        
        def similarity(W1, W2):
            return sum([W1[i] != W2[i] for i in range(n)])
        
        res = []
        for W1 in queries:
            for W2 in dictionary:
                if similarity(W1, W2) <= 2:
                    res.append(W1)
                    break
        
        return res