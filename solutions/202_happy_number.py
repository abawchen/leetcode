def isHappy(n):
    d = {}
    while n != 1:
        s = str(n)
        n = 0
        for c in s:
            n = n + int(c)**2
        print n
        if d.has_key(n):
            return False
        else:
            d[n] = True
    return True


print isHappy(19)
