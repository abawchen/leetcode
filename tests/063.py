import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.063_unique_paths_ii', fromlist='*')


class Test(unittest.TestCase):

    def test_uniquePathsWithObstacles(self):
        s = solutions.Solution()

        grid = [
            [0,0,0],
            [0,1,0],
            [0,0,0]
        ]
        self.assertEquals(s.uniquePathsWithObstacles(grid), 2)

        grid = [
            [1,0,0],
            [0,1,0],
            [0,0,0]
        ]
        self.assertEquals(s.uniquePathsWithObstacles(grid), 0)


        grid = [
            [0,0,1],
            [0,0,0]
        ]
        self.assertEquals(s.uniquePathsWithObstacles(grid), 2)


        grid = [
            [0,0,0],
            [0,0,1]
        ]
        self.assertEquals(s.uniquePathsWithObstacles(grid), 0)

        grid = [
            [0,0],
            [1,1],
            [0,0]
        ]
        self.assertEquals(s.uniquePathsWithObstacles(grid), 0)

        grid = [[0]]
        self.assertEquals(s.uniquePathsWithObstacles(grid), 1)
        


if __name__ == '__main__':
    unittest.main()
