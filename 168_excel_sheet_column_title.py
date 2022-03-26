import math 

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = {l:v for l, v in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
        output = ''
        
        while columnNumber > 0:
            columnNumber -= 1
            
            columnNumber, i = divmod(columnNumber, 26)
            output += alphabet[i]
        
        return output[::-1]

test = Solution()
print(test.convertToTitle(1))
print(test.convertToTitle(28))
print(test.convertToTitle(701))
print(test.convertToTitle(2147483647))