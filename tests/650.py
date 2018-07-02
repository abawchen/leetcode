solution = __import__('solutions.650', fromlist='*')


def test_solution():
    s = solution.Solution()
    assert s.minSteps(0) == 0
    assert s.minSteps(1) == 0
    assert s.minSteps(2) == 2
    assert s.minSteps(3) == 3
    assert s.minSteps(4) == 4
    assert s.minSteps(5) == 5
    assert s.minSteps(6) == 5
    assert s.minSteps(7) == 7
    assert s.minSteps(8) == 6
    assert s.minSteps(9) == 6

"""
# 5(5)
A       (copy)
AA
AAA
AAAA
AAAAA


A       (copy)
AA      (paste)
        (copy)
AAAA    (paste)

# 6
A       (copy)
AA      (paste)
AAA     (paste)
        (copy)
AAAAAA  (paste)

# 8
A       (copy)
AA      (paste)
        (copy)
AAAA    (paste)
        (copy)
AAAAAAAA(paste)
"""
