class Solution:
    def shiftGrid(self, grid, k):
        one_lyst = []
        m = len(grid)
        n = len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                one_lyst.append(grid[i][j])
        
        start = (m * n) - k
        end = 0
        sorted_k = one_lyst[start:] + one_lyst[end:start]
        
        output = []
        
        start = 0
        end = n 
        for i in range(m):
            output.append(sorted_k[start:end])
            start += n 
            end += n 
        
        return output

test = Solution()
print(test.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 1))
print(test.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4))
print(test.shiftGrid([[1,2,3],[4,5,6],[7,8,9]], 9))