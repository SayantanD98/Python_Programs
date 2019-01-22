def sumofsquares(m):
    if m<0:
        return False
    i = 1
    while i*i <= m:
        j = 1
        while j*j <= m:  
            if((i*i)+(j*j)==m):
                return True
            j =j+1
        i = i+1
    return False        
