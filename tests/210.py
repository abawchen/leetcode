solution = __import__('solutions.210', fromlist='*')


def test_solution():
    s = solution.Solution()
    assert s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0,2,1,3]
    assert s.findOrder(2, [[1,0]]) == [0,1]
    assert s.findOrder(0, []) == []
    assert s.findOrder(1, []) == [0]
    assert s.findOrder(2, []) == [1,0]
    assert s.findOrder(3, [[1,0]]) == [0,2,1]
    assert s.findOrder(5, [[1,0],[2,1],[3,1],[4,2]]) == [0,1,2,4,3]
    assert s.findOrder(5, [[1,0],[2,0],[3,1],[4,3],[4,2]]) == [0,1,2,3,4]
    assert s.findOrder(2, [[0,1],[1,0]]) == []
    assert s.findOrder(3, [[0,2],[1,2],[2,0]]) == []
    assert s.findOrder(8, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]) == []
