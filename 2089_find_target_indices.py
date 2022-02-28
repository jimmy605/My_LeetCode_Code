def targetIndices(nums: list[int], target: int) -> list[int]:
    indices = []
    
    for idx, num in enumerate(sorted(nums)):
        if target == num:
            indices.append(idx)
        if num > target:
            break
    
    return indices

print(targetIndices([1,2,5,2,3], 2))