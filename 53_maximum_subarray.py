class Solution:
    def maxSubArray(self, nums):
        curr_subarray = max_subarray = nums[0]
        
        for i in range(1, len(nums)):
            curr_subarray

test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # [0, 1, 0, 1, 0, 1, 1, 0, 1]