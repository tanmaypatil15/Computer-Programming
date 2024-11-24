ch = input("Enter Your Own Character : ")

if(ch >= 'A' and ch <= 'Z'):
    print("The Given Character ", ch, "is an Uppercase Alphabet") 
elif(ch >= 'a' and ch <= 'z'):
    print("The Given Character ", ch, "is a Lowercase Alphabet")
elif(ch >= '0' and ch <= '9'):
    print("The Given Character ", ch, "is a Numeric Value")
else:
    print("The Given Character ", ch, "is Not a Lower or Uppercase Alphabet")
