print("Enter the Words In the List :")
x=input()
text=[]
count=1
i=0
while(x!='-1'):
    text.append(x)
    x=input("Enter a Words :")
    count+=1

for i in range(0,count):
    if('ACPCE'==text[i]or'acpce'==text[i]):
        print("String'ACPCE'present in the Entered Text.")
        break
    else:
         print("String'ACPCE' not present in the Entered Text.")
         break
