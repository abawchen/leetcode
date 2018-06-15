# -*- coding: utf-8 -*-
solution = __import__('solutions.312', fromlist='*')

def test_solution():
    s = solution.Solution()
    """
    assert s.maxCoins([10]) == 10
    assert s.maxCoins([3,8]) == 3*8 + 8
    assert s.maxCoins([3,10,3]) == (90 + 9 + 3)
    """
    """
    assert s.maxCoins([3,5,8]) == 152 #(3*5*8 + 3*8 + 8)
    assert s.maxCoins([1,5,8]) == (5 + 40 + 8)
    assert s.maxCoins([8,5,3]) == 152
    assert s.maxCoins([3,1,5,8]) == (15 + 152)
    assert s.maxCoins([0,3,1,5,8]) == 167
    assert s.maxCoins([3,0,1,5,8]) == 167
    """

    assert s.maxCoins([3,2,5,8]) == (3*2*5 + 152)
    assert s.maxCoins([3,5,8]) == 120 + 24 + 8 # 30
    assert s.maxCoins([3,2,8]) == 48 + 24 + 8  # 80
    # assert s.maxCoins([3,1,2,5,8]) == (6 + 30 + 152)
    """
    assert s.maxCoins([1,3,5,8]) == (3 + 152)
    assert s.maxCoins([1,3,2,5,8]) == (3 + 30 + 152)
    assert s.maxCoins([9,76,64,21]) == 116718 # (102144 + 14574)
    assert s.maxCoins([9,76,21]) == 14574
    assert s.maxCoins([76,64,21,21]) == 137332 # (64*76*21 + 35188)
    # """
    """
    ==> 先砍 64
        76*64*21 + 76*21*21 + 76*21 + 76
                   ^^^^^^^^
    ==> 先砍 21
        64*21*21 + 76*64*61 + 76*21 + 76
        ^^^^^^^^
    """
    """
    assert s.maxCoins([76,21,21]) == 35188
    assert s.maxCoins([76,64,21]) == 103816
    """
