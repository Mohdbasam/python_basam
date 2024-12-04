co1 = ["red","blue","green"]
co2 = ["yellow","blue"]
print(co1,co2)
for i in range(len(co1)):
    if co1[i] not in co2:
        print("The colour is : ",co1[i])