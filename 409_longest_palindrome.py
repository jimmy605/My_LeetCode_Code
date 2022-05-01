class Solution:
    def longestPalindrome(self, s: str) -> int:
        L = len(s)
        # If s in == 1: return 1
        if L == 1:
            return 1
        
        # If d is all the same chars: return len(s)
        if s.count(s[0]) == L:
            return L
        
        # Store the data for s
        s_dict = {}
        # Iterate through the s and store the letters in a dict
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        output_total = 0
        
        # Iterate through the s_dict:
        for char, count in s_dict.items():
            if count >= 2:
                output_total += (count // 2) * 2
                # print(char, count, output_total)
                s_dict[char] -= (count // 2) * 2
        
        # print(s_dict)
        if 1 in s_dict.values():
            return output_total + 1
        return output_total

test = Solution()
print(test.longestPalindrome('a'))
print(test.longestPalindrome('bb'))
print(test.longestPalindrome('abccccdd'))
print(test.longestPalindrome("zeusnilemacaronimaisanitratetartinasiaminoracamelinsuez"))

# {'z': 2, 'e': 5, 'u': 2, 's': 4, 'n': 6, 'i': 8, 'l': 2, 'm': 4, 'a': 10, 'c': 2, 'r': 4, 'o': 2, 't': 4}