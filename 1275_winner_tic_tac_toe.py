class Solution:
    def tictactoe(self, moves):
        # Player A moves
        A = [moves[i] for i in range(len(moves)) if i % 2 == 0]
        
        # Player B moves
        B = [moves[i] for i in range(len(moves)) if i % 2 == 1]
        
    
    def check_win(self, player_moves):
        winning_plays = {
            0: [[0,0], [0,1],[0,2]],
            1: [[1,0], [1,1],[1,2]],
            3: [[2,0], [2,1],[2,2]],
            4: [[0,0], [1,0],[2,0]],
            5: [[0,1], [1,1],[2,1]],
            6: [[0,2], [1,2],[2,2]],
            7: [[0,0], [1,1],[2,2]],
            8: [[0,2], [1,1],[2,0]],
        }
        
        for i, moves in winning_plays.items():
            if moves == player_moves:
                

test = Solution()
test.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]])