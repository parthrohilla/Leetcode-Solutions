class Solution:
    def secondHighest(self, s: str) -> int:
        largest, second = -1, -1
        for char in s:
            if char.isnumeric() and int(char) > largest: 
                second = largest
                largest = int(char)
            elif char.isnumeric() and int(char) > second and int(char) < largest: 
                second = int(char)
        return second