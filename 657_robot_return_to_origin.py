class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x_axis = 0
        y_axis = 0
        
        score = {'L': -1, 'R': 1, 'U': 1, 'D': -1}
        
        for move in moves:
            if move in ['L', 'R']:
                x_axis += score[move]
            else:
                y_axis += score[move]
        
        return True if x_axis == 0 and y_axis == 0 else False 

test = Solution()
print(test.judgeCircle('UD'))

print(test.judgeCircle('LL'))