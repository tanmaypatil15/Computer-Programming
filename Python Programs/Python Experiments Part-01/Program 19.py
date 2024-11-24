gen=input("Enter Your Gender :")
sal=int(input("Enter Your Salary :"))

if(gen=="Male"):
    salary=sal+(sal*0.05)
    print("The Bonus Salary is :",salary)

    if(sal<10000):
        bonus=salary+(sal*0.02)
        print("The Salary after additional Bonus is :",bonus)

elif(gen=="Female"):
    salary=sal+(sal*0.01)
    print("The Bonus Salary is :",salary)

    if(sal<10000):
        bonus=salary+(sal*0.02)
        print("The Salary after additional Bonus is :",bonus)

else:
    print("You have entered wrong Choice")
