list=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    val=int(input("Enter the value:"))
    list.append(val)
print(list)
max=list[0]
min=list[0]
for i in list:
    if i>max:
        max=i
for i in list:
    if i<min:
        min=i
print("Max value is:",max)
print("Min value is:",min)