class Solution:
    def isHappy(self, n: int) -> bool:
        # Keep track of repeat values. If they occur twice return False
        repeat_values = {}
        
        # Create a while loop that keeps iterating if n > 1
        while n > 1:
        # Convert the number into a string, split the number up into len(n)
            total = 0
            for digit in str(n):
                total += int(digit) ** 2
            
            if total in repeat_values:
                return False 
            else:
                n = total
                repeat_values[n] = 1
            print(n)
        
        # Once it breaks if == 1 return True else False
        return True if n == 1 else False 

test = Solution()
print(test.isHappy(19))
print(test.isHappy(2))