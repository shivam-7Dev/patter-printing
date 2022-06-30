n=int(input("Enter number of rows:"))
i=1
k=1
while i<=n:
    b=1
    while b<=n-i:
        print(" ",end="")
        b+=1
    j=1
    while j<=k:
        print("x",end="")
        j+=1
    k+=2
    print()
    i+=1