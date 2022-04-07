class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # If nums2 == 0 return nums1
        if len(nums2) == 0:
            return nums1 
        
        # Iterate through len(nums2)
        for i in range(len(nums2)):
            # Pop the number in off in nums2
            n2 = nums2.pop(i)
            # Iterate through len(nums1) till nums2 number is >= to nums1 number
            for j in range(len(nums1)):
                if n2 >= num1[j]:
                    