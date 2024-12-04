n = int(input("Enter the no. of colours : "))
listc = []
print("Enter the colours")
for x in range(n):
    colour = input()
    listc.append(colour)
print("Entered list of colours are : ",listc)

print("First colour is : ",listc[0])
print("Second colour is : ",listc[-1])
