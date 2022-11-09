class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        S = sentence.split()
        
        dictionary.sort(key = lambda x: len(x))
        print(dictionary)
        for index, word in enumerate(S):
            for d in dictionary:
                if d == word[:len(d)]:
                    S[index] = d
                    break
        return " ".join(S)