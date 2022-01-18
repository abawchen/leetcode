import unittest

class Attendee:

    def __init__(self, left: int, num_of_left: int):
        self.left = left
        self.num_of_left = num_of_left


class Solution:

    def maximumInvitations(self, favorite: list[int]) -> int:
        ans = 0
        pool = {i: v for i, v in enumerate(favorite)}
        attendees = {}
        for cur, fav in enumerate(favorite):
            prev = -1
            cur_num = 0
            if cur in pool:
                while cur in pool:
                    fav = pool.pop(cur)
                    attendees[cur] = Attendee(prev, cur_num)
                    cur_num += 1
                    prev = cur
                    cur = fav
                if cur != attendees[prev].left:
                    cur_num -= attendees[cur].num_of_left
                ans = max(ans, cur_num)

        return ans


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        expected = 3
        result = self.solution.maximumInvitations([2,2,1,2])
        self.assertEqual(expected, result)

    def test_02(self):
        expected = 3
        result = self.solution.maximumInvitations([1, 2, 0])
        self.assertEqual(expected, result)

    def test_03(self):
        expected = 4
        result = self.solution.maximumInvitations([3,0,1,4,1])
        self.assertEqual(expected, result)

    def test_04(self):
        expected = 0
        result = self.solution.maximumInvitations([])
        self.assertEqual(expected, result);

    def test_05(self):
        expected = 6
        result = self.solution.maximumInvitations([1,0,0,2,1,4,7,8,9,6,7,10,8])
        self.assertEqual(expected, result);

if __name__ == '__main__':
    unittest.main() 