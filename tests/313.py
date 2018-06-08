solution = __import__('solutions.313_super_ugly_number', fromlist='*')

from math import pow

def test_solution():
    s = solution.Solution()
    primes = [2, 3, 5]
    assert s.nthSuperUglyNumber(1, primes) == 1
    assert s.nthSuperUglyNumber(2, primes) == 2
    assert s.nthSuperUglyNumber(3, primes) == 3
    assert s.nthSuperUglyNumber(4, primes) == 4
    assert s.nthSuperUglyNumber(5, primes) == 5
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

    assert s.nthSuperUglyNumber(3, [2]) == 4
    assert s.nthSuperUglyNumber(3, [2,3,5]) == 3
    assert s.nthSuperUglyNumber(10, [2,5,7,11,13,17,23,29,43,53]) == 14
    assert s.nthSuperUglyNumber(12, [2,7,13,19]) == 32
    assert s.nthSuperUglyNumber(100000, [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]) == 1092889481
