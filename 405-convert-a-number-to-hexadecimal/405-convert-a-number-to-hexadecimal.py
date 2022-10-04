class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        mapping = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"a",11:"b",12:"c",13:"d",14:"e",15:"f"}
        ans = ""
        num &= 0xFFFFFFFF
        while num:
            rem = num % 16
            ans = mapping[rem] + ans
            num = num // 16
        return ans