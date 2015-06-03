import unittest
import sys
import itertools
sys.path.append('./')

# solutions = __import__('solutions.047_permutations_ii.py', fromlist='*')
solutions = __import__('solutions.047_permutations_ii', fromlist='*')


class Test012(unittest.TestCase):

    def test_intToRoman(self):
        s = solutions.Solution()

        l = [1, 1, 2, 2]
        self.assertEqual(sorted(s.permuteUnique(l)), sorted(self._permutaions(l)))


        l = [1, 1, 2]
        self.assertEqual(sorted(s.permuteUnique(l)), sorted(self._permutaions(l)))


    
    def _permutaions(self, l):
        return sorted([ list(pair) for pair in set(itertools.permutations(l)) ])



if __name__ == '__main__':
    unittest.main()
