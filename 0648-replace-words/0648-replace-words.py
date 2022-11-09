class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        S = sentence.split()
        D = sorted(dictionary, key = lambda x: len(x))
        for index, word in enumerate(S):
            for key in D:
                if key == word[:len(key)]:
                    S[index] = key
                    break
        return " ".join(S)