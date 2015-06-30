import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.055_jump_game', fromlist='*')


class Test(unittest.TestCase):

    def test_canJump(self):
        s = solutions.Solution()

        nums = [2, 3, 1, 1, 4]
        self.assertEquals(s.canJump(nums), True)

        nums = [3, 2, 1, 0, 4]
        self.assertEquals(s.canJump(nums), False)

        nums = [20]
        self.assertEquals(s.canJump(nums), True)

        nums = [2,0]
        self.assertEquals(s.canJump(nums), True)

        
if __name__ == '__main__':
    unittest.main()
