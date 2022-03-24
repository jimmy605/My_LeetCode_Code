# aaacbbb (one letter occurs an odd number of times, thus, is a palindrome)
# aaa: one letter occurs an odd number of times, thus, is a palindrome
# aabb: zero letters occur an odd number of times, thus, is a palindrome
# aabbcd: two letters occur an odd number of times, thus, is not a palindrome


from itertools import permutations

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) == 1: return True 
        
        # Permutations of the given string
        perms = permutations(s)
        
        def is_palindrome(w):
            """Checks if word is a palindrome. Returns a boolean"""
            L = len(w)
            left = 0
            right = L - 1
            
            for i in range(L // 2):
                if w[left] != w[right]:
                    return False 
                left += 1
                right -= 1
            
            return True 
        
        for perm in perms:
            if is_palindrome(perm):
                return True 