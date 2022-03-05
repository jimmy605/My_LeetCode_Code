def searchInsert(nums: list, target: int) -> int:
    for idx, num in enumerate(nums):
        if target == num:
            return idx
        elif num > target:
            return idx 
        elif idx == len(nums) - 1:
            return idx + 1

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))