class Solution:
    def findMissingRanges(self, nums: int, lower: int, upper: int) -> str:
        # Store output list of lists
        missing = []
        
        # We know what lower and upper are so iterate through lower:upper+1 and check if i is in nums. If not add to missing.
        for i in range(lower, upper + 1):
            if i not in nums:
                missing.append(i)
        
        # Iterate through missing
        for idx, i in missing:
            # Need to check if one consecutive digit or multiple
            
                # Recursive function? 
                    # Base case returns i if i + 1 != next i iteration?