import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.045_jump_game_ii', fromlist='*')


class Test(unittest.TestCase):

    def test_jump(self):
        s = solutions.Solution()

        # nums = [2, 3, 1, 1, 4]
        # self.assertEquals(s.jump(nums), 2)

        # nums = [20]
        # self.assertEquals(s.jump(nums), 0)

        # nums = [2,0]
        # self.assertEquals(s.jump(nums), 1)

        # nums = [2, 5, 0, 0]
        # self.assertEquals(s.jump(nums), 2)

        nums = [2, 4, 1, 6, 4, 1, 1, 1, 1, 1]
        self.assertEquals(s.jump(nums), 3)


        
if __name__ == '__main__':
    unittest.main()
