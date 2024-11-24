#To Calculate Factorial of n Numbers Using For loop 
fact=1
print("Enter The Value of n :")
n=int(input())

for i in range(1,n + 1):
    fact=fact*i
    
print("Factorial of",n,"Number is :",fact)
