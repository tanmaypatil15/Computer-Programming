def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
def mod(x,y):
    return x%y

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

print("Select Operation to perform:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
n=int(input())
if(n==1):
    print(a,"+",b,"=",add(a,b))
elif(n==2):
    print(a,"-",b,"=",sub(a,b))    
elif(n==3):
    print(a,"*",b,"=",multiply(a,b))
elif(n==4):
    print(a,"/",b,"=",division(a,b))
elif(n==5):
    print(a,"%",b,"=",mod(a,b))
else:
    print("Invalid choice...!!!")
