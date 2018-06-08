solution = __import__('solutions.315_count_of_smaller_numbers_after_self', fromlist='*')

def test_solution():
    s = solution.Solution()
    assert s.countSmallerTLE([5,2,6,1]) == [2,1,1,0]
    assert s.countSmallerTLE([1, 20, 3, 1, 10, 9, 9, 8, 7, 11, 23]) == [0, 8, 1, 0, 4, 2, 2, 1, 0, 0, 0]
    assert s.countSmallerTLE([10, 200, 30, 10, 100, 90, 90, 80, 70, 110, 230]) == [0, 8, 1, 0, 4, 2, 2, 1, 0, 0, 0]
