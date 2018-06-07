solution = __import__('solutions.313_super_ugly_number', fromlist='*')

from math import pow

def test_solution():
    s = solution.Solution()
    primes = [2, 3, 5]
    """
    assert s.nthSuperUglyNumber(1, primes) == 1
    assert s.nthSuperUglyNumber(2, primes) == 2
    assert s.nthSuperUglyNumber(3, primes) == 3
    assert s.nthSuperUglyNumber(4, primes) == 4
    """
    assert s.nthSuperUglyNumber(5, primes) == 5
    """
    assert s.nthSuperUglyNumber(6, primes) == 6
    assert s.nthSuperUglyNumber(7, primes) == 8
    assert s.nthSuperUglyNumber(8, primes) == 9
    assert s.nthSuperUglyNumber(9, primes) == 10
    assert s.nthSuperUglyNumber(10, primes) == 12
    assert s.nthSuperUglyNumber(11, primes) == 15
    assert s.nthSuperUglyNumber(12, primes) == 16
    assert s.nthSuperUglyNumber(20, primes) == 36
    assert s.nthSuperUglyNumber(30, primes) == 80
    assert s.nthSuperUglyNumber(38, primes) == 128
    assert s.nthSuperUglyNumber(1690, primes) == 2123366400
    """
