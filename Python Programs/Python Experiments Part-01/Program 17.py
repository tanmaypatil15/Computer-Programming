#WAP to Read untill -1 is encountered and also count Positive,
#negative and Zeros.

pos_count=0
pos_sum=0
neg_count=0
neg_sum=0
zero=0

while(1):
    print("Enter The Values :")
    n=int(input())
    if(n==-1):
        print("-1 is encountered!")
        break
    elif(n<0):
        print(n,"is Negative.")
        neg_count=neg_count+1
        neg_sum=neg_sum+1
    elif(n>0):
        print(n,"is Positive")
        pos_count=pos_count+1
        pos_sum=pos_sum+1
    else:
        print(n,"is found.")
        zero=zero+1
    sum1=(neg_sum+neg_count)/2
    sum2=(pos_sum+pos_count)/2
print("Total Number of Postive Number Encountered Are :",pos_count)
print("Total Average of Postive Number Encountered Are :",sum2)
print("Total Number of Negative Number Encountered Are :",neg_count)
print("Total Average of Negative Number Encountered Are :",sum1)
print("Total Number of Zeros Encountered Are :",zero)

