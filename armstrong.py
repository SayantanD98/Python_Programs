# To Check whether a number is Armstrong Number or Not.

num=int(input("Enter a Number = \n"))
sum=0
temp=num

while temp>0:
    d=temp%10
    sum=sum+d**3
    temp=temp/10

if (num==sum):
    print ("Armstrong Number")
else:
    print ("Not Armstrong Number")
