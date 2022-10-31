# Not an easy question. Discussions is that it's a medium at the minimum 

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total = 0
        ones = 0
        zeros = 0
        
        for element in s:
            if element == '0':
                zeros += 1
            else:
                ones += 1
            

test = Solution()
print(test.countBinarySubstrings("00110011"))