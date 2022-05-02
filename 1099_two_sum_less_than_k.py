class Solution:
    def twoSumLessThanK(self, nums, k):
        if len(nums)== 1:
            if nums[0] > k:
                return -1
            else: nums[0]
        
        nums.sort()
        top_sum = -1
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                temp_sum = sum([nums[i], nums[j]])
                if temp_sum < k and temp_sum > top_sum:
                    top_sum = temp_sum
        
        return top_sum if top_sum < k else -1 


test = Solution()
print(test.twoSumLessThanK([358,898,450,732,672,672,256,542,320,573,423,543,591,280,399,923,920,254,135,952,115,536,143,896,411,722,815,635,353,486,127,146,974,495,229,21,733,918,314,670,671,537,533,716,140,599,758,777,185,549], 1800))