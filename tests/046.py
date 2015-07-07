import unittest
import sys
import itertools
sys.path.append('./')

solutions = __import__('solutions.046_permutations', fromlist='*')


class Test046(unittest.TestCase):

    def test_permute(self):
        s = solutions.Solution()

        l = [1]
        self.assertEqual(s.permute(l), self._permutaions(l))

        l = [1, 2]
        self.assertEqual(s.permute(l), self._permutaions(l))

        l = [1, 2, 3]
        self.assertEqual(s.permute(l), self._permutaions(l))

        l = [1, 2, 3, 4]
        self.assertEqual(s.permute(l), self._permutaions(l))

        
        # for i in xrange(9):
        #     l = [ n for n in xrange(i+1) ]
        #     self.assertEqual(s.permute(l), self._permutaions(l))

    def _permutaions(self, l):
        return sorted([ list(pair) for pair in itertools.permutations(l) ])

if __name__ == '__main__':
    unittest.main()
