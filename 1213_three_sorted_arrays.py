class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        output = []
        
        for num in arr1:
            if num in arr2 and num in arr3:
                output.append(num)
        
        return output