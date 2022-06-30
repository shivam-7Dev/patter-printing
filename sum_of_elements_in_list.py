list1=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    value=int(input("Enter the value:"))
    list1.append(value)
print(list1)
sum=0
for i in range(0,len(list1)):
    sum+=list1[i]
print("the sum of list elements is:",sum)
