solution = __import__('solutions.312', fromlist='*')



def test_burstBalloon():
    s = solution.Solution()
    nums = [3,8]
    assert s.burstBalloon(nums, 0) == (24, [8])

    nums = [3,5,8]
    assert s.burstBalloon(nums, 1) == (120, [3,8])

"""
def test_solution():
    s = solution.Solution()
    assert s.maxCoins([3,8]) == 3*8 + 8
    assert s.maxCoins([3,5,8]) == 3*5*8 + 3*8 + 8
    assert s.maxCoins([3,1,5,8]) == 167
"""
