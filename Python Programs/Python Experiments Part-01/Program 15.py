#WAP to Read untill -1 is encountered and also count Positive,
#negative and Zeros.

pos=0
neg=0
zero=0

while(1):
    print("Enter The Values :")
    n=int(input())
    if(n==-1):
        print("-1 is encountered!")
        break
    elif(n<0):
        print(n,"is Negative.")
        neg=neg+1
    elif(n>0):
        print(n,"is Positive")
        pos=pos+1
    else:
        print(n,"is found.")
        zero=zero+1
print("Total Number of Postive Number Encountered Are :",pos)
print("Total Number of Negative Number Encountered Are :",neg)
print("Total Number of Zeros Encountered Are :",zero)
