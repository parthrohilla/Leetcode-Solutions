class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_pad = {"2": "abc",
                   "3": "def",
                   "4": "ghi",
                   "5": "jkl",
                   "6": "mno",
                   "7": "pqrs",
                   "8": "tuv",
                   "9": "wxyz"
                   }
        
        def helper(number):
            if len(number) == 0:
                return []
            if len(number) == 1:
                temp = []
                for char in num_pad[number[0]]:
                    temp.append(char)
                return temp
                
                
            small = helper(number[1:])
            output = []
            for char in num_pad[number[0]]:
                for combination in small:
                    output.append(char + combination)
            
            return output
        
        return helper(digits)
        