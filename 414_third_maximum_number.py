def thirdMax(nums):
    # If len() == 1: return the max_number
    # Iterate through it for O(n) and do conditional statements?
    unique_nums = list(set(nums))
    unique_nums.sort()
    
    if len(unique_nums) < 3:
        return unique_nums[-1]
    
    return unique_nums[-3]

print(thirdMax([3,2,1]))