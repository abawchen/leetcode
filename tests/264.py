solution = __import__('solutions.264_ugly_number_ii', fromlist='*')

from math import pow

def test_solution():
    s = solution.Solution()
    assert s.nthUglyNumber(1) == 1
    assert s.nthUglyNumber(2) == 2
    assert s.nthUglyNumber(3) == 3
    assert s.nthUglyNumber(4) == 4
    assert s.nthUglyNumber(5) == 5
    assert s.nthUglyNumber(6) == 6
    assert s.nthUglyNumber(7) == 8
    assert s.nthUglyNumber(8) == 9
    assert s.nthUglyNumber(9) == 10
    assert s.nthUglyNumber(10) == 12
    assert s.nthUglyNumber(11) == 15
    assert s.nthUglyNumber(12) == 16
    assert s.nthUglyNumber(20) == 36
    assert s.nthUglyNumber(30) == 80
    assert s.nthUglyNumber(38) == 128
    assert s.nthUglyNumber(1690) == 2123366400
