solution = __import__('solutions.310', fromlist='*')


def test_solution():
    s = solution.Solution()
    # """
    assert s.findMinHeightTrees(1,[]) == [0]
    assert s.findMinHeightTrees(2,[[0,1]]) == [0,1]
    assert s.findMinHeightTrees(4,[[1,0],[1,2],[1,3]]) == [1]
    assert s.findMinHeightTrees(6,[[0,3],[1,3],[2,3],[4,3],[5,4]]) == [3,4]
    assert s.findMinHeightTrees(6,[[0,1],[0,2],[0,3],[3,4],[4,5]]) == [3]
    # """
    """
      0
     /|\
    1 2 3
        |
        4
        |
        5
    """
    assert s.findMinHeightTrees(11, [[0,1],[0,2],[2,3],[0,4],[2,5],[5,6],[3,7],[6,8],[8,9],[9,10]]) == [5,6]
    """
        0
       /|\
      1 2 4
        |\
        3 5
        | |
        7 6
          |
          8
          |
          9
          |
          10
    """
    assert s.findMinHeightTrees(17, [[0,1],[0,2],[1,3],[3,4],[0,5],[0,6],[4,7],[3,8],[6,9],[1,10],[10,11],[9,12],[2,13],[10,14],[12,15],[4,16]]) == [0]
    """
            0 - 6 - 9 - 12 - 15
           /|\
          1 2 5
         /|  \
        3 10 13
       /| | \
      4 8 11 14
      |\
      7 16

            0 - 6 - 9 - 12
           /|
          1 2
         /|
        3 10
       /
      4
            0 - 6 - 9
           /
          1
         /
        3
    """
