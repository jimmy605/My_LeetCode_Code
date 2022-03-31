class Solution:
    def findDuplicate(self, nums) -> int:
        nums_dict = {}
        
        for num in nums:
            if num in nums_dict:
                return num 
            else:
                nums_dict[num] = 1
        
        nums.sort
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]


test = Solution()
print(test.findDuplicate([3,1,3,4,2]))