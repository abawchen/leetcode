solution = __import__('solutions.316', fromlist='*')


def test_solution():
    s = solution.Solution()
    assert s.removeDuplicateLetters('') == ''
    assert s.removeDuplicateLetters('a') == 'a'
    assert s.removeDuplicateLetters('bcabc') == 'abc'
    assert s.removeDuplicateLetters('bca') == 'bca'
    assert s.removeDuplicateLetters('bcab') == 'bca'
    assert s.removeDuplicateLetters('cbacdcbc') == 'acdb'
    '''
    cbacdcbc
      ^^^ ^
    cbcdcbc
     ^^^
    cbdcbc
     ^^^
    '''
