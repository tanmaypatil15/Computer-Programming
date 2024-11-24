#To Print The Following Pattern 1.
print("Enter Number of Rows :")
n=int(input())

for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
    

#To Print The Following Pattern 2.
print("Enter Number of Rows :")
m=int(input())

for i in range(1,m):
    for j in range(0,i):
        print(i ,end="")
    print("\r")
