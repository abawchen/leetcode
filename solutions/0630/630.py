import bisect 
import unittest


class Course(object):
    def __init__(self, course: list[int]):
        self.duration = course[0]
        self.last_day = course[1]

    def __lt__(self, other):
        return self.duration < other.duration

    def __repr__(self):
        return f"[{self.duration}, {self.last_day}]"


class Solution:

    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses_by_last_day = sorted(courses, key = lambda c: c[1])
        courses_by_duration = []
        day = 0
        for c in courses_by_last_day:
            if c[1] < c[0]:
                continue
            course = Course(c)
            if day + course.duration <= course.last_day:
                day += course.duration
                bisect.insort_left(courses_by_duration, course)
            elif courses_by_duration[-1].duration > course.duration:
                pop = courses_by_duration.pop()
                bisect.insort_left(courses_by_duration, course)
                day = day - pop.duration + course.duration

        return len(courses_by_duration)


class SolutionTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_01(self):
        courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
        expected = 3
        got = self.solution.scheduleCourse(courses)
        self.assertEqual(expected, got)

    def test_02(self):
        courses = [[1,2]]
        expected = 1
        got = self.solution.scheduleCourse(courses)
        self.assertEqual(expected, got)

    def test_03(self):
        courses = [[3,2],[4,3]]
        expected = 0
        got = self.solution.scheduleCourse(courses)
        self.assertEqual(expected, got)

    def test_04(self):
        courses = [[5,5],[4,6],[2,6]]
        expected = 2
        got = self.solution.scheduleCourse(courses)
        self.assertEqual(expected, got)        

if __name__ == '__main__':
    unittest.main()
