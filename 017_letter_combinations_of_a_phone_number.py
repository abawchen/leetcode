# Given a digit string, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want. 

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        phoneDic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = []
        stack = list(phoneDic[digits[0]])
        while stack:
            letters = stack.pop()
            if len(letters) < len(digits):
                stack.extend([ letters + d for d in phoneDic[digits[len(letters)]] ])
            else:
                combinations.append(letters)

        return combinations

s = Solution()
print s.letterCombinations('23')
print s.letterCombinations('2')
print len(s.letterCombinations('327')), s.letterCombinations('327')