class Solution:
    def lastStoneWeight(self, stones):
        # Check that stones is > 1 else return the value of stone
        if len(stones) < 2:
            return stones[0]
        
        num_stones = len(stones)
        
        while num_stones > 1:
            # find the 2 heaviest stones
            y, x = sorted(stones, reverse=True)[:2]
            
            # if both stones == each other pop both
            if x == y:
                ind_x = stones.index(x)
                stones.pop(ind_x)
                ind_y = stones.index(y)
                stones.pop(ind_y)
                
            # if stones don't == each other destory x and y - x
            elif x != y:
                ind_x = stones.index(x)
                pop_x = stones.pop(ind_x)
                ind_y = stones.index(y)
                stones[ind_y] = y - pop_x
            
            num_stones = len(stones)
        
        return 0 if stones == [] else stones[0]

test = Solution()
print(test.lastStoneWeight([2,7,4,1,8,1]))