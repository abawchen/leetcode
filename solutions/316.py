class Solution:

    def larger(self, s, t):
        return list(filter(lambda x: x > t, s))

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ''

        from collections import defaultdict
        seen = defaultdict(set)
        position = defaultdict(list)
        for i, v in enumerate(s[::-1]):
            p = len(s)-i-1
            position[v].insert(0, p)
            if p != len(s)-1:
                previous = seen[p+1].copy()
                seen[p] = previous
                seen[p].add(s[p+1])

        letters = sorted(position.keys())
        tmp = [-1, position[letters[0]][0], len(s)]
        for letter in letters[1:]:
            print(tmp)
            ps = position[letter]
            m = 0
            n = 0
            p = -1
            while p == -1:

                if n == len(tmp)-2:
                    p = n+1
                elif ps[m] > tmp[n] and ps[m] < tmp[n+1]:
                    m_seen = self.larger(seen[ps[m]], letter)
                    n_seen = self.larger(seen[tmp[n+1]], letter)
                    if len(m_seen) > len(n_seen):
                        p = n+1
                    elif m == len(ps)-1:
                        p = n+1
                    else:
                        m += 1
                else:
                    n += 1

            tmp.insert(p, ps[m])
        print(tmp)
        return ''.join(list(map(lambda i: s[i], tmp[1:-1])))

        # print(seen)
        # print(position)
        """
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
        return ''.join(list(map(lambda i: s[i], ans))
        """
