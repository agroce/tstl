def cutNull(s,n=None):
    i = 0
    ns = ""
    for c in s:
    	if (c == '\0') or ((n != None) and (i == n)):
            return ns
        else:
            ns += c
            i += 1
    return ns

def strncmp(s1,s2,n):
    s1c = cutNull(s1,n)
    s2c = cutNull(s2,n)
    if s1c < s2c:
        return -1
    if s1c > s2c:
        return 1
    return 0

def memcmp(s1,s2,n):
    if s1c < s2c:
        return -1
    if s1c > s2c:
        return 1
    return 0    

def strnlen(s,n):
    return len(cutNull(s,n))


