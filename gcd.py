num1 = int(input("enter 1st number : "))
num2 = int(input("Enter 2nd number"))
i=1
while(i<=num1 and i<=num2):
    if(num1%i==0 and num2%i==0):
        gcd = i
