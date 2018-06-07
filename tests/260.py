solution = __import__('solutions.260_single_number_iii', fromlist='*')

from math import pow

def test_solution():
    s = solution.Solution()
    assert s.singleNumber([1,2,1,3,2,5]) == [3, 5]
