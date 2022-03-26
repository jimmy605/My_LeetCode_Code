class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(f'{nums[i]} : {nums[j]}')
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False

test = Solution()
print(test.containsNearbyDuplicate([1,2,3,1,2,3], 2))