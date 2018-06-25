solution = __import__('solutions.278', fromlist='*')

from math import pow

def test_solution():
    # f = lambda x: x >= 4
    s = solution.Solution()
    """
    assert s.firstBadVersion(5) == 4
    assert s.firstBadVersion(4) == 4
    """

    # f = lambda x: x >= 1
    assert s.firstBadVersion(5) == 1
    assert s.firstBadVersion(4) == 1
    assert s.firstBadVersion(2) == 1
    assert s.firstBadVersion(1) == 1

