solution = __import__('solutions.264_ugly_number_ii', fromlist='*')

from math import pow

def test_solution():
    s = solution.Solution()
    assert s.nthUglyNumber(1) == 1
    assert s.nthUglyNumber(6) == 6
    assert s.nthUglyNumber(10) == 12
    assert s.nthUglyNumber(20) == 36
    assert s.nthUglyNumber(1690) == 1
