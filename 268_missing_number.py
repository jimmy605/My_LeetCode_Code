class Solution:
    def missingNumber(self, nums) -> int:
        nums.sort()
        
        idx = 0
        for num in nums:
            if num != idx:
                return idx 
            idx += 1
        
        return len(nums)

test = Solution()
print(test.missingNumber([3,0,1]))
print(test.missingNumber([0,1]))
print(test.missingNumber([9,6,4,2,3,5,7,0,1]))