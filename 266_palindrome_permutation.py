# aaacbbb (one letter occurs an odd number of times, thus, is a palindrome)
# aaa: one letter occurs an odd number of times, thus, is a palindrome
# aabb: zero letters occur an odd number of times, thus, is a palindrome
# aabbcd: two letters occur an odd number of times, thus, is not a palindrome
from itertools import permutations

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 1: return True 
        
        letters = {}
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        
        count = 0
        for num in letters.values():
            if num % 2 == 1:
                count += 1
        
        if count == 1 or count == 0:
            return True 
        else:
            return False


test = Solution()
print(test.canPermutePalindrome('code'))