class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0] 
        
        data = []
        
        for i in range(len(nums)):
            if nums[i] > -1:
                data.append(1)
            else:
                data.append(0)
        
        return data

test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # [0, 1, 0, 1, 0, 1, 1, 0, 1]