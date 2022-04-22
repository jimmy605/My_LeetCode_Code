class Solution:
    def decompressRLElist(self, nums):
        output = []
        
        for i in range(0, len(nums), 2):
            # freq, val = nums[i], nums[i+1]
            # output += [val] * freq
            output += [nums[i+1]] * nums[i]
        
        return output 

test = Solution()
print(test.decompressRLElist([1,2,3,4]))
print(test.decompressRLElist([1,1,2,3]))