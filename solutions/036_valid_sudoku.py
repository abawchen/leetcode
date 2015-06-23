# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

# A partially filled sudoku which is valid.

# Note:
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        # map 1 - 9 to the first 9 primes(won't use 1)
        PRIMES = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]

        rows, cols, squares = map(lambda n: [1]*n, [9]*3)

        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == '.':
                    continue

                p = PRIMES[int(board[i][j])]
                if rows[i] % p == 0 or cols[j] % p == 0 or squares[i-i%3 + j/3] % p == 0:
                    return False

                rows[i], cols[j], squares[i-i%3 + j/3] = map(lambda x: x * p, [rows[i], cols[j], squares[i-i%3 + j/3]])

        return True

        