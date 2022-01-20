import unittest
from collections import defaultdict

class Attendee:

    def __init__(self):
        self.accu = 0
        self.favorited_by = []

class Solution:

    def bfs(self, root, is_couple, attendees) -> int:
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
        return accu if is_couple else 0

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

        # start from standalone couples
        for x, y in couples.items():
            accu_x = self.bfs(x, True, attendees)
            accu_y = self.bfs(y, True, attendees)
            ans = max(ans, accu_x + accu_y)
        
        # include all standalone couples
        ans += 2 * len(couples)

        for k, v in list(attendees.items()):
            if k in attendees:
                accu = self.bfs(k, False, attendees)
                ans = max(ans, 1+accu)

        return ans


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        data = [2,2,1,2]
        expected = 3
        got = self.solution.maximumInvitations(data)
        self.assertEqual(expected, got)

    def test_02(self):
        data = [1, 2, 0]
        expected = 3
        got = self.solution.maximumInvitations(data)
        self.assertEqual(expected, got)

    def test_03(self):
        data = [3,0,1,4,1]
        expected = 4
        got = self.solution.maximumInvitations(data)
        self.assertEqual(expected, got)

    def test_04(self):
        data = []
        expected = 0
        got = self.solution.maximumInvitations(data)
        self.assertEqual(expected, got)

    def test_05(self):
        data = [1,0,0,2,1,4,7,8,9,6,7,10,8]
        expected = 6
        got = self.solution.maximumInvitations(data)
        self.assertEqual(expected, got)

    def test_06(self):
        data = [1,0,3,2,5,6,7,4,9,8,11,10,11,12,10]
        expected = 11
        got = self.solution.maximumInvitations(data)
        self.assertEqual(expected, got)

    def test_07(self):
        data = [1, 0]
        expected = 2
        got = self.solution.maximumInvitations(data)
        self.assertEqual(expected, got)

    def test_08(self):
        data = [1, 0, 3, 2]
        expected = 4
        got = self.solution.maximumInvitations(data)
        self.assertEqual(expected, got)

    def test_09(self):
        data = [19,20,16,11,18,6,7,1,16,3,7,2,1,7,0,0,13,14,20,20,15]
        expected = 4
        got = self.solution.maximumInvitations(data)
        self.assertEqual(expected, got)

    def test_10(self):
        data =  [22,9,3,4,6,23,5,12,16,20,13,9,1,17,4,3,9,18,16,24,0,18,11,22,1]
        expected = 5
        got = self.solution.maximumInvitations(data)
        self.assertEqual(expected, got)

if __name__ == '__main__':
    unittest.main()
