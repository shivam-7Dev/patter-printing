list=[]
size=int(input("Enter the size of list:"))
for i in range(size):
    val=int(input("Enter the value:"))
    list.append(val)
print(list)
i=0
j=len(list)-1
while i<j:
    t=list[i]
    list[i]=list[j]
    list[j]=t
    i+=1
    j-=1
print(list)