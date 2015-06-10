# Write a function to find the longest common prefix string amongst an array of strings. 

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        lcp = ""
        base = strs[0]
        for i in range(len(base)):
            for s in strs[1:]:
                if i > len(s) - 1:
                    return lcp
                if base[i] != s[i]:
                    return lcp
            lcp += base[i]
        return lcp

        # lcp = ""
        # for z in zip(*strs):
        #     bag = set(z);
        #     if len(bag) == 1:
        #         lcp += bag.pop()
        #     else:
        #         break
        # return lcp

        # 84 ms
        # lcp = strs[0]
        # for s in strs[1:]:
        #     i, j, local = 0, 0, ""
        #     while i < len(lcp) and j < len(s):
        #         if lcp[i] != s[j]:
        #             break
        #         local += lcp[j]
        #         i, j = i+1, j+1

        #     if not local:
        #         return ""

        #     lcp = local

        # return lcp
