from typing import Tuple

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = len(s)
        
        if L == 1:
            return 1
        
        if s == '':
            return 0
        
        unique_values = list(set(s))
        
        if len(unique_values) == L:
            return L 
        
        max_chars = 0
        
        for i in range(L):
            characters = unique_values[:]
            count = 0
            
            if max_chars >= len(s) - i:
                break 
            
            for char in s[i:]:
                if char not in characters:
                    break 
                else:
                    characters.remove(char)
                    count += 1
                if count > max_chars:
                        max_chars = count 
        
        return max_chars

test = Solution()
print(test.lengthOfLongestSubstring('pwwkew'))
print(test.lengthOfLongestSubstring('au'))