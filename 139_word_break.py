# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# Return true because "leetcode" can be segmented as "leet code". 

import time
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if not s or not wordDict:
            return False

        dic = {}
        realDic = dict((word, True) for word in wordDict)
        for i in xrange(len(s)):
            for j in xrange(i+1, len(s)+1):
                if (i == 0 or i-1 in dic) and s[i:j] in realDic:
                    dic[j-1] = True

        return len(s)-1 in dic

        # i = 0
        # idx = 0
        # l = []
        # dic = {}
        # realDic = dict((word, True) for word in wordDict)
        # while i < len(s):
        #     for j in xrange(i+1, len(s)+1):
        #         word = s[i:j]
        #         if word in realDic and j-1 not in dic:
        #             dic[j-1] = True
        #             l.append(j-1)
            
        #     if idx == len(l):
        #         return False

        #     i = len(s) if not l else l[idx] + 1
        #     idx += 1
        
        # return len(s) - 1 in dic

start_time = time.time()
s = Solution()
print s.wordBreak("aaaaaaaa", ["aaaa","aa","a"]) #True
print s.wordBreak("leet", ["leet"]) #True
print s.wordBreak("leetcode", ["leet", "code"]) #True
print s.wordBreak("aaaaaaa", ["aaaa", "aa"]) #False
print s.wordBreak("aaaaaaa", ["aaaa", "aaa"]) #True
print s.wordBreak("aaaaaaa", ["aaa", "aaaa"]) #True
print s.wordBreak("dogs", ["dog","s","gs"]) #True
print s.wordBreak("cars", ["car", "ca", "rs"]) #True


print s.wordBreak("leafjeifjifanvaeruieet", ["leet"]) #False
print s.wordBreak("leafjeifjifanvaeruieet", ["leafjeifjifanvaeruieet"]) #True
print s.wordBreak("leafjeifjifanvaeruieet", ["l", "e", "a", "f", "j", "e", "i", "f", "j", "i", "f", "a", "n", "v", "a", "e", "ruieet"]) #True
print("--- %s seconds ---" % (time.time() - start_time))