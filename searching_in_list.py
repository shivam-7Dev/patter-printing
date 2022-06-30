list=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    val=int(input("Enter the value:"))
    list.append(val)
print(list)
key=int(input("Enter the value to search:"))
flag=0
for i in range(len(list)):
    if list[i]==key:
        print("value found at:",i)
        flag=1
        break
if flag==0:
    print("value not found")    
        