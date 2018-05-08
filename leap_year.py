# To determine whether the entered year is a leap year or not

def leap_year(y):
    if y % 400 == 0:
        print ("Leap Year")
        #return True
    if y % 100 == 0:
        print ("Not Leap Year")
        #return False
    if y % 4 == 0:
        print ("Leap Year")
        #return True
    else:
        print ("Not Leap Year")
        #return False
