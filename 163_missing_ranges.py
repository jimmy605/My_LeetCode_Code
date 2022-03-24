def findMissingRanges(nums: int, lower: int, upper: int) -> str:
    
    missing = [i for i in range(lower, upper + 1) if i not in nums]
    output = []
    
    # Pointers
    before = 0 
    after = 0
    
    for idx, num in enumerate(missing):
        # i is by itself
        if idx == 0 and num[idx + 1] != 

print(findMissingRanges([0,1,3,50,75], 0, 99))