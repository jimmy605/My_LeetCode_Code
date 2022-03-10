class Solution:
    def toHex(self, num: int) -> str:
        return hex(num)


test = Solution()
print(test.toHex(26))
print(test.toHex(-1))