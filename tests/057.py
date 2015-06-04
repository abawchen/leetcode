import unittest
import sys
sys.path.append('./')
solutions = __import__('solutions.057_insert_interval', fromlist='*')
utils = __import__('utils.interval', fromlist='*')


class Test056(unittest.TestCase):

    def test_insert(self):
        s = solutions.Solution()


        intervals = []
        newInterval = utils.Interval(1, 2)
        self.assertEqual(
            self._intervalsValue(s.insert(intervals, newInterval)), 
            self._intervalsValue([
                utils.Interval(1, 2)
            ])
        )

        intervals = [utils.Interval(1, 5)]
        newInterval = utils.Interval(2, 7)
        self.assertEqual(
            self._intervalsValue(s.insert(intervals, newInterval)), 
            self._intervalsValue([
                utils.Interval(1, 7)
            ])
        )

        intervals = [utils.Interval(1, 5)]
        newInterval = utils.Interval(6, 8)
        self.assertEqual(
            self._intervalsValue(s.insert(intervals, newInterval)), 
            self._intervalsValue([
                utils.Interval(1, 5),
                utils.Interval(6, 8)
            ])
        )

        intervals = [
            utils.Interval(1, 5),
            utils.Interval(10, 50)
        ]
        newInterval = utils.Interval(45, 80)
        self.assertEqual(
            self._intervalsValue(s.insert(intervals, newInterval)), 
            self._intervalsValue([
                utils.Interval(1, 5),
                utils.Interval(10, 80)
            ])
        )

        intervals = [
            utils.Interval(1, 5),
            utils.Interval(10, 50)
        ]
        newInterval = utils.Interval(0, 80)
        self.assertEqual(
            self._intervalsValue(s.insert(intervals, newInterval)), 
            self._intervalsValue([
                utils.Interval(0, 80)
            ])
        )


        intervals = [
            utils.Interval(1, 5),
            utils.Interval(10, 50)
        ]
        newInterval = utils.Interval(51, 80)
        self.assertEqual(
            self._intervalsValue(s.insert(intervals, newInterval)), 
            self._intervalsValue([
                utils.Interval(1, 5),
                utils.Interval(10, 50),
                utils.Interval(51, 80),
            ])
        )

        intervals = [
            utils.Interval(1, 3),
            utils.Interval(6, 9)
        ]
        newInterval = utils.Interval(2, 5)
        self.assertEqual(
            self._intervalsValue(s.insert(intervals, newInterval)), 
            self._intervalsValue([
                utils.Interval(1, 5),
                utils.Interval(6, 9)   
            ])
        )


        intervals = [
            utils.Interval(1, 2),
            utils.Interval(3, 5),
            utils.Interval(6, 7),
            utils.Interval(8, 10),
            utils.Interval(12, 16),
        ]
        newInterval = utils.Interval(4, 9)
        self.assertEqual(
            self._intervalsValue(s.insert(intervals, newInterval)), 
            self._intervalsValue([
                utils.Interval(1, 2),
                utils.Interval(3, 10),
                utils.Interval(12, 16),
            ])
        )

        intervals = [
            utils.Interval(1, 2),
            utils.Interval(3, 100),
            utils.Interval(105, 700),
        ]
        newInterval = utils.Interval(4, 50)
        self.assertEqual(
            self._intervalsValue(s.insert(intervals, newInterval)), 
            self._intervalsValue([
                utils.Interval(1, 2),
                utils.Interval(3, 100),
                utils.Interval(105, 700),
            ])
        )

    def _intervalsValue(self, intervals):
        vals = []
        for interval in intervals:
            vals.append((interval.start, interval.end))
        return vals

if __name__ == '__main__':
    unittest.main()