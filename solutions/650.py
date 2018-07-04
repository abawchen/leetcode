"""
https://leetcode.com/problems/2-keys-keyboard/description/

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Note:
The n will be in the range [1, 1000].
"""

class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [0, 0] + [x for x in range(2, n+1)]
        for i in range(2, n+1):
            if n%i == 0:
                for j in range(2, int(n/i)+1):
                    t = i*j
                    steps[t] = min(steps[t], steps[i]+j)
        return steps[n]
