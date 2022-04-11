# class KthLargest:

#     def __init__(self, k, nums):
#         self.k = k
#         self.nums = nums 

#     def add(self, val):
#         self.nums += val
        
#         if len(self.nums) >= 3:
#             self.nums = sorted(self.nums,reverse=True)[:3]
#             return self.nums[2]
        
#         else:
#             self.nums = sorted(self.nums,reverse=True)
#             return self.nums[len(self.nums) - 1]

class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums 

    def add(self, val):
        self.nums += val
        
        if self.nums == []:
            return []
        
        elif len(self.nums) >= 3:
            return sorted(self.nums,reverse=True)[2]
        
        else:
            self.nums = sorted(self.nums,reverse=True)
            return self.nums[len(self.nums) - 1]


# test =KthLargest(3, [4,5,8,2])
# print(test.add([3]))
# print(test.add([5]))
# print(test.add([10]))
# print(test.add([9]))
# print(test.add([4]))
print()
test1 = KthLargest(1, [])
print(test1.add([-3]))
print(test1.add([-2]))
print(test1.add([-4]))
print(test1.add([0]))
print(test1.add([4]))