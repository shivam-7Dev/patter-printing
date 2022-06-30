list=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    val=int(input("Enter the value:"))
    list.append(val)
print(list)
key=int(input("enter the value to count"))
count=0
for i in list:
    if i==key:
        count+=1
print("The frequency of number is:",count)