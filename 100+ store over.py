a = int(input("How many numbers you want to store"))
a=list()
print("Enter the values")
result = []
for x in range(0,a):
 bb = int(input())

for x in range(a):
    if x<100:
        result.append(x)
    else :
        result.append("Over")
print("Entered numbers are : ",result)
