# To display the Fibonacci Series upto the entered range.

n=int(input("Enter the nth Number = "))

n1=0
n2=1
count=0

if (n<= 0):
   print("Please enter a positive integer")
elif (n==1):
   print("Fibonacci sequence is 0. ")
else:
   print("Fibonacci sequence upto %d is : " %(n))
   while (count<n):
       print(n1)
       sum=n1+n2
       n1=n2
       n2=sum
       count=count+1
