class Solution:
    
    def searchMatrix(self, matrix, target: int) -> bool:
        # binary Search
        def binary_serach(lyst, search):
            left = 0
            right = len(lyst) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                num = lyst[mid]
                if num == search:
                    return True 
                elif num > search:
                    right = mid - 1
                else: 
                    left = mid + 1
            
            return False 
        
        # If lists only have 1 list in it and less than 3 ints
        if len(matrix) == 1:
            if len(matrix[0]) < 3:
                return target in matrix[0]
            else:
                return binary_serach(matrix[0], target)
        
        # If lists has more than 1 list and more than 1 int
        if len(matrix) > 1 and len(matrix[0]) < 3:
            for row in matrix:
                if target in row:
                    return True
            return False 
        
        # Iterate through the list of lists 0's indexes
        first_index = 0
        for i in range(len(matrix)):
            # If range less then 1 from the end
            if i + 1 < len(matrix):
                # If target > row[0][0] and < row[1][0]
                if target >= matrix[i][first_index] and target < matrix[i + 1][first_index]:
                    # target can only be in row[0] and use binary search - return True or False
                    return binary_serach(matrix[i], target)
            # Else it's in the last row and use binary search
            else:
                return binary_serach(matrix[-1], target)


test = Solution()
print(test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(test.searchMatrix([[1]], 2))
print(test.searchMatrix([[1,1]], 2))
print(test.searchMatrix([[1],[3]], 2))
print(test.searchMatrix([[1],[3]], 3))
print(test.searchMatrix([[1,3,5]], 6))