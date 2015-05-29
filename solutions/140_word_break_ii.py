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

        else:
            return []


s = Solution()

# https://leetcode.com/discuss/18248/word-break-ii-time-limit-exceeded-error-when-input-is-a
# print s.wordBreak(
#     "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
#     ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])

# #['aaa aaaa', 'a a a aaaa', 'aaaa aaa', 'a aaa aaa', 'aaa a aaa', 'a a a a aaa', 'a a aaaa a', 'aaa aaa a', 'a a a aaa a', 'a aaaa a a', 'a a aaa a a', 'aaaa a a a', 'a aaa a a a', 'aaa a a a a', 'a a a a a a a']


# print s.wordBreak("leet", ["leet"]) #['leet']
print s.wordBreak("leetcode", ["leet", "code"]) #['leet code']
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) #['cat sand dog', 'cats and dog']

print s.wordBreak("aaaaaaa", ["aaaa", "aa"]) #[]
print s.wordBreak("aaaaaaa", ["aaaa", "aaa"]) #['aaa aaaa', 'aaaa aaa']
print s.wordBreak("aaaaaaa", ["aaa", "aaaa", "a"])
# #['aaa aaaa', 'a a a aaaa', 'aaaa aaa', 'a aaa aaa', 'aaa a aaa', 'a a a a aaa', 'a a aaaa a', 'aaa aaa a', 'a a a aaa a', 'a aaaa a a', 'a a aaa a a', 'aaaa a a a', 'a aaa a a a', 'aaa a a a a', 'a a a a a a a']

# print s.wordBreak("leafjeifjifanvaeruieet", ["leet"]) #[]
# print s.wordBreak("leafjeifjifanvaeruieet", ["leafjeifjifanvaeruieet"]) #['leafjeifjifanvaeruieet']
# print s.wordBreak("leafjeifjifanvaeruieet", ["l", "e", "a", "f", "j", "e", "i", "f", "j", "i", "f", "a", "n", "v", "a", "e", "ruieet"]) #['l e a f j e i f j i f a n v a e ruieet']