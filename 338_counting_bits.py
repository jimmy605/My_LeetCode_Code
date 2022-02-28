class Solution:
    def countBits(n: int) -> list[int]:
        return [bin(i)[2:].count('1') for i in range(n + 1)]
        
print(Solution.countBits(5))