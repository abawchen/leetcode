import unittest
import sys
import itertools
sys.path.append('./')

solutions = __import__('solutions.060_permutation_sequence', fromlist='*')


class Test046(unittest.TestCase):

    def test_getPermutation(self):
        s = solutions.Solution()

        n, k = 1, 1
        self.assertEqual(s.getPermutation(n, k), '1')    

        n, k = 3, 1
        self.assertEqual(s.getPermutation(n, k), '123')

        n, k = 3, 2
        self.assertEqual(s.getPermutation(n, k), '132')

        n, k = 3, 3
        self.assertEqual(s.getPermutation(n, k), '213')

        n, k = 3, 4
        self.assertEqual(s.getPermutation(n, k), '231')

        n, k = 3, 5
        self.assertEqual(s.getPermutation(n, k), '312')

        n, k = 3, 6
        self.assertEqual(s.getPermutation(n, k), '321')

        n = 7
        l = [ str(x+1) for x in xrange(n) ]
        ans = sorted([ list(pair) for pair in itertools.permutations(l) ])

        for k in xrange(len(ans)):
            self.assertEqual(s.getPermutation(n, k+1), ''.join(ans[k]))

    def _permutaions(self, l):
        return sorted([ list(pair) for pair in itertools.permutations(l) ])

if __name__ == '__main__':
    unittest.main()