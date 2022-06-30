#  n=int(input("Enter the number of rows:"))
#  for i in range(1,n+1):
#      for j in range(1,i):
#          print("*")
n=int(input("Enter the number of rows:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i+=1