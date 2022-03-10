class Solution:
    def arrangeCoins(self, n: int) -> int:
        # if count > n:
        #     return 0
        # else:
        #     return 1 + self.arrangeCoins(n - count, count + 1)
        
        count = 0
        
        while count < n:
            count += 1
            n -= count
        
        return count

test = Solution()
# print(test.arrangeCoins(5))
print(test.arrangeCoins(5))