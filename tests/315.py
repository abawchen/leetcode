solution = __import__('solutions.263_ugly_number', fromlist='*')

from math import pow

def test_solution():
    s = solution.Solution()
    assert s.isUgly(-2147483648) == False
    assert s.isUgly(-1) == False
    assert s.isUgly(0) == False
    assert s.isUgly(1) == True
    assert s.isUgly(2) == True
    assert s.isUgly(6) == True
    assert s.isUgly(7) == False
    assert s.isUgly(14) == False

    assert s.isUgly(pow(2, 31)) == True
    assert s.isUgly(pow(2, 31) - 1) == False
