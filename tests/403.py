solution = __import__('solutions.403', fromlist='*')


def test_solution():
    s = solution.Solution()
    assert s.canCross([0,1,3,5,6,8,12,17]) == True
    assert s.minSteps([0,1,2,3,4,8,9,11]) == False
