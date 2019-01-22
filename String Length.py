def callength(s):
    if type(s) == str :
        l = len(s)
        print("Length of the string = ", l)
    else:
        print("The input is not a string")


st = eval(input("Enter your String : "))
callength(st)
