class TwoSum:

    def __init__(self):
        self.nums = []
        self.is_sorted = False 

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.is_sorted = False 

    def find(self, value: int) -> bool:
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True 
        
        low, high = 0, len(self.nums) - 1
        while low < high:
            curr_sum = self.nums[low] + self.nums[high]
            if curr_sum < value:
                low += 1
            elif curr_sum > value:
                high -= 1
            else:
                return True 
        
        return False


test = TwoSum()
test.add(0)
test.add(-1)
test.add(1)
# print(test.find(0))
# ["TwoSum","add","add","add","find"]
# [[],[0],[-1],[1],[0]] True

test2 = TwoSum()
test2.add(1)
test2.add(-1)
print(test2.find(0))