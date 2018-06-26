solution = __import__('solutions.279', fromlist='*')

from math import pow

def test_solution():
    s = solution.Solution()
    assert s.numSquares(202) == 2
    assert s.numSquares(203) == 3
    assert s.numSquares(371) == 3
    assert s.numSquares(427) == 3
    assert s.numSquares(0) == 0
    assert s.numSquares(1) == 1
    assert s.numSquares(2) == 2
    assert s.numSquares(3) == 3
    assert s.numSquares(4) == 1
    assert s.numSquares(6) == 3
    assert s.numSquares(8) == 2
    assert s.numSquares(9) == 1
    assert s.numSquares(12) == 3
    assert s.numSquares(13) == 2
    assert s.numSquares(26) == 2
    assert s.numSquares(25 + 9) == 2
    assert s.numSquares(25 + 9 + 4) == 3
    assert s.numSquares(32) == 2
    assert s.numSquares(35) == 3 # 25+9+1
    assert s.numSquares(7217) == 3
    assert s.numSquares(32) == 2
    assert s.numSquares(48) == 3
    assert s.numSquares(88) == 3
    assert s.numSquares(7115) == 3
    assert s.numSquares(427) == 3
