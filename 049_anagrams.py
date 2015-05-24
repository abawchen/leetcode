# Given an array of strings, return all groups of strings that are anagrams.
# Note: All inputs will be in lower-case.

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        if not strs:
            return []

        # Another 2 better solutions:
        # import collections

        # count = collections.Counter([tuple(sorted(s)) for s in strs])
        # return filter(lambda x: count[tuple(sorted(x))]>1, strs)

        # d = collections.defaultdict(list)
        # for s in strs:
        #     d[tuple(sorted(s))].append(s)  
        # return [a for agram_group in d.values() if len(agram_group)>1 for a in agram_group]


        import string
        answer = {}
        checkDic = {}
        asciiDic = dict((c, i) for i, c in enumerate(string.ascii_lowercase))
        for s in strs:
            l = [0 for i in xrange(26)]
            for c in s:
                l[asciiDic[c]] += 1

            key = ''.join(c+str(n) for (c, n) in zip(string.ascii_lowercase, l))
            if key in checkDic:
                checkDic[key].append(s)
                answer[key] = True
            else:
                checkDic[key] = [s]

        result = []
        for key in answer:
            result.extend(checkDic[key])

        return result

s = Solution()

# print s.anagrams(["cat","rye","aye","dog", "god","cud","cat","old","fop","bra"])
print s.anagrams(["and","dan"])
# print s.anagrams(["ant","ant"])
# print s.anagrams(["dog","cat","god","tac"])
# print s.anagrams([])
# print s.anagrams(["abc"])
# print s.anagrams(["tin","ram","zip","cry","pus","jon","zip","pyx"])