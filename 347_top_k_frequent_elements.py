from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        k_list = []
        nums_data = Counter(nums)
        
        ele_nums = sorted(nums_data.values(), reverse=True)[:k]
        print(nums_data)
        print(ele_nums)
        
        for ele, count in nums_data.items():
            if count in ele_nums:
                k_list.append(ele)
        
        return k_list

test = Solution()
print(test.topKFrequent([1,1,1,2,2,3], 2))