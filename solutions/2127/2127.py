import unittest

class Attendee:

    def __init__(self, left: int, num_of_left: int):
        self.left = left
        self.right = -1
        self.num_of_left = num_of_left
        self.merged = False


class Solution:

    def maximumInvitations(self, favorite: list[int]) -> int:
        ans = 0
        # pool = {i: v for i, v in enumerate(favorite)}
        # couples = []

        print(couples)

        # starts = dict(pool)
        # for f in favorite:
        #     starts.pop(f, None)
        # if len(starts) == 0:
        #     return len(favorite)
        # print(starts)

        # attendees = {}
        # for cur, fav in starts.items():
        #     prev = -1
        #     cur_num = 0
        #     if cur in pool:
        #         print("*" * 10)
        #         while cur in pool:
        #             print(cur)
        #             fav = pool.pop(cur)
        #             attendees[cur] = Attendee(prev, cur_num)
        #             cur_num += 1
        #             prev = cur
        #             cur = fav
        #         # if attendees[cur].merged:
        #             # cur_num += 2
        #         if cur != attendees[prev].left:
        #             cur_num -= attendees[cur].num_of_left
        #         else:
        #             attendees[prev].merged = True
                    
        #             attendees[cur].merged = True
        #             attendees[cur].right = prev
        #             attendees[cur].num_of_right = 1
        #             attendees[cur].num_of_left = max(self.num_of_left, cur_num - 2)


        #         ans = max(ans, cur_num)

        return ans


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    # def test_01(self):
    #     expected = 3
    #     result = self.solution.maximumInvitations([2,2,1,2])
    #     self.assertEqual(expected, result)

    # def test_02(self):
    #     expected = 3
    #     result = self.solution.maximumInvitations([1, 2, 0])
    #     self.assertEqual(expected, result)

    # def test_03(self):
    #     expected = 4
    #     result = self.solution.maximumInvitations([3,0,1,4,1])
    #     self.assertEqual(expected, result)

    # def test_04(self):
    #     expected = 0
    #     result = self.solution.maximumInvitations([])
    #     self.assertEqual(expected, result);

    def test_05(self):
        expected = 6
        # result = self.solution.maximumInvitations([1,0,0,2,1,4,7,8,9,6,7,10,8])
        result = self.solution.maximumInvitations([1,0,0,2,1,4])
        self.assertEqual(expected, result);

if __name__ == '__main__':
    unittest.main() 