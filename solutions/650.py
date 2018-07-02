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
        if n <= 1:
            return 0
        if n%2 != 0:
            return n

        steps = [0]*(n+1)
        for i in range(1, n+1):
            if i%2 == 0:
                steps[i] = -1
            else:
                steps[i] = i
        steps[2] = 2
        return self._minSteps(steps, n)

    def _minSteps(self, steps, n):
        if steps[n] == -1:
            return 2 + self._minSteps(steps, int(n/2))
        return steps[n]
