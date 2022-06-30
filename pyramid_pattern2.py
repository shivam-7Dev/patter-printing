n=int(input("Enter number of rows:"))
i=1
while n>0:
    # printing space
    b=1
    while b<i:
        print(" ",end="")
        b+=1
    # printing Stars
    j=1
    while j<=((n*2)-i):
        print("*",end="")
        j+=1
    print()
    n-=1
    i+=1