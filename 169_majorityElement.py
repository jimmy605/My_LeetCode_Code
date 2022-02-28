def majorityElement(nums):
    l = int(len(nums) / 2)
    return sorted(nums)[l]

print(majorityElement([3,2,3]))
print(majorityElement([2,2,1,1,1,2,2]))

############## Retry ###################