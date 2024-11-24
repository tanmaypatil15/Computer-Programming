#Sum of the Squares of Even Numbers.
sum=0
print("Enter The Value of n :")
n=int(input())
for i in range(0,n + 1):
    sum+=(2*i)*(2*i)
print("Sum of Squares of Even Numbers :",sum)
