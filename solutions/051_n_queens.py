class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        board = [[1 for i in xrange(n)] for i in xrange(n)]
        rs = range(n)
        self.queens = []
        self.directions = [[(-i, i), (i, i)] for i in xrange(1, n)]
        self.recursive(board, n, 0, rs)
        return self.queens

    def recursive(self, wb, n, c, rs):
        for r in rs:
            if wb[r][c] == 1:
                wb, marks = self.mark(wb, n, (r, c))
                if c == n-1:
                    self.queens.append(map(lambda q: ''.join(map(lambda x: 'Q' if x == 0 else '.', q)), wb))
                else:
                    nrs = rs[:]
                    nrs.remove(r)
                    self.recursive(wb, n, c+1, nrs)
                wb = self.unmark(wb, marks)
        


    def mark(self, board, n, (x, y)):
        marks = []
        for (a, b) in [(x, c) for c in range(y, n)]:
            if board[a][b] != -1:
                board[a][b] = -1
                marks.append((a, b))
            
        for d in self.directions[:len(self.directions)-y]:
            for (a, b) in map(lambda s: (x+s[0], y+s[1]), d):
                if a >= 0 and a < n and b >= 0 and b < n and board[a][b] != -1:
                    board[a][b] = -1
                    marks.append((a, b))

        board[x][y] = 0
        return board, marks

    def unmark(self, board, marks):
        for (x, y) in marks:
            board[x][y] = 1
        return board



import time
start_time = time.time()

s = Solution()
print s.solveNQueens(1)
print s.solveNQueens(2)
print s.solveNQueens(3)
print (4, s.solveNQueens(4))
print (5, len(s.solveNQueens(5)))
print (6, len(s.solveNQueens(6)))
print (7, len(s.solveNQueens(7)))
print (8, len(s.solveNQueens(8)))
print (9, len(s.solveNQueens(9)))
print (10, len(s.solveNQueens(10)))
print (11, len(s.solveNQueens(11)))

print("--- %s seconds ---" % (time.time() - start_time))
# s.solveNQueens(4)

# qs = s.solveNQueens(5)
# for q in qs:
#     print "-------------------"
#     for r in q:
#         print r
#     print "-------------------"
