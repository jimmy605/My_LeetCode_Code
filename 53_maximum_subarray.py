import math 
class Solution:
    def maxSubArray(self, nums):
        max_subarray = -math.inf
        
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        
        return max_subarray

test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # [4,-1,2,1]
print(test.maxSubArray([1])) # 1
print(test.maxSubArray([-2,-1]))