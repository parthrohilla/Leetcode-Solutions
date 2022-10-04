class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for base in range(2,n-1):
            if not self.palindrome(n,base):
                return False
        return True
    
    def palindrome(self,num,b):
        string = ""
        while num > 0:
            rem = num % b
            string = str(rem) + string
            num = num // b
        return string == string[::-1]