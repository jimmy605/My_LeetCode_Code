def singleNumber(nums: list[int]) -> int:
    for i in nums:
        if nums.count(i) == 1:
            return i 

print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
print(singleNumber([1]))