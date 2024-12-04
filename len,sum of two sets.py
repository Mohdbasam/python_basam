list1 = [1,2,3,4,5]
list2 = [2,4,6,8]
print("Elements in list one are : ",list1)
print("Elements in list second are : ",list2)
if len(list1) == len(list2):
    print("lists have same length")
else:
    print("List length have different length")
s1=0
s2=0
for i in range(len(list1)):
    s1=s1+list1[i]
print("The sum of list1 is : ",s1)

for i in range(len(list2)):
    s2=s2+list2[i]
print("The sum of list2 is : ",s2)
if s1==s2:
    print("the sum of lists are same")
else:
    print("the sum of lists are not same")
print("the common of lists are same : ")
for i in list1:
    for j in list2:
        if i==j:
            print(i)