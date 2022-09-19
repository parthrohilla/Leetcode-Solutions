class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = []
        for word in title.split():
            temp = ""
            for char in word:
                if not temp and len(word) > 2: temp += char.upper()
                else: temp += char.lower()
            ans.append(temp)
        return " ".join(ans)
            