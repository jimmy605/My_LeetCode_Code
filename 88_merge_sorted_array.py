# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         # If nums2 == 0 return nums1
#         if len(nums2) == 0:
#             return nums1 
        
#         # Iterate through len(nums2)
#         for i in range(len(nums2)):
#             # Pop the number in off in nums2
#             n2 = nums2.pop(i)
#             # Iterate through len(nums1) till nums2 number is >= to nums1 number
#             for j in range(len(nums1)):
#                 if n2 >= num1[j]:




class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # If both num1 and num2 is empty
        if m == 0 and n == 0:
            return nums1 
        
        # If num1 is empty and num2 isn't 
        if m == 0 and n != 0:
            for i in range(len[n]):
                nums1.append(nums2.pop())
        
        # If num1 isn't empty and nums 2 is
        if m != 0 and n == 0:
            return nums1 
        
        # If nums1 and num2 have numbers in them
        nums1 = nums1[:-n]
        for i in range(len(nums2)):
            nums1.append(nums2.pop(0))
        
        nums1.sort(reverse=False)
        
        return nums1

test = Solution()
print(test.merge([1,2,3,0,0,0], 3, [2,5,6], 3))