# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"]. 


class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return []

        dic = {}
        for i in xrange(len(s)):
            for j in xrange(i+1, len(s)+1):
                if (i == 0 or i-1 in dic) and s[i:j] in wordDict:
                    if i == 0:
                        dic[j-1] = [(-1, s[i:j])]
                    elif j-1 in dic:
                        dic[j-1].append((i-1, s[i:j]))

                    else:
                        dic[j-1] = [(i-1, s[i:j])]

        if len(s)-1 in dic:
            answer = []
            stack = [[pair, []] for pair in dic[len(s)-1]]
            while stack:
                ((idx, word), words) = stack.pop()
                words = [word] + words
                if idx != -1:
                    stack.extend([ [pair, words] for pair in dic[idx] ])
                else:
                    answer.append(' '.join(words))

            return answer

        return []