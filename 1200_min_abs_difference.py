class Solution:
    def minimumAbsDifference(self, arr):
        # Sort the array
        arr.sort() 
        # Variable to hold the lowest absolute value
        lowest_val = None 
        # Iterate through the array and compare values
        for i in range(len(arr) - 1):
            temp_sum = abs(arr[i+1] - arr[i])
            if lowest_val == None:
                lowest_val = temp_sum
            elif temp_sum < lowest_val:
                lowest_val = temp_sum
        
        # Store the number pairs with the lowest absolute values
        output = []
        for i in range(len(arr) - 1):
            temp_sum = abs(arr[i+1] - arr[i])
            if temp_sum == lowest_val:
                output.append([arr[i], arr[i+1]])
        
        return output

test = Solution()
print(test.minimumAbsDifference([4,2,1,3]))
