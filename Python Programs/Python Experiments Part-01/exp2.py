#WAP to swap two numbers and find whether the number is positive, negative and zero.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("Number before swapping are {0} and {1}".format(a,b))
temp=a
a=b
b=temp
print("Number after swapping are {0} and {1}".format(a,b))
if a>0:
    print("First number is positive after swapping.")
elif a<0:
    print("First number is negative after swapping.")
else:
    print("First number is zero after swapping.")

