a =int(input("Enter starting year : "))
b =int(input("Enter ending year : "))
if b<a:
    print("Wrong inputs starting element should be greater")
    exit()

print(f"leap years from {a} to {b} are : ")
lp = False
for x in range(a,b+1):
        if (x % 4==0 and x % 100!=0) or (x % 400==0):
         print(x)
         lp = True
if not lp:
    print(f"No leap year found under {a} and {b}")