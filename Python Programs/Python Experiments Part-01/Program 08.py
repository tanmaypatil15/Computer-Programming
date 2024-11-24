#To Print No's From m to n and Classify Whether No's Even or Odd.
print("Enter The Value of m :")
m=int(input())
print("Enter The Value of n :")
n=int(input())

for i in range(m,n + 1,1):
    if (i % 2) == 0:
       print("{0} is Even".format(i))
    else:
       print("{0} is Odd".format(i))
