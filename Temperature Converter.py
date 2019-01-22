def ctof(c):
    if c < -273.15:
        print("That temperature doesn't make sense!")
    else :
        f = c * (9 / 5) + 32
        print("The Temperature in Fahrenheit : ", f)


cel = float(input("Enter The Temperature in Celsius :"))
ctof(cel)
