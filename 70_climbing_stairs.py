class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        a, b, i = 1, 2, 3
        total_steps = 0
        
        while i <= n:
            total_steps = a + b
            a, b = b, total_steps
            i += 1
        
        return total_steps