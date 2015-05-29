def reverseWords(s):
    if s == None:
        return s

    s = s.strip()
    n = ""
    counting = False
    start = 0
    end = 0
    for i, c in enumerate(s):
        if c == " ":
            if counting:
                end = i
                counting = False
                n = s[start:end] + " " + n
        elif not counting:
            start = i
            counting = True

    n = s[start:len(s)] + " " + n
    return n.strip()
    
reverseWords("the sky   is   blue")

reverseWords("abaw")

print(reverseWords("   a   b "))