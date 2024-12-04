print("Enter 3 numbers :- ")
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))

if a>b and a>c:
    print("largest number is a : ",a)
elif b>a and b>c:
    print("Largest number is b : ",b)
elif c>a and c>b:
    print("largest number is c : ",c)
else:
    print("Entered numbers are same")
