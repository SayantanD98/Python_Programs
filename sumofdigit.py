# To enter a number and find the sum of digits of that number

Number = int(input("Please Enter any Number: "))
Sum = 0
 
while(Number > 0):
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number //10
 
print("\nSum of the digits of Given Number = %d" %Sum)
