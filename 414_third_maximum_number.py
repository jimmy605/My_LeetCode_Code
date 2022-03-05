def thirdMax(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    nums.sort(reverse=True)
    
    # max variables
    max3 = 0
    max2 = 0
    max1 = nums[0]
    
    for num in nums[1:]:
        