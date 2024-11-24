#Program to convert a list of values into a set

s=set([1,23,524,"a","Tanmay",34.7])
print(s)
list01=[1,2,3,4,5,4,3,2,1,6,7,9,9]           #List creation
print(set(list01))                           #Coversion of List into Set.
mytup=('a','b',123,3.645)                    #Tuple creation
print(set(mytup))                            #Conversion of Tuple into Set.
a="TANMAY PATIL"                          #String
print(set(a))                                #Conversion of String into Set.
print(set("My name is TANMAY VISHWAJIT PATIL".split()))

a={1,2,3,4,5,6,7,8,9}
b={0,2,4,6,8}
print("Union operation:",a|b,"\nIntersection opration:",a&b,"\nSet difference:",a-b,"\nSymmetric difference:",a^b,)     #Menu driven of sets
                                 
a=set(input("Enter set 1:"))            
b=set(input("Enter set 2:"))
print(set(a))
print(set(b))
ch='y'
while(ch=='y'):
    print("Menu\n1.union\n2.Intersection\n3.Difference\n4.Symmetric Difference\n5.Exit !")
    i=int(input("Your choice:"))
    if(i==1):
        print("Union:",a|b)
    elif(i==2):
        print("Intersection:",a&b)
    elif(i==3):
        print("Difference:",a-b)
    elif(i==4):
        print("Symmetric difference:",a^b)
    elif(i<5):
        print("Invalid choice")
    else:
        break
    ch=input(" Do you want to continue(y/n):")
        
