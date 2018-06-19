class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''

        from collections import defaultdict
        d = defaultdict(list)
        for i, v in enumerate(s):
            d[v].append(i)
        # print(d)
        letters = sorted(d.keys())[::-1]
        ans = [d[letters[0]][-1]]
        for letter in letters[1:]:
            print(ans)
            ps = d[letter]
            e = 0
            i = 0
            print('*'*10)
            print(ps[i], ans[e])
            while e < len(ans) and ps[i] > ans[e]:
                print('here?')
                e += 1
            if e == len(ans):
                print('there?')
                ans.append(ps[-1])
            else:
                while i < len(ps) and ps[i] < ans[e]:
                    i += 1
                print(e, i)
                ans.insert(e, ps[i-1])
        print(ans)
        return ''.join(list(map(lambda i: s[i], ans)))
        """
        idx = set()
        for v in l:
            idx.add(d[v][-1])
        ans = ''
        for i, v in enumerate(s):
            if i in idx:
                ans += v
        return ans
        """
