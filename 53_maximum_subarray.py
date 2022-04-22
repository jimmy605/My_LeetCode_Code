class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        max_subarray = None 
        sub_total = nums[0]
        
        for left in range(len(nums)):
            right = len(nums)
            for i in range(len(nums), left, -1):
                # test_total = sum(nums[left:right])
                # if test_total > sub_total:
                #     sub_total = test_total
                #     max_subarray = nums[left:right]
                test_subarray = nums[left:right]
                total = sum(test_subarray)
                if total > sub_total:
                    sub_total = total 
                    max_subarray = test_subarray
                total -= test_subarray.pop()
                right -= 1
        
        return sub_total, max_subarray

# Need to sum the initial subarray then pop a number off the end of the list, return that value to take off the previous total for the list. Will save sum() iterating through the list everytime. 

test = Solution()
print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # [4,-1,2,1]
print(test.maxSubArray([1])) # 1
print(test.maxSubArray([-2,-1]))