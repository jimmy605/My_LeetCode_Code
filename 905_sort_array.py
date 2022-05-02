class Solution:
    def sortArrayByParity(self, nums):
        odd = []
        even = []
        
        for num in nums:
            if num % 2 != 0:
                odd.append(num)
            else:
                even.append(num)
        even.extend(odd)
        
        return even