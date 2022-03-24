def findDisappearedNumbers(nums):
    have_nums = {n: True for n in nums}
    return [i for i in range(1, len(nums) + 1) if i not in have_nums]

print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(findDisappearedNumbers([1,1]))