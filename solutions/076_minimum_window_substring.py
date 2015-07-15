# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# For example,
# S = "ADOBECODEBANC"
# T = "ABC"

# Minimum window is "BANC".

# Note:
# If there is no such window in S that covers all characters in T, return the emtpy string "".

# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S. 

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        from collections import defaultdict
        fixedDic = defaultdict(int)
        targetDic = defaultdict(int)
        currentDic = defaultdict(int)

        for c in t:
            fixedDic[c] += 1
            targetDic[c] += 1

        l = []
        count = 0
        window = "a" * (len(s)+1)
        for i, c in enumerate(s):
            if c in targetDic:
                currentDic[c] += 1
                l.append(i)

                if targetDic[c] >= 1:
                    targetDic[c] -= 1
                    count += 1

                if count == len(t):
                    while True:
                        if l[-1] - l[0] + 1 < len(window):
                            window = s[l[0]:l[-1]+1]

                        p = s[l.pop(0)]
                        currentDic[p] -= 1

                        if currentDic[p] < fixedDic[p]:
                            targetDic[p] += 1
                            count -= 1
                            break

        return window if len(window) <= len(s) else ""