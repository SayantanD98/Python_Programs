def wellbracketed(st):
    countopen = 0
    countclose = 0
    for i in st:
        if i == '(':
            countopen+=1
        elif i == ')':
            countclose+=1
    if countopen==countclose:
        return True
    else:
        return False

print wellbracketed('22)')
print wellbracketed('(a+b)(a-b)')
