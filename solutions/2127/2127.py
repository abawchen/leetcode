import unittest
from collections import defaultdict

class Attendee:

    def __init__(self):
        self.accu = 0
        self.favorited_by = []

class Solution:

    def bfs(self, root, attendees) -> int:
        accu = 0
        stack = [attendees.pop(root, Attendee())]
        while len(stack) != 0:
            cur = stack.pop()
            accu = max(accu, cur.accu)
            for fav in cur.favorited_by:
                if fav == root:
                    return accu
                attendees[fav].accu = cur.accu + 1
                stack.append(attendees[fav])
                attendees.pop(fav, None)
        return accu

    def maximumInvitations(self, favorite: list[int]) -> int:
        ans = 0
        attendees = defaultdict(Attendee)
        couples = {}
        for i, v in enumerate(favorite):
            if i == favorite[v]:
                if v not in couples:
                    couples[i] = v
            else:
                attendees[v].favorited_by.append(i)
        for x, y in couples.items():
            accu_x = self.bfs(x, attendees)
            accu_y = self.bfs(y, attendees)
            ans = max(ans, 2+accu_x+accu_y)

        for k, v in list(attendees.items()):
            if k in attendees:
                accu = self.bfs(k, attendees)
                ans = max(ans, 1+accu)

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
        # result = self.solution.maximumInvitations([1,0,0,2,1,4])
        self.assertEqual(expected, result);

if __name__ == '__main__':
    unittest.main()
