def findMissingRanges(nums: int, lower: int, upper: int) -> str:
    
    def missing_nums(nums, lower, upper):
        """Return a list of the missing numbers"""
        missing = []
        
        for i in range(lower, upper + 1):
            if i not in nums:
                missing.append(i)
        
        return missing 
    
    iter_nums = missing_nums(nums, lower, upper) # Missing numbers
    count = iter_nums[-1] # Last value of missing numbers
    output = []
    
    for num in iter_nums[::-1]:
        

print(findMissingRanges([0,1,3,50,75], 0, 99))