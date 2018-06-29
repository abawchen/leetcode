solution = __import__('solutions.207', fromlist='*')


def test_solution():
    s = solution.Solution()
    assert s.canFinish(4, [[1,0],[2,0],[3,1],[3,2]]) == True
    assert s.canFinish(2, [[1,0]]) == True
    assert s.canFinish(0, []) == True
    assert s.canFinish(1, []) == True
    assert s.canFinish(2, []) == True
    assert s.canFinish(3, [[1,0]]) == True
    assert s.canFinish(5, [[1,0],[2,1],[3,1],[4,2]]) == True
    assert s.canFinish(5, [[1,0],[2,0],[3,1],[4,3],[4,2]]) == True
    assert s.canFinish(2, [[0,1],[1,0]]) == False
    assert s.canFinish(3, [[0,2],[1,2],[2,0]]) == False
    assert s.canFinish(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]) == False
