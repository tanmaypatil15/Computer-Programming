#WAP to Read untill a is encountered and also count UpperCase,
#Lowercase and Numeric Values.

upper=0
lower=0
num=0
while(1):
    print("Enter The Alphabets :")
    n=(input())
    if(n=='a'):
        print("a is encountered!")
        break
    elif(n>='A'and n<='Z'):
        print(n,"is UpperCase Character.")
        upper=upper+1
    elif(n>='b' and n<='z'):
        print(n,"is LowerCase Character.")
        lower=lower+1
    elif(n>='0' and n<='9'):
        print(n,"is Numeric Values.")
        num=num+1
    else:
        print(n,"is not found.")
print("Total Number of UpperCase Characters Encountered Are :",upper)
print("Total Number of LowerCase Characters Encountered Are :",lower)
print("Total Number of Numeric Values Encountered Are :",num)
