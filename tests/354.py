solution = __import__('solutions.354', fromlist='*')


def test_solution():
    s = solution.Solution()
    assert s.maxEnvelopes([]) == 0
    assert s.maxEnvelopes([[1,1]]) == 1
    assert s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3
