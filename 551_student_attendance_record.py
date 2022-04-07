class Solution:
    def checkRecord(self, s: str) -> bool:
        # a = 0
        # l = 0
        
        # for attendance in s:
        #     # Check if A
        #     if attendance == 'A':
        #         a += 1
        #         l = 0
        #         if a == 2:
        #             return False
            
        #     if attendance == 'P':
        #         l = 0
            
        #     # Check L three times in a row
        #     if attendance == 'L':
        #         l += 1
        #         if l == 3:
        #             return False 
        
        # return True

        if "LLL" in s or s.count('A') > 1:
            return False
        
        return True


test = Solution()
print(test.checkRecord('PPALLP'))
print(test.checkRecord('PPALLL'))
print(test.checkRecord('AAAA'))
print(test.checkRecord('AA'))