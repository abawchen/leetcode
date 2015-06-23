def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    d1, d2 = {}, {}
    for i in xrange(len(s)):
        a, b = s[i], t[i]
        if d1.has_key(a) and d1[a] == b and d2.has_key(b) and d2[b] == a:
            continue
        elif not d1.has_key(a) and not d2.has_key(b):
            d1[a], d2[b] = b, a
        else:
            return False
    
    return True