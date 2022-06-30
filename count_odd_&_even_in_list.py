list=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    val=int(input("Enter the value:"))
    list.append(val)
print(list)
odd=0
even=0
for i in range(len(list)):
    if list[i]%2==0:
        even+=1
    else:
        odd+=1
print("Total odd numbers are:",odd)
print("Total even numbers are:",even)
