import math 

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = {l + 1:v for l, v in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
        
        output = ''
        
        while columnNumber > 0:
            letter = columnNumber // 26
            output += alphabet[letter]
            
            columnNumber -= 26 * letter
        
        return output

test = Solution()
print(test.convertToTitle(1))
print(test.convertToTitle(28))
print(test.convertToTitle(701))