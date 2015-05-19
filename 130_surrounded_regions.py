class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):

        dic = {}
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        stack = [board[0][0]]

        
        rows = len(board)
        columns = len(board[0])
        for i in xrange(rows):
            for j in xrange(columns):
                if not dic.has_key((i, j)):
                    if board[i][j] == 'O':
                        result = self._dfs(board, dic, (i, j))
                    # if board[i][j] == 'X':
                    #     dic[(i, j)] = True
                    # else:
                    #     if i in [0, rows-1] or j in [0, columns-1]:
                    #         dic[(i, j)] = False
                    #     else:
                    #         dic[(i, j)] = self._dfs(board, (i, j))

    def _dfs(self, board, dic, (i, j)):
        if i in [0, rows-1] or j in [0, columns-1]:
            dic[(i, j)] = False
            return False
        else:


        # while stack:
        #     node = stack.pop()
