print("Swapping Of Numbers :")
print("")
a=int(input("Enter the First Number :"))
b=int(input("Enter the Second Number :"))
temp=0;
print("Before Swapping Numbers Are a = ",a,"b = ",b)
if(a>0):
    print("The Given number is Positive:")
elif(a<0):
    print("The Given number is Negative:")
else:
    print("Number is Zero");
temp=a
a=b
b=temp
print("After Swapping Numbers are a = ",a,"b = ",b )
if(a>0):
    print("After Swapping Number1 is Positive:")
elif(a<0):
    print("After Swapping Number1 is Negative:")
else:
    print("After Swapping Number1 is Zero");

    
