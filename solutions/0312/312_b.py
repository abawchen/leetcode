# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

#  1,2,3,4
# [3,1,5,8]


================
# dp[1][1]
    # k: 1
    # nums[i-1]*nums[k]*nums[j+1]


================
# dp[1][2]
    # k: 1
    # nums[i-1]*nums[k]*nums[j+1] + dp[2][2]

    # k: 2
    # dp[1][1] + nums[i-1]*nums[k]*nums[j+1]


================
# dp[1][3]
    # k: 1 $$
    # nums[i-1]*nums[k]*nums[j+1], dp[2][3]
                                   --------
    # k: 2
    # dp[1][1], nums[i-1]*nums[k]*nums[j+1], dp[3][3]

    # k: 3
    # dp[1][2], nums[i-1]*nums[k]*nums[j+1]


================
# dp[1][4]
    # k: 1
    # nums[i-1]*nums[k]*nums[j+1] + dp[2][4]
                                    --------

# dp[1][4]
    # k: 2
    # dp[1][1] + nums[i-1]*nums[k]*nums[j+1] + dp[3][4]
                                               --------

# dp[1][4]
    # k: 3
    # dp[1][2] + nums[i-1]*nums[k]*nums[j+1] + dp[4][4]


# dp[1][4]
    # k: 4 $$
    # dp[1][3] + nums[i-1]*nums[k]*nums[j+1]


================
# dp[2][3]
    # k: 2
    # nums[i-1]*nums[k]*nums[j+1] + dp[3][3]

    # k: 3
    # dp[2][2] + nums[i-1]*nums[k]*nums[j+1]


# dp[2][4]
    # k: 2
    # nums[i-1]*nums[k]*nums[j+1] + dp[3][4]

    # k: 3
    # dp[2][2] + nums[i-1]*nums[k]*nums[j+1] + dp[4][4]

    # k: 4
    # dp[2][3] + nums[i-1]*nums[k]*nums[j+1]