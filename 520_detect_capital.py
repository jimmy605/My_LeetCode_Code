class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()

test = Solution()
print(test.detectCapitalUse("USA"))
