# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
# Runtime: 33 ms, faster than 95.03% of Python3 online submissions for Find Winner on a Tic Tac Toe Game.
# Memory Usage: 13.8 MB, less than 86.42% of Python3 online submissions for Find Winner on a Tic Tac Toe Game.

# 40 minutes

# Let n be the size of the board and m be the length of input moves.
# Time Complexity: O(m)
# Space Complexity: O(n)

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        last_move = moves[-1]
        last_player = "A" if len(moves) % 2 == 1 else "B"
        row = [0, 0, 0]
        col = [0, 0, 0]
        dag = [0, 0]
        
        # Go through all the moves of the last player
        i = len(moves) - 1
        while i >= 0:
            pos = moves[i]
            
            # We always make progess towards a row and col win
            row[pos[0]] += 1
            col[pos[1]] += 1
            
            # We make progress towards first diagonal when have top left and bottom right spaces (or middle)
            if(pos[0] == pos[1]):
                dag[0] += 1
            # We make progress towards second diagonal when have top right and bottom left spaces (or middle)
            if(pos[0] + pos[1] == 2):
                dag[1] += 1
            
            i -= 2
        
        # If we have 3 in-a-row in any catagory, we win
        if(max(row) == 3 or max(col) == 3 or max(dag) == 3):
            return last_player
        
        # If we haven't won and filled up the board it's a draw
        if(len(moves) == 9):
            return "Draw"
        # If we get here, the game must still be in progress
        else:
            return "Pending"
          
