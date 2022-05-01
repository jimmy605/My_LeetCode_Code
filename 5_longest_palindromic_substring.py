class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        char_count = 0
        
        for i in range(len(s), -1, -1):
            if s[:i] == s[i-1::-1]:
                if len(s[:i]) > char_count:
                    longest = s[:i]
                    char_count = len(s[:i])

        return longest, char_count

test = Solution()
print(test.longestPalindrome("babad"))
print(test.longestPalindrome('cbbd'))