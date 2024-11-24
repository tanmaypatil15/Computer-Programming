print("ARRAY FUNCTIONS")
print("")
MyString=["Tanmay","Patil","AC Patil","SE"]
print(MyString)
MyString.append("Kharghar")
print(MyString)
MyString.remove("Kharghar")
print(MyString)
MyString.pop(3)
print(MyString)
MyString.count(3)
MyString.sort()
print(MyString)
MyString.sort(reverse=True)
print(MyString)
MyString.reverse()
print(MyString)
MyString.insert(1,"Vishwajit")
print(MyString)
ColorString2=["Red","Blue","Green","Yellow"]
MyString.extend(ColorString2)
print(MyString)
print("")

print("RANGE FUNCTIONS")
print("")

for naturalNumber in range(0,15,3):
    print(naturalNumber)
print("")

print("STRING FUNCTIONS")
print("")

print(MyString[4].casefold())
print(MyString[3].find("AC"))
print("Number of 'k' in string is",MyString[3].count("k"))
print(MyString[1].split())
print(MyString)
newString="SECOND YEAR"
print("New String is",newString)
print("Is new String Lower Case?",newString.islower())
print("Is new String Upper Case?",newString.isupper())
