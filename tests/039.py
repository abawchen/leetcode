import unittest
import sys
sys.path.append('./')

solutions = __import__('solutions.039_combination_sum', fromlist='*')


class Test(unittest.TestCase):

    def test_combinationSum(self):
        s = solutions.Solution()

        candidates, target = [2, 3, 6, 7], 7
        answer = [[7], [2, 2, 3]]
        self.assertEqual(
            self._listElementToTupleSet(s.combinationSum(candidates, target)),
            self._listElementToTupleSet(answer))


        candidates, target = [2, 4, 5, 6, 7, 10], 10
        answer = [[10], [4, 6], [2, 2, 6], [5, 5], [2, 2, 2, 2, 2], [2, 2, 2, 4], [2, 4, 4]]
        self.assertEqual(
            self._listElementToTupleSet(s.combinationSum(candidates, target)),
            self._listElementToTupleSet(answer))


        candidates, target = [1, 2], 3
        answer = [[1, 1, 1] ,[1, 2]]
        self.assertEqual(
            self._listElementToTupleSet(s.combinationSum(candidates, target)),
            self._listElementToTupleSet(answer))


        candidates, target = [1, 2], 4
        answer = [[1, 1, 1, 1], [1, 1, 2], [2, 2]]
        self.assertEqual(
            self._listElementToTupleSet(s.combinationSum(candidates, target)),
            self._listElementToTupleSet(answer))




        candidates, target = [5], 8
        answer = []
        self.assertEqual(
            self._listElementToTupleSet(s.combinationSum(candidates, target)),
            self._listElementToTupleSet(answer))




    def _listElementToTupleSet(self, l):
        tuples = []
        for e in l:
            tuples.append(tuple(e))
        return set(tuples)


if __name__ == '__main__':
    unittest.main()
