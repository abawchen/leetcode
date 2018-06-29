solution = __import__('solutions.322', fromlist='*')


def test_solution():
    s = solution.Solution()
    assert s.coinChange([1,2,5], 11) == 3
    assert s.coinChange([2], 3) == -1
    assert s.coinChange([], 1) == -1
    assert s.coinChange([1, 3, 4], 0) == 0
    assert s.coinChange([1,2,5,12], 11) == 3
    assert s.coinChange([1,2,5,11], 11) == 1
