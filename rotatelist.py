def rotatelist(l,k):
    if k<0:
        return l
    p = l
    for i in range(k):
        for j in range(1,len(l)):
            c = p[0]
            p[0] = p[j]
            p[j] = c
    return p
